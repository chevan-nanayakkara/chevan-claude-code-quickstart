# AI Configuration Template — {{REPO_NAME}}

> **Template note:** copy this file to `/AICONFIG.md` at the root of your target repo when bootstrapping CWOS. Replace `{{REPO_NAME}}`, `{{PROJECT_DESCRIPTION}}`, `{{REPO_STRUCTURE}}`, etc. Adjust standards as your repo evolves. The skeleton below covers the universal sections (canonical source note, core instructions, writing standards, file conventions, git workflow); fill in repo-specific sections (project context, repository context) for your own situation.

---

Repository: {{REPO_NAME}}

Version: 1.0.0

Last Updated: {{DATE}}

---

## CANONICAL SOURCE NOTE

**This file (AICONFIG.md) is the canonical, vendor-agnostic source of truth for all behavioral rules in this repository.** Vendor-specific files (`CLAUDE.md`, `AGENTS.md`, individual memory files at `operations/cwos/memory/`, etc.) should reference this file, not duplicate its content. New behavioral rules belong here first; vendor-specific files exist only as bootstraps and lightweight session-spanning reminders.

**For the operating system specification** (Conversational Work Operating System: hub-and-spoke variants, the three-layer split, vendor-agnostic principle, aiconversations extension, foundation files, deployment scenarios), see [`/CWOS.md`](CWOS.md). For setting up the same architecture in a new repo, see [`/CWOS-SETUP.md`](CWOS-SETUP.md). For the implementation layer in this repo (memory, skills, reference), see [`/operations/cwos/README.md`](operations/cwos/README.md). For vocabulary used across these docs, see [`/operations/cwos/reference/taxonomy.md`](operations/cwos/reference/taxonomy.md).

**Always-restart pattern.** This repo's operational preference: when context needs refreshing, restart the AI session rather than refresh in place. All reasoning lives in durable artifacts (conversation files, memory at `operations/cwos/memory/`, AICONFIG.md, CWOS.md), so restart is cheap and produces a cleaner state than refresh.

### Where new behavioral content goes (three-layer split)

When codifying new AI behavior, choose by shape, not by vendor. CWOS's three-layer split (configuration / state / procedure):

1. **Configuration — behavioral rules** (always-on guidance)
   - **Home:** `/AICONFIG.md`, in the appropriate section.
   - **Why:** Vendor-agnostic plain text. Auto-loaded once at session start by every AI tool's bootstrap.
2. **Procedure — multi-step workflows** (with branching, sequencing, runtime decisions)
   - **Home:** `/operations/cwos/skills/<name>/SKILL.md` in Agent Skills standard format.
   - **Why:** Vendor-agnostic, cross-vendor portable. Loaded on demand. Zero baseline token cost.
3. **State — decisions, project status, accumulated learnings**
   - **Home:** `/operations/cwos/memory/` (decisions/, projects/<spoke>/, archive/, plus feedback memories indexed in MEMORY.md).

**Vendor-specific slash-command UX** is a fourth surface that sits on top of any of the above. Always a thin shell referencing canonical content; never duplicates.

**Decision tree:**

- Single always-on rule? → AICONFIG.md (configuration).
- Multi-step procedure? → operations/cwos/skills/<name>/SKILL.md (procedure).
- A decision worth recording? → operations/cwos/memory/decisions/NNN-slug.md (state, ADR).
- A re-entry brief? → operations/cwos/memory/projects/<spoke>/re-entry.md (state).
- One-time note? → not a rule. Conversation file or `working/`.

### What belongs in AICONFIG.md (writing standards, file conventions, brand guidelines, not just "AI rules")

Writing standards, file-naming conventions, brand guidelines, document-layout rules, voice and tone preferences — these aren't only "AI-behavioral rules." They're standards that apply to anyone (human or AI) working in the repo, and AICONFIG.md is the canonical home for all of them. Three reasons:

1. AICONFIG.md is the one file AI tools auto-load, so embedded standards get applied automatically every session
2. It serves as the canonical reference for humans needing to check conventions
3. Keeping standards in one place avoids the multi-file drift that older install-pipeline patterns produced (where standards lived in scattered template files that had to be "installed" into a config — each install drifted slightly from the source)

