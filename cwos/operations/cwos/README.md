# operations/cwos/ — CWOS Implementation Layer

**Purpose:** this folder is the implementation layer for the Conversational Work Operating System (CWOS) in this repository. The canonical CWOS specification lives at [`/CWOS.md`](../../CWOS.md); this folder is where the spec's concepts get materialized as actual files.

This README ships with the starter as a working draft. Keep the structure, replace the deviations section with your own, and delete this paragraph.

**Three-folder structure (separation of concerns):**

- **`memory/`** — accumulated state. Decisions (ADRs), per-project re-entry briefs, learned patterns, always-loaded context, archived material. Mostly write-by-AI-assisted, read-by-both. Dynamic.
- **`skills/`** — reusable procedures. Each skill is a directory containing a `SKILL.md` in the Agent Skills standard format. Loaded on demand when a task matches the skill's description. Mostly write-by-human (or human-AI collab), read-by-AI on demand. Procedural.
- **`reference/`** — standing knowledge. Taxonomy/glossary, conventions, tool reference (MCP servers, Agent Skills standard, Conventional Commits). Written-by-human, read-by-both as needed.

**A fourth folder appears once work crosses surfaces.** `handoffs/` holds cross-surface handoff documents, one folder per project: files written by one AI session for another to read, across repositories and surfaces. Create it when the first handoff is written, not at bootstrap. A repository whose work never leaves it has no correspondence to file. Protocol detail in [`reference/handoff-protocol.md`](reference/handoff-protocol.md), which ships whether or not the folder exists, because knowing how handoffs work costs nothing and having an empty inbox costs an explanation.

**`handoffs/` does not map onto the configuration / state / procedure split, and forcing it would be dishonest.** The first three folders are the CWOS spec's layers. Handoffs are an inbox and an outbox, correspondence rather than accumulated state, procedure, or standing knowledge. They sit here because the operations layer is where working infrastructure lives, not because they are a fourth layer of the same kind.

For the canonical definitions of the three layers and the configuration / state / procedure split, see [`/CWOS.md`](../../CWOS.md) and [`reference/taxonomy.md`](reference/taxonomy.md).

---

## What's where

- **Configuration / behavioral rules:** [`/AICONFIG.md`](../../AICONFIG.md) at repo root, not inside this folder. This folder holds state, procedure, and reference; AICONFIG.md holds the rules.
- **State** (decisions, project re-entry, archives): `memory/`
- **Procedure** (Agent Skills format): `skills/`
- **Standing knowledge** (vocabulary, tool reference, format specs): `reference/`
- **Cross-surface correspondence**, if this repo has any (handoffs to and from spokes, other hubs, and non-CLI surfaces): `handoffs/`, with the protocol in [`reference/handoff-protocol.md`](reference/handoff-protocol.md).

If a derived view over any of these is useful later (a handoff ledger, a skills index, a decisions timeline), keep it outside this folder. This layer holds records; a view over records belongs with the other aggregation surfaces, wherever this repo puts them.

## This repo's deviations from the CWOS spec

*(Record them here rather than editing `CWOS.md`. The spec describes several valid variants, so most entries in this section are choices rather than departures: single-repo versus multi-repo hub-and-spoke, folder naming and capitalization, any layer this repo adds or omits. Say which variant and why, so a later reader does not read a deliberate choice as drift. Delete this italic note once the section has real content.)*

## Maintenance

Memory pruning recommended quarterly; full periodic review recommended biannually. See [`/CWOS.md`](../../CWOS.md) "Periodic review" section for the schedule and what to look for.
