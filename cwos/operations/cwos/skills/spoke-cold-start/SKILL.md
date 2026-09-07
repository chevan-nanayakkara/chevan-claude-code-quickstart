---
name: spoke-cold-start
description: Orient an AI session running in a spoke or development repository to its relationship with the CWOS hub — load the behavioral rules that apply everywhere, the handoff protocol and this surface's inbox, and the boundary rules about what may and may not be written into a development repo. Deliberately narrower than cwos-cold-start, which loads the hub's full work state and is for hub sessions only. Use at the start of a session in a spoke repo, after compaction, or when a spoke session needs to re-establish what belongs where.
---

# spoke-cold-start

Bind a spoke session to the hub without importing the hub's whole world.

**This is not `cwos-cold-start` for spokes.** That skill loads the hub's full operating state: the work-status dashboard, the open-projects rollup, ADRs about hub architecture, the conversation taxonomy. A spoke session needs almost none of it, and loading it creates the specific failure this skill exists to prevent — a spoke session that has absorbed hub structure and starts reproducing it inside a development repository.

A spoke session needs three things: the rules that apply to any work anywhere, the mechanism for talking to the hub, and a clear line about what may be written where.

Hub paths below come from [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md) in the hub — `{{HUB_PATH}}` and `{{HANDOFF_DIR}}`.

## When to invoke

- Session start in a spoke or development repository.
- After compaction in a long spoke session.
- When a spoke session seems unsure what belongs in the repo versus the hub.

## When NOT to invoke

- **In the hub.** Use `cwos-cold-start` there. If the working directory is the hub repo, this is the wrong skill.
- Mid-task for a single rule question. Cite the specific rule instead.

## Procedure

### Step 1 — Load the rules that apply everywhere

Read the hub's `AICONFIG.md` by absolute path (`{{HUB_PATH}}/AICONFIG.md`).

It is the canonical, vendor-agnostic behavioral charter, and it applies to work in any repository, not only the hub. What matters most in a spoke:

- `## STANDARDS - WRITING` — voice, the AI-pattern avoid list, formatting rules, no meta-evaluation of user input. These govern documentation and commit messages written here.
- `## CORE INSTRUCTIONS` — git guardrails, and the rule that authorization does not extend from one batch of work to the next unless explicitly granted.
- `## FILE OPERATIONS` — edits go through the Edit and Write tools, never terminal in-place edits.

Do **not** load `CWOS.md`, the conversation taxonomy, or the hub's project structure. A spoke does not need the operating system specification in order to follow the rules.

### Step 2 — Read the memory index, load selectively

Read `{{HUB_PATH}}/operations/cwos/memory/MEMORY.md`.

Load the feedback memories that govern work anywhere: writing voice, no autonomous commits, formatting rules, handoffs are files. Skip the ones about hub-internal structure and dashboards.

### Step 3 — Establish the handoff relationship

Read `{{HUB_PATH}}/operations/cwos/reference/handoff-protocol.md`.

Determine this session's surface token, which is the repository folder name plus `-cli`, and confirm it appears in the taxonomy. If it does not, say so; registering it is a hub-side task.

**Handoffs for this surface live in the hub**, at `{{HUB_PATH}}/{{HANDOFF_DIR}}/<project>/`, in both directions. They are never written into this repository. Scan that folder for files addressed to this surface and report anything waiting; `handoff-inbox` does this if it is available.

### Step 4 — State the boundary back

The point of the hub is that development repositories stay clean of one operator's AI workflow. Those repositories are read by other people: collaborators, other organizations, future maintainers, sometimes the public.

**Belongs in this repository:** source code, configuration, tests, and documentation that a future maintainer of *this codebase* needs. Architecture decisions, data provenance, deployment constraints, governance of the data this project handles. Anything answering "why is the software like this."

**Belongs in the hub:** handoffs, session notes, reasoning traces, work-status tracking, project rollups, conversation files. Anything answering "what is the operator working on, and why did they decide it that way across projects."

The test is audience. If it would mean something to a stranger who cloned this repository, it belongs here. If it only means something to the operator coordinating sessions, it belongs in the hub.

**A specific trap:** after reading hub context, the pull toward mirroring hub structure into the repository goes up rather than down. Creating a `docs/handoff/` folder here, or a conversations directory, or a work-status file, is the failure mode. Do not.

**Write scope in the hub.** This session may **read anywhere** in the hub, and its **only writable path there is `{{HANDOFF_DIR}}/`**. Conversation files, `-tasks.md` trackers, dashboards and rollups, memory, skills, reference docs, and AICONFIG are hub-owned. If something in the hub needs to change, request it in the return handoff rather than making the edit.

Two reasons: a spoke session editing hub trackers collides with the hub session working the same files, and hub state needs context a spoke session does not have.

**This overrides a skill's own steps.** If a hub skill's procedure tells this session to write hub-owned content, stop and say so rather than following it faithfully. That is how the rule gets broken by a session doing everything else right.

### Step 5 — Read this repository's own documentation

Whatever it has, typically `README.md` and `docs/`. This is the project context, and it is the part that actually determines what the work is.

### Step 6 — Summarize and stop

Report briefly:

- Surface token, and whether it is registered.
- Which behavioral rules are loaded and being applied here.
- Where handoffs live, and what is waiting for this surface.
- The boundary, in one sentence, to demonstrate it was absorbed.
- What this repository is, from its own documentation.

Then wait for direction. Do not begin work, and do not act on a waiting handoff without being told to.

## Output expectations

Short. Roughly 150 to 250 words. A spoke session that produces a hub-sized orientation summary has loaded too much and should be restarted with less.

## Don't do

- **Don't load the hub's work state.** No work-status dashboard, no project rollup, no ADRs, no conversation files beyond the one an inbound handoff cites as its reasoning trace.
- **Don't write anything during orientation.** Read-only.
- **Don't create structure in this repository to mirror the hub.**
- **Don't assume commit permission.** It is granted per repository and per batch unless a handoff says otherwise.

## References

- `{{HUB_PATH}}/AICONFIG.md` — the behavioral charter.
- [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md) — surface taxonomy, filename convention, routing rule.
- Companion skill `cwos-cold-start` — the hub-side equivalent, deliberately much larger.
- Companion skills `handoff-write` and `handoff-inbox`.
