#!/usr/bin/env python3
"""Build a pandoc reference.docx carrying a document's brand.

Starts from pandoc's own default reference so every style id pandoc expects
still exists, then replaces the styles that matter, adds the custom ones the
Lua filter targets, and attaches a running header and footer.

    build_reference.py <out.docx> [--brand brand.json]
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand as brand_mod

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
SIDES = ("top", "left", "bottom", "right")


def fonts(name):
    return ('<w:rFonts w:ascii="{0}" w:hAnsi="{0}" w:cs="{0}" w:eastAsia="{0}"/>'.format(name))


def style(sid, name, kind="paragraph", based=None, nxt=None, custom=False, ppr="", rpr=""):
    return (
        '<w:style w:type="%s"%s w:styleId="%s"><w:name w:val="%s"/>%s%s<w:qFormat/>%s%s</w:style>'
        % (kind,
           ' w:customStyle="1"' if custom else "",
           sid, name,
           '<w:basedOn w:val="%s"/>' % based if based else "",
           '<w:next w:val="%s"/>' % nxt if nxt else "",
           "<w:pPr>%s</w:pPr>" % ppr if ppr else "",
           "<w:rPr>%s</w:rPr>" % rpr if rpr else "")
    )


def border(side, sz, color, space=0):
    return '<w:%s w:val="single" w:sz="%d" w:space="%d" w:color="%s"/>' % (side, sz, space, color)


def build_styles(b):
    """Return (replacements, additions, table_style)."""
    body, head = b["bodyFont"], b["headFont"]

    replace = {
        "Normal": style(
            "Normal", "Normal",
            ppr='<w:jc w:val="left"/><w:spacing w:after="160" w:line="288" w:lineRule="auto"/>',
            rpr=fonts(body) + '<w:color w:val="%s"/><w:sz w:val="21"/><w:szCs w:val="21"/>' % b["text"],
        ).replace('w:styleId="Normal"', 'w:default="1" w:styleId="Normal"'),

        "BodyText": style("BodyText", "Body Text", based="Normal",
                          ppr='<w:spacing w:after="160"/>'),

        "FirstParagraph": style("FirstParagraph", "First Paragraph", based="BodyText", custom=True),

        # pandoc puts table cells and tight list items in Compact
        "Compact": style("Compact", "Compact", based="Normal", custom=True,
                         ppr='<w:spacing w:before="40" w:after="40" w:line="252" w:lineRule="auto"/>',
                         rpr='<w:sz w:val="19"/><w:szCs w:val="19"/>'),

        "Heading1": style("Heading1", "heading 1", based="Normal", nxt="FirstParagraph",
                          ppr='<w:keepNext/><w:spacing w:before="0" w:after="160"/><w:outlineLvl w:val="0"/>',
                          rpr=fonts(head) + '<w:b/><w:color w:val="%s"/><w:sz w:val="56"/><w:szCs w:val="56"/>' % b["text"]),

        "Heading2": style("Heading2", "heading 2", based="Normal", nxt="FirstParagraph",
                          ppr='<w:keepNext/><w:pBdr>%s</w:pBdr>'
                              '<w:spacing w:before="360" w:after="140"/><w:outlineLvl w:val="1"/>'
                              % border("top", 6, b["rule"], space=8),
                          rpr=fonts(head) + '<w:b/><w:color w:val="%s"/><w:sz w:val="38"/><w:szCs w:val="38"/>' % b["text"]),

        "Heading3": style("Heading3", "heading 3", based="Normal", nxt="FirstParagraph",
                          ppr='<w:keepNext/><w:spacing w:before="260" w:after="90"/><w:outlineLvl w:val="2"/>',
                          rpr=fonts(head) + '<w:b/><w:color w:val="%s"/><w:sz w:val="27"/><w:szCs w:val="27"/>' % b["text"]),

        "Heading4": style("Heading4", "heading 4", based="Normal", nxt="FirstParagraph",
                          ppr='<w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="3"/>',
                          rpr=fonts(body) + '<w:b/><w:color w:val="%s"/><w:sz w:val="21"/><w:szCs w:val="21"/>' % b["accent"]),

        # blockquotes: tinted panel with a hairline ring
        "BlockText": style("BlockText", "Block Text", based="Normal", nxt="BodyText",
                           ppr='<w:shd w:val="clear" w:color="auto" w:fill="%s"/><w:pBdr>%s</w:pBdr>'
                               '<w:spacing w:before="140" w:after="180"/><w:ind w:left="120" w:right="120"/>'
                               % (b["quoteFill"], "".join(border(s, 6, b["rule"], space=6) for s in SIDES)),
                           rpr='<w:sz w:val="20"/><w:szCs w:val="20"/>'),

        "ImageCaption": style("ImageCaption", "Image Caption", based="Normal", custom=True,
                              ppr='<w:spacing w:before="60" w:after="220"/>',
                              rpr='<w:i/><w:color w:val="%s"/><w:sz w:val="18"/><w:szCs w:val="18"/>' % b["muted"]),
    }

    additions = [
        # <aside> callouts
        style("Callout", "Callout", based="Normal", nxt="BodyText", custom=True,
              ppr='<w:shd w:val="clear" w:color="auto" w:fill="%s"/>'
                  '<w:spacing w:before="120" w:after="180"/><w:ind w:left="120" w:right="120"/>' % b["calloutFill"],
              rpr='<w:sz w:val="20"/><w:szCs w:val="20"/>'),

        # small uppercase accent labels; keepNext holds them to what they introduce
        style("Label", "Label", based="Normal", nxt="BodyText", custom=True,
              ppr='<w:keepNext/><w:spacing w:before="200" w:after="40"/><w:contextualSpacing/>',
              rpr='<w:b/><w:caps/><w:color w:val="%s"/><w:spacing w:val="20"/>'
                  '<w:sz w:val="17"/><w:szCs w:val="17"/>' % b["accent"]),

        style("LabelMuted", "Label Muted", based="Normal", nxt="BodyText", custom=True,
              ppr='<w:keepNext/><w:pBdr>%s</w:pBdr><w:spacing w:before="240" w:after="120"/>'
                  % border("bottom", 6, b["rule"], space=6),
              rpr='<w:b/><w:caps/><w:color w:val="8A8A8A"/><w:spacing w:val="20"/>'
                  '<w:sz w:val="17"/><w:szCs w:val="17"/>'),

        style("Header", "header", based="Normal",
              ppr='<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs><w:pBdr>%s</w:pBdr>'
                  '<w:spacing w:after="0"/>'
                  % (b["pageWidth"] - 2 * b["pageMargin"], border("bottom", 6, b["rule"], space=6)),
              rpr='<w:caps/><w:color w:val="8A8A8A"/><w:spacing w:val="20"/><w:sz w:val="16"/>'),

        style("Footer", "footer", based="Normal",
              ppr='<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs><w:pBdr>%s</w:pBdr>'
                  '<w:spacing w:before="0" w:after="0"/>'
                  % (b["pageWidth"] - 2 * b["pageMargin"], border("top", 6, b["rule"], space=6)),
              rpr='<w:color w:val="8A8A8A"/><w:sz w:val="16"/>'),

        # character styles the Lua filter applies
        style("NumberMark", "Number Mark", kind="character", custom=True,
              rpr='<w:b/><w:color w:val="%s"/>' % b["accent"]),
        style("CalloutLabel", "Callout Label", kind="character", custom=True,
              rpr='<w:b/><w:caps/><w:color w:val="%s"/><w:spacing w:val="20"/><w:sz w:val="17"/>' % b["accent"]),
    ]

    table = (
        '<w:style w:type="table" w:default="1" w:styleId="Table">'
        '<w:name w:val="Table"/><w:basedOn w:val="TableNormal"/><w:qFormat/>'
        '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/>'
        '<w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
        '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar>'
        '<w:tblBorders>%s</w:tblBorders></w:tblPr>'
        '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:color w:val="%s"/></w:rPr>'
        '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="%s"/>'
        '<w:tcBorders>%s</w:tcBorders><w:vAlign w:val="bottom"/></w:tcPr></w:tblStylePr></w:style>'
        % ("".join(border(s, 6, b["tableGrid"]) for s in SIDES + ("insideH", "insideV")),
           b["text"], b["tableHeadFill"], border("bottom", 12, b["tableHeadGrid"]))
    )
    return replace, additions, table


def furniture(b):
    def para(style_id, left, right):
        runs = '<w:r><w:t xml:space="preserve">%s</w:t></w:r>' % left
        if right:
            runs += '<w:r><w:tab/><w:t xml:space="preserve">%s</w:t></w:r>' % right
        return '<w:p><w:pPr><w:pStyle w:val="%s"/></w:pPr>%s</w:p>' % (style_id, runs)

    header = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr %s>%s</w:hdr>'
              % (W, para("Header", b["headerLeft"], b["headerRight"])))
    footer = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr %s>%s</w:ftr>'
              % (W, para("Footer", b["footerLeft"], b["footerRight"])))
    sectpr = (
        "<w:sectPr>"
        '<w:headerReference w:type="default" r:id="rIdHdr1"/>'
        '<w:footerReference w:type="default" r:id="rIdFtr1"/>'
        '<w:pgSz w:w="%d" w:h="%d"/>'
        '<w:pgMar w:top="%d" w:right="%d" w:bottom="%d" w:left="%d" '
        'w:header="576" w:footer="576" w:gutter="0"/>'
        "</w:sectPr>"
        % (b["pageWidth"], b["pageHeight"],
           b["pageMargin"], b["pageMargin"], b["pageMargin"], b["pageMargin"])
    )
    return header, footer, sectpr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--brand", default=None)
    args = ap.parse_args()

    b = brand_mod.load(args.brand)
    replace, additions, table = build_styles(b)
    header_xml, footer_xml, sectpr = furniture(b)

    base = os.path.join(tempfile.mkdtemp(), "reference.docx")
    subprocess.run(["pandoc", "-o", base, "--print-default-data-file", "reference.docx"],
                   check=True)

    src = zipfile.ZipFile(base)
    parts = {n: src.read(n) for n in src.namelist()}

    styles = parts["word/styles.xml"].decode()
    for sid, xml in replace.items():
        styles, n = re.subn(r'<w:style [^>]*w:styleId="%s"[ >].*?</w:style>' % sid,
                            lambda _m, x=xml: x, styles, count=1, flags=re.S)
        if n != 1:
            sys.exit("expected style %s in pandoc's default reference" % sid)
    styles = re.sub(r'<w:style w:type="table"[^>]*w:styleId="Table"[ >].*?</w:style>',
                    lambda _m: table, styles, count=1, flags=re.S)
    parts["word/styles.xml"] = styles.replace("</w:styles>", "".join(additions) + "</w:styles>").encode()

    doc = parts["word/document.xml"].decode()
    parts["word/document.xml"] = re.sub(r"<w:sectPr>.*?</w:sectPr>", lambda _m: sectpr,
                                        doc, count=1, flags=re.S).encode()

    rels = parts["word/_rels/document.xml.rels"].decode()
    base_ns = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    parts["word/_rels/document.xml.rels"] = rels.replace(
        "</Relationships>",
        '<Relationship Id="rIdHdr1" Type="%s/header" Target="header1.xml"/>'
        '<Relationship Id="rIdFtr1" Type="%s/footer" Target="footer1.xml"/></Relationships>'
        % (base_ns, base_ns)).encode()

    ct_ns = "application/vnd.openxmlformats-officedocument.wordprocessingml"
    parts["[Content_Types].xml"] = parts["[Content_Types].xml"].decode().replace(
        "</Types>",
        '<Override PartName="/word/header1.xml" ContentType="%s.header+xml"/>'
        '<Override PartName="/word/footer1.xml" ContentType="%s.footer+xml"/></Types>'
        % (ct_ns, ct_ns)).encode()

    parts["word/header1.xml"] = header_xml.encode()
    parts["word/footer1.xml"] = footer_xml.encode()

    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)

    print("wrote %s (%dKB, %d parts)" % (args.out, os.path.getsize(args.out) // 1024, len(parts)))


if __name__ == "__main__":
    main()
