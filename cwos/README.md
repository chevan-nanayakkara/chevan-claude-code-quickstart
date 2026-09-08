# cwos/ — Conversational Work Operating System starter

A vendor-agnostic architecture for AI-augmented work. Layered configuration / state / procedure split so any AI tool (Claude Code, Codex, Cursor, Aider) can plug into the same repo and operate consistently.

This subdirectory of [`chevan-quickstarts`](../) is a self-contained CWOS starter kit. Use it to bootstrap a new repo with CWOS or to migrate an existing repo from the older `operations/conversational-work/` predecessor.

**New to CWOS?** Start with **[WHY-CWOS.md](WHY-CWOS.md)** — narrative intro covering what CWOS is, the friction it solves, the three-layer approach, and why it's in the public domain. Then come back here for the operational details.

---

## What's here

### Root-level canonical files

- **[`WHY-CWOS.md`](WHY-CWOS.md)** — narrative intro: what CWOS is, the problem it solves, the approach, philosophy, who it's for. Read first if you want the why before the what.
- **[`CWOS.md`](CWOS.md)** — canonical CWOS specification. Read first if you want the architecture spec.
- **[`CWOS-SETUP.md`](CWOS-SETUP.md)** — bootstrap procedure. Four deployment scenarios (hub / spoke / single-repo / polyrepo), step-by-step setup, migration recipe from `operations/conversational-work/`, session-refresh patterns.
- **[`AGENTS.md`](AGENTS.md)** — thin cross-vendor entry point template. Drop into a target repo at root; references AICONFIG.md.

### Templates (placeholders for repo-specific content)

- **[`AICONFIG.template.md`](AICONFIG.template.md)** — AICONFIG.md template with universal sections (canonical source note, core instructions, writing standards, file conventions, git workflow) filled in. Placeholders for repo-specific sections (project context, repository context). Rename to `AICONFIG.md` in the target.
- **[`CLAUDE.template.md`](CLAUDE.template.md)** — thin Claude Code bootstrap template. Rename to `CLAUDE.md` in the target.

### Implementation layer (canonical at `operations/cwos/`)

- **[`operations/cwos/README.md`](operations/cwos/README.md)** — describes the implementation layer itself: the three folders, the conditional fourth (`handoffs/`), and where each kind of content goes. Copy it and replace the deviations section with the target repo's own.
- **[`operations/cwos/skills/`](operations/cwos/skills/)** — universal Agent Skills, grouped into lanes: core workflow (run-prompt protocol, conversation archiving, migration from the predecessor), maintenance (detection-only frontmatter and drift sweeps), session orientation (hub and spoke cold starts), project management (open-projects rollup, prioritization, the refresh orchestrator), cross-surface handoffs (authoring and inbox), and document production (HTML bundle to PDF and Word, with a bundled `scripts/` toolkit). Plus `_template/` for authoring new ones. **[`skills/README.md`](operations/cwos/skills/README.md) is the authoritative inventory**, one paragraph per skill.
- **[`operations/cwos/reference/`](operations/cwos/reference/)** — standing knowledge: CWOS vocabulary, Conventional Commits, the Agent Skills standard, MCP server configuration, the C+E permissions posture, portable writing standards for dropping into non-CWOS repos, and the cross-surface handoff protocol. **[`reference/README.md`](operations/cwos/reference/README.md) is the authoritative inventory.**
- **[`operations/cwos/memory/`](operations/cwos/memory/)** — templates only:
  - `decisions/_template.md` — ADR template (Architecture Decision Records, Michael Nygard format)
  - `projects/_template.md` — re-entry brief template for project resumption

The two README pointers above are deliberate. Naming every artifact here would put the same list in three places, and the copy that gets forgotten is always the one furthest from the files.

---

## How to consume (three patterns)

### Pattern 1: Raw GitHub URL fetches (one-off, no clone)

For a target repo where you only need CWOS files once.

**The lists below are a snapshot, not the inventory.** `operations/cwos/skills/README.md` and `operations/cwos/reference/README.md` are authoritative, and Pattern 2 installs everything without anyone maintaining a list. If you take this path, read those two files afterward to see whether anything shipped since.

