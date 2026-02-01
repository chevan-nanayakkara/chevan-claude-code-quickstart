# CLAUDE.md Files: Creating Institutional Memory

| Attribute                   | Details                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Document Type**     | Implementation Guide and Best Practices                                                                                                          |
| **Version**           | 1.1.0                                                                                                                                            |
| **Date**              | January 17, 2026                                                                                                                                 |
| **Author**            | Chevan Nanayakkara                                                                                                                               |
| **Status**            | Active                                                                                                                                           |
| **Classification**    | Internal Reference                                                                                                                               |
| **Purpose**           | Guide for creating, maintaining, and operationalizing CLAUDE.md files for solo and team contexts                                                 |
| **Audience**          | Solo practitioners, team leads, anyone using Claude Code regularly                                                                               |
| **Related Documents** | Teams Guide (organizational patterns), Core Guide (workflow basics),**CLAUDE.md Templates (ready-to-use templates)** , README (navigation) |

---

## Executive Summary

**CLAUDE.md files are project-specific instructions** that Claude Code reads to understand your repository's conventions, terminology, and standards.

 **Core insight from Anthropic** : Teams at Anthropic maintain shared CLAUDE.md files in git. Every mistake becomes a documented rule. The longer you work together, the smarter Claude becomes about your project.

 **Key benefits** :

* Claude follows your conventions automatically
* Mistakes documented once, prevented forever
* New team members (human or AI) inherit accumulated wisdom instantly
* Institutional knowledge persists in version control

 **For solopreneurs** : Your future self is your first teammate. CLAUDE.md captures today's decisions for tomorrow's you.

 **This guide covers** :

* When to create CLAUDE.md (and when to skip)
* How to structure effectively
* Solo operationalization patterns
* Team scaling strategies
* Maintenance and evolution

**Ready to start?** See companion document **CLAUDE.md Templates** for ready-to-use templates (Documentation, Operations, Development, Hybrid repos) with AI pattern avoidance guidelines. Copy, customize, and begin using immediately.

---

## What is CLAUDE.md?

### The Concept

**CLAUDE.md is a markdown file** in your repository root containing instructions for Claude Code:

```
your-project/
├── .git/
├── .gitignore
├── CLAUDE.md          ← Instructions for Claude
├── README.md
└── [your project files]
```

 **When Claude Code starts** , it can read CLAUDE.md to understand:

* Project context and purpose
* Terminology and naming conventions
* File structure and organization
* Code/writing standards
* Common mistakes to avoid
* How you prefer to work

### What Makes It Powerful

 **Persistent memory** : Claude has no memory between sessions. CLAUDE.md provides continuity.

 **Version controlled** : Lives in git with your project. History shows organizational learning.

 **Self-documenting** : Captures "why" decisions were made, not just "what" the rules are.

 **Scalable** : Works solo (personal standards), small teams (shared conventions), large orgs (federated knowledge).

 **Evolutionary** : Starts minimal, grows as you learn, adapts as project changes.

### What It's NOT

 **Not a replacement for** :

* README.md (project overview for humans)
* Documentation (user guides, API docs)
* Code comments (inline explanations)
* .gitignore (file exclusions)

 **Not required for** :

* Every repository (only active ones with specific needs)
* Simple projects (2-3 files, no conventions)
* Projects you rarely touch

---

## When to Create CLAUDE.md

### Decision Framework

 **Create CLAUDE.md when 2+ of these are true** :

1. ✅ You use Claude Code on this repo **weekly or more**
2. ✅ The repo has **specific terminology** or naming conventions
3. ✅ You've made **mistakes you want to prevent** repeating
4. ✅ The repo has **standards or patterns** to follow
5. ✅ You'll **eventually have teammates** (prepare now)
6. ✅ It's a **long-term project** (6+ months)

 **Skip CLAUDE.md when** :

1. ❌ Tiny repo (2-3 files, very simple)
2. ❌ Archive/reference only (read-only, rarely updated)
3. ❌ Experimental/temporary (will delete in weeks)
4. ❌ Generic code with no special conventions
5. ❌ You almost never use Claude Code on it

### Examples by Repository Type

**Documentation repositories** (strategy, research, writing):

```
✅ CREATE for:
- Strategy documents with specific terminology
- Long-form writing with style guidelines
- Multi-document projects with cross-references
- Business plans with versioning conventions

❌ SKIP for:
- Simple meeting notes
- Quick reference lists
- Temporary research dumps
```

**Code repositories** (software, scripts, automation):

```
✅ CREATE for:
- Web applications with architecture patterns
- API projects with naming conventions
- Automation scripts with specific standards
- Long-term development projects

❌ SKIP for:
- One-off scripts
- Code experiments
- Tutorial/learning repos
```

**Operational repositories** (processes, SOPs, templates):

```
✅ CREATE for:
- Company operations with process standards
- Client onboarding with template conventions
- Team handbooks with formatting rules

❌ SKIP for:
- Simple checklists
- Personal notes
```

### Your Specific Repos - Recommendations

Based on typical usage patterns:

