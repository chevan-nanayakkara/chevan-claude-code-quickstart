---
name: document-export
description: Convert a self-contained HTML document export (a `*.dc.html` design-document bundle with its `_ds/` design system, `assets/`, and `uploads/`) into an email-ready PDF and a Google-Docs-friendly .docx that carries the document's fonts, colors, callouts, tables, and running header/footer. Use when the user asks to convert, render, or export such a bundle to PDF or Word, when a generated .docx needs to survive Google Docs import (no bookmarks, visible table borders, real lists), or when a previously exported PDF/.docx needs regenerating after the HTML source changed.
---

# Document Export — HTML bundle → PDF and Google-Docs-friendly .docx

Design-document bundles render through JavaScript web components and a CSS design system. Neither format converts by pointing a tool at the file: the PDF needs a real browser engine, and the .docx needs every CSS-only visual affordance re-expressed in Word's model. This skill codifies both paths and the failure modes that otherwise pass silently.

Bundled toolkit: [`scripts/`](scripts/) — four parameterized Python scripts, usable as-is or as reference.

## When to invoke

- "Convert `<bundle>/` to PDF" / "render this document" / "compress it so I can email it"
- "Convert it to Word" / "make it Google Docs friendly" / "no bookmarks"
- A generated .docx shows invisible table borders, stray bookmark markers, scrambled contents, half-width images, or run-together numbers
- The HTML source changed and the PDF or .docx needs regenerating (neither auto-follows)

## Inputs

