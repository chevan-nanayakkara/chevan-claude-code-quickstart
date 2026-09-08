# cwos/ Changelog

Per-inhabitant change log for the CWOS starter inside [`chevan-quickstarts`](../). For umbrella-level changes (new inhabitants, structural reorganization, top-level docs), see [`../CHANGELOG.md`](../CHANGELOG.md).

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) loosely followed; versioning [SemVer](https://semver.org).

**This is the CWOS release line.** CWOS is developed in `workspace-chevan` (trunk) and released here: each `cwos-vX.Y.Z` tag is a release of the starter, and the entries below are its release notes. Consumer instances adopt a release by tag and record which one they are on. See [`WHY-CWOS.md`](WHY-CWOS.md) "Status".

---

## [1.18.0] — 2026-09-07

### Fixed

**The starter's front door was handing newcomers a silent subset of itself.** `cwos/README.md` advertised "four universal Agent Skills" and "four universal reference docs" while fourteen skill directories and seven reference docs shipped, and the Pattern 1 copy-paste fetch block hardcoded the same 2026-era four-and-four. Anyone bootstrapping that way got a working install missing `document-export`, the entire cross-surface handoff lane, both cold-start skills, the project-management trio, `frontmatter-validate`, the C+E permissions posture, the portable writing standards, and the handoff protocol, with nothing to signal the gap. A visible gap is recoverable; a silent subset is not, because the reader has been told that is everything there is.

- **Pattern 1 now fetches every skill and every reference doc**, and the lists were validated against the filesystem rather than typed from memory.
- **`document-export`'s `scripts/` toolkit is fetched too.** The loop pulled one `SKILL.md` per skill, which for the only skill in the starter that ships executable support left an install whose documented procedure cannot run. That was the sharpest edge of the same defect.
- **The block now names itself a snapshot** and points at the two folder READMEs as authoritative, with Pattern 2 named as the path that installs everything without anyone maintaining a list. The lists can drift again; the reader will know where truth is.

### Changed

**The implementation-layer index dropped its per-artifact lists in favor of lanes plus pointers.** Counting artifacts in `cwos/README.md` put the same inventory in three places, and the copy that goes stale is always the one furthest from the files. `skills/` is now described by its lanes (core workflow, maintenance, session orientation, project management, cross-surface handoffs, document production, plus the authoring template) and `reference/` by what it covers, each naming its own README as the authoritative inventory. No counts remain in either line: a number is the part that dates first.

**The writing-scope prompt line lost its em-dashes.** v1.17.0 shipped the line as sent, with two em-dashes four lines above the block's own "No em-dashes." Not a rule violation, since a prompt block is documentation, but the block exists to be pasted by people who never read the section above it, and a rule that has to be defended against the text beside it gets ignored. Upstream rewrote it as two sentences with a colon carrying the list; ported verbatim into both prompt blocks.

---

## [1.17.0] — 2026-09-07

### Added

**`operations/cwos/README.md`, the implementation-layer README the starter told adopters to write and never shipped.** `CWOS-SETUP.md` Step 2 lists the file and describes its job, and every other file in that tree had a template behind it. Genericized from the upstream reference implementation: the four-folder framing became three plus a conditional fourth, and the dated folder-move provenance and the repo-specific ledger path came out. What survives is the part that earns the file, the statement that `handoffs/` does not map onto the configuration / state / procedure split, and the three-way "what goes where" list.

Shipped as a populated `README.md` rather than a `_template.md`, because that is what `CWOS-SETUP.md` tells an adopter to create and what the sibling folders already carry. The deviations section ships as an italic instruction the adopter deletes once it has real content. Registered in `cwos/README.md`'s implementation-layer list, its Pattern 1 fetch block, and `CWOS-SETUP.md`'s "directly copyable" list.

**The scope note the writing standards were missing.** The em-dash prohibition and the watermark rules stated a rule without saying what it governed, which is why a reader could not tell whether a changelog entry using an em-dash was a defect. It was not: the rules govern prose written in the operator's voice, and technical documentation is written in an institutional register that has never been held to them. Ported from upstream AICONFIG v5.14.0.

- **`AICONFIG.template.md`** — new `### What these rules govern` subsection opening `## STANDARDS - WRITING`, ahead of Voice and Tone.
- **`operations/cwos/reference/writing-style-portable.md`** — the same text as `## What These Rules Govern`, ahead of Voice and Tone. This is the copy that matters: the file is built to be dropped into repositories where nobody has the surrounding context, and an unscoped prohibition there gets over-applied or quietly ignored.
- **Both operator prompt blocks** gain a scope line ahead of "Write in prose."
- The bare "No em-dashes" bullet is unchanged; it inherits scope from the section it now sits under.

**The rule was never being violated. It was never scoped.** That is the distinction the new text records, and the reason this is an addition rather than a correction.

### Changed

**`CWOS.md` gains the conditional note under the hub tree**, so the spec and the setup guide agree about `handoffs/`: create it when the first handoff is written, not at bootstrap. The paragraph closes by saying why the other three folders are unconditional, which turns the exception into a test the next person adding a folder to that tree can apply.

**`CWOS-SETUP.md` Step 2 restructured to match upstream exactly.** v1.16.0 put `handoffs/` inside the main scaffolding tree. Upstream adopted the fix but split the conditional folder into its own block after the tree, which reads better: what an adopter creates at bootstrap stays visually separate from what waits for a reason to exist. Step 2 is now byte-identical to the upstream copy, and Scenario A's layout went back to three folders for the same reason.

---

## [1.16.0] — 2026-09-07

### Added

**`handoffs/` in the spec's hub-repo structure, closing the gap v1.15.0 left open on purpose.** The portable spec's hub tree listed `memory/`, `skills/`, and `reference/` and stopped there, which is what v1.15.0's release notes recorded as deliberate: the starter's handoff lane had to name the operations layer before the spec could describe it. It does, so the spec follows. Tree block and the paragraph under it ported verbatim from the upstream reference implementation.

- **`CWOS.md`** — `handoffs/` added to the hub tree with `<project-name>/` and the `YYYY-MM-DD-HHMM-<from>-to-<to>.md` filename beneath it. The only other lines that moved are `reference/` from `└──` to `├──` and its four children from spaces to `│`.
- **The paragraph under the tree states that `handoffs/` is a fourth folder, not a fourth layer.** The first three are the configuration / state / procedure split; handoffs are correspondence, an inbox and an outbox, rather than a fourth kind of knowledge. Without that sentence a reader counts four boxes in the tree and goes looking for a fourth entry in a three-layer model.

**`CWOS-SETUP.md` now scaffolds the folder it tells you to use.** Both layout trees in the setup guide stopped at three folders, so a repo bootstrapped from the guide came up without the folder the handoff protocol in the same starter routes files into.

- Scenario A's layout gains `handoffs/`, marked as conditional on the hub exchanging work with other surfaces.
- Step 2's `operations/cwos/` tree gains `handoffs/<project-name>/` and, under `reference/`, the `handoff-protocol.md` that shipped in v1.12.0 and was never added to this list. Step 2's instruction line said "the three-folder structure" and now names the layer instead.
- One sentence after that tree says `handoffs/` is the only conditional one of the four: a repo that never crosses surfaces does not need it, and a repo that does should create it here rather than under `working/` or another scratch area.

---

## [1.15.0] — 2026-09-07

### Fixed

**`document-export` crashed on any bundle containing an SVG.** `prep_html.py`'s `convert_images()` called `Image.open()` on every `<img>` source. Pillow is a raster library, so a vector source raised `UnidentifiedImageError`, which propagated out and took the entire .docx path down: not a degraded document, no document. Any bundle whose logo is an SVG hit it, which is most bundles that have a logo. The skill's other eight failure modes all fail silently; this one was the loud one, and the only defect that produced no output at all.

- **New module-level `VECTOR_EXTS = (".svg", ".svgz", ".eps", ".pdf")`**, sitting with the other tuning constants and carrying the reason in a comment.
- **A guard in `repl()`, placed after the existing `img/` check** so already-built assets still pass through untouched. Matching is case-folded, because a bundle carrying `LOGO.SVG` should not slip through.
- **Dropped loudly, not silently.** Each dropped file is named on stderr after the `images:` line, with the note that the PDF path is unaffected (Chrome renders vectors natively) and the remedy: export to PNG and repoint the tag. A silent drop would have made this the ninth silent failure in a skill whose premise is that silent failures are the enemy.
- **`SKILL.md` records it as a ninth failure mode**, with the section heading changed from "each of these fails silently" to "eight silent, one loud" and a paragraph stating that this one is the opposite shape from the other eight. A reader skimming the list would otherwise assume it is uniformly about silent corruption.

### Added

**Ghostscript alias note** in `document-export`'s PDF procedure. `gs` is a two-letter command and a common alias target, so an alias can shadow the binary and make the compression step read as "Ghostscript is not installed." Resolve the real path with `command -v gs`. Stated as the general case, not as one machine's configuration.

### Changed

**The handoff lane now states where handoffs live rather than naming a scratch path.** `handoff-protocol.md`'s `{{HANDOFF_DIR}}` definition shipped in 1.12.0 pointing at `working/cwos-handoffs`. Handoffs are the durable record of what a receiving surface was told and what it returned, and they routinely stay live for weeks, so the "this is scratch" framing was wrong. The definition now states the convention first — handoffs belong in the operations layer, one folder per project, alongside `memory/`, `skills/`, and `reference/` — and gives `operations/cwos/handoffs/<project>/` as what that means in a CWOS repository, with an explicit warning against filing them under `working/`.

The starter needed the change in one place only. Every other consumer (`handoff-write`, `handoff-inbox`, `spoke-cold-start`, the skills README) already reads `{{HANDOFF_DIR}}` from the reference doc rather than hard-coding a literal, which is what the 1.12.0 genericization bought.

### Notes

**`CWOS.md`'s hub-repo structure tree still lists three operations folders** (`memory/`, `skills/`, `reference/`) and does not include `handoffs/`. Deliberately unchanged here: that tree is the portable spec, and the upstream reference implementation holds the pen on it. The spec catches up after the starter does, in that order.

---

## [1.14.0] — 2026-09-07

### Changed

**Tasks-file standard: Notes / Reference is now pointers only.** `AICONFIG.template.md` `#### Tasks File Structure (Standard)` item 5 previously described this section as a "catch-all for context the work depends on" and a "reference shop" while every example it gave was a pointer. That wording is what licensed the drift it now forbids: an upstream survey of 32 `-tasks.md` files found roughly eight holding genuine reference content, meaning those files were following the standard rather than breaking it. Every repo bootstrapped from this template inherited the same leak, so the fix lands at the source.

- **Pointers only**, stated as a prohibition rather than a preference, with the section's job restated as *where to look, not what is true*.
- **The diagnostic travels with the rule:** close every project in the file; whatever is left standing was never project state.
- **The distinction named:** orchestration content changes when the work moves, reference content changes when the world moves. A `-tasks.md` file holds only the first kind.
- **Four-destination routing** for content that does not belong: the companion domain folder (via the `companionTo` frontmatter field every conversation file already carries), the conversation file for reasoning, `operations/cwos/memory/decisions/` for ADRs, `operations/cwos/reference/` for durable procedure and specification.
- **The five `##` sections are declared the complete permitted set** — no preamble above Open Projects, no appendix below Notes / Reference. A strategy briefing on top of a project tracker is the same defect wearing a different heading level.
- **Companion rule for conversation files** stated inline: when substantial structured content accumulates beyond dialogue, extract it and leave a pointer. Each of the three files holds one kind of thing.

### Fixed

The "Why this section order" paragraph at the end of the same section still called Notes / Reference "the stable reference shop," contradicting the rule above it. Reworded to "the pointer index."

---

## [1.13.0] — 2026-09-07

### Added

**Writing-style standards ported from the upstream reference implementation.** `AICONFIG.template.md` `### Avoid AI Patterns and Watermarks` grew from four word-level bullets to the full standard, and the same content ships in standalone vendor-neutral form as `operations/cwos/reference/writing-style-portable.md`.

- **Structural anti-patterns** — eight named generative habits with a mechanism and a fix each: corrective antithesis, trailing significance, metronomic rhythm, compulsive triads, meta/roadmap paragraphs, restatement close, performed judiciousness, colon-plus-fragment. The framing that motivates them: word-level bans are the weakest instruction because the model routes around them.
- **Borrowed technical jargon used as emphasis** — the existing figurative `load-bearing` ban generalized to a shelf of fourteen terms, each glossed with the plain word it is standing in for, plus the substitution diagnostic.
- **Obtuse principle as change of subject** and **balanced construction ("X is Y, and it is also Z")** — two AI-cadence patterns surfaced August 28, 2026 in the upstream hub and codified there September 7, 2026. Each ships with a flagged example, a fix, and (for the second) a diagnostic.
- **Operator writing-style prompt block** — a vendor-neutral copy-paste form of the whole section for AI sessions that do not auto-load `AICONFIG.md` (Cursor, Codex, ChatGPT, Gemini), including the two lines for the new patterns above.
- **"The thing underneath"** — the closing frame explaining why each habit above is a shape that signals a conclusion has been reached, with the single-sentence falsifiability diagnostic.
- **New reference doc:** `operations/cwos/reference/writing-style-portable.md`, registered in that folder's `README.md`. Drop-in for non-CWOS repos as `WRITING-STYLE.md`, referenced from whatever config file the target repo's AI tool reads.

### Notes

Released before `1.12.0`, which was reserved at the time for the handoff-lane port and shipped later the same day. The out-of-sequence ordering is deliberate: reserving the number rather than renumbering kept this starter's releases aligned with the upstream release plan.

---

## [1.12.0] — 2026-09-07

### Added

**The cross-surface handoff lane, genericized.** Four artifacts that let an operator running AI sessions in more than one repository move work between them as durable files rather than chat messages. Ported from the upstream reference implementation and stripped of its ecosystem: no hub or spoke names, no cross-repo relative paths, no incident history.

- **New reference doc: `operations/cwos/reference/handoff-protocol.md`.** Surface taxonomy (`hub`, `<spoke>-cli`, browser surfaces, and the prefix convention for other AI tools), the `YYYY-MM-DD-HHMM-<from>-to-<to>.md` filename convention, the YAML frontmatter spec, and the routing rule. Opens with a `{{HUB_REPO}}` / `{{HUB_PATH}}` / `{{HANDOFF_DIR}}` configuration block; the three skills read their paths from here rather than hard-coding them.
- **New skill: `handoff-write`.** Interactive authoring. Gathers the frontmatter fields, computes the filename and destination, and writes a structured body (Context / The ask / Standing rules / Return handoff / Origin).
- **New skill: `handoff-inbox`.** Read-only companion. Lists handoffs addressed to the current session's surface and not yet answered, auto-detecting the surface from the working directory. Frontmatter-first parse with a filename fallback; reply-tracking via `in-reply-to` where present, explicitly labeled heuristic where not.
- **New skill: `spoke-cold-start`.** Orientation for a session running in a spoke or development repo, and the narrow counterpart to `cwos-cold-start`. Loads the behavioral charter, the handoff protocol, and this surface's inbox, then deliberately stops. Registered in the existing Session orientation lane; the two handoff skills get a new **Cross-surface handoffs** lane in `skills/README.md`.

**The rule the lane exists to enforce:** a handoff lands in the receiver's inbox, except when the receiver is a shared code repository, in which case it stages hub-side. The reference doc argues the case rather than just stating it, because both simpler formulations are wrong in opposite directions — "hub-side always" strands hub-to-hub handoffs where the receiver never looks, and "receiver's inbox always" pushes one operator's workflow artifacts into repositories that collaborators, other organizations, and future maintainers read.

### Notes

**No memory file ships with this lane.** Upstream, the routing rule is also carried as `operations/cwos/memory/feedback_handoff_prompts_are_files.md`. This starter's `operations/cwos/memory/README.md` states that only templates live here and that real memory content is per-repo, so shipping a populated `feedback_*.md` would break that policy. Instead, `handoff-protocol.md` carries the full text of the memory an adopting repo should create, under **Recommended companion memory**, with a note to index it in `MEMORY.md`. The rule reaches the always-loaded layer without the starter contradicting itself.

**Frontmatter gained a `supplements:` field** not present upstream. It came out of using the protocol: a handoff that has already been sent must not be edited, because sender and receiver then hold different documents with no way to tell. A supplement is a new file that names what it extends.

---

## [1.11.0] — 2026-08-07

### Added

**New skill: `document-export`.** Convert a self-contained HTML design-document bundle (`*.dc.html` + `_ds/` design system + `assets/` + `uploads/`) into an email-ready PDF and a Google-Docs-friendly `.docx`. Ships with a bundled `scripts/` toolkit (~900 lines Python + Lua) — the first `scripts/`-bundled skill in this starter.

- Two render paths: **PDF** via headless Chrome + Ghostscript compression; **docx** via pandoc + a brand reference.docx + a lua filter for anchor stripping.
- Codifies **seven silent-failure modes** with cause and fix:
  1. Word style-level `w:tblBorders` is honored by Word but discarded by Google Docs on import → borders must be written as direct formatting onto every table and cell.
  2. Every HTML-to-docx converter emits heading anchor ids that become Word bookmarks, which Docs renders as stray markers → strip ids during conversion (`filter.lua`).
  3. Bundle fonts are `@font-face` in the design system; Chrome renders them but Word cannot embed URLs → localize the fonts into a system-installable folder before rendering.
  4. Chrome print media crops narrow images at print-page width → normalize `<img>` extents in `prep_html.py`.
  5. Design-system callouts render via CSS gradients + JavaScript web components → `prep_html.py` transforms the light DOM into pandoc-friendly markup before conversion.
  6. Ordered lists show as run-together numbers when the design-system stylesheet is preserved intact → strip the numbered-list rules from the localized CSS.
  7. Two-column contents grid loses one column in Word → collapse to a single ordered list during prep.
- **Brand-as-config** pattern: `scripts/brand.example.json` is a neutral placeholder. Copy to `brand.<project>.json` and derive colors from the bundle's own `_ds/*/tokens/colors.css` (rgba tints flattened against white first).
- Ports the skill authored in `chevan-content` on August 6-7, 2026 (driving conversation: `aiconversations/business/msslc-transformation-conversation.md`), scripted, verified against a real bundle (paragraph styles / character styles / bookmark count / table count / borders / list numbering / image extents / declared fonts / header-footer parts all reproducible), then genericized for public reuse.
- `scripts/prep_html.py`'s transforms are pattern-matched against the Claude design-document export family (`<doc-page>` light DOM, `slot="header"`, `<sc-if>`, swatch spans, two-column contents grid). Each transform no-ops harmlessly when its pattern is absent, so the toolkit is safe on other bundles, just less useful.

Registered in `cwos/operations/cwos/skills/README.md` under a new **Document production** lane; the `README.md` file version bumped to reflect the new skill.

Chevan-content's skills index (v1.2.0, August 7) is the source-of-truth registration; this starter mirrors the lane structure.

---

## [1.10.0] — 2026-07-22

### Changed

**Tasks File Structure standard restructured (June 20, 2026 second revision + July 22, 2026 Priority-order convention added).** The prior four-section layout (Summary of Open Projects / Notes/Reference / Open Projects / Closed / Completed Projects) is replaced with a cleaner five-item layout:

1. YAML frontmatter
2. Title and header information
3. **Open Projects** — leads with `### Summary` subsection + NEW `### Priority order (AI-maintained recommendation)` subsection + per-project detail blocks
4. **Closed Projects** — leads with `### Summary` subsection + detail blocks (renamed from "Closed / Completed Projects")
5. **Notes / Reference** — at the end (moved from position 2; renamed from "Notes/Reference")

Section-name simplifications: `Closed / Completed Projects` → `Closed Projects`; `Notes/Reference` → `Notes / Reference`. Each of Open Projects and Closed Projects now leads with its own focused `### Summary` subsection instead of a single standalone summary section — keeps open-vs-closed digests separate.

**New: `### Priority order (AI-maintained recommendation)` subsection (July 22, 2026 convention).** Sits under Open Projects right below `### Summary`. Carries the AI's current recommended ranking of the file's open projects — a durable answer to "if I picked up this thread cold, what should I work on first?"

- Item-level provenance markers: `*(AI)*` (AI-ranked; free to re-rank on next groom) or `*(operator)*` (manually set; preserved verbatim on subsequent groomings). Unmarked = treated as `*(AI)*` for backward compat.
- Bounded write scope: AI writes to only this subsection during grooming. Everything else in Open Projects, all of Closed Projects, and all of Notes / Reference stays operator-authoritative.
- Convention originated in workspace-chevan July 22, 2026; also in chevan-content AICONFIG.md (July 22 same-day port); this v1.10.0 release ships it into the public starter.

**New grooming rule — move the row Open→Closed on close (the most commonly missed step).** When a project completes, in the same edit move its row from `Open Projects → ### Summary` to `Closed Projects → ### Summary` AND migrate its detail block. Prevents the corruption where a completed project stays listed as if open — which the open-projects skill would then propagate into the hub rollup.

**`operations/cwos/skills/open-projects/SKILL.md` updated** to understand three tasks-file formats during transition (newest first: current `## Open Projects → ### Summary`, intermediate `## Summary of Recent Work → ### Open Projects`, oldest `## Summary of Open Projects`). Prefers newest when parsing. New Step 2 summary-staleness check: watches for completed items in the open digest and captures them as cleanup findings (safety net for the grooming rule above).

### Notes

This v1.10.0 release closes the standard-parity gap between chevan-content and chevan-quickstarts that had been flagged since June 20. Workspace-chevan is separately maintained (its own hub, not part of the chevan-content/chevan-quickstarts cluster) — the same standard already applies there.

Bumped MINOR per SemVer (behavioral standard change; backward-compatible parsing via the three-format tolerance in the skill).

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-07-22 5:06PM refresh batch).