```
~/git/work/
├── strategy-vision/          ✅ YES
│   Why: Active work, specific terminology ("Knowledge Authority"),
│        multi-doc coordination, long-term project
│
├── protocol-infrastructure/  ✅ YES (when created)
│   Why: Technical architecture, naming standards
│
└── website/                  ✅ YES (when created)
    Why: Code standards, component patterns

~/git/personal/
├── example-repo/           ? MAYBE
│   Yes if: You use Claude Code weekly for writing
│   No if: Mostly manual writing, occasional Claude
│
└── another-project/      ? MAYBE
    Evaluate: How often you work on it with Claude

~/git/company/
├── ops/                      ✅ YES
│   Why: Operational standards, template conventions
│
└── [other repos]             ? Evaluate case by case
```

---

## CLAUDE.md Structure

### Minimal Template (Start Here)

 **For any new CLAUDE.md** , start with this 20-30 line template:

```markdown
# [Project Name] Guide for Claude

## Project Context
[1-2 paragraphs: What is this project? Who is it for?]

## Terminology
[Key terms and their correct usage]

## Standards
[How to work in this repo - formatting, structure, conventions]

## Common Mistakes
[Lessons learned - starts empty, grows as you learn]

## Instructions for Claude
- Read only files I explicitly specify
- Ask before making assumptions
- Show me what you plan to change before changing files
- Use operational transparency
```

**That's it!** Don't overthink. Start minimal, grow as needed.

### Complete Template (Full Featured)

**For mature projects** with accumulated knowledge:

```markdown
# [Project Name] Guide for Claude

## Project Context
[Detailed description of what this project is, goals, audience]

## Current Phase
[What stage: early development, active production, maintenance, etc.]

## Key Documents/Files
[Important files and their purposes]

## Instructions for Claude Code

### What to Do
- Read only files I explicitly specify
- Ask before making assumptions about scope
- Show planned changes before executing
- Use operational transparency
- Preserve existing voice/style

### What NOT to Do
- Don't auto-scan directories
- Don't assume I want all related files updated
- Don't reformat unnecessarily
- Don't add unrequested content

## Critical Terminology

### Always Use
- [Term 1]: [Definition and usage]
- [Term 2]: [Definition and usage]

### Never Use
- ❌ [Incorrect term]: Use [correct term] instead
- ❌ [Another wrong term]: Use [correct alternative]

### Context-Specific
[Terms that mean different things in different contexts]

## Document/Code Standards

### Structure
[How documents/code should be organized]

### Formatting
[Specific formatting rules - headings, spacing, etc.]

### Naming Conventions
[File names, variable names, function names, etc.]

### Version Control
[How versioning works in this repo]

## File Operations

### Multi-File Updates
[How to handle updates across multiple files]

### Consistency Checks
[What to verify when checking consistency]

### Cross-References
[How to create and maintain references between files]

## Common Mistakes I've Made

### [Category 1]
- [Mistake]: [What went wrong, correct approach]
- [Date added, optional]

### [Category 2]
- [Mistake]: [What went wrong, correct approach]

## Working with Me

### When Starting a Task
[Your preferred workflow for beginning work]

### When Making Changes
[How you want Claude to communicate changes]

### When Complete
[How you want Claude to summarize and confirm]

## Project Evolution Notes

### Changes Log
- [Date]: [What changed in this CLAUDE.md]

### Lessons Learned
[Significant patterns discovered over time]

---

**Remember**: This is a living document. Update whenever you discover a pattern, make a mistake, or learn something new about working effectively on this project.
```

### Section-by-Section Guidance

**Project Context** (Essential):

```markdown
## Project Context
WorkCorp is building protocol infrastructure for decentralized
knowledge networks. This repository contains strategic positioning,
market analysis, and business model documentation.

Current phase: Strategy development (pre-implementation).
```

 **Why this matters** : Claude understands the big picture, can make context-appropriate decisions.

**Terminology** (Critical if you have specific terms):

```markdown
## Critical Terminology

### Always Use
- "Knowledge Authority" - Our term for creators who establish expertise
- "Knowledge Publisher" - Platform that distributes Authority content
- "Protocol Infrastructure" - The underlying technical architecture

### Never Use
- ❌ "Generator" - Use "Knowledge Authority" instead
- ❌ "Packager" - Use "Knowledge Publisher" instead
- ❌ "Platform" - Use "Protocol Infrastructure" (unless discussing platforms generally)

### Common Mistake
Don't change "power generator" to "power Knowledge Authority" -
understand context (electricity generation vs. our product naming).
```

 **Why this matters** : Prevents terminology mistakes, maintains consistent language across documents.

**Standards** (Grows over time):

```markdown
## Document Standards

### Structure
All strategy documents follow:
- Executive Summary (2-3 pages)
- Context and Background
- Analysis (detailed sections)
- Recommendations
- Appendices (optional)

### Formatting
- Version format: vX.Y.Z
- Cross-references: "See [Document Name] Section X.Y"
- Headings: Use markdown ##, ###
- No bullet points in prose (use paragraphs)

### Writing Style
- Professional but conversational tone
- No em-dashes (use commas or semicolons)
- UK spelling
- Define technical terms on first use
```

 **Why this matters** : Claude generates content matching your established patterns.

**Common Mistakes** (Your learning history):

```markdown
## Common Mistakes I've Made

### Terminology
- Don't apply "Knowledge Authority" too literally
  Context: Changed "power generator" to "power Knowledge Authority"
  Lesson: Understand context before term substitution

### Formatting
- Don't use bullet points when prose is requested
  Context: Multiple strategy documents
  Lesson: Prose reads better for narrative content

### Cross-References
- Verify sections exist before referencing them
  Context: Referenced non-existent sections
  Lesson: Check document structure first
```

 **Why this matters** : Mistakes documented once, prevented forever.

