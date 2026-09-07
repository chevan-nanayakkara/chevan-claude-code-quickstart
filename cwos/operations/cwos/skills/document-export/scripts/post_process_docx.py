#!/usr/bin/env python3
"""Apply the direct formatting Google Docs needs, in place.

Two things a reference.docx alone cannot deliver:

1. Table borders. Word honors style-level w:tblBorders; Google Docs discards
   them on import and only respects borders written directly onto each table
   and each cell. Style-only borders means invisible tables in Docs.
2. List marker color. Markers take formatting from the paragraph mark, so an
   accent color needs an rPr inside each list paragraph's pPr.

    post_process_docx.py <file.docx> [--brand brand.json]
"""
import argparse
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand as brand_mod

SIDES = ("top", "left", "bottom", "right")


def border(side, sz, color):
    return '<w:%s w:val="single" w:sz="%d" w:space="0" w:color="%s"/>' % (side, sz, color)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--brand", default=None)
    args = ap.parse_args()

    b = brand_mod.load(args.brand)
    grid, head_grid, head_fill, accent = (
        b["tableGrid"], b["tableHeadGrid"], b["tableHeadFill"], b["accent"])

    tbl_borders = ("<w:tblBorders>"
                   + "".join(border(s, 6, grid) for s in SIDES + ("insideH", "insideV"))
                   + "</w:tblBorders>")
    cell_borders = "<w:tcBorders>" + "".join(border(s, 6, grid) for s in SIDES) + "</w:tcBorders>"
    head_cell = ("<w:tcBorders>"
                 + border("top", 6, grid) + border("left", 6, grid)
                 + border("bottom", 12, head_grid) + border("right", 6, grid)
                 + "</w:tcBorders>"
                 + '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % head_fill)

    def fix_cells(row_xml, props):
        # CT_TcPr order: cnfStyle, tcW, gridSpan, ... then tcBorders, shd
        def one(m):
            inner = m.group(1) or ""
            gridspan = re.search(r"<w:gridSpan[^/]*/>", inner)
            head, tail = ((inner[: gridspan.end()], inner[gridspan.end():])
                          if gridspan else ("", inner))
            return "<w:tcPr>%s%s%s</w:tcPr>" % (head, props, tail)

        return re.sub(r"<w:tcPr>(.*?)</w:tcPr>", one, row_xml, flags=re.S)

    def fix_table(m):
        tbl = re.sub(r"(<w:tblW[^/]*/>)", lambda w: w.group(1) + tbl_borders, m.group(0), count=1)
        return re.sub(r"<w:tr>.*?</w:tr>",
                      lambda r: fix_cells(r.group(0),
                                          head_cell if "<w:tblHeader" in r.group(0) else cell_borders),
                      tbl, flags=re.S)

    def color_marker(m):
        ppr = m.group(0)
        if "<w:numPr>" not in ppr or "<w:rPr>" in ppr:
            return ppr
        # w:rPr is the last child of w:pPr per CT_PPr
        return ppr.replace("</w:pPr>",
                           '<w:rPr><w:b/><w:color w:val="%s"/></w:rPr></w:pPr>' % accent)

    src = zipfile.ZipFile(args.docx)
    parts = {n: src.read(n) for n in src.namelist()}
    src.close()

    doc = parts["word/document.xml"].decode()
    doc = doc.replace("<w:tcPr />", "<w:tcPr></w:tcPr>").replace("<w:tcPr/>", "<w:tcPr></w:tcPr>")
    doc, tables = re.subn(r"<w:tbl>.*?</w:tbl>", fix_table, doc, flags=re.S)
    doc = re.sub(r"<w:pPr>.*?</w:pPr>", color_marker, doc, flags=re.S)
    parts["word/document.xml"] = doc.encode()

    with zipfile.ZipFile(args.docx, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)

    print("tables bordered: %d | cells: %d | header cells shaded: %d | list markers: %d"
          % (tables, doc.count("<w:tcBorders>"), doc.count(head_fill),
             len(re.findall(r"<w:numPr>", doc))))


if __name__ == "__main__":
    main()