---

## [1.9.0] — 2026-06-17

### Added

**`## Priority View` section pattern in `aiconversations/0-project.template.md`.** Pattern originated in workspace-chevan June 17, 2026. Manually-maintained tiered priority outline (P1-P4 style) sits above the auto-derived domain rollup body. Answers "what should I work on next?" — distinct from the auto-derived rollup which answers "what specific projects are open?" The `prioritize-open-projects` skill produces an ephemeral version of this analysis on demand; the Priority View section is the persistent home where the latest tiered view lives.

**`operations/cwos/skills/open-projects/SKILL.md` updated to preserve the Priority View section on regeneration.** Step 4 of the skill explicitly captures everything between `## Priority View` and the next top-level `## ` heading, holds it, and writes it back verbatim after the auto-derived rollup body is regenerated. Operator's hand-maintained content is never overwritten by the regeneration. If `0-project.md` does not exist yet, the Priority View block is also not written by the skill — the operator adds it on first manual edit, and subsequent regenerations preserve it.

**`operations/cwos/reference/permissions-posture-ce.md`** — new reference doc documenting the C+E permissions posture as the recommended starting shape for `.claude/settings.local.json` in CWOS-aligned repos. Three-layer model: auto-allow read tools + Edit/MultiEdit + read-only Bash + read-only `gh`; ask gates Write and mutating Bash; hard-deny destructive Bash. Codified in workspace-chevan June 14, 2026; ported to chevan-content and chevan-quickstarts June 16, 2026. Includes background (March 2026 incident rationale), three-layer detail, per-repo customization guidance, verification probes.