**Instructions for Claude** (Your working preferences):

```markdown
## Instructions for Claude Code

### What to Do
- Read only files I explicitly specify (no auto-scanning)
- Ask before assuming which documents to update
- Show me planned changes before executing
- Use operational transparency (show file operations)
- Match my writing voice and style

### What NOT to Do
- Don't scan directories without instruction
- Don't assume all related docs need updating
- Don't reformat existing paragraphs unnecessarily
- Don't add content beyond the specific task
```

 **Why this matters** : Sets clear expectations for how Claude should work with you.

---

## Solo Operationalization

### Your First CLAUDE.md (Step by Step)

 **Choose your most active repo** :

```bash
# Example: WorkCorp strategy documents
cd ~/git/work/strategy-vision
```

 **Create CLAUDE.md** :

```bash
nano CLAUDE.md
```

**Start with minimal template** (20-30 lines):

```markdown
# WorkCorp Strategy & Vision Guide

## Project Context
Strategic positioning and business model documentation for WorkCorp
protocol infrastructure. Focus on market analysis and go-to-market strategy.

## Terminology
- "Knowledge Authority" NEVER "Generator"
- "Knowledge Publisher" NEVER "Packager"
- "Protocol Infrastructure" NOT "platform"

## Standards
- Documents: Executive Summary, Analysis, Recommendations
- Version format: vX.Y.Z
- Writing: Professional but conversational, no em-dashes, UK spelling

## Common Mistakes
[Will grow as I work on this repo]

## Instructions for Claude
- Read only files I specify
- Ask before assumptions
- Show changes before making them
```

 **Save and commit** :

```bash
# Ctrl+X, Y, Enter to save

git add CLAUDE.md
git commit -m "docs: Add CLAUDE.md with project standards"
git push
```

 **Test it immediately** :

```bash
claude

You: "Read CLAUDE.md"
# Claude learns your standards

You: "What are my terminology standards?"
# Claude should reference CLAUDE.md correctly

You: "Read strategic-vision.md and check terminology compliance"
# Claude applies standards to real work
```

### Configuration: Auto-Read vs Explicit

**Option 1: Explicit reading** (recommended for solo):

`~/.claude/config.json`:

```json
{
  "autoReadFiles": [],
  // You manually say "Read CLAUDE.md" each session
}
```

 **Workflow** :

```bash
claude
You: "Read CLAUDE.md"
You: "Read strategic-vision.md"
You: "Update terminology..."
```

 **Pros** :

* Full control over what Claude reads
* Reminds you standards exist
* Explicit about project context

 **Cons** :

* Extra step each session
* Might forget to read CLAUDE.md

**Option 2: Auto-read** (convenience):

`~/.claude/config.json`:

```json
{
  "autoReadFiles": ["CLAUDE.md"],
  // Claude auto-reads CLAUDE.md when starting
}
```

 **Workflow** :

```bash
claude
# CLAUDE.md already loaded
You: "Read strategic-vision.md"
You: "Update terminology..."
```

 **Pros** :

* Automatic, no extra step
* Standards always active
* Simpler workflow

 **Cons** :

* Less explicit
* Might forget CLAUDE.md is being read

 **My recommendation** : Start with **explicit** (Option 1). The ritual of saying "Read CLAUDE.md" keeps you conscious of your standards. Switch to auto-read later if it feels tedious.

### Growing Your CLAUDE.md Organically

**Week 1: Start minimal**

```markdown
# Guide for Claude

## Project Context
[3 lines]

## Terminology
[5 key terms]

## Standards
[3 basic rules]

Total: ~20 lines
```

**Week 4: After first mistakes**

```markdown
# Guide for Claude

## Project Context
[3 lines]

## Terminology
[5 key terms]

## Standards
[5 rules - added 2 new ones]

## Common Mistakes
- Don't use "platform" when discussing our protocol
  (Added: Week 2, after Claude made this mistake)
- Verify cross-references exist before adding them
  (Added: Week 3, after broken references)

Total: ~35 lines
```

**Month 3: Established patterns**

```markdown
# Guide for Claude

## Project Context
[5 lines - more detailed]

## Terminology
[8 terms - added 3 new ones]

## Standards
### Document Structure
[Detailed section structure]

### Writing Style
[Detailed style guide]

## Common Mistakes
[6 documented mistakes with context]

## Working Preferences
[How I like Claude to work with me]

Total: ~80 lines
```

 **Pattern** : Grows naturally based on actual experience, not pre-planned comprehensiveness.

### Maintenance Rhythm

**After mistakes** (reactive - immediate):

```bash
# Claude does something wrong
# Fix it
# Document it

nano CLAUDE.md
# Add to "Common Mistakes" section

git add CLAUDE.md
git commit -m "docs: Document [specific mistake] to prevent recurrence"
```

**Monthly review** (proactive - scheduled):

```bash
# First Monday of month
cd ~/git/work/strategy-vision

# Review git history
git log --since="1 month ago" --oneline

# What patterns emerged?
# What mistakes happened?
# What can be formalized?

nano CLAUDE.md
# Add new patterns
# Update outdated sections

git add CLAUDE.md
git commit -m "docs: Monthly CLAUDE.md review - [Month Year]"
```

