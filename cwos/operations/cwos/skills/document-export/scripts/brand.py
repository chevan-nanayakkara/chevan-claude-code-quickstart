"""Shared brand configuration for the document-export scripts.

Colors are RRGGBB without the leading '#', which is what OOXML expects.
Defaults are a neutral professional palette; pass --brand <file.json> to
override with values derived from the bundle's own design tokens.
"""
import json

DEFAULTS = {
    "bodyFont": "Calibri",
    "headFont": "Calibri",
    "accent": "1F4E79",        # section numbers, labels, run-in headings
    "text": "2D2D2D",          # body copy
    "muted": "6F6F6F",         # captions
    "calloutFill": "F2F2F2",   # <aside> callouts
    "quoteFill": "FAFAFA",     # blockquotes
    "rule": "D9D9D9",          # hairlines under headings, quote borders
    "tableGrid": "A6A6A6",     # table rules
    "tableHeadGrid": "7F7F7F", # heavier rule under a header row
    "tableHeadFill": "EDEDED", # header row fill
    "headerLeft": "",
    "headerRight": "",
    "footerLeft": "",
    "footerRight": "",
    "pageWidth": 12240,        # twips; 12240 x 15840 = US Letter portrait
    "pageHeight": 15840,
    "pageMargin": 1224,        # twips; 1224 = 0.85in
}


def load(path=None):
    """Return the brand config, overlaying <path> onto the defaults."""
    brand = dict(DEFAULTS)
    if path:
        with open(path, encoding="utf-8") as f:
            brand.update(json.load(f))
    return brand


def text_width_px(brand, dpi=96):
    """Printable column width in pixels, for sizing images."""
    twips = brand["pageWidth"] - 2 * brand["pageMargin"]
    return int(twips / 1440 * dpi)