`operations/cwos/reference/README.md` index updated to include the new doc.

### Notes

The Priority View pattern keeps the manual-prioritization layer in the same file as the auto-derived rollup, so a single read gives the operator both *what's open* and *what to do first*. The skill's preservation logic makes the pattern safe to use — operators can hand-edit the Priority View freely without worrying about the next auto-regeneration clobbering their work.

The C+E permissions reference doc joins the existing reference set (`taxonomy.md`, `conventional-commits.md`, `agent-skills-standard.md`, `mcp-stack.md`) — five reference docs now in the CWOS starter. Future bootstrappers get the recommended permissions shape documented upfront rather than discovered through trial and error.

Bumped MINOR per SemVer (new pattern + new reference doc + behavioral change to existing skill, backward-compatible via the if-not-present fallback).

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 10:16PM refresh batch).

---

## [1.8.0] — 2026-06-16

### Added

**New `## FILE OPERATIONS` top-level section in `AICONFIG.template.md`** (placed after `## STANDARDS - MAINTENANCE`, before `## 📋 REFERENCE`) with subsection `### Editing files: use the Edit/Write tools, not terminal in-place edits`.

The rule: when changing a file's contents, use the dedicated Edit and Write tools, never terminal in-place edits (`perl -i`, `sed -i`, `awk -i`, or `>` / `>>` redirects that rewrite a file). Terminal writes bypass the editor sync, so if the file is open in the operator's editor, the editor's buffer overwrites the terminal change on its next save and silently reverts the work. Terminal reads/searches (`grep`, `wc`, `cat` for inspection) are fine; only *writes* must go through the tools. Bulk transforms that are genuinely unavoidable need the operator to close or reload the file first.