**Quarterly cleanup** (maintenance - scheduled):

```bash
# Every 3 months
nano CLAUDE.md

# Review all content:
# - Remove outdated rules
# - Consolidate similar items
# - Reorganize if too long (>200 lines)
# - Update project context if changed

git add CLAUDE.md
git commit -m "docs: Quarterly CLAUDE.md cleanup - Q[N] [Year]"
```

### Multiple CLAUDE.md Files (Multi-Repo Pattern)

 **You'll eventually have several** :

```
~/git/
├── work/
│   ├── strategy-vision/
│   │   └── CLAUDE.md (strategy standards)
│   └── protocol-implementation/
│       └── CLAUDE.md (code standards)
├── personal/
│   └── example-repo/
│       └── CLAUDE.md (writing standards)
└── company/
    └── ops/
        └── CLAUDE.md (operational standards)
```

 **Each is independent** :

* Different project contexts
* Different terminology
* Different standards
* Different mistakes

 **But common patterns emerge** :

* Similar writing style across all docs
* Same git commit format
* Same approach to versioning

 **Two approaches to common patterns** :

**Approach 1: Duplicate** (simpler):

```markdown
# Each CLAUDE.md includes common sections

## Writing Style (Same in all my repos)
- Professional but conversational
- No em-dashes
- UK spelling
[Copy/paste to each CLAUDE.md]
```

**Approach 2: Reference** (DRY):

```
~/git/
├── SHARED-STANDARDS.md (your common patterns)
└── [repos with individual CLAUDE.md files]
```

```markdown
# Repo-specific CLAUDE.md

## Shared Standards
Read ~/git/SHARED-STANDARDS.md for common writing/git conventions.

## Project-Specific
[Only what's unique to this repo]
```

**For solo work, I recommend Approach 1** (duplicate). Most repos have unique enough needs that sharing doesn't save much, and self-contained is simpler.

---

## Team Operationalization

### Solo → First Hire

 **Your CLAUDE.md becomes shared team knowledge** :

**Before** (solo):

```markdown
# WorkCorp Strategy Guide

## Project Context
I'm building strategic positioning documents...

## My Preferences
I prefer...

## Mistakes I've Made
- 2026-01-16: Don't change "power generator" literally
```

**After** (team):

```markdown
# WorkCorp Strategy Guide

## Team
- Chevan: Strategy, positioning
- Alex: Market analysis, competitive research

## Project Context
We're building strategic positioning documents...

## Team Standards
We prefer...

## Common Mistakes
- 2026-01-16 (Chevan): Don't change "power generator" literally
- 2026-02-10 (Alex): Don't use passive voice in executive summaries
- 2026-02-28 (Chevan): Verify data sources before citing
```

 **Key changes** :

* "I" → "We"
* "My" → "Team"
* Attribute mistakes to people (learn who found what)
* Shared conventions emerge

### Team Contribution Workflow

 **Anyone can update** :

```bash
# Team member discovers pattern
nano CLAUDE.md
# Add to relevant section

git add CLAUDE.md
git commit -m "docs: Add requirement for data source verification"
git push

# Other team members pull
git pull
# Now have updated standards
```

**Weekly review** (team ritual):

```
Team standup:
1. Regular updates
2. CLAUDE.md changes this week?
   - Review new additions
   - Discuss if any should be modified
   - Approve or request changes
3. Continue
```

 **git log shows team learning** :

```bash
git log --oneline CLAUDE.md

a7f3c2b Alex: Add data source verification requirement
9b12e4f Chevan: Update terminology section with "Protocol Layer"
c4e8d1a Alex: Document mistake with passive voice
2d91c7b Chevan: Initial CLAUDE.md creation
```

### Small Team → Multiple Teams

 **When you have 6+ people or distinct functional areas** :

```
~/git/work/
├── CLAUDE.md (company-wide standards)
├── backend/
│   └── CLAUDE.md (backend team standards)
├── frontend/
│   └── CLAUDE.md (frontend team standards)
└── strategy/
    └── CLAUDE.md (strategy team standards)
```

**Company-wide** (shared across all teams):

```markdown
# WorkCorp Company Standards

## All Teams Follow
- Terminology: "Knowledge Authority" not "Generator"
- Git commits: type(scope): message format
- Documentation: UK spelling, professional tone
- Code review: Minimum 1 approval required

## Cross-Team Coordination
- API contracts in /contracts directory
- Breaking changes require 2-week notice
- Security changes need #security-review Slack discussion
```

**Team-specific** (backend example):

```markdown
# Backend Team Standards

## Inherits From
Company-wide standards: ~/git/work/CLAUDE.md

## Team Context
Backend API, database, authentication, background jobs.
Tech stack: Node.js, PostgreSQL, Redis.

## Our Conventions
[Backend-specific standards]

## Common Backend Mistakes
[Team's accumulated wisdom]
```

 **Claude reads hierarchically** :

```bash
cd ~/git/work/backend
claude

You: "Read ../CLAUDE.md and ./CLAUDE.md"
# Gets both company + team standards

# Or configure auto-read:
{
  "autoReadFiles": ["CLAUDE.md", "../CLAUDE.md"]
}
```

### Team Governance

**Who approves CLAUDE.md changes?**

**Small team** (2-5 people):

