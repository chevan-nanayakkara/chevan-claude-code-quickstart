---
name: handoff-write
description: Author a cross-surface handoff file with an explicit-from-to filename and YAML frontmatter. Ask the operator for from / to / project / subject / kind / response-expected; route the file per the handoff protocol (receiver's inbox, except shared code repos which stage hub-side); return the path. Handoffs never land in a spoke or development repo. Use when the operator says "write a handoff", "hand off to <surface>", or when authoring a cross-surface brief that would otherwise be lost in a chat buffer.
---

# handoff-write

Author a cross-surface handoff file that follows the CWOS Handoff Protocol: surface taxonomy, explicit-from-to filename, YAML frontmatter, and the routing rule. The output is a file; the receiving session reads it by absolute path.

Canonical spec: [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md). That file also holds the `{{HUB_REPO}}` / `{{HUB_PATH}}` / `{{HANDOFF_DIR}}` values this skill uses; read them from there rather than hard-coding them here.

## When to invoke

- Operator says "write a handoff", "hand this off to <surface>", "send this to <spoke>".
- Authoring a cross-surface brief that would otherwise live only in a chat buffer.
- Return handoffs from a spoke session back to the hub, invoked from the spoke session.

## When NOT to invoke

- Trivial one-liner requests that do not need durable form.
- Same-session inline continuation, where no surface is being crossed.
- Content that belongs in a `-tasks.md` project detail block rather than as a standalone handoff.

## Inputs

Ask the operator for these in order; accept explicit values if the invocation supplied them.

- **`from`** — sender surface. Auto-suggest from the working directory: `hub` when running in `{{HUB_REPO}}`, otherwise `<repo-folder-name>-cli`. Confirm, and accept an override.
- **`to`** — receiver surface, from the taxonomy. Ask which.
- **`project`** — the umbrella project this handoff belongs to. Becomes the folder name inside the inbox. A project slug, not a date-stamped folder.
- **`subject`** — one short sentence identifying the substantive topic.
- **`kind`** — `work` or `admin`. `work` moves a project forward; `admin` is plumbing. Default `work`. If a handoff mixes both, pick the primary axis and note the secondary in the body.
- **`response-expected`** — `yes` or `no`.
- **`in-reply-to`** — optional. Path to the inbound handoff being answered; `null` for a fresh one.
- **`body`** — the content. Either the operator supplies it, or the skill drafts it from the current conversation and asks for confirmation before writing.

## Routing — where the file lands

**Receiver's inbox, except shared code repos, which stage hub-side.** Filename is always `YYYY-MM-DD-HHMM-<from>-to-<to>.md`.

- **`to: hub`** (this hub) → `{{HANDOFF_DIR}}/<project>/` in this hub.
- **`to: <spoke>-cli`, or any development repo** → hub-side, in the authoring hub's `{{HANDOFF_DIR}}/<project>/`. Those repos never carry handoff artifacts.
- **`to:` another hub** → **that hub's** handoff folder. A hub is a working surface the operator sits inside; a file left in the authoring hub is one they never find. Write the file there, and **do not run git operations in the other hub.**
- **`to: designer` / `to: claude-ai`** → hub-side; the operator carries it across manually. In practice browser handoffs often stay chat-only, so produce a file only when the operator wants durability.

Create the `<project>/` folder if it does not exist.

**Never write a handoff into a spoke or development repo.** Handoffs are artifacts of the operator's AI workflow, and those repos are read by other people. A development repo's own `docs/` is for documentation a future maintainer of that codebase needs; anything coordinating the operator's sessions belongs in the hub.

## Procedure

1. **Gather inputs.** Ask for missing fields; validate `from` and `to` against the taxonomy in the protocol reference. If a token is missing from the roster, say so rather than inventing one — registering a surface is a hub-side task.
2. **Compute the destination.** Apply the routing rule above. Create the project folder if needed.
3. **Compute the timestamp.** Run `date "+%Y-%m-%d-%H%M"` for the filename and `date "+%B %-d, %Y %-I:%M%p"` for prose. Actual posting time, never extrapolated from session start.
4. **Assemble the file.**

    ```markdown
    ---
    from: <from>
    to: <to>
    project: <project>
    subject: <subject>
    kind: work|admin
    response-expected: yes|no
    in-reply-to: <path or null>
    ---

    # Handoff — <from> → <to> — <subject>

    *Written <human-readable timestamp>. In reply to <path>, or "Fresh handoff — no prior inbound".*

    ---

    ## Context

    <what the receiving session needs to know to act>

    ## The ask

    <what the receiver should do, concretely enough to execute>

    ## Standing rules for the receiving session

    - No commits without explicit permission for this batch; authorization does not carry over from a previous one.
    - File writes via Edit/Write tools, never terminal in-place edits.
    - No AI-workflow artifacts in a development repo — handoffs and reasoning traces stay hub-side.
    - <any repo-specific rules: protected branches, PR path, review requirements>

    ## Return handoff

    <when response-expected is yes: the expected return path, absolute, and the shape it should take>

    ## Origin

    Reasoning trace: <conversation file path + timestamp range>.
    ```

5. **Write the file** with the Write tool. Never terminal in-place edits.
6. **Return the path.** "Handoff written at `<path>`. Open the `<receiving-surface>` session and read it from there to execute." Give the absolute path for a non-hub receiver, since that session's working directory is elsewhere.

## Outputs

- A new file at the routed location.
- A summary line naming the path and how to open it.

## Verification

- The file exists at the computed path, and that path matches the routing rule for this receiver.
- Filename follows `YYYY-MM-DD-HHMM-<from>-to-<to>.md`.
- Frontmatter is valid YAML, and its `from` / `to` match the filename tokens.
- Body carries Context / The ask / Standing rules / Return handoff (when applicable) / Origin.
- No commits made, unless the operator's current prompt authorized them.

## Common failure modes

- **Writing the handoff into the receiving code repo.** The most likely error, because "put it where the receiver will see it" is intuitive and wrong here. The receiving session reads the hub by absolute path.
- **Applying "hub-side always" to a hub-to-hub handoff.** The compressed version of the rule is wrong at exactly this case. A handoff to another hub goes into that hub.
- **Editing a handoff already sent.** Write a supplement with `supplements:` in frontmatter instead. Editing in place leaves sender and receiver holding different documents.
- **Chat-only handoff.** If the operator says "just tell me what to hand off" and takes it back to chat, the durable record is lost. Produce the file.
- **Terminal in-place edits.** Never `perl -i`, `sed -i`, or `> file`. Write tool only.

## References

- [`operations/cwos/reference/handoff-protocol.md`](../../reference/handoff-protocol.md) — canonical spec and configuration values.
- Companion skill `handoff-inbox` — list incoming handoffs for the current surface.
- Companion skill `spoke-cold-start` — orient a spoke session to the hub relationship.