### Notes

Origin: June 16, 2026, in workspace-chevan — a `perl -i` pass adding horizontal-rule separators to a conversation file was applied to disk correctly but reverted twice by the operator's open editor saving its older buffer; Edit-tool entries in the same session survived because they synced to the IDE. workspace-chevan codified the rule in its own AICONFIG.md `## FILE OPERATIONS` section the same day; chevan-content carries the matching rule in v5.12.0; this v1.8.0 release ports the rule to the chevan-quickstarts CWOS template so the rule reaches all future bootstrapped repos.

This is a general AI-editing-discipline rule, not specific to any one repo's content shape. Bumped MINOR per SemVer (new behavioral rule).

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 10:07PM, seeded from workspace-chevan).

---

## [1.7.0] — 2026-06-16

### Added

**`#### Tasks File Structure (Standard)` subsection in `AICONFIG.template.md`** — codifies the four-section layout (Summary of Open Projects / Notes/Reference / Open Projects / Closed / Completed Projects), four-level hierarchy (`### Project N:` / `#### Phase N:` / `**Deliverable**` / `- [ ] Task`), and the "Why this section order" rationale. Lifted from chevan-content `AICONFIG.md` (v5.11.0 codification) and workspace-chevan `AICONFIG.md` (June 10, 2026 originator). Was flagged as candidate v1.5.0 / v1.6.0 work in prior changelog entries; now shipped.

