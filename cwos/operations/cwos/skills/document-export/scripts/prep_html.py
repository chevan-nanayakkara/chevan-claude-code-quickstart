#!/usr/bin/env python3
"""Prepare a design-document bundle's HTML for conversion to .docx.

Extracts the document's light DOM and applies the structural repairs that
pandoc cannot infer. Each transform is pattern-matched and reports its own
count, so a bundle lacking a given pattern is simply skipped (count 0).

    prep_html.py <bundle-dir> <build-dir> [--brand brand.json]

Writes <build-dir>/content.html and <build-dir>/img/.
"""
import argparse
import os
import re
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand as brand_mod

MAX_IMAGE_HEIGHT_IN = 7.4   # leaves room for a caption on the same page
LOGO_WIDTH_PX = 256


def cut_balanced(text, open_pattern):
    """Remove a <div ...>...</div> block matched by open_pattern, counting nesting."""
    m = re.search(open_pattern, text)
    if not m:
        return text
    depth, start = 1, m.end()
    for tag in re.finditer(r"</?div\b", text[start:]):
        depth += 1 if tag.group(0) == "<div" else -1
        if depth == 0:
            return text[: m.start()] + text[start + tag.end() + 1 :]
    return text


def extract_body(html):
    """Return the light DOM inside <doc-page>, minus runtime-only wrappers."""
    if "<doc-page" in html:
        start = html.index(">", html.index("<doc-page")) + 1
        body = html[start : html.index("</doc-page>")]
    else:                                   # plain HTML fallback
        body = re.search(r"<body[^>]*>(.*)</body>", html, re.S).group(1)

    body = cut_balanced(body, r'<div slot="header"[^>]*>')
    body = cut_balanced(body, r'<div slot="footer"[^>]*>')
    return re.sub(r"</?sc-if\b[^>]*>", "", body)   # template conditionals


def linearize_contents(text):
    """A two-column CSS grid's DOM order is column-interleaved (1, 7, 2, 8...).
    Re-sort to reading order and emit real <ol> lists, so Word and Docs get
    genuine numbering rather than numbers typed into the text."""
    m = re.search(r'<div style="display: grid; grid-template-columns: 1fr 1fr;.*?</div>\s*</div>',
                  text, re.S)
    if not m:
        print("contents grid: not present")
        return text

    items = re.findall(r"<div><span[^>]*>([^<]*)</span>([^<]*)</div>", m.group(0))
    if not items:
        return text

    def key(item):
        label = item[0].strip()
        return (0, int(label), "") if label.isdigit() else (1, 0, label)

    ordered = sorted(items, key=key)
    numbered = [t.strip() for n, t in ordered if n.strip().isdigit()]
    lettered = [t.strip() for n, t in ordered if not n.strip().isdigit()]

    lists = '<ol type="1">' + "".join("<li>%s</li>" % t for t in numbered) + "</ol>"
    if lettered:
        lists += '<ol type="A">' + "".join("<li>%s</li>" % t for t in lettered) + "</ol>"

    print("contents grid: %d items linearized into %d real list(s)"
          % (len(items), 1 + bool(lettered)))
    return text[: m.start()] + lists + text[m.end() :]


def replace_swatches(text, build_dir):
    """Color chips drawn as empty spans with a CSS background carry no content
    into a .docx. Emit real chip images instead."""
    made = {}

    def chip(hex_color):
        name = "img/swatch-%s.png" % hex_color.lstrip("#").lower()
        path = os.path.join(build_dir, name)
        if name not in made:
            w, h = 136, 60                   # 4x the on-screen chip, for print
            edge = Image.new("RGB", (w, h), (214, 209, 202))
            edge.paste(Image.new("RGB", (w - 4, h - 4), hex_color), (2, 2))
            edge.save(path, dpi=(96, 96))
            made[name] = True
        return name

    pattern = re.compile(r'<span style="display: block; width: (\d+)px; height: \d+px;[^"]*'
                         r'background: (#[0-9A-Fa-f]{6})[^"]*"></span>')
    text, n = pattern.subn(
        lambda m: '<img src="%s" width="%s" alt="%s">' % (chip(m.group(2)), m.group(1), m.group(2)),
        text)
    print("palette swatches: %d converted to chip images" % n)
    return text