* Anyone can add, commit immediately
* Review in weekly standup
* Trust-based, move fast

**Medium team** (6-15 people):

* Team lead approves changes
* Pull request required for CLAUDE.md
* Discussion if controversial

**Large org** (multiple teams):

* Company CLAUDE.md: Architecture team approves
* Team CLAUDE.md: Team lead approves
* Clear ownership boundaries

 **Example PR process** :

```bash
# Team member creates branch
git checkout -b update-claude-md

nano CLAUDE.md
# Make changes

git add CLAUDE.md
git commit -m "docs: Add requirement for integration tests"
git push -u origin update-claude-md

# Create PR
# Team lead reviews
# Discusses in Slack if needed
# Approves and merges
```

---

## Practical Examples

### Example 1: Documentation Repository

 **Project** : Company strategy documents

 **CLAUDE.md** :

```markdown
# Company Strategy Documentation Guide

## Project Context
Strategic planning documents for company leadership. Updated quarterly,
referenced by board, investors, and executive team.

## Current Documents
- strategic-vision.md - 5-year vision and positioning
- market-analysis.md - Competitive landscape and opportunities
- financial-model.md - Revenue projections and unit economics

## Critical Terminology
- "Revenue Engine" not "Sales Team" (strategic framing)
- "Market Category" not "Industry" (we're creating new category)
- "Knowledge Protocol" not "Knowledge Platform"

## Document Standards

### Structure
- Executive Summary (max 2 pages)
- Context (1-2 pages)
- Analysis (5-10 pages, detailed)
- Recommendations (1-2 pages)
- Appendices (supporting data)

### Version Control
- Version format: vX.Y.Z
- Increment major (X) for strategic pivots
- Increment minor (Y) for new sections
- Increment patch (Z) for corrections/clarifications

### Cross-References
- Format: "See [Document Name] Section X.Y"
- Verify sections exist before referencing
- Update when section numbers change

## Writing Style
- Audience: Board members and investors (sophisticated but not technical)
- Tone: Confident but not arrogant, data-driven
- Length: Be comprehensive, avoid fluff
- Formatting: No bullet points in prose (use paragraphs)

## Common Mistakes
- Don't use "platform" when discussing our protocol infrastructure
  Lesson: Platforms are what others build; we provide protocol layer

- Don't reference sections that don't exist yet
  Lesson: Verify cross-references before creating them

- Don't use em-dashes in formal documents
  Lesson: Use commas or semicolons for clarity

## Working with Me
- Ask which documents need updating (don't assume all)
- Show me planned changes before executing
- Summarize what changed when complete
```

### Example 2: Software Development Repository

 **Project** : Web application

 **CLAUDE.md** :

```markdown
# Company Web Application Guide

## Project Context
React-based web application for knowledge protocol platform.
Production app serving 10K+ users, deployed via Vercel.

Tech stack: React 18, TypeScript, Tailwind, Vite.

## Code Standards

### File Structure
- Components in /src/components
- Hooks in /src/hooks
- Utils in /src/lib
- Types in /src/types
- Max 300 lines per file (split if longer)

### Naming Conventions
- Components: PascalCase (UserProfile.tsx)
- Functions: camelCase (getUserData)
- Constants: SCREAMING_SNAKE (API_BASE_URL)
- Types: PascalCase with T prefix (TUserData)

### TypeScript Rules
- Always use strict mode
- No `any` type - use `unknown` or specific types
- Export types separately from implementations
- Document complex types with JSDoc

### Component Patterns
- Prefer functional components over class components
- Use named exports, not default exports
- Props: Destructure in function signature
- State: useState for local, Context for shared

## Testing Requirements
- Every component needs test file (ComponentName.test.tsx)
- Use React Testing Library, not Enzyme
- Test user interactions, not implementation
- Min 80% coverage on new code

## Common Mistakes
- Don't use `any` type
  Context: PR #234 - caused runtime error
  Solution: Use `unknown` and type narrowing

- Don't wrap async functions in try/catch twice
  Context: PR #267 - double error handling
  Solution: Error boundary at component level OR try/catch, not both

- Don't mock database in tests
  Context: PR #289 - mocks hid real database schema issue
  Solution: Use test database with real schema

## Git Workflow
- Branch naming: feature/issue-number-description
- Commit format: "type(scope): message"
  Types: feat, fix, docs, refactor, test, chore
- PR requires: Tests pass, 80% coverage, 1 approval
```

### Example 3: Operations Repository

 **Project** : Company SOPs and templates

 **CLAUDE.md** :