**`Conversational Work Help` section in `aiconversations/0-work-status.template.md`** — the canonical skill-invocation reference block (work management, conversation file maintenance, session orientation, run-prompt workflow, bootstrap/migration, skill management, configuration sources, standing rules). Same content the implementation repos (chevan-content, workspace-chevan) use, with one principled adaptation noting that `work-status-dashboard` skill is repo-specific and not shipped in the starter.

### Changed

**Canonical structure rules codified in `aiconversations/README.md`** — the structural invariants for `0-work-status.md` and `0-project.md` across CWOS-aligned repos:

- Parallel lean frontmatter schema (documentType / purpose / version / versionNote / lastUpdated / lastUpdatedNote / status / location / companionSurface / generatedBy).
- 0-work-status.md section structure: tables (`## N. Domain Name`) + Maintenance notes + Conversational Work Help.
- 0-project.md section structure: domain sections mirroring 0-work-status.md's table set + Files needing cleanup (optional) + Notes on this rollup.
- **Mirror rule**: 0-project.md section numbering and labels MUST mirror 0-work-status.md's table set so the two surfaces cross-reference cleanly.

**`aiconversations/0-work-status.template.md` frontmatter cleaned up to canonical lean schema** — switched from the prior multi-line `purpose: |` block to a one-line `purpose:`; added `version` + `versionNote` fields; consolidated the `lastUpdatedNote:` description. Added a "Canonical structure note" paragraph in the template body explaining the mirror rule with `0-project.md`.

**`aiconversations/0-project.template.md` restructured to use mirror-numbering** — sections changed from `## DOMAIN 1` to `## 1. Domain Name` to match the dashboard's table numbering convention. Added "Canonical structure note" paragraph explaining the mirror rule. Added optional "Files needing cleanup" section between the domain sections and Notes section. Frontmatter aligned to the canonical schema.

### Notes

