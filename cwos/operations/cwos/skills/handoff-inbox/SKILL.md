---
name: handoff-inbox
description: List cross-surface handoffs addressed to the current session's surface and not yet answered. Scans the hub's handoff folder, which is the fixed location for every handoff except those addressed to another hub; the surface acts as a filter, not a location. Auto-detects the surface from the working directory; accepts an explicit --surface override. Frontmatter-first parse with a filename fallback. Read-only. Use at session start to see what work is queued for this surface, or when the operator asks "what's waiting for me here?".
---

# handoff-inbox

Report which cross-surface handoffs are waiting for this session: the files another surface wrote for this one to act on. Complements `handoff-write`, which authors outbound handoffs.

Canonical spec: [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md), which also holds the `{{HUB_REPO}}` / `{{HUB_PATH}}` / `{{HANDOFF_DIR}}` values used below.

## When to invoke

- Session start, in any session, to see what is queued.
- Operator says "what's waiting for me here?", "what handoffs are queued?", "handoff inbox".
- After finishing a task and before closing the session, to check nothing was routed while working.

## When NOT to invoke

- Operator says "just do X". Go do X; do not sidetrack into an inbox scan.
- Handoff volume is low enough that a manual `ls` is faster than the skill's structured output.

## Inputs

- **`--surface`** (optional) — explicit surface token. If omitted, auto-detect from the working directory:
  - Working directory is `{{HUB_REPO}}` → `hub`.
  - Working directory is a known spoke or development repo → `<repo-folder-name>-cli`.
  - Otherwise, ask the operator rather than guessing.

## Where to look — one location, almost always

Scan `{{HANDOFF_DIR}}/**/*.md` in the hub. From a session running elsewhere, use the absolute path `{{HUB_PATH}}/{{HANDOFF_DIR}}/`.

That one path covers every surface in the ecosystem: handoffs to the hub land there, and handoffs to spokes and development repos stage there rather than in those repos. **The one exception is a handoff addressed to another hub**, which is written into that hub's own folder and is therefore that hub's inbox to scan, not this one's.

The surface determines only the *filter*: include any file with `to: <surface>` in frontmatter, or a filename ending `-to-<surface>.md`. Group by parent folder, which is the `project`.

This holds for browser surfaces too. They have no filesystem access and the operator carries briefs across manually, but the files still live in the same place and can still be listed.

**Do not scan spoke or development repos.** They hold no handoff files. If one turns up in a repo's `docs/handoff/`, it predates the routing rule and should be moved hub-side.

## Procedure

1. **Resolve the surface.** Auto-detect or take `--surface`. If ambiguous, ask. The surface is a filter, not a location.
2. **Scan the hub's handoff folder**, by absolute path if this session runs elsewhere.
3. **Filter to this surface, then sort.** Include files addressed to the resolved surface; exclude `README.md`. Sort newest-first by the filename timestamp, which is authoritative.
4. **Parse each candidate.**
   - **Frontmatter-first.** If the file has YAML frontmatter with a `to` field, use it.
   - **Filename fallback.** If frontmatter is absent, parse `YYYY-MM-DD-HHMM-<from>-to-<to>.md`.
5. **Determine waiting status.**
   - **Explicit reply-tracking.** A file with `response-expected: yes` is waiting unless a sibling file names it in `in-reply-to`.
   - **Heuristic fallback.** Without frontmatter, list handoffs to this surface newer than the most recent outbound from this surface in the same folder, and label the result as heuristic.
   - **Supplements.** A file whose frontmatter carries `supplements:` extends an earlier handoff rather than replacing it. Report both, and note that the earlier one is still in force unless the supplement says otherwise.
6. **Report structured output.** Group by project. For each file: filename, from → to, subject, status, and the first sentence of its Context section.

## Output format

```
Handoff inbox — <surface>

<project-folder>/  (N waiting)
  - 2026-07-23-1015-hub-to-<spoke-a>-cli.md
    hub → <spoke-a>-cli · "<subject>" · waiting
    <first-sentence summary>

<another-project-folder>/  (0 waiting)
  (no unanswered handoffs)

Total: N waiting across M projects. Read one to act on it; use handoff-write to reply.
```

## Read-only guarantee

This skill does not modify any handoff file. It reads, parses, reports.

## Verification

- Every reported file exists at the reported path.
- The frontmatter `to` field, or the filename fallback, matches the resolved surface.
- Waiting and answered status derives from actual sibling files, never fabricated.
- No files were modified.

## Common failure modes

- **Wrong surface auto-detected.** Detection assumes canonical repo folder names. If a folder has been renamed, or the session is in an unusual location, ask rather than guess.
- **Looking in the current repo instead of the hub.** From a spoke session the intuition is to scan locally. There is nothing there.
- **Missing a handoff addressed to another hub.** Those live in the other hub, by design. If the operator expects one and it is absent here, check there before reporting nothing.
- **False "waiting" reports.** When reply-tracking is heuristic, say so rather than claiming certainty.

## References

- [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md) — canonical spec and configuration values.
- Companion skill `handoff-write` — author outbound handoffs.