```markdown
# Operations & Processes Guide

## Project Context
Standard operating procedures, templates, and runbooks for company operations.
Used by entire team, updated as processes evolve.

## Document Types
- SOPs: /sops/ - Step-by-step operational procedures
- Templates: /templates/ - Fillable forms and documents
- Runbooks: /runbooks/ - Incident response and troubleshooting

## Terminology
- "Runbook" not "Playbook" (our standard term)
- "SOP" not "Process Doc" (consistency)
- "Template" not "Form" (when referring to reusable docs)

## Document Standards

### SOP Structure
1. Purpose (1 paragraph)
2. Scope (who this applies to)
3. Procedure (numbered steps)
4. Related Documents (links)
5. Revision History (at bottom)

### Template Conventions
- Use [BRACKETED PLACEHOLDERS] for fill-ins
- Include instructions in italics at top
- Version number in footer
- Last updated date in header

### Runbook Format
- Symptoms (how you know there's an issue)
- Severity (P0-P3 classification)
- Investigation Steps (numbered)
- Resolution Steps (numbered)
- Escalation Path (who to contact)

## Version Control
- SOPs: Update revision history table on every change
- Templates: Increment version number (v1.0, v1.1, v2.0)
- Runbooks: Date-stamp each significant update

## Common Mistakes
- Don't skip the "Purpose" section
  Lesson: Context helps people know if SOP applies to them

- Don't forget to update revision history
  Lesson: Audit trail is critical for compliance

- Don't use passive voice in procedures
  Lesson: "The file is uploaded" vs "Upload the file" - active is clearer

## Team Contribution
- Anyone can propose SOP updates via PR
- Operations lead reviews and approves
- Major process changes need team discussion
```

---

## Advanced Patterns

### Pattern 1: Conditional Standards

 **When standards vary by context** :

```markdown
## Code Standards

### Frontend Code
- Use React functional components
- Tailwind for styling
- Component max: 200 lines

### Backend Code
- Use Express router pattern
- No inline SQL (use ORM)
- Route handler max: 100 lines

### Shared Across Both
- TypeScript strict mode
- No `any` type
- 80% test coverage minimum
```

### Pattern 2: Workflow-Specific Instructions

```markdown
## Working with Me

### For New Features
1. Read feature spec first
2. Ask clarifying questions
3. Propose implementation approach
4. Wait for approval
5. Implement with tests
6. Summarize changes

### For Bug Fixes
1. Understand the bug (read issue)
2. Locate root cause
3. Propose fix
4. Implement with regression test
5. Verify fix in related areas

### For Refactoring
1. Explain what and why
2. Show before/after structure
3. Confirm no behavior changes
4. Execute with comprehensive tests
```

### Pattern 3: External References

 **Link to external documentation** :

```markdown
## Code Standards

### React Patterns
Follow our team's React style guide:
https://company.notion.so/React-Style-Guide

Key points for Claude:
- Functional components only
- Custom hooks for shared logic
- Props destructured in signature

### API Standards
API contracts documented in:
/contracts/api-specification.md

Claude should:
- Verify endpoints against spec
- Match exact response formats
- Include all required fields
```

### Pattern 4: Examples Library

 **Provide concrete examples** :

```markdown
## Code Standards

### Good Component Example
See: src/components/UserProfile.tsx
- Clean prop types
- Proper error handling
- Comprehensive tests

### Good Hook Example
See: src/hooks/useUserData.ts
- Single responsibility
- Error states handled
- Documented with JSDoc

### API Call Pattern
See: src/lib/api/users.ts
- Consistent error handling
- Type-safe responses
- Loading states managed

When implementing similar code, follow these patterns.
```

---

## Troubleshooting

### Issue: CLAUDE.md Too Long

 **Problem** : File exceeds 200 lines, becoming hard to maintain.

 **Solutions** :

**Option 1: Split by hierarchy**

```
/
├── CLAUDE.md (high-level project standards)
└── docs/
    ├── CLAUDE-FRONTEND.md (frontend specifics)
    ├── CLAUDE-BACKEND.md (backend specifics)
    └── CLAUDE-TESTING.md (testing specifics)
```

**Option 2: Extract to separate docs**

```markdown
# CLAUDE.md (streamlined)

## Project Context
[Brief overview]

## Critical Standards
[Only most important rules - top 10]

## Detailed Documentation
- Code standards: See docs/CODE-STANDARDS.md
- Testing guide: See docs/TESTING.md
- Deployment process: See docs/DEPLOYMENT.md

Claude: Read those docs when working in those areas.
```

**Option 3: Prune aggressively**

```bash
# Review each section:
# - Is this still relevant?
# - Does Claude need to know this?
# - Can this be external documentation instead?

# Remove 30-50% of content
# Keep only what Claude actually uses
```

### Issue: Team Ignoring CLAUDE.md

 **Problem** : Team doesn't update CLAUDE.md when they should.

 **Solutions** :

 **Make it part of workflow** :

```
PR checklist:
□ Tests passing
□ Code reviewed
□ Documentation updated
□ CLAUDE.md updated if:
  □ New pattern discovered
  □ Mistake prevented
  □ Standard changed
```

 **Celebrate updates** :

```
Weekly standup:
"Great CLAUDE.md update this week by Alex!
Documented the async/await pattern we discussed.
This will prevent future mistakes."
```

 **Make it visible** :

```bash
# Add to git commit template
# .gitmessage

# If this commit introduces a new pattern or fixes a common mistake,
# consider updating CLAUDE.md to document it for the team.
```

### Issue: Conflicting Standards

 **Problem** : Two team members have different preferences, both documented.

 **Solution** : Discuss and decide**:

```markdown
# Before (conflict):

## Code Style
- Use single quotes (added by Alex)
- Use double quotes (added by Chevan)

# After (resolved):

## Code Style
- Use single quotes for strings
  Decision: Team meeting 2026-01-16
  Rationale: Matches JavaScript community standard
  Note: Existing double quotes will be migrated gradually
```

**Document the resolution** so it doesn't come up again.

### Issue: CLAUDE.md Outdated

 **Problem** : Project evolved, CLAUDE.md didn't.

 **Solutions** :

 **Quarterly review ritual** :

