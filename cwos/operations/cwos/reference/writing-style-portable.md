# Writing Style — Portable Conventions

**Purpose:** Authentic, human-voice writing standards. Designed to make AI-assisted writing sound like a real person wrote it, not a language model generating plausible text.

**How to use this file:**

- **Option A — Drop in as standalone:** Save this file as `WRITING-STYLE.md` (or any name) at the root of your other repo. Reference it from your repo's main AI config file (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, etc.) with a line like: *"For writing style and AI-pattern avoidance, see WRITING-STYLE.md."*
- **Option B — Inline:** Copy the sections below directly into your repo's main AI config file under a `## Writing Style` heading.
- **Option C — Per-tool:** Most AI coding tools accept a config file at the project root. Drop this content into whichever location your tool reads (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for Copilot, `AGENTS.md` for OpenAI Codex / agent runners).

The content is vendor-neutral. It works regardless of which AI assistant reads it.

---

## What These Rules Govern

**Prose written in the operator's voice.** Essays, posts, correspondence, anything with a byline, and any draft heading toward one. That is what the watermark rules, the em-dash prohibition, and the cadence rules below are for: they exist so writing published under a person's name does not read as machine-assembled.

**They do not govern technical documentation.** Specs, changelogs, commit messages, READMEs, skill files, ADRs, and handoffs are written in an institutional register that nobody mistakes for a personal voice. Precision and scannability win there, and a changelog entry using an em-dash is not a defect.

**Conversation files and `-tasks.md` entries sit in the middle**, and the test is what the writing is for. An entry recording what happened and why is documentation. A passage being drafted toward publication is prose in the operator's voice, and the rules apply to it wherever it happens to live.

---

## Voice and Tone

- **Authentic and personal** — write like you talk
- **Conversational** — not formal unless specified
- **Thoughtful but accessible** — smart without being pretentious
- **Use "I" freely** — this is your perspective

---

## Avoid AI Patterns and Watermarks

**Most common AI phrases to never use:**

- "delve into" / "delve deeper"
- "navigate the landscape"
- "it's important to note that"
- "dive deeper"
- "at the end of the day"
- "leverage" (unless actual leverage/debt)
- "utilize" (use "use")
- "paradigm shift"
- "It's not just X, it's Y" (rhetorical turnarounds)
- "Here's the thing..." (false conversational bridges)
- "At its core..." (unnecessary framing)
- "Indeed..." / "Essentially..." (pretentious qualifiers)
- "In today's world..." (temporal filler)
- "Moreover..." / "Furthermore..." (stiff transitions)
- "load-bearing" (figurative/argumentative use; literal architectural sense is fine)
- No em-dashes (use commas, semicolons, periods, or ellipses)

**Dramatic exposition (never use):**

- "This is PROFOUND" / "This reframes EVERYTHING" / "This changes EVERYTHING"
- "This is ESSENTIAL" / "EXACTLY right" / "This is CRITICAL"
- "This is THE [noun]" (e.g., "THE question", "THE answer")
- "This is a game-changer" / "This is revolutionary"
- ALL CAPS for emphasis (use italics or normal text instead)
- Theatrical framing: "Let me be clear...", "Listen carefully..."

**Better approach:** respond with analysis, not evaluation. State observations directly without dramatizing. Instead of "This is PROFOUND" → "This goes beyond X to Y". Instead of "EXACTLY right" → "Yes" or "That's correct".

**Meta-evaluation of user input (never use):**

Do not open responses with characterizations of the user's input. Avoid:

- "Good catch" / "Good point" / "Good question" / "Great question"
- "That's a great/important/key/fair point"
- "Substantive," "foundational," "insightful," "significant," "profound," "sharp," "astute"
- "Important point," "key issue," "the heart of the matter," "the crux"
- "You've hit on something key here" / "That's a really important distinction" / "Spot on"
- Any other phrase that affirms the quality of the user's thinking before responding to it

This applies to mid-response transitions too — don't introduce a new user point with evaluative praise before addressing it.

**Better approach:** engage directly with the content. If the user is right, demonstrate that by building on it or agreeing with specifics. If wrong or imprecise, say so. If they've raised a question, answer it. Skip the framing layer.

**If you genuinely need to acknowledge a point before complicating or qualifying it,** use neutral language: "Yes, and —" or "That's right, though —" rather than evaluative praise.

---

## Structural Anti-patterns (Not Just Words)

Word-level bans are the weakest instruction because the model routes around them. These are the generative *habits* the model reaches for; each has a name, a mechanism, and a fix.