```bash
RAW="https://raw.githubusercontent.com/chevan-nanayakkara/chevan-quickstarts/main/cwos"

# Root canonical files
curl -s "$RAW/CWOS.md" -o CWOS.md
curl -s "$RAW/CWOS-SETUP.md" -o CWOS-SETUP.md
curl -s "$RAW/AGENTS.md" -o AGENTS.md
curl -s "$RAW/AICONFIG.template.md" -o AICONFIG.template.md
curl -s "$RAW/CLAUDE.template.md" -o CLAUDE.template.md

# Implementation-layer README
mkdir -p operations/cwos
curl -s "$RAW/operations/cwos/README.md" -o operations/cwos/README.md

# Universal skills
for skill in \
  run-prompt-protocol conversation-archiving cwos-migrate-from-conversational-work \
  frontmatter-validate conversational-maintenance-review \
  cwos-cold-start spoke-cold-start \
  open-projects prioritize-open-projects refresh-work-management \
  handoff-write handoff-inbox \
  document-export _template; do
  mkdir -p "operations/cwos/skills/$skill"
  curl -s "$RAW/operations/cwos/skills/$skill/SKILL.md" \
    -o "operations/cwos/skills/$skill/SKILL.md"
done

# document-export ships a scripts/ toolkit; a SKILL.md-only fetch leaves it unusable
mkdir -p operations/cwos/skills/document-export/scripts
for f in brand.py brand.example.json build_reference.py filter.lua \
         localize_fonts.py post_process_docx.py prep_html.py; do
  curl -s "$RAW/operations/cwos/skills/document-export/scripts/$f" \
    -o "operations/cwos/skills/document-export/scripts/$f"
done

# Reference docs
mkdir -p operations/cwos/reference
for ref in taxonomy.md conventional-commits.md agent-skills-standard.md mcp-stack.md \
           permissions-posture-ce.md writing-style-portable.md handoff-protocol.md; do
  curl -s "$RAW/operations/cwos/reference/$ref" \
    -o "operations/cwos/reference/$ref"
done

# Memory templates
mkdir -p operations/cwos/memory/decisions operations/cwos/memory/projects
curl -s "$RAW/operations/cwos/memory/decisions/_template.md" \
  -o operations/cwos/memory/decisions/_template.md
curl -s "$RAW/operations/cwos/memory/projects/_template.md" \
  -o operations/cwos/memory/projects/_template.md
```

### Pattern 2: Sparse checkout (cwos only, persistent local)

For keeping a local copy of just the cwos subdirectory:

```bash
git clone --filter=blob:none --no-checkout https://github.com/chevan-nanayakkara/chevan-quickstarts.git ~/git/cwos-source
cd ~/git/cwos-source
git sparse-checkout init
git sparse-checkout set cwos
git checkout main

# Reference paths: ~/git/cwos-source/cwos/CWOS.md etc.
```

### Pattern 3: Full clone (multi-use)

For doing multiple migrations or using chevan-quickstarts across many target repos:

```bash
git clone git@github.com:chevan-nanayakkara/chevan-quickstarts.git ~/git/chevan-quickstarts

# Reference paths: ~/git/chevan-quickstarts/cwos/CWOS.md etc.
```

---

## Bootstrap or migrate

After you have the cwos source available, two paths:

### Bootstrap (target has no predecessor infrastructure)

Follow `cwos/CWOS-SETUP.md` "Bootstrap procedure (applies to all scenarios)." Pick a deployment scenario (A hub / B spoke / C single-repo / D polyrepo); copy canonical files; scaffold `operations/cwos/{memory,skills,reference}/`; rename `AICONFIG.template.md` → `AICONFIG.md` and fill in placeholders; rename `CLAUDE.template.md` → `CLAUDE.md`; commit.

### Migrate (target has `operations/conversational-work/`)

Follow the runnable skill at [`operations/cwos/skills/cwos-migrate-from-conversational-work/SKILL.md`](operations/cwos/skills/cwos-migrate-from-conversational-work/SKILL.md). Three sessions (Foundation / Skills + reference / Migration + cleanup); clean-break approach.

In either case, the canonical doc to read first is `cwos/CWOS.md` (the architecture spec) and the operational doc is `cwos/CWOS-SETUP.md` (the bootstrap procedure).

---

## Verify after install

Cold-start verification prompt (from `cwos/CWOS-SETUP.md` "Refreshing an existing session" → Scenario 1):

```
Read /AICONFIG.md for behavioral rules and /README.md for repo orientation. CLAUDE.md auto-loads. Then summarize the CWOS three-layer split (configuration / state / procedure) and the always-restart pattern so I know you've absorbed them.
```

If the summary reflects the architecture, the install is complete.

---

## Where CWOS comes from

CWOS is developed in `workspace-chevan` (trunk, private) and released here. **This starter is the release surface**: each `cwos-vX.Y.Z` tag is a release, [`cwos/CHANGELOG.md`](CHANGELOG.md) is its release notes, and adopting CWOS means taking a tag and recording which one you are on.

**This is not a periodically-synced mirror of somebody's working repository.** Content lands here deliberately, versioned, with notes describing what changed and why.

To suggest improvements, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## License

Unlicense (public domain). See [`../LICENSE`](../LICENSE).