The distinction between "AI rules" and "project conventions" is blurry in practice. Both apply to whoever is doing work. Put them in AICONFIG.md (under `## STANDARDS - WRITING` / `## STANDARDS - OPERATIONS` / `## STANDARDS - MAINTENANCE` as appropriate) and let one canonical source serve both audiences.

If you're migrating from an older `operations/conversational-work/` predecessor that used the install-pipeline pattern, see [`/CWOS-SETUP.md`](CWOS-SETUP.md) "Standards consolidation" for the procedure that lifts template content into the canonical AICONFIG.md sections.

---

## ⚠️ CORE INSTRUCTIONS (Always Follow)

### What to Do

- **Read only files explicitly specified** — never auto-scan.
- **Match context to task** — writing voice for content, precision for configuration.
- **Ask before making assumptions** — covers personal and technical content.
- **Show planned changes before changing files.**
- **Preserve intent** — don't over-polish writing, don't break configurations.

### What NOT to Do

- **Don't auto-read files** — respect privacy and avoid irrelevant context.
- **Don't assume all writing needs editing** — some is just thinking.
- **Don't add content not requested** — stay focused.
- **Don't commit, push, or run destructive git operations without explicit instruction** — file edits are fine; `git add` / `git commit` / `git push` / branch operations require explicit per-task authorization. Past authorization does not extend to new work.

### When Asked for Git Work

