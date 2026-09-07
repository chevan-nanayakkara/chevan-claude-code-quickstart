# operations/cwos/reference/ — Universal CWOS Reference Docs

Standing knowledge for CWOS-aligned repos. These docs don't change frequently; they describe formats, standards, and vocabulary used across CWOS deployments.

---

## Docs in this starter

- **[`taxonomy.md`](taxonomy.md)** — CWOS vocabulary glossary. Definitions of hub, spoke, memory, skill, ADR, conversation file, the three-layer split, session lifecycle terms, operating tests (sovereignty, accumulation), and deprecated vocabulary. Read first to standardize terminology across sessions.
- **[`conventional-commits.md`](conventional-commits.md)** — Conventional Commits format reference. Types (feat, fix, docs, chore, refactor, etc.), scope syntax, breaking-change conventions, examples.
- **[`agent-skills-standard.md`](agent-skills-standard.md)** — Anthropic Agent Skills standard reference. Format spec (YAML frontmatter, SKILL.md body, supporting files like scripts/ and references/ and assets/), authoring guidance, when skills are useful vs overkill.
- **[`mcp-stack.md`](mcp-stack.md)** — Model Context Protocol (MCP) server configuration reference. Common MCP servers, configuration patterns, vendor-specific setup notes.
- **[`permissions-posture-ce.md`](permissions-posture-ce.md)** — The C+E permissions posture: a recommended starting shape for `.claude/settings.local.json`. Three layers (auto-allow read tools + Edit; ask gates Write and mutating Bash; hard-deny destructive Bash). Codified in workspace-chevan June 14, 2026; ported to chevan-content and chevan-quickstarts June 16, 2026. Includes per-repo customization guidance and verification probes.
- **[`writing-style-portable.md`](writing-style-portable.md)** — Vendor-neutral writing standards in standalone form: AI watermark word bans, the structural anti-patterns (corrective antithesis, trailing significance, metronomic rhythm, compulsive triads, restatement close, performed judiciousness), borrowed technical jargon, obtuse-principle and balanced-construction patterns, and a copy-paste operator prompt block. Mirrors `AICONFIG.template.md` `### Avoid AI Patterns and Watermarks`. Designed to drop into a non-CWOS repo as `WRITING-STYLE.md` and be referenced from whatever config file that repo's AI tool reads (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, `.github/copilot-instructions.md`).
- **[`handoff-protocol.md`](handoff-protocol.md)** — Cross-surface handoff protocol: surface taxonomy (`hub`, `<spoke>-cli`, browser surfaces), the `YYYY-MM-DD-HHMM-<from>-to-<to>.md` filename convention, YAML frontmatter (`project`, `subject`, `kind: work|admin`, `response-expected`, `in-reply-to`, `supplements`), and the route-by-receiver-inbox rule with its shared-code-repo exception. Ships with a `{{HUB_REPO}}` / `{{HUB_PATH}}` / `{{HANDOFF_DIR}}` configuration block to fill in once at adoption, plus the text of the companion feedback memory an adopting repo should create. Consumed by the `handoff-write`, `handoff-inbox`, and `spoke-cold-start` skills.

## Adding repo-specific reference docs

When a target repo adopts CWOS, you may add repo-specific reference docs to this folder (e.g., a domain-specific glossary, a coding standards reference for the repo's primary language, etc.). Same pattern: stable content that doesn't change frequently and gets read on demand.

## What does NOT belong here

- **Decisions** → `operations/cwos/memory/decisions/` (ADRs).
- **Procedures** → `operations/cwos/skills/<name>/SKILL.md` (skills).
- **Project status** → `operations/cwos/memory/projects/<spoke>/re-entry.md`.

Reference docs are facts that don't change session-to-session. If content evolves with each project or decision, it belongs in memory, not reference.

---

[End of Document]
