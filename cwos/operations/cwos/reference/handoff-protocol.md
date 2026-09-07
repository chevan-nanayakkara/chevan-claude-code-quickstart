# Handoff Protocol

*Reference for cross-surface handoff files: surface taxonomy, filename convention, YAML frontmatter, and the routing rule that decides which repository a handoff lands in. Universal — adopt as-is and fill in the configuration block below.*

---

## Configure before use

This document ships with placeholders. Replace them once, in this file, when the hub repo adopts CWOS; the two handoff skills read their paths from here.

- **`{{HUB_REPO}}`** — the folder name of your hub repository (the repo where reasoning, conversations, and work tracking live). Example: `my-hub`.
- **`{{HUB_PATH}}`** — the absolute path to that repo, for sessions running elsewhere. Example: `~/git/personal/my-hub`.
- **`{{HANDOFF_DIR}}`** — the hub-relative folder handoffs live in. Conventionally `working/cwos-handoffs`, but any stable path works as long as every surface agrees on it.
- **The spoke roster** in the taxonomy section below — replace the example tokens with your own repos.

If you run only one repository and never cross surfaces, you do not need this protocol. It earns its keep the moment a second session in a second repo starts doing work that the first one has to know about.

---

## The problem this solves

An operator running AI sessions in more than one place has to move work between them: a brief from the hub to a session in a code repo, a status return coming back, a design brief carried into a browser tool. Done in chat, that hand-off is ephemeral. The receiving session never sees it, and a week later nobody can reconstruct what was asked.

Every cross-surface hand-off is therefore a **file** with a durable filesystem home. This reference codifies four things:

1. **Surface taxonomy** — how each place an AI runs gets named.
2. **Filename convention** — how a handoff file self-describes its direction.
3. **YAML frontmatter** — machine-readable metadata.
4. **Routing** — which repository the file lands in.

The taxonomy and convention exist so the operator can open one folder and immediately see what work is waiting for which surface.

---

## Surface taxonomy

A **surface** is a distinct AI-and-tool session location. Each surface has a canonical short token used in filenames and frontmatter.

- **`hub`** — the CLI session running in `{{HUB_REPO}}`. The reasoning hub.
- **`<spoke>-cli`** — a CLI session running in a spoke or development repo. The spoke slug matches the repo folder name. Example roster to replace with your own: `<spoke-a>-cli`, `<spoke-b>-cli`, `<spoke-c>-cli`.
- **`designer`** — a browser-based design tool session.
- **`claude-ai`** — a general browser chat session.

**Extensibility.** When a different AI tool enters the workflow, prefix its shorthand: `cursor-<location>`, `chatgpt`, `gemini-<location>`. The bare-location shorthand (`hub`, `<spoke>-cli`) is reserved for whichever CLI tool is dominant in your workflow.

**Registering a new surface is a hub-side task.** A spoke session that finds its own token missing from this roster should say so in its return handoff rather than adding it, since the roster is hub-owned.

**More than one hub.** If two hubs coordinate, each keeps its own copy of this protocol with its own roster. Use the other hub's surface token (`<other-hub>-cli`, or `hub` when the receiver already knows the context). Cross-repo parity is not enforced and should not be: each ecosystem carries the version that fits it.

---

## Filename convention

**`YYYY-MM-DD-HHMM-<from>-to-<to>.md`**

Both `<from>` and `<to>` are surface tokens from the taxonomy. Every handoff file self-describes its direction from the filename alone, with no need to open it.

Examples:

- `2026-07-23-1015-hub-to-<spoke-a>-cli.md` — the hub authors a brief for a spoke session.
- `2026-07-23-1400-<spoke-a>-cli-to-hub.md` — that spoke returns a status update.
- `2026-07-23-1600-hub-to-designer.md` — the hub composes a design brief the operator carries into a browser tool.

The filename timestamp is authoritative for sorting. It is the posting time, not an extrapolation.

---

## YAML frontmatter

The filename carries direction; frontmatter carries the rest. Optional in general, required if the file will be consumed by the `handoff-write` and `handoff-inbox` skills, which expect machine-readable metadata.

```yaml
---
from: hub
to: <spoke-a>-cli
project: <project-slug>
subject: <one short sentence>
kind: work                # work | admin
response-expected: yes
in-reply-to: null         # or relative path to the inbound handoff
---
```

**`kind`** is a two-value enum. `work` covers handoffs that move a project forward: build briefs, design briefs, verification returns with substantive output, protocol or governance design. `admin` covers the plumbing: commit sweeps, cleanup, ceremony execution, folder retirements, config hygiene. The split lets a reader tell at a frontmatter glance whether they are looking at project-advancing work or housekeeping. `work` is the common case, and a project that never accumulates an `admin` handoff is unremarkable. When a handoff genuinely mixes both, pick the primary axis and note the secondary in the body.

**`in-reply-to`** is what makes reply-tracking mechanical rather than heuristic. A handoff with `response-expected: yes` counts as answered when a sibling file names it here. Skip the field and the inbox skill has to guess.

