#!/usr/bin/env python3
"""Self-host a bundle's Google Fonts so a render never depends on network state.

These design-document bundles load their brand faces through an @import in
`_ds/*/tokens/fonts.css`. Offline, the page silently falls back to system
sans-serif. This downloads the latin / latin-ext woff2 files into the bundle
copy and rewrites fonts.css to point at them.

Run against the BUILD COPY, never the operator's source bundle.

    localize_fonts.py <build-dir>
"""
import glob
import os
import re
import sys
import urllib.request

# a browser UA is required or Google Fonts serves ttf instead of woff2
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
KEEP_SUBSETS = re.compile(r"^/\* latin(-ext)? \*/")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def find_fonts_css(build_dir):
    hits = glob.glob(os.path.join(build_dir, "_ds", "*", "tokens", "fonts.css"))
    hits += glob.glob(os.path.join(build_dir, "**", "fonts.css"), recursive=True)
    for path in hits:
        if "@import" in open(path, encoding="utf-8").read():
            return path
    return None


def main(build_dir):
    css_path = find_fonts_css(build_dir)
    if not css_path:
        print("no fonts.css with an @import found; nothing to localize")
        return 0

    source = open(css_path, encoding="utf-8").read()
    m = re.search(r"@import url\(['\"]?(https://fonts\.googleapis\.com/[^'\")]+)", source)
    if not m:
        print("fonts.css has no Google Fonts @import; nothing to localize")
        return 0

    css = fetch(m.group(1)).decode("utf-8")
    out_dir = os.path.join(os.path.dirname(css_path), "webfonts")
    os.makedirs(out_dir, exist_ok=True)

    blocks = re.split(r"(?=/\* [a-z0-9-]+ \*/)", css)
    kept, files = [], 0
    for block in blocks:
        if not KEEP_SUBSETS.match(block.strip()):
            continue
        for url in re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", block):
            name = "f%02d-%s" % (files, os.path.basename(url.split("?")[0]))
            with open(os.path.join(out_dir, name), "wb") as f:
                f.write(fetch(url))
            block = block.replace(url, "webfonts/%s" % name)
            files += 1
        kept.append(block)

    header = ("/* Webfonts localized for offline export by the CWOS\n"
              "   document-export skill. Latin + latin-ext subsets only. */\n\n")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(header + "".join(kept))

    print("localized %d font files into %s" % (files, os.path.relpath(out_dir, build_dir)))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