def hoist_figure_labels(text):
    """A <figure> holding label + image + caption becomes a two-column figure
    table in pandoc, halving the image. Lift the label out."""
    pattern = re.compile(r'(<figure[^>]*>)\s*(<div style="[^"]*uppercase[^"]*"[^>]*>.*?</div>)', re.S)
    text, n = pattern.subn(lambda m: m.group(2) + m.group(1), text)
    print("figure labels: %d hoisted out of <figure>" % n)
    return text


def convert_images(text, bundle_dir, build_dir, column_px):
    """Re-encode plates as JPEG (a .docx should stay email-sized), keep the logo
    as PNG for transparency, and normalize everything to 96 dpi so the width
    attribute maps 1:1 to the display size pandoc computes."""
    seen = {}

    def convert(rel):
        im = Image.open(os.path.join(bundle_dir, rel))
        base = os.path.splitext(os.path.basename(rel))[0]

        if rel.startswith("assets/"):                     # logo / marks
            im = im.convert("RGBA")
            im.thumbnail((640, 640), Image.LANCZOS)
            out = "img/%s.png" % base
            im.save(os.path.join(build_dir, out), optimize=True, dpi=(96, 96))
            return out, LOGO_WIDTH_PX

        if im.mode in ("RGBA", "LA", "P"):                # flatten onto white
            flat = Image.new("RGB", im.size, (255, 255, 255))
            im = im.convert("RGBA")
            flat.paste(im, mask=im.split()[-1])
            im = flat
        else:
            im = im.convert("RGB")

        out = "img/%s.jpg" % base
        im.save(os.path.join(build_dir, out), "JPEG", quality=82, optimize=True,
                progressive=True, dpi=(96, 96))

        width = column_px
        aspect = im.size[1] / im.size[0]
        if width * aspect > MAX_IMAGE_HEIGHT_IN * 96:
            width = int(MAX_IMAGE_HEIGHT_IN * 96 / aspect)
        return out, width

    def repl(m):
        tag, rel = m.group(0), m.group(1)
        if rel.startswith("img/"):                        # already-built asset
            return tag
        if rel not in seen:
            seen[rel] = convert(rel)
        out, width = seen[rel]
        # the source's inline style (width: auto, max-width: 100%) confuses
        # pandoc's sizing; an explicit width attribute is predictable
        tag = re.sub(r'\sstyle="[^"]*"', "", tag)
        return tag.replace('src="%s"' % rel, 'src="%s" width="%d"' % (out, width))

    text = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', repl, text)
    total = sum(os.path.getsize(os.path.join(build_dir, o)) for o, _ in seen.values())
    print("images: %d re-encoded, %dKB total" % (len(seen), total // 1024))
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle_dir")
    ap.add_argument("build_dir")
    ap.add_argument("--brand", default=None)
    args = ap.parse_args()

    cfg = brand_mod.load(args.brand)
    column_px = brand_mod.text_width_px(cfg)
    os.makedirs(os.path.join(args.build_dir, "img"), exist_ok=True)

    sources = [f for f in os.listdir(args.bundle_dir) if f.endswith(".html")]
    if not sources:
        sys.exit("no .html file found in %s" % args.bundle_dir)
    source = os.path.join(args.bundle_dir, sorted(sources, key=len)[0])
    print("source: %s" % os.path.basename(source))

    body = extract_body(open(source, encoding="utf-8").read())
    body = linearize_contents(body)
    body = replace_swatches(body, args.build_dir)
    body = hoist_figure_labels(body)
    body = convert_images(body, args.bundle_dir, args.build_dir, column_px)

    # no <title>: pandoc would emit it as a duplicate Title paragraph above the
    # document's own H1
    doc = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>\n%s\n</body></html>' % body
    out = os.path.join(args.build_dir, "content.html")
    open(out, "w", encoding="utf-8").write(doc)
    print("wrote %s (%dKB); image column width %dpx" % (out, len(doc) // 1024, column_px))


if __name__ == "__main__":
    main()