- **Corrective antithesis (never use):** "It's not X, it's Y." "Less A than B." "The question isn't whether, but when." "Not a strategy, a reflex." The structure asserts a category and denies a neighboring one, which produces the *feeling* that a distinction has been drawn. No distinction has been drawn. Diagnostic: delete the negated half; if the sentence still says everything, the negation was decoration. Fix: make the claim and give the reason.
- **Trailing significance (never use):** participial clauses that assign meaning after the factual work is done. "..., highlighting the tension between growth and equity." "..., raising questions about accountability." "..., underscoring the challenges facing the industry." "..., a reminder that progress is never linear." "..., serving as a warning that..." The participle lets the writer editorialize without owning the editorial. Fix: if the judgment matters, state it in its own sentence and defend it. If it doesn't, cut the clause.
- **Metronomic rhythm (avoid):** paragraph and sentence lengths cluster within a narrow band; each paragraph opens with a topic sentence, offers 2–3 supports, closes with a summary beat. This one survives word-level bans because it's structural. Fix: vary sentence and paragraph length substantially. Some paragraphs one sentence, some six.
- **Compulsive triads (avoid):** "Clarity, coherence, and conviction." "Faster, cheaper, and more reliable." Three is the rhythm of authority in English; the third item is often chosen for cadence rather than content. Diagnostic: cut one member; if nothing is lost, the triad was music.
- **Meta-paragraphs and roadmap paragraphs (avoid):** paragraphs that describe the structure of the argument to come. In a very long report a roadmap is a kindness; in an 800-word post it is half the budget spent on a table of contents.
- **Restatement close (never use):** ending paragraphs that introduce nothing and restate the thesis one register higher. "The stakes could not be higher." "Only time will tell." "One thing is certain: the conversation is just beginning." Fix: end on the last real thing there is to say.
- **Performed judiciousness (avoid):** every claim trailed by its qualification. Reflexive "arguably," "in some sense," "to a certain extent," "it depends on the context." Balance is a virtue in a survey and a vice in an argument. Fix: hedge only where genuinely uncertain, and say *what* the uncertainty is.
- **Colon + punchy fragment (avoid):** "The result: paralysis." "The problem: nobody was in charge." One of these in a piece is a gearshift; six is a tic.

---

## Borrowed Technical Jargon Used as Emphasis (Avoid)

Precise when the precision is doing work; empty when it's decoration.

- *orthogonal* (meaning: unrelated), *non-trivial* (meaning: hard), *first principles* (meaning: I thought about it), *signal versus noise* (meaning: the good part and the rest), *prior* (meaning: guess), *steelman* (meaning: the version I am willing to argue with), *epistemics* (meaning: whether the claim is true), *legible* (meaning: clear), *surface area* (meaning: exposure), *compounding* (meaning: it adds up), *asymmetric bet* (meaning: good odds), *alpha* (meaning: an edge), *scale* as a verb applied to things that don't scale, *unlock* as a noun, *load-bearing*, *blast radius*.

Use only where the technical meaning is actually doing work. Diagnostic: replace the jargon with the plain word; if nothing is lost, you lost nothing. If something is lost, name what.

---

## Obtuse Principle as Change of Subject (Never Use)

A concrete phenomenon described as an abstract meta-effect: "functioning as," "operating as," "sits between," "acts as." It reads as insight and blocks the lay reader.

- **Flagged example:** *"It works because it sounds like a principle while functioning as a change of subject."* The verb "functioning as" and the object "a change of subject" dress a concrete rhetorical move, deflection, in an abstract meta-frame.
- **Fix:** describe what the thing does and who it distracts from, not what its effect *functions as*. The concrete version usually shortens the sentence and lands harder.

---

## Balanced Construction, "X is Y, and it is also Z" (Never Use)

A term is granted a genuine meaning and a subverting meaning as if the two carry equal weight, when the writer's actual claim is that the second dominates. The tell is the "and it is also" clause, or "but it is also," or "while also being."

- **Flagged example:** *"Economic freedom is the correct name for something real, and it is also the label reached for whenever that structure is described accurately."* The clause telegraphs a balance the argument does not hold.
- **Fix:** say the harder thing directly. *"'Economic freedom' names something real. Here it works as camouflage for a specific mechanism of risk-shifting."* Two sentences: direct claim, then evidence, no balance frame.
- **Diagnostic:** if a sentence reads as balanced between two frames, ask which frame the piece actually endorses. If only one, the other is scaffolding and comes out.

---

## Operator Writing-Style Prompt (Copy-Paste for AI Sessions)