These changes close the structural-parity gap between `0-work-status.md` and `0-project.md` across the three CWOS implementation repos. Future bootstraps now have:

- A documented frontmatter schema (lean, optional-field-aware)
- A documented section structure for both files
- The mirror rule made explicit (cross-reference between dashboard tables and rollup sections)
- The tasks-file standard available in the AICONFIG template (no more need to re-author per repo)

The existing implementation repos (chevan-content, workspace-chevan) have files that mostly match the canonical structure but with legacy frontmatter shape differences. Per the standing "don't force a one-off reshuffle" rule, those files converge naturally at the next meaningful edit rather than via a forced rewrite.

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 5:50PM).

---

## [1.6.0] — 2026-06-16

### Changed

**`refresh-work-management` skill extended to chain `prioritize-open-projects` as Step 3.** Previously the orchestrator ran two steps (dashboard refresh + projects rollup refresh); now it runs three steps with prioritization as the final read-only analytic pass. Single command (`refresh work management`) now produces the full work-management workflow: dashboard + rollup + priority outline.

- Description updated to mention the prioritization step explicitly so the AI invokes the orchestrator on prompts like "what should I work on?" as well as the prior "refresh the dashboards" / "what's active?" triggers.
- New `--skip-prioritize` flag preserves the v1.5.x and earlier two-step behavior for cases where the operator wants refresh without analysis.
- New Step 3 in the procedure invokes `prioritize-open-projects` against the just-refreshed rollup.
- Combined report (Step 4) expanded with a "Priority outline" section showing tiers produced, "Recommended focus this week" pick, and closure candidates flagged.

The three underlying skills (`work-status-dashboard`, `open-projects`, `prioritize-open-projects`) remain independently invokable. The orchestrator is the recommended common case; the individual skills are for edge cases (only-dashboard, only-projects, only-prioritize).

### Notes

This is a behavioral change to an existing skill — bumped MINOR per SemVer. Operators who scripted the orchestrator's prior two-step behavior can pass `--skip-prioritize` to preserve it.

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 5:31PM).

---

## [1.5.0] — 2026-06-16

### Added

**`prioritize-open-projects` skill** at `operations/cwos/skills/prioritize-open-projects/`. Reads the open-projects rollup (or walks `-tasks.md` files directly) and produces a priority-ranked tier outline (P1-P7-ish) with reasoning per tier and an honest "recommended focus this week" pick of 1-3 items. Read-only — does NOT modify `0-project.md`, `0-work-status.md`, or any `-tasks.md` file. Closes the gap between `open-projects` (which says *what's open*) and operator decision-making (which needs *what to do first*).

**Dashboard template files** at `aiconversations/`:

- `0-work-status.template.md` — Work-status dashboard skeleton with frontmatter, placeholder table set (5 tables with `{{TABLE N NAME}}` placeholders), and table-set adaptation notes. Bootstrappers copy and customize for their content domains.
- `0-project.template.md` — Open-projects rollup skeleton with frontmatter and domain placeholders. After bootstrap, the `open-projects` skill regenerates the content from real `-tasks.md` data.
- `README.md` for the folder explains the bootstrap procedure, the rationale for shipping templates (the dashboard FILE follows a stable shape; the dashboard-refresh SKILL stays repo-specific because table-set logic varies per repo).

### Notes

The companion `work-status-dashboard` skill is still NOT shipped in the CWOS starter — that remains a repo-specific authoring exercise per the existing v1.2.0 / v1.4.0 architectural decision. Shipping the dashboard template files closes a different gap: bootstrappers now have a structural starting point for the FILE without having to derive it from scratch, even though they still author the refresh SKILL themselves.

The reverse-parity tasks-file refinements from chevan-content v5.11.0 Part 2 (bullet-list summary, "Closed / Completed Projects" naming, "Project N:" numbering, "Why this order" rationale) are still NOT ported into `AICONFIG.template.md` — separate decision, still candidate for a later v1.6.0 if a bootstrapper wants the full Tasks File Structure standard pre-shipped rather than authored from scratch per repo.

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 5:18PM).

---

## [1.4.0] — 2026-06-16

### Changed