1. File edits and read-only `git status` / `git log` / `git diff` are fine without asking.
2. `git add`, `git commit`, `git push`, branch creation/deletion, force-push, reset, rebase — require explicit go-ahead per task.
3. A "commit and push" instruction authorizes that one batch only.
4. When work is done, summarize what changed and ask whether to commit and how to group.
5. Never bypass hooks (`--no-verify`), never amend pushed commits, never force-push to main without explicit instruction.
6. **Commit message format:** use [Conventional Commits](operations/cwos/reference/conventional-commits.md) (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:` with optional scope like `feat(api):` or `docs(operations):`).

---

## PROJECT CONTEXT

{{PROJECT_DESCRIPTION}}

(Describe what this repo is, who maintains it, what work happens here, and any cross-cutting context an AI session needs to understand the work.)

---

## REPOSITORY CONTEXT

{{REPO_STRUCTURE}}

(Describe the top-level folder structure, what each major folder contains, and any naming conventions specific to this repo. Use a tree diagram if helpful.)

Example skeleton:

```
{{REPO_NAME}}/
├── AICONFIG.md              # This file (canonical AI configuration)
├── CWOS.md                  # CWOS specification (copied from upstream)
├── CWOS-SETUP.md            # Bootstrap procedure
├── CLAUDE.md                # Thin Claude Code pointer to AICONFIG.md
├── AGENTS.md                # Thin cross-vendor pointer
├── README.md                # Repo overview
├── operations/
│   └── cwos/                # CWOS implementation layer
│       ├── memory/          # Accumulated state (ADRs, projects, archive)
│       ├── skills/          # Reusable procedures (Agent Skills format)
│       └── reference/       # Standing knowledge (taxonomy, standards)
└── (your domain folders)
```

---

## STANDARDS - WRITING

### What these rules govern

**Prose written in the operator's voice.** Essays, posts, correspondence, anything with a byline, and any draft heading toward one. That is what the watermark rules, the em-dash prohibition, and the cadence rules below are for: they exist so writing published under a person's name does not read as machine-assembled.

**They do not govern technical documentation.** Specs, changelogs, commit messages, READMEs, skill files, ADRs, and handoffs are written in an institutional register that nobody mistakes for a personal voice. Precision and scannability win there, and a changelog entry using an em-dash is not a defect.

**Conversation files and `-tasks.md` entries sit in the middle**, and the test is what the writing is for. An entry recording what happened and why is documentation. A passage being drafted toward publication is prose in the operator's voice, and the rules apply to it wherever it happens to live.

### Voice and Tone

- **Authentic and personal** — write like you talk, not like a corporate brand.
- **Direct** — say what you mean, drop the hedging.
- **Conversational rhythm** — use ellipses (...) for pauses instead of em-dashes.

### Avoid AI Patterns and Watermarks

**Word-level bans:**

- **No em-dashes (—).** Use ellipses (...) for pauses, commas for clauses, or restructure the sentence.
- **No "load-bearing" used figuratively.** ("Load-bearing pillar," "load-bearing assumption," etc.) Pet peeve; needs active self-policing because it's a common AI tic.
- **No dramatic exposition.** No theatrical "here's the thing," no ALL CAPS for emphasis, no "imagine if."
- **No meta-evaluation of user input.** Never open responses with praise of the user's question ("Good catch," "Good point," "great question," "insightful," "the heart of the matter," etc.). Engage directly with content. Neutral acknowledgments ("Yes, and" / "That's right, though") are fine when the conversation calls for them; meta-praise is not.

**Structural anti-patterns (not just words):**

Word-level bans are the weakest instruction because the model routes around them. These are the generative *habits* the model reaches for; each has a name, a mechanism, and a fix.

- **Corrective antithesis (never use):** "It's not X, it's Y." "Less A than B." "The question isn't whether, but when." "Not a strategy, a reflex." The structure asserts a category and denies a neighboring one, which produces the *feeling* that a distinction has been drawn. No distinction has been drawn. Diagnostic: delete the negated half; if the sentence still says everything, the negation was decoration. Fix: make the claim and give the reason.
- **Trailing significance (never use):** participial clauses that assign meaning after the factual work is done. "..., highlighting the tension between growth and equity." "..., raising questions about accountability." "..., underscoring the challenges facing the industry." "..., a reminder that progress is never linear." The participle lets the writer editorialize without owning the editorial. Fix: if the judgment matters, state it in its own sentence and defend it. If it doesn't, cut the clause.
- **Metronomic rhythm (avoid):** paragraph and sentence lengths cluster within a narrow band; each paragraph opens with a topic sentence, offers 2-3 supports, closes with a summary beat. This one survives word-level bans because it's structural. Fix: vary sentence and paragraph length substantially. Some paragraphs one sentence, some six. A one-sentence paragraph lands because the paragraphs around it are eight lines; uniformity flattens all of that.
- **Compulsive triads (avoid):** "Clarity, coherence, and conviction." "Faster, cheaper, and more reliable." Three is the rhythm of authority in English; the third item is often chosen for cadence rather than content. Diagnostic: cut one member; if nothing is lost, the triad was music.
- **Meta-paragraphs and roadmap paragraphs (avoid):** paragraphs that describe the structure of the argument to come. In a very long report a roadmap is a kindness; in an 800-word post it is half the budget spent on a table of contents.
- **Restatement close (never use):** ending paragraphs that introduce nothing and restate the thesis one register higher, reaching for a benedictory note. "The stakes could not be higher." "Only time will tell." "One thing is certain: the conversation is just beginning." Fix: end on the last real thing there is to say, placed last.
- **Performed judiciousness (avoid):** every claim trailed by its qualification. Reflexive "arguably," "in some sense," "to a certain extent," "it depends on the context." "While critics argue X, proponents counter Y, and the truth likely lies somewhere in between." Balance is a virtue in a survey and a vice in an argument. Fix: hedge only where genuinely uncertain, and say *what* the uncertainty is.
- **Colon + punchy fragment (avoid):** "The result: paralysis." "The problem: nobody was in charge." One of these in a piece is a gearshift; six is a tic.

**Borrowed technical jargon used as emphasis (avoid):**

Precise when the precision is doing work; empty when it's decoration. The rule on *load-bearing* above generalizes to a whole shelf:

- *orthogonal* (meaning: unrelated), *non-trivial* (meaning: hard), *first principles* (meaning: I thought about it), *signal versus noise* (meaning: the good part and the rest), *prior* (meaning: guess), *steelman* (meaning: the version I am willing to argue with), *epistemics* (meaning: whether the claim is true), *legible* (meaning: clear), *surface area* (meaning: exposure), *compounding* (meaning: it adds up), *asymmetric bet* (meaning: good odds), *alpha* (meaning: an edge), *blast radius* (figurative use; the literal safety-engineering sense is fine), *scale* as a verb applied to things that don't scale, *unlock* as a noun.

Use only where the technical meaning is actually doing work. Diagnostic: replace the jargon with the plain word; if nothing is lost, you lost nothing. If something is lost, name what.

**Obtuse principle as change of subject (never use):**

A concrete phenomenon described as an abstract meta-effect: "functioning as," "operating as," "sits between," "acts as." It reads as insight and blocks the lay reader.

- **Flagged example:** *"It works because it sounds like a principle while functioning as a change of subject."* The verb "functioning as" and the object "a change of subject" dress a concrete rhetorical move, deflection, in an abstract meta-frame.
- **Fix:** describe what the thing does and who it distracts from, not what its effect *functions as*. The concrete version usually shortens the sentence and lands harder.

**Balanced construction, "X is Y, and it is also Z" (never use):**

A term is granted a genuine meaning and a subverting meaning as if the two carry equal weight, when the writer's actual claim is that the second dominates. The tell is the "and it is also" clause, or "but it is also," or "while also being."

- **Flagged example:** *"Economic freedom is the correct name for something real, and it is also the label reached for whenever that structure is described accurately."* The clause telegraphs a balance the argument does not hold.
- **Fix:** say the harder thing directly. *"'Economic freedom' names something real. Here it works as camouflage for a specific mechanism of risk-shifting."* Two sentences: direct claim, then evidence, no balance frame.
- **Diagnostic:** if a sentence reads as balanced between two frames, ask which frame the piece actually endorses. If only one, the other is scaffolding and comes out.

**Operator writing-style prompt (copy-paste for other AI sessions):**

Vendor-neutral form of the rules above; paste into any AI session (Cursor, Codex, ChatGPT, Gemini) that doesn't auto-load this file.

> These rules govern prose written in my voice: essays, posts, correspondence, anything with a byline. They do not govern technical documentation — specs, changelogs, commit messages, READMEs — which is written in an institutional register nobody mistakes for a personal voice. Where a draft is heading toward publication, the rules apply wherever it currently lives.
> Write in prose. Lists only when the content is genuinely a list. Subheadings only in long, multi-part pieces.
> No corrective antithesis: never "it's not X, it's Y," "less A than B," or "the question isn't whether, but when." Make the claim and give the reason.
> No trailing participial commentary that assigns significance: no "highlighting," "underscoring," "raising questions about," "serving as a reminder that." If a judgment matters, state it in its own sentence and defend it.
> Vary sentence and paragraph length substantially. Some paragraphs one sentence, some six.
> No signposting: no "let's unpack," "it's important to note," "here's the thing," "at its core," "essentially," "the reality is."
> Do not end by summarizing. End on the last real thing there is to say.
> No em-dashes. Use commas, semicolons, periods, or ellipses.
> Hedge only where genuinely uncertain, and say what the uncertainty is.
> Avoid borrowed technical jargon used as emphasis: load-bearing, orthogonal, non-trivial, first principles, surface area, asymmetric, compounding, unlock as a noun. Use them only where the technical meaning is doing work.
> Avoid: delve, tapestry, testament, underscore, navigate, realm, foster, harness, myriad, multifaceted, crucial, pivotal, robust, leverage, utilize, ecosystem, landscape, lens, interplay.
> Do not describe a concrete thing as an abstract meta-effect: no "functioning as," "operating as," "acts as," "sits between." Say what it does and to whom.
> No balanced construction: no "X is Y, and it is also Z." If the argument endorses one frame, drop the other and say the harder thing directly.
> No praise. Do not characterize my input before responding. Analysis, not evaluation.

**The thing underneath:** every habit above is a shape that signals a conclusion has been reached. Rhetoric developed these forms to carry arguments; copied without the argument, they read as confident and say nothing. If you strike every "delve" in a document and still have a document that gestures at insight it has not paid for, the word-level fix did not go deep enough. The instruction that helps most is also the one hardest to write into a system prompt: **make the claim, then give the reason.** Everything above is a special case. Single-sentence diagnostic: take any sentence that felt like it landed and ask what would have to be true for it to be false. If you can't answer, the sentence was a shape.

**Portable form:** the whole of this section, in a vendor-neutral standalone file suitable for dropping into a non-CWOS repo, is at [`operations/cwos/reference/writing-style-portable.md`](operations/cwos/reference/writing-style-portable.md).

### Formatting

- **No markdown tables.** WYSIWYG editors (especially VS Code's markdown preview) render tables poorly; cell contents become unreadable. Use bullet lists with key/value patterns (`**Label:** value`), definition-style sub-bullets, or prose. Tables acceptable only when (a) content is genuinely tabular AND (b) the file's primary consumer renders tables correctly (e.g., GitHub README viewed on github.com).
- **No hard line breaks within paragraphs.** No trailing-2-spaces+newline, no backslash+newline, no `<br>` tags, no source-text hard-wrapping. Paragraphs are single long lines that wrap naturally on the reader's screen.
- **Standard markdown** — headers, lists, code fences, blockquotes. Keep it simple.

### Numbering Conventions

- **1-indexed** for human-facing lists, sections, and steps.
- Exceptions: prerequisites (sometimes labeled 0), code (where 0-indexed arrays are standard).

---

## STANDARDS - OPERATIONS

### Brand-Free Folders

If your repo has folders intended for external review (e.g., `business/for-review/`), use concept-based names and content — never brand names, project codenames, or internal identifiers. Brand naming creates the impression you're shopping the work to specific buyers; concept naming keeps options open.

### File Naming

- **Snake_case for system files** (`memory_index.md`, `repo_paths.md`).
- **kebab-case for content** (`my-essay-title.md`, `2026-05-24-event-recap.md`).
- **PascalCase for canonical capitalized docs** (`CWOS.md`, `AICONFIG.md`, `README.md`, `LICENSE`).
- **ISO 8601 dates** in filenames (`YYYY-MM-DD-slug.md`).

### Conversation Files

For repos using the `aiconversations/` extension (long-form AI dialogue threads):

- **Entry label convention:** `### [User | DATE TIME]` and `### [AI Assistant | DATE TIME]` — vendor-agnostic. Don't use `[Claude | ...]` or vendor-specific labels.
- **Timestamp discipline:** always run `date "+%B %-d, %Y %-I:%M%p"` immediately before writing an `[AI Assistant | ...]` entry. Never extrapolate or reuse a session-start timestamp.
- **Run-prompt protocol:** when the user says "run prompt [User | DATE TIME] in FILE.md," follow the procedure in `operations/cwos/skills/run-prompt-protocol/SKILL.md`. The response always gets written back to the conversation file, not just chat. Always add a `[User | +2min]` stub for the next entry.

### Project tracking — distributed `-tasks.md` files with centralized rollup

For repos using the `aiconversations/` extension with companion task tracking, the pattern is:

- **Per-conversation `-tasks.md` files** capture project state close to the conversation that produced it. Each `-tasks.md` file has a "Summary of Open Projects" section at the top listing currently-open projects with status and next action. This is the canonical detail surface.
- **Centralized rollup at `/aiconversations/0-project.md`** is a derived view: a domain → conversation → project listing aggregated from every `-tasks.md` file. Generated by the [`open-projects`](operations/cwos/skills/open-projects/SKILL.md) skill. This is the scanning surface for cross-corpus visibility.
- **Refresh discipline:** invoke the `open-projects` skill on demand or as part of the quarterly maintenance review. The rollup never goes out of sync because it's regenerated from the source files each time.
- **Companion to `0-work-status.md`:** the two surfaces answer different questions. Work-status tells you *which threads need attention*; the project rollup tells you *what specific projects are open*. Both regenerate from distributed sources on the same refresh cadence.

The split (capture in `-tasks.md`, visibility in `0-project.md`) preserves per-conversation isolation as the corpus scales while solving the "I lose track of distributed task files" visibility problem. See the `open-projects` skill for the full procedure and `CWOS.md` for the architectural framing.

#### Tasks File Structure (Standard)

**Section Layout:**

Every `-tasks.md` file uses this layout, in this order. (Format current as of June 20, 2026, second revision of the day. No standalone summary section and no Status Key block; each of Open Projects and Closed Projects leads with its own focused `### Summary` subsection, and Notes / Reference sits at the end.)

1. **YAML frontmatter.**
2. **Title and header information** — companion conversation pointer, reference pointers, anything orienting.
3. **Open Projects** — leads with a `### Summary` subsection (one-line digest per open project: number, name, status, key dependency or next-action signal; bullets, not a table per the no-markdown-tables rule), followed by a `### Priority order (AI-maintained recommendation)` subsection (ranked list of the open projects with rationale per position; see the Priority-order convention below), then one detail block per open project. The Deferred backlog lives here too.
4. **Closed Projects** — leads with a `### Summary` subsection (recently closed projects, most recent first), then the detail blocks. Append-only; do not prune. (Covers both completed-with-delivery and closed-without-completion.)
5. **Notes / Reference** — at the end: **pointers only.** Session-starter prompts, file paths, links to ADRs / decision logs / sibling conversations, a glossary entry where a term needs disambiguating. It says *where to look*, not *what is true*. Living document; prune as projects close out.

**Notes / Reference holds no content.** This is the rule most often broken, and it is usually broken by permissive wording in the standard itself: describe this section as a "catch-all for context the work depends on" or a "reference shop" and it will license far more than its own examples show. Reference material accumulates here because this is the file that happens to be open when it shows up, not because it belongs here.

**The test: close every project in the file. What is left standing?**

Anything still standing was never project state. A checkbox, a phase marker, a priority ranking, a closure record, a dependency note: all of these die with the project that owns them. A reading list, a lab value, an enrollment figure, a set of talking points for a meeting: none of these care whether a project exists.

Said another way: **orchestration content changes when the work moves; reference content changes when the world moves.** A `-tasks.md` file holds only the first kind.

**Where the content goes instead — four destinations:**

- **The companion domain folder** — the path in the conversation file's `companionTo` frontmatter field. Domain reference content, and the overwhelming majority case. A reading list goes to the domain folder for that hobby; recurring measurements go to that domain's `data/` folder; roles and headcount go to the folder for that business or property. The routing target is already declared in every conversation file; the pointer exists and has simply never been used as a routing rule.
- **The conversation file** — reasoning. Chronological, append-only. Why a decision was reached, what an option traded off.
- **`operations/cwos/memory/decisions/`** — decisions with alternatives and consequences, as ADRs.
- **`operations/cwos/reference/`** — durable procedure and specification that is none of the above: not a behavioral rule, not state, not reasoning, not a decision. A protocol document, a taxonomy, a design spec for an unbuilt subsystem.

**The five `##` sections above are the complete permitted set.** No preamble sections above Open Projects, no appendix sections below Notes / Reference. A strategy briefing sitting on top of a project tracker, or a design specification interleaved between two projects, is the same defect as an overstuffed Notes / Reference wearing a different heading level.

**Companion rule for conversation files.** The same principle governs the conversation file: when substantial structured content accumulates there beyond the dialogue itself — a table someone will look up later, a spec, a compiled list — extract it to its proper destination above and leave a pointer in its place. One rule, two files. **Each of the three files (conversation, tasks, domain reference) holds one kind of thing, and reference material belongs to none of the first two.**

No Status Key legend block: `[ ]` / `[x]` checkboxes are self-evident; any non-standard marker is explained inline where used.

**Grooming rule — move the row Open→Closed on close (the most commonly missed step).** When you complete or close a project, in the *same edit* move its row from the `### Summary` under **Open Projects** to the `### Summary` under **Closed Projects** (and migrate its detail block from Open Projects to Closed Projects). The open Summary must never list a completed project as if open. Grooming is not finished until the open Summary matches the actual open work. The `open-projects` skill reads `Open Projects → ### Summary` to build the hub rollup, so a stale open Summary corrupts it; the skill flags any completed project still in the open Summary under its "Files needing cleanup" findings.

**Priority-order convention (July 22, 2026).** The `### Priority order (AI-maintained recommendation)` subsection sits under **Open Projects** right below `### Summary`. It carries the AI's current recommended ranking of the file's open projects — a durable answer to "if I picked up this thread cold, what should I work on first?" Rationale: operators repeatedly ask mid-conversation for a priority order + reasoning, then lose it as the conversation moves on. Making it a required subsection puts the answer in the file that owns those projects.

**Shape of the subsection:**

```markdown
### Priority order (AI-maintained recommendation)

*Refreshed <date> by AI. Each item marked `*(AI)*` was ranked by the AI on this grooming pass; each `*(operator)*` was manually set and is preserved verbatim on subsequent grooming touches.*

1. **Project N — <title>.** *(AI)* / *(operator)* <One-line rationale for this position — the "why first" or "why this rank," including any sync/dependency notes.>
2. **Project N — <title>.** *(AI)* / *(operator)* ...
```

**Item-level provenance markers** — each item carries one of two markers so subsequent groomings know what to preserve:

- **`*(AI)*`** — the AI ranked this item. The next grooming pass is free to re-rank, re-rationalize, or reorder it as new signals surface.
- **`*(operator)*`** — the operator manually set this item's position (and typically wrote or approved its rationale). The next grooming preserves it verbatim in its current position; the AI never overwrites operator-set items.
- **Unmarked** — treated as `*(AI)*` for backward compatibility with pre-convention files.

**Bounded write scope** — the AI writes to *only* this subsection during grooming. Everything else in **Open Projects** (the `### Summary` above, the per-project detail blocks below), all of **Closed Projects**, and all of **Notes / Reference** stays operator-authoritative (the AI only edits those when the operator's current prompt explicitly asks — e.g., adding a new project, moving a project Open→Closed).

**Behavior on grooming** — every AI grooming touch of a `-tasks.md` file refreshes this subsection: read existing items, preserve `*(operator)*` items exactly (position + rationale), re-rank the `*(AI)*` items among themselves in whatever gaps remain, insert any new projects with `*(AI)*` at the position the AI thinks best. If the AI wants to note an alternative view on an operator-set item, that note goes in the current run-prompt response or conversation entry, **never inside the subsection** — the subsection stays clean.

**Relationship to `prioritize-open-projects` skill** — different flow, different scope. The `prioritize-open-projects` skill produces on-demand *cross-file* analytical output (tiered view across the whole workspace) to chat or the invoking conversation file, still read-only, never writes to `-tasks.md`. This `### Priority order` subsection is *per-file* durable ranking refreshed by any grooming touch. The two answer different questions ("across the whole workspace, what?" vs. "inside this thread, what?").

**On operator override without conflict** — if the operator never manually overrides the AI's ranking, that is fine. Leaving everything marked `*(AI)*` is a valid steady state; the AI just re-ranks on each groom based on current signals. The `*(operator)*` marker is available when the operator has a specific reason to lock a position, not required.

*(Convention originated in workspace-chevan July 22, 2026. Ported here as part of cwos-v1.10.0 for cross-repo standard parity.)*

**Four-Level Hierarchy:**

Within the Open Projects and Closed Projects sections, use this hierarchy:

- **Project** (H3, prefixed with "Project N:"): `### Project 1: Config Enhancement`
- **Phase** (H4): `#### Phase 1: Research`
- **Deliverable** (bold text): `**Enhancement spec document**`
- **Task** (checkbox): `- [x] Draft spec outline`

The numbering prefix (`Project N:`) enables stable cross-document references ("see Project 3 in `media-platform-work-tasks.md`") and survives renames better than name-only references.

**Closed Projects Section:**

Each entry should include:

- What was delivered (brief description of outputs)
- Completion or closure date
- File references (paths to deliverables, specs, or artifacts produced)
- Reason for closure if not completed-with-delivery (e.g., scope shift, deprioritized, blocked indefinitely)

**Why this section order:** giving each of Open and Closed its own `### Summary` keeps each digest focused and relevant (open summary = open work only; closed summary = closed work only), instead of one mixed standalone summary. Open Projects leads because it is the live work; Closed Projects is the historical record; Notes / Reference, the pointer index, sits at the end out of the way of the active work.

This structure scales from single-project tasks files to multi-project tracking while keeping the summary scannable and the detail organized.

### Cross-repo pointer convention (hub→spoke companions — optional)

If this repo is a **hub** in a multi-repo hub-and-spoke setup, conversation files may sometimes need to reference content that lives in a separate spoke repo (typically live code or active output that wasn't migrated to the hub). The Option α convention (adopted as canonical for the workspace-chevan hub on 2026-05-31; portable to any hub) uses a `companionRepo` + `companionPath` field pair in frontmatter:

```yaml
companionRepo: <spoke-short-name>
companionPath: /relative/path/from/spoke/root.tsx
```

- `companionRepo:` is the spoke's short name as registered in `operations/cwos/reference/spoke-registry.md` (if you author one) — it resolves to the spoke's absolute filesystem path
- `companionPath:` is the path **relative to the spoke's repo root** (starts with `/`)
- The two fields appear together; either both or neither

For hub-internal companion references (the dominant case), use `companionTo:` with a hub-internal path. The cross-repo fields are opt-in and only relevant when a conversation actually references live spoke content.

The same `Repo` / `Path` pattern extends to other relationship fields when cross-repo references are needed (`parentRepo:` + `parentPath:`, `relatedRepo:` + `relatedPath:`). Skip this convention entirely if the repo is single-repo, a spoke, or polyrepo without a hub.
- **Size management:** archive conversation files when they exceed 75KB. See `operations/cwos/skills/conversation-archiving/SKILL.md`.

---

## STANDARDS - MAINTENANCE

### Periodic Review

CWOS-aligned repos benefit from periodic review of memory, skills, and reference content:

- **Monthly:** scan `operations/cwos/memory/` for stale or contradicted entries. Update or archive.
- **Quarterly:** review skills for drift against actual workflow. Update or retire skills that no longer reflect what's actually done. Run the [`conversational-maintenance-review`](operations/cwos/skills/conversational-maintenance-review/SKILL.md) skill orchestrator for the full quarterly sweep (validates frontmatter + flags size-threshold files + flags stalled/completed threads + surfaces possible duplicates).
- **As-needed:** add ADRs for cross-cutting decisions, re-entry briefs for projects paused for an extended time.

### Frontmatter validation after restructures

The CWOS architecture treats conversation-file YAML frontmatter as the canonical navigation graph. Structural pointers — `companionTo`, `archives`, `parentConversation`, `subConversations`, `relatedDocuments`, `location`, `companionTasks` — must resolve to existing paths, or be intentionally absent.

**Rule:** after any folder rename, file relocation, or conversation deletion, run the [`frontmatter-validate`](operations/cwos/skills/frontmatter-validate/SKILL.md) skill before committing the restructure. The skill reports dangling references file-by-file; apply the 4-rule maintenance pattern (Rule A: cross-system path migrations; Rule B: root-folder relocations; Rule C: stale archive folders; Rule D: sibling renames + dangling drops) to clean any findings.

The canonical worked example of the 4-rule pattern is the workspace-chevan May 31, 2026 maintenance pass — refer to that as the reference implementation when cleaning new findings; the pattern transfers to any CWOS-aligned repo.

---

## FILE OPERATIONS

### Editing files: use the Edit/Write tools, not terminal in-place edits

When changing a file's contents, use the dedicated Edit and Write tools, not terminal in-place edits (`perl -i`, `sed -i`, `awk -i`, or `>` / `>>` redirects that rewrite a file). Terminal writes bypass the editor sync, so if the file is open in the operator's editor, the editor's buffer overwrites the terminal change on its next save, silently reverting the work. This matters most for `aiconversations/` files, which the operator usually has open. Terminal commands for reading and searching (`grep`, `wc`, inspecting with `cat`) are fine; it is *writes* that must go through the tools. If a bulk transform is genuinely unavoidable, ask the operator to close or reload the file first, then apply it. (Codified June 16, 2026 after a `perl`-applied horizontal-rule pass to a conversation file was repeatedly reverted by the open editor — Edit-tool entries in the same session survived because they synced to the IDE.)

---

## 📋 REFERENCE

### Common Mistakes to Avoid

- **Duplicating canonical content in vendor-specific files.** Keep `CLAUDE.md`, `AGENTS.md`, etc. as thin pointers. New rules go in `AICONFIG.md`; vendor entries reference.
- **Embedding multi-step procedures in `AICONFIG.md`.** Procedures with branching belong in `operations/cwos/skills/<name>/SKILL.md`. AICONFIG.md side keeps a one-line reference.
- **Authoring memories speculatively.** Only write feedback memories, ADRs, or re-entry briefs that capture real decisions, real feedback, or real state. Speculative memories rot.
- **Refreshing in place when restart would be cleaner.** Always-restart pattern; restart cost is cheap because all durable state lives in git-versioned artifacts.

---

## Version History

- {{DATE}} — v1.0.0: Initial CWOS bootstrap. AICONFIG.md authored from chevan-quickstarts template.

(Add subsequent version entries in descending date order.)