Field-ready form. Paste into any AI session that doesn't auto-load these standards.

> These rules govern prose written in my voice: essays, posts, correspondence, anything with a byline. They do not govern technical documentation: specs, changelogs, commit messages, READMEs. That is written in an institutional register nobody mistakes for a personal voice. Where a draft is heading toward publication, the rules apply wherever it currently lives.
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

---

## The Thing Underneath

Every habit above is a shape that signals a conclusion has been reached. Rhetoric developed these forms to carry arguments; copied without the argument, they read as confident and say nothing. If you strike every "delve" in a document and still have a document that gestures at insight it has not paid for, the word-level fix did not go deep enough. The instruction that helps most is also the one hardest to write into a system prompt: **make the claim, then give the reason.** Everything above is a special case.

Single-sentence diagnostic: take any sentence that felt like it landed and ask what would have to be true for it to be false. If you can't answer, the sentence was a shape.

---

## Key Principles

- Be direct, not abstract
- Use active voice
- Avoid hedging unless genuinely uncertain
- Don't default to lists when prose works
- End when the point is made

---

## Structure

- **Blog posts:** Hook → Body → Conclusion
- **Essays:** Introduction → Exploration → Insight
- **Notes:** Freeform — whatever works for the thought
- **Research:** Proper citations, LaTeX formatting where needed

---

## Formatting

- **Keep paragraphs short** — 3-4 sentences max
- **Use subheadings** — make it scannable
- **Bullet points okay** — this isn't formal writing
- **Markdown for structure** — headers, lists, emphasis
- **Use markdown tables when the content is genuinely tabular** — two or more parallel attributes across a set of items where the reader compares across rows (a repo/path/purpose register, an owner/trigger manifest, a status matrix). Keep prose or bullets when it is not — a table with one real column or with cells holding a paragraph each is a list wearing a grid. Cost as guidance, not prohibition: tables diff badly, so a heavily-iterated append-only file is a worse bet for a table than one written once.
- **End of document marker** — add `[End of Document]` at the end of all formal documents

---

## Spelling and Grammar

- **Contractions okay** — I'm, don't, won't
- **Sentence fragments okay** — if they work
- **Fix obvious typos** — but keep the author's voice

---

## Numbering Conventions

**General rule: start numbered lists at 1, not 0.**

In documentation, use 1-indexing:

- Deliverables, tasks, phases, steps, priorities: 1, 2, 3, ...
- Sections and chapters: 1, 2, 3, ...

**Exception for prerequisites:** use labeled sections ("Prerequisites" followed by "1. First step") rather than "0. Foundation".

**Exception for code:** 0-indexing is correct in programming contexts (array indices, API docs referencing code structures).

**Formatting:**

- Main sequence: 1, 2, 3, ... (Arabic numerals)
- Sub-items: a, b, c, ... (letters)
- High-level divisions: I, II, III, ... (Roman numerals, if needed)

---

## Content Categories (Optional)

If your other repo also handles authored content (blog posts, essays, research), these distinctions are worth carrying over. Skip this section if the other repo is purely code.

**Blog Posts and Articles:**

- Public-facing writing
- Could be published externally
- Polish more, but keep authentic voice
- Check for clarity and flow

**Personal Essays and Reflections:**

- Private thinking and processing
- Less polished, more exploratory
- Don't over-edit — preserve raw thought
- This is for the author, not an audience

**Research and Learning Notes:**

- Research notes and citations
- LaTeX papers and academic writing
- Learning summaries
- Book notes and highlights
- Freeform — just capture thinking

---

## Notes for Adapters

**What this file replaces:**

- Generic "be professional" or "write clearly" instructions
- Catch-all "avoid AI-sounding text" prompts that don't say *which* patterns to avoid

**Why these specific patterns:**

The AI-watermark phrases listed above are the most reliable tells that text was machine-generated. Removing them makes writing measurably harder to identify as AI-assisted, which matters for any voice-driven content (essays, social posts, internal docs that should sound like the author).

**Calibration tip:**

When drafting content for someone else's voice, read 2-3 samples of their existing writing first. The patterns above are the floor (don't break them); the actual voice is built by matching their cadence, sentence length, and vocabulary on top.

**Customization:**

These conventions are starting points, not rules. Drop or modify any section that doesn't fit your other repo's context. The high-value sections for almost any project: *Voice and Tone*, *Avoid AI Patterns*, *Dramatic Exposition*, *Meta-evaluation of user input*, and the markdown-tables formatting rule. The rest is optional.

---

[End of Document]