- Path to the bundle directory (contains `*.dc.html`, `_ds/`, `assets/`, `uploads/`, usually a `README.txt`)
- Which outputs are wanted: PDF, .docx, or both
- Optionally a brand JSON (see [Brand configuration](#brand-configuration)); without one the scripts use neutral defaults

Preconditions: Chrome (or Edge), Ghostscript, Pandoc, Python with Pillow. LibreOffice is needed only for verification rendering.

## The core principle

**Never edit the source bundle.** Copy it to a scratch build directory and transform the copy. The operator's folder stays pristine and re-runnable.

**Never trust the conversion.** Eight of the nine failure modes below produce a file that opens fine and is quietly wrong. Render the result back to images and read it. The ninth (vector images) is the exception that announces itself, and is described where it sits in the list.

## Procedure — PDF

1. **Copy the bundle** to a scratch build directory.

2. **Localize the web fonts.** These bundles load Roboto/Open Sans (or similar) from Google Fonts at runtime, so the render depends on network state, and offline it silently falls back to system sans. Run `scripts/localize_fonts.py <build-dir>`: it downloads the latin/latin-ext woff2 files and rewrites the copy's `fonts.css` to reference them locally.

3. **Serve the build directory over HTTP** (`python3 -m http.server`) rather than rendering from `file://`. Chrome applies cross-origin restrictions to fonts on local-file loads, which drops them without an error.

4. **Render with headless Chrome:**

   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --user-data-dir=<scratch-profile> \
     --no-pdf-header-footer --virtual-time-budget=30000 \
     --print-to-pdf=<out.pdf> "http://127.0.0.1:<port>/<Document>.dc.html"
   ```

   `--no-pdf-header-footer` suppresses Chrome's date/URL furniture; the document draws its own running header and footer. The `doc-page` component already injects `print-color-adjust: exact` and `@page { margin: 0 }`, so backgrounds print. Chrome may not exit after writing the file — check for the PDF rather than waiting on the process.

5. **Compress with Ghostscript** — 150 dpi color/gray, DCT-encoded, duplicate-image detection, fonts kept embedded. Typically an 85-90% reduction, which is what makes it emailable.

   `gs` is a two-letter command and a common alias target, so a shell alias can shadow the binary and the compression step then fails in a way that reads as "Ghostscript is not installed." Resolve the real path with `command -v gs` and invoke that.

6. **Verify** per the checklist below.

## Procedure — .docx

1. **`scripts/prep_html.py <bundle-dir> <build-dir>`** — extracts the document's light DOM and applies the five structural repairs (see Failure modes). Writes `content.html` plus an optimized `img/`.

2. **`scripts/build_reference.py <build-dir>/reference.docx [--brand brand.json]`** — builds the Word style sheet: fonts, heading scale, accent color, callout and quote fills, table style, page geometry, and the running header/footer parts.

3. **Convert:**

   ```bash
   pandoc content.html -f html -t docx \
     --reference-doc=reference.docx --lua-filter=scripts/filter.lua -o "<Document>.docx"
   ```

4. **`scripts/post_process_docx.py "<Document>.docx" [--brand brand.json]`** — writes table borders as direct formatting and colors list markers. Required; see Failure modes.

5. **Verify** per the checklist below.

## Failure modes — eight silent, one loud

**Bookmarks.** Every HTML→docx converter generates an anchor id per heading, and each becomes a Word bookmark that Google Docs renders as a stray marker. The Lua filter strips identifiers from headings, divs, spans, tables, figures, cells, and rows. Verify zero `w:bookmarkStart` in `word/document.xml`.

**Table borders defined in the style.** Word honors style-level `w:tblBorders`; **Google Docs discards them on import** and only respects borders written directly onto each table and cell. Style-only borders means invisible tables in Docs. `post_process_docx.py` writes them directly onto every table and every cell.

**Backgrounds on empty elements.** Color swatches are often empty `<span>`s with a CSS background. Nothing carries that into a .docx — the column goes blank with no sign anything is missing. `prep_html.py` generates real chip images from the hex values.

**CSS grid reading order.** A two-column grid's DOM order is column-interleaved (1, 7, 2, 8...). Flattened into a document, that's the order it reads. `prep_html.py` re-sorts to reading order.

**Nothing is a list unless it's marked up as one.** These bundles frequently contain no `<ul>`/`<ol>`/`<li>` at all — visual lists are styled paragraphs. `prep_html.py` converts the contents block into real `<ol>` lists (decimal for sections, `type="A"` for appendices) so Word and Docs get genuine numbering. Before converting anything else, check whether the source renders it as a list; if the original shows plain paragraphs, converting them changes the author's document rather than the format. Ask the operator — that's an authoring decision.

**Margins on inline elements.** A `margin-right` on a number span has no equivalent in a Word run, so numbers run into titles ("1Purpose", "ESTIMATE$12,000"). The filter inserts real spacing characters.

**Multi-part figures.** A `<figure>` holding label + image + caption makes pandoc emit a two-column figure table, halving every image. `prep_html.py` hoists the label out. Related: pandoc sizes images from the `width` attribute in px (inline `style` widths are ignored), so images are saved at 96 dpi and given explicit pixel widths, with the source's max-height honored so tall plates still fit a page.

**List marker color.** Markers take formatting from the paragraph mark, not the runs, so an accent color needs an `rPr` inside each list paragraph's `pPr`. Handled by `post_process_docx.py`.

**Vector images crash the .docx path.** Pillow is a raster library. `prep_html.py` opened every `<img>` source with it, and an SVG raises `UnidentifiedImageError`, which propagated out and took the whole .docx build down: not a degraded document, no document. Any bundle whose logo is an SVG hits this, which is most bundles that have a logo. `prep_html.py` now drops `.svg` / `.svgz` / `.eps` / `.pdf` sources from the .docx input and names each dropped file on stderr. The PDF path is unaffected, since Chrome renders vectors natively; to keep a vector in Word, export it to PNG and repoint the tag.

**That last one is the opposite shape from the eight above.** They produce a file that opens fine and is quietly wrong. This produced no file at all, and after the fix it produces a correct file with a stated omission. The drop is reported loudly on purpose: a missing logo the operator was never told about would just be the ninth silent failure.

## Brand configuration

The scripts read an optional JSON file:

```json
{
  "bodyFont": "Open Sans",
  "headFont": "Roboto",
  "accent": "D6503A",
  "text": "2D2D2D",
  "calloutFill": "FBEFE8",
  "quoteFill": "FFF8F4",
  "rule": "F0D9C8",
  "tableGrid": "C8A78C",
  "tableHeadGrid": "A97A57",
  "tableHeadFill": "F6E4D7",
  "headerLeft": "Organization Name",
  "headerRight": "Document Title",
  "footerLeft": "Footer note",
  "footerRight": "Address or reference"
}
```

Derive the colors from the bundle's own `_ds/*/tokens/colors.css` so the Word file matches the source. Translucent tints (`rgba(...)`) must be flattened against white first. `scripts/brand.example.json` ships with neutral placeholder values — copy it to `brand.<project>.json` and fill in from the bundle.

## Verification checklist

Run all of it. Structural checks catch what visual checks miss, and vice versa.

**Structural** (read `word/document.xml` / `pdfinfo`):

- Page count and page size match the source's setup
- Zero `w:bookmarkStart`
- `w:tblBorders` present on every table; `w:tcBorders` on every cell
- `w:numPr` present on list paragraphs; numbering formats correct
- Image extents sane — full-column plates near the text width, not half
- Fonts: for the PDF, embedded; for the .docx, named in `styles.xml`

**Visual** (render to images and actually look):

- PDF: rasterize with `pdftoppm` and read the title page, a body page, and an appendix plate
- .docx: convert to PDF with `soffice --headless --convert-to pdf` and read the same
- Check the smallest text in any image-heavy plate at 300 dpi before and after compression

**Content parity:** extract text from both outputs and compare word counts. Differences should trace only to ligature artifacts in PDF extraction ("specification" → "speci" + "cation"), never to missing content.

## Outputs

- `<Document>.pdf` and/or `<Document>.docx`, placed alongside the source bundle unless the operator says otherwise
- The source bundle unchanged
- A summary naming what was verified, and any authoring decisions left to the operator

## Known limitations

- Both outputs are point-in-time snapshots; neither follows edits to the HTML source
- Fonts named in the .docx render properly in Google Docs (Roboto and Open Sans are native there) but substitute in desktop Word unless installed locally
- Word list numbering adds a period ("1." not "1"); avoiding it means fake numbers typed as text
- Multi-column CSS layouts become linear; that is inherent to a reflowable format

## References

- [`scripts/`](scripts/) — the toolkit
- AICONFIG.md `## FILE OPERATIONS` — edit through tools, not terminal in-place writes
- AICONFIG.md `## CORE INSTRUCTIONS` — no commits without per-batch authorization; these exports are left uncommitted
- Worked example: `aiconversations/business/msslc-transformation-conversation.md`, August 6-7, 2026 — the Campus Renovation Plan export where every failure mode above was found and fixed