**Supplementing a handoff already sent.** Do not edit a handoff the receiver may have already read. Write a new file with `supplements: <path>` alongside `in-reply-to:`, and say in the body what has changed. Editing in place means the receiver and the sender no longer hold the same document, with no way to tell.

---

## Route-by-receiver-inbox, modified form

**A handoff lands in the receiver's inbox, except when the receiver is a shared code repository, in which case it stages hub-side.**

- **Hub receivers** get it in *their* hub, at `{{HANDOFF_DIR}}/<project>/`. This includes hub-to-hub handoffs: a handoff addressed to another hub is written into *that* hub, because a hub is a working surface the operator sits inside and will not find a file left somewhere else. File writes into another hub are fine for this purpose; **git operations there are not** — the receiving hub commits its own work.
- **Spoke and development repo receivers** get it **hub-side**, in the authoring hub's folder. Those repos never carry handoff artifacts. The spoke session reads them from the hub by absolute path and writes its returns to the same place.
- **Browser surfaces** (`designer`, `claude-ai`) have no filesystem access. Hub-side, and the operator carries the brief across manually.

The filename's `<to>` token and the frontmatter `to:` field route a handoff to a *surface*. The rule above decides its *location*. These are different questions and conflating them is the usual source of lost handoffs.

**The distinction is who reads the repository.** A hub is one operator's working surface, so workflow artifacts belong there and are findable there. A shared code repository is read by collaborators, other organizations, future maintainers, sometimes the public, and should carry project documentation rather than one operator's reasoning trace. That is the entire purpose of having a hub, and letting handoffs leak into development repos dissolves it. It also means a repo can be transferred, open-sourced, or handed to another maintainer without carrying workflow artifacts that mean nothing to them.

**Consequence for project docs.** A development repo's own `docs/` is still the right home for design decisions that a future maintainer of *that codebase* needs: architecture, data provenance, deployment constraints. The line is audience. If it explains the software, it belongs in the repo. If it coordinates the operator's sessions, it belongs in the hub.

**A note on the tempting wrong rule.** "Hub-side always" is simpler to state and is wrong, because it strands hub-to-hub handoffs in the authoring hub where the receiver never looks. "Receiver's inbox always" is equally simple and equally wrong, because it pushes workflow artifacts into shared code repos. The modified form above is the one that handles both cases, and it is worth stating in full rather than compressing.

---

## Recommended companion memory

This starter ships templates only in `operations/cwos/memory/`, so no populated memory file is included here. An adopting repo should add one, since the routing rule needs to be in the always-loaded layer rather than only in a reference doc read on demand. Create `operations/cwos/memory/feedback_handoff_prompts_are_files.md`:

```markdown
---
name: feedback_handoff_prompts_are_files
description: "Cross-surface handoff prompts are files, never chat-only. They land in the receiver's inbox, except when the receiver is a shared code repo, which stages hub-side. Hub-to-hub handoffs go to the RECEIVING hub."
metadata:
  node_type: memory
  type: feedback
---

Cross-surface handoff prompts are stored as **files**, never chat-only.

**Route-by-receiver-inbox, modified form.** A handoff lands in the receiver's inbox, except when the receiver is a shared code repo, which stages hub-side. Canonical spec at `operations/cwos/reference/handoff-protocol.md`.

**Why:** two separate reasons. Handoffs must not live only in the chat buffer, which is ephemeral and lost. And spoke and development repos are read by other people, so they should carry project documentation, not the operator's AI reasoning trace.

**How to apply:** when producing any cross-surface handoff, WRITE it as a file using the `YYYY-MM-DD-HHMM-<from>-to-<to>.md` convention. The conversation still carries the narrative and the decision; the file carries the exact prompt or bundle.
```

Index it in `MEMORY.md` alongside your other feedback memories.

---

## Skills

Three skills consume this reference:

- **`handoff-write`** — interactive authoring; produces the correctly-named file at the right location. See [`../skills/handoff-write/SKILL.md`](../skills/handoff-write/SKILL.md).
- **`handoff-inbox`** — for the current session's surface, list incoming handoffs waiting for a response. See [`../skills/handoff-inbox/SKILL.md`](../skills/handoff-inbox/SKILL.md).
- **`spoke-cold-start`** — orient a session running in a spoke or development repo to its relationship with the hub, including this protocol. See [`../skills/spoke-cold-start/SKILL.md`](../skills/spoke-cold-start/SKILL.md).

---

## Adoption notes

- **Start with the filename convention alone.** It is most of the value and costs nothing. Frontmatter and the skills can follow once handoff volume justifies them.
- **The routing rule matters more as the number of repos grows.** With one hub and one spoke, any consistent choice works. At five spokes, an inconsistent one means handoffs are permanently scattered.
- **Retire spoke-side drop zones deliberately.** If handoffs already exist inside development repos under something like `docs/handoff/`, move them hub-side in one pass and delete the folders, rather than leaving two conventions live. A repo that still has the folder will keep receiving files in it.

---

[End of Document]