```bash
# Calendar reminder: Review CLAUDE.md
# Every 3 months

# Checklist:
□ Does project context reflect current state?
□ Are all terminologies still accurate?
□ Do standards match current practices?
□ Are examples still relevant?
□ Can anything be removed?
```

 **Git log analysis** :

```bash
# See what actually changed in project
git log --since="3 months ago" --oneline

# Update CLAUDE.md to reflect reality
# Don't keep aspirational standards nobody follows
```

 **Team feedback** :

```
Standup question (monthly):
"Is CLAUDE.md still accurate?
What should we add/change/remove?"
```

---

## Best Practices

### Do's

✅ **Start minimal** (20-30 lines)

* Easy to maintain
* Grows organically
* Not overwhelming

✅ **Update immediately after mistakes**

* Fresh in memory
* Prevents recurrence
* Builds good habit

✅ **Use concrete examples**

* "Don't do X, do Y instead"
* Reference actual files
* Show, don't just tell

✅ **Attribute learnings** (in teams)

* "Added by Alex on 2026-01-16"
* Shows who discovered what
* Encourages contribution

✅ **Version control in git**

* Tracks evolution
* Shows team learning
* Enables rollback if needed

✅ **Review regularly**

* Monthly: Quick scan
* Quarterly: Deep review
* Prune outdated content

✅ **Keep it actionable**

* Clear instructions
* Specific rules
* Avoid vague guidance

### Don'ts

❌ **Don't create for every repo**

* Only active repos with specific needs
* Overhead without benefit otherwise

❌ **Don't make it too long**

* Over 200 lines becomes unwieldy
* Split or prune if too long

❌ **Don't duplicate documentation**

* Link to existing docs
* CLAUDE.md is for Claude-specific guidance
* Not a replacement for README/docs

❌ **Don't set aspirational standards**

* Document what you actually do
* Not what you wish you did
* Standards nobody follows get ignored

❌ **Don't forget to update**

* Outdated CLAUDE.md worse than none
* Schedule regular reviews
* Make updates part of workflow

❌ **Don't over-specify**

* Trust Claude's general knowledge
* Only specify project-specific things
* Avoid teaching basic concepts

❌ **Don't create without need**

* Evaluate: Do we actually need this?
* Simple repos don't need it
* Better to start later when clear need

---

## Migration Strategies

### Adding CLAUDE.md to Existing Project

 **Scenario** : Project is 6 months old, never had CLAUDE.md.

 **Approach** :

**Week 1: Capture current state**

```markdown
# Project Guide

## Project Context
[Write 2-3 paragraphs about current project state]

## Current Practices
[Document how we actually work today, not ideals]

## Known Issues
[Problems we've encountered, patterns we've noticed]
```

**Week 2-4: Observe and document**

```bash
# Work normally
# Every time Claude does something wrong, add to CLAUDE.md
# Every pattern you notice, document it

nano CLAUDE.md
# Add to "Common Mistakes" or "Standards"
git add CLAUDE.md
git commit -m "docs: Document [pattern/mistake]"
```

**Month 2: Refine**

```markdown
# Now you have real data
# Organize into coherent sections
# Remove anything that didn't matter
# Emphasize what actually helps
```

### Splitting Monolithic CLAUDE.md

 **Scenario** : Single CLAUDE.md has grown to 400+ lines.

 **Approach** :

 **Identify natural boundaries** :

```
Current CLAUDE.md (400 lines):
├── Lines 1-50: Project context and general standards
├── Lines 51-150: Frontend-specific (100 lines)
├── Lines 151-250: Backend-specific (100 lines)
├── Lines 251-350: Testing standards (100 lines)
└── Lines 351-400: Deployment process (50 lines)
```

 **Create hierarchy** :

```
/
├── CLAUDE.md (50 lines - general standards)
└── docs/
    ├── CLAUDE-FRONTEND.md (100 lines)
    ├── CLAUDE-BACKEND.md (100 lines)
    ├── CLAUDE-TESTING.md (100 lines)
    └── CLAUDE-DEPLOYMENT.md (50 lines)
```

 **Update main CLAUDE.md** :

```markdown
# Project Guide

## Project Context
[General project info]

## Critical Standards (All Code)
[Top 10 most important rules]

## Area-Specific Standards
When working in specific areas, also read:
- Frontend: docs/CLAUDE-FRONTEND.md
- Backend: docs/CLAUDE-BACKEND.md
- Testing: docs/CLAUDE-TESTING.md
- Deployment: docs/CLAUDE-DEPLOYMENT.md
```

 **Usage** :

```bash
# Frontend work
claude
You: "Read CLAUDE.md and docs/CLAUDE-FRONTEND.md"

# Backend work
claude
You: "Read CLAUDE.md and docs/CLAUDE-BACKEND.md"
```

### Consolidating Multiple CLAUDE.md Files

 **Scenario** : Created separate CLAUDE.md in 5 repos, realize 80% is duplicated.

 **Approach** :

 **Extract shared patterns** :

```
~/git/
├── SHARED-CLAUDE.md (your common standards)
├── work/
│   └── strategy/
│       └── CLAUDE.md (strategy-specific only)
├── personal/
│   └── content/
│       └── CLAUDE.md (content-specific only)
└── company/
    └── ops/
        └── CLAUDE.md (ops-specific only)
```

 **SHARED-CLAUDE.md** :