**`[End of Document]` marker deprecated for formal documents (parity with chevan-content v5.11.0 and workspace-chevan's earlier June 3, 2026 deprecation).** The marker added noise without value — git history is the record of completeness. Exception preserved: archive chunks still end with `[End of Document]` as an immutable historical record. Active conversation files end with the trailing user placeholder stub (already canonical).

Anyone bootstrapping a new CWOS repo from this starter no longer inherits the deprecated rule.

### Removed

- Trailing `[End of Document]` markers stripped from the four canonical starter files that carried them:
  - `cwos/AICONFIG.template.md`
  - `cwos/WHY-CWOS.md`
  - `cwos/CWOS-SETUP.md`
  - `cwos/AGENTS.md`
- `cwos/CWOS.md` and `cwos/README.md` were already free of the marker; no change needed.

### Notes

The chevan-quickstarts `AICONFIG.template.md` Formatting section had already been free of the explicit "End of document marker" rule for some time, so no behavioral-rule edit was needed there — this release is the file-content sweep that aligns the starter's own files with the rule's absence.

Reverse parity from workspace-chevan's June 10, 2026 tasks-file refinements (bullet-list summary, "Closed / Completed Projects" naming, "Project N:" numbering prefix, "Why this order" rationale) was NOT brought into this template release — those refinements live in chevan-content `AICONFIG.md` (v5.11.0) and workspace-chevan `AICONFIG.md`. They can be lifted into `chevan-quickstarts/cwos/AICONFIG.template.md` as a future v1.5.0 if a target repo bootstrapper wants the full Tasks File Structure standard pre-shipped rather than authored from scratch per repo.

Driving conversation: chevan-content `aiconversations/_system/operations/conversational-work-operations-conversation.md` (entry 2026-06-16 3:14PM).

---

## [1.3.0] — 2026-06-02

### Added

**Standards-consolidation step in the migration playbook (closes a real gap that emerged from reviewing the chevan-content migration history).** The original `operations/conversational-work/` install-pipeline pattern stored standards content (writing-style, conversation-files, document-layout, essay-workflow, etc.) in `ai-configs/github/prompts/<template>.md` templates that got "installed" into AICONFIG.md on demand. Migrating a repo that hasn't run the consolidation pass yet would functionally orphan that standards content when the LEGACY notice goes on `operations/conversational-work/`.

- `operations/cwos/skills/cwos-migrate-from-conversational-work/SKILL.md` — pre-flight check expanded to audit standards-consolidation state (templates present? AICONFIG.md STANDARDS sections populated?). Surfaces three states (A: consolidated, B: unconsolidated, C: no templates) and recommends a consolidation pass in Session B if the target is in State B. Session B procedure adds explicit step 7 covering the consolidation work — read each template, identify the right AICONFIG.md section, lift behavioral content, skip install-pipeline metadata, commit as `chore(aiconfig): consolidate ... from predecessor templates`.
- `CWOS-SETUP.md` "Migrating from operations/conversational-work/" — new "Standards consolidation (if predecessor templates have unconsolidated content)" subsection after "Cleanup horizon." Documents the three states, the per-template lift procedure, the canonical worked example reference (chevan-content v5.8.x changelog entries).
- Pre-flight check shell snippet in CWOS-SETUP.md migration section also expanded with the consolidation audit (`ls operations/conversational-work/ai-configs/github/prompts/` + `grep STANDARDS AICONFIG.md`).

**"What belongs in AICONFIG.md" framing clarification (clears up a real interpretive ambiguity).** The doc previously left implicit that writing standards, file conventions, brand guidelines, and other "non-AI" configurations are still AICONFIG.md content — the rules apply to humans and AI alike, so AICONFIG.md is the canonical home regardless of who's reading it.

- `cwos/WHY-CWOS.md` — new "### A note on what belongs in AICONFIG.md" subsection at the end of "The approach: three layers." Three-reason framing: AI auto-loads it, humans use it as canonical reference, multi-file drift gets prevented.
- `cwos/AICONFIG.template.md` — same clarification added under the three-layer-split decision tree. Cross-references CWOS-SETUP.md "Standards consolidation" for migration cases.

### Rationale

These additions emerged from a 2026-06-02 review of the chevan-content migration history (`v5.8.x` consolidation series → `v5.9.0` CWOS migration). The chevan-content case worked cleanly because consolidation predated the migration; the playbook silently assumed that pattern. For repos doing migration without the pre-consolidation work, the gap would functionally orphan standards content. v1.3.0 closes the gap by making the consolidation step explicit and surfacing the audit at pre-flight time.

---

## [1.2.0] — 2026-06-02

### Added

**Project-tracking pattern: distributed `-tasks.md` files with centralized rollup + orchestrator.** Codifies the solution to a visibility problem that emerged in workspace-chevan after months of operation: per-conversation `-tasks.md` files capture project state well, but cross-corpus visibility requires opening each file individually. The fix is a derived rollup that aggregates without breaking the capture convention, plus a thin orchestrator that refreshes both rollup surfaces in sync.

- `operations/cwos/skills/open-projects/` — new skill that walks `aiconversations/**/*-tasks.md`, extracts each file's "Summary of Open Projects" section, and assembles a domain → conversation → project view at `aiconversations/0-project.md`. Derived view; the `-tasks.md` files remain canonical detail. Companion to a repo-specific work-status dashboard (different signal, same shape). Only currently-open projects appear in the rollup; completed work stays in the source files. Skill auto-detects the repo's domain grouping from `0-work-status.md`'s top-level headings (or falls back to grouping by `aiconversations/` top-level folder if no dashboard exists yet).
- `operations/cwos/skills/refresh-work-management/` — thin orchestrator that invokes the repo's `work-status-dashboard` skill and the `open-projects` skill in sequence, ensuring both derived surfaces stay in sync. Composition pattern (over collapsing the two skills into one), matching the pattern already used by `conversational-maintenance-review` and `cwos-cold-start`. Recommended common-case invocation for "refresh the work management surfaces"; the two underlying skills remain available for edge cases.
- `AICONFIG.template.md` STANDARDS - OPERATIONS gains a new "Project tracking — distributed `-tasks.md` files with centralized rollup" subsection inside Conversation Files. Documents the capture/visibility split and points at the `open-projects` and `refresh-work-management` skills.
- `CWOS.md` "aiconversations — long-form dialogue threads" section gains a "Dual rollup pattern: work-state and project-state" subsection. Frames the two derived surfaces (`0-work-status.md` for thread-level, `0-project.md` for project-level) at the architecture level so future readers see the pattern as part of the aiconversations extension's design, not as a hidden skill.

### Rationale

The pattern emerged on 2026-06-02 when the workspace-chevan operator noticed that distributed `-tasks.md` files were going stale and undiscovered. The first instinct was to centralize all project tracking into a single file, but size analysis showed that approach would require structural rotation rules to bound growth — essentially recreating per-file isolation inside one big file. The cleaner answer was to add a rollup (derived view) alongside the existing `-tasks.md` files. This v1.2.0 codifies the rollup pattern at the starter level so future CWOS deployments get it from day one. Companion case study lives at the chevan-content knowledgebase (`knowledgebase/knowledge-architecture/cwos-migration-frontmatter-as-navigation-graph.md`) — the project-tracking pattern is part of the same operational maturity lane as the frontmatter-as-navigation-graph work.

---

## [1.1.0] — 2026-06-01

### Added

**Maintenance lane (3 new universal skills + supporting AICONFIG.template.md updates):** ported the maintenance-tooling pattern that emerged from the workspace-chevan May 31, 2026 post-CWOS-migration maintenance pass. These were authored in workspace-chevan (the second CWOS deployment) on 2026-05-31 to codify the drift-detection and periodic-review patterns; brought back into this starter so future CWOS deployments get the tooling lane from day one.

- `operations/cwos/skills/frontmatter-validate/` — detection-only skill that walks every conversation file's YAML frontmatter and reports dangling structural pointers (`companionTo`, `archives`, `parentConversation`, `subConversations`, `relatedDocuments`, `location`, `companionTasks`, plus optional `companionRepo`/`companionPath`). Codifies the 4-rule maintenance pattern (A: cross-system path migrations; B: root-folder relocations; C: stale archive folders; D: sibling renames + dangling drops).
- `operations/cwos/skills/conversational-maintenance-review/` — periodic detection-only orchestrator. Runs the four-phase sweep (frontmatter validation → size-threshold scan → status/activity scan → optional dedup heuristic) and produces a punch list grouped by which skill should fix each finding. Designed for the CWOS quarterly review schedule. Invokes `frontmatter-validate` for Phase 1.
- `operations/cwos/skills/cwos-cold-start/` — invokable cold-start session-orientation skill. Reads canonical files (`AICONFIG.md`, `README.md`, `CWOS.md`, `operations/cwos/README.md`, memory index, work-status dashboard if present) and produces an absorbed-state summary covering architecture / repo context / current active work / open re-entry briefs / recent governance decisions. Read-only; the invokable equivalent of the cold-start prompt template in the repo's README.md.

**AICONFIG.template.md updates:**

- New `### Cross-repo pointer convention (hub→spoke companions — optional)` subsection under STANDARDS - WRITING. Documents the Option α field pair (`companionRepo:` + `companionPath:`) backed by a spoke registry. Marked optional — only relevant for hub repos in multi-repo hub-and-spoke setups; skip for single-repo / spoke / polyrepo deployments.
- New `### Frontmatter validation after restructures` subsection under STANDARDS - MAINTENANCE. Codifies the post-restructure rule: after any folder rename, file relocation, or conversation deletion, run `frontmatter-validate` before committing. Quarterly via `conversational-maintenance-review`.
- Quarterly periodic-review note updated to reference the orchestrator skill.

**Skills README updates:** restructured the skill listing into four subsections (Core workflow / Maintenance lane / Session orientation / Template) to surface the lane structure that emerged in workspace-chevan.

### Rationale

These additions emerged from the workspace-chevan migration's discovery that CWOS treats frontmatter as the canonical navigation graph, which raised the standard for "navigable" from *findable* (a determined human + AI can locate the target) to *traversable without context* (a fresh agent with no session history can follow only the declared pointers). The maintenance lane codifies the discipline that supports the new standard, and the cold-start skill gives operators an invokable alternative to the text-prompt template. See the case study at chevan-content `knowledgebase/knowledge-architecture/cwos-migration-frontmatter-as-navigation-graph.md` for the conceptual framing.

---

## [1.0.0] — 2026-06-01

### Added

Initial release of the cwos starter as the first inhabitant of `chevan-quickstarts`. Synced from the maintainer's reference implementation at `chevan-content`.

**Root-level canonical files:**

- `WHY-CWOS.md` — narrative intro covering the acronym (Conversational Work Operating System), the concept of conversational work, the three-layer approach, knowledge architecture (memory / inference / reasoning), why this works for human-human work too, philosophy, who it's for.
- `CWOS.md` — canonical CWOS architectural specification (hub-and-spoke variants, three-layer split, vendor-agnostic principle, foundation files, the optional aiconversations extension).
- `CWOS-SETUP.md` — bootstrap procedure (four deployment scenarios), migration recipe from `operations/conversational-work/` predecessor infrastructure, session-refresh patterns.
- `AGENTS.md` — thin cross-vendor entry-point template (Codex, Cursor, Aider, others reading AGENTS.md).
- `AICONFIG.template.md` — operational charter template with universal sections filled in and `{{REPO_NAME}}` / `{{PROJECT_CONTEXT}}` placeholders for repo-specific content.
- `CLAUDE.template.md` — thin Claude Code bootstrap template.
- `README.md` — inhabitant overview with three consumption patterns (raw URL fetches, sparse checkout, full clone).

**Universal Agent Skills** (`operations/cwos/skills/`):

- `run-prompt-protocol/` — the core run-prompt workflow.
- `conversation-archiving/` — archive conversation files over 75 KB.
- `cwos-migrate-from-conversational-work/` — clean-break migration from the older `operations/conversational-work/` predecessor infrastructure to CWOS.
- `_template/` — Agent Skills format scaffold for authoring new skills.

**Universal reference docs** (`operations/cwos/reference/`):

- `taxonomy.md` — CWOS vocabulary glossary (lightly genericized from the reference implementation).
- `conventional-commits.md` — Conventional Commits format reference.
- `agent-skills-standard.md` — Anthropic Agent Skills standard reference.
- `mcp-stack.md` — Model Context Protocol server configuration reference.

**Memory templates** (`operations/cwos/memory/`):

- `decisions/_template.md` — Architecture Decision Record (Nygard format) template.
- `projects/_template.md` — project re-entry brief template.

---

## How to update this changelog

Contributors submitting PRs that touch `cwos/` should add an entry to the **Unreleased** section at the top of this file (create it if it doesn't exist). On release, the maintainer rolls Unreleased into the next versioned section and tags accordingly.

For umbrella-level changes (adding a new inhabitant, top-level renames, license changes), update the umbrella `CHANGELOG.md` at the repo root instead of (or in addition to) this file.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution flow.