```markdown
# Shared Claude Code Standards

## Writing Style (All Documentation)
[Common writing patterns]

## Git Workflow (All Repos)
[Common git conventions]

## Claude Working Preferences (All Projects)
[How I generally like to work]
```

 **Repo-specific CLAUDE.md** :

```markdown
# [Project] Guide

## Shared Standards
First read: ~/git/SHARED-CLAUDE.md

## Project-Specific Standards
[Only what's unique to this project]
```

 **Trade-off** : More organized but adds dependency. Worth it if truly 80%+ shared.

---

## Measuring Success

### For Solo Work

 **Metrics that matter** :

 **Mistake reduction** :

```
Month 1: Claude makes 8 mistakes requiring fixes
Month 2: Claude makes 5 mistakes (3 new issues documented)
Month 3: Claude makes 2 mistakes (1 new issue documented)
Month 6: Claude makes <1 mistake per month
```

 **CLAUDE.md growth rate** :

```
Week 1: 25 lines (initial)
Month 1: 45 lines (added learnings)
Month 3: 70 lines (patterns emerged)
Month 6: 75 lines (stable, occasional updates)
```

 **Healthy pattern** : Rapid growth initially, plateaus as patterns stabilize.

 **Time saved** :

```
Before CLAUDE.md:
- Explain conventions each session: 5 min
- Fix mistakes: 10 min/mistake × 8 = 80 min
- Total: 85 min/month wasted

After CLAUDE.md:
- Claude reads CLAUDE.md: 0 min (auto-read)
- Fix mistakes: 10 min/mistake × 1 = 10 min
- Total: 10 min/month wasted

Saved: 75 min/month per repo
```

### For Teams

 **Team metrics** :

 **Contribution rate** :

```bash
# How many team members contributing?
git log CLAUDE.md --format='%an' | sort -u | wc -l

# Healthy: All active team members contribute
# Unhealthy: Only 1-2 people updating
```

 **Update frequency** :

```bash
# How often updated?
git log CLAUDE.md --since="1 month ago" --oneline | wc -l

# Healthy: 5-10 updates/month for active team
# Unhealthy: 0 updates (not being used) or 50+ updates (too noisy)
```

 **Onboarding time** :

```
Before CLAUDE.md:
New hire productive: Week 3-4
Time learning conventions: 2-3 weeks

After CLAUDE.md:
New hire productive: Week 1-2
Time learning conventions: 2-3 days (read CLAUDE.md + ask questions)

Improvement: 1-2 weeks saved per new hire
```

---

## Conclusion

**CLAUDE.md transforms Claude from stateless AI into project-aware assistant** with institutional memory.

**Start small** (20-30 lines), grow organically based on actual experience.

 **For solo work** : Your future self inherits your current wisdom. Mistakes documented once, prevented forever.

 **For teams** : Shared CLAUDE.md in git becomes collective team memory. Every person's learning benefits everyone.

 **The pattern** :

```
Individual mistake → Document in CLAUDE.md → Team/future never repeats
```

 **Success looks like** :

* Fewer repeated mistakes over time
* Faster onboarding (human or AI)
* Consistent output across sessions/people
* Institutional knowledge in version control

 **Get started today** : Pick your most active repo, create CLAUDE.md with 20 lines, use it in your next Claude Code session.

Your CLAUDE.md will grow as you learn. Six months from now, you'll have accumulated wisdom that makes every session more productive.

---

## Document Version History

| Version         | Date             | Summary of Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Author             |
| --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **1.1.0** | January 17, 2026 | Added reference to new CLAUDE.md Templates companion document in Related Documents and Executive Summary. Templates document provides ready-to-use templates for Documentation, Operations, Development, and Hybrid repositories with complete AI pattern avoidance guidelines. Minor update to encourage use of templates for faster CLAUDE.md creation (30-60 min time savings). No structural changes to guide content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Chevan Nanayakkara |
| **1.0.0** | January 16, 2026 | Initial comprehensive guide to CLAUDE.md files. Covers: when to create (decision framework, examples by repo type), structure (minimal to complete templates, section guidance), solo operationalization (first CLAUDE.md, configuration options, organic growth, maintenance rhythms), team operationalization (solo to team transition, contribution workflows, governance), practical examples (documentation, code, operations repos), advanced patterns (conditional standards, workflow-specific instructions, external references), troubleshooting (too long, team adoption, conflicts), best practices, migration strategies, and success metrics. Designed for both solo practitioners building personal institutional memory and teams creating shared knowledge repositories. Emphasizes starting minimal and growing based on actual experience rather than comprehensive pre-planning. | Chevan Nanayakkara |

---

## Quick Reference

 **Creating your first CLAUDE.md** :

```bash
cd your-repo
nano CLAUDE.md
# Start with 20-30 lines
# Project context, terminology, basic standards
git add CLAUDE.md
git commit -m "docs: Add CLAUDE.md"
```

 **Using it** :

```bash
claude
You: "Read CLAUDE.md"
# Now Claude knows your standards
```

 **Updating after mistakes** :

```bash
nano CLAUDE.md
# Add to "Common Mistakes" section
git add CLAUDE.md
git commit -m "docs: Document [mistake] to prevent recurrence"
```

**That's it!** Start simple, grow as needed, let experience guide you.
