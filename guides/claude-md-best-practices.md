# CLAUDE.md Templates and Best Practices

| Attribute                   | Details                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Document Type**     | Templates and Reference Guide                                                                        |
| **Version**           | 1.0.0                                                                                                |
| **Date**              | January 17, 2026                                                                                     |
| **Author**            | Chevan Nanayakkara                                                                                   |
| **Status**            | Active                                                                                               |
| **Classification**    | Internal Reference                                                                                   |
| **Purpose**           | Ready-to-use CLAUDE.md templates for documentation, operations, and development repositories         |
| **Audience**          | Anyone creating CLAUDE.md files for new or existing projects                                         |
| **Related Documents** | CLAUDE.md Guide (when to create, how to evolve), Core Guide (workflows), Teams Guide (team patterns) |

---

## Purpose of This Document

This document provides **ready-to-use templates** for creating CLAUDE.md files in your repositories. Copy the appropriate template, customize for your project, and start working with project-specific context immediately.

**Why templates?** Starting from a well-structured template:

* Ensures you include all important sections
* Provides AI pattern avoidance guidelines (reusable across all projects)
* Saves 30-60 minutes per new CLAUDE.md creation
* Gives examples of what to include in each section

 **Four templates provided** :

1. Documentation Repo Template (strategy docs, writing, content)
2. Operations Repo Template (SOPs, templates, processes)
3. Development Repo Template (code, software, APIs)
4. Hybrid Repo Template (multiple purposes in one repo)

---

## AI Pattern Avoidance List (Universal)

**This section is identical across all templates** - copy into any CLAUDE.md to avoid AI watermarks and generic phrasing.

### Avoid AI Patterns and Watermarks

 **Never use these AI-typical phrases** :

* "delve into" / "delve deeper"
* "navigate the landscape"
* "it's important to note that"
* "dive deeper"
* "at the end of the day"
* "leverage" (unless discussing actual leverage/debt)
* "robust" (unless discussing technical robustness)
* "utilize" (use "use" instead)
* "paradigm shift"
* "ecosystem" (unless discussing actual ecosystems)
* "cutting-edge" / "state-of-the-art" (be specific instead)
* "game-changer"
* "synergy"
* "optimize" (unless specifically about optimization algorithms)

**No em-dashes** - Use commas, semicolons, or periods instead

 **No excessive adverbs** :

* Avoid: very, really, quite, extremely, incredibly
* Use specific language instead

**No hedging language** (unless genuinely uncertain):

* Avoid: "seems to," "appears to," "might suggest"
* Be direct: "shows," "indicates," "demonstrates"

 **No repetitive transitions** :

* Avoid: "Furthermore," "Moreover," "Additionally," at the start of every paragraph
* Vary sentence structure naturally

---

## Template 1: Documentation Repository

 **Use for** : Strategy documents, writing, content creation, research, personal knowledge management

```markdown
# [Project Name] Documentation Guide

## Project Context
[Brief description of what this project is about - 2-3 sentences]

**Current phase**: [Pre-launch / Active development / Mature product / etc.]

## Repository Structure

**Active work**:
- `[folder/` - [What's stored here]
- `[another-folder/` - [What's stored here]

**Finding files**:
[How files are organized - by date? by topic? Explain the pattern, not every file]

## When to Use Claude Code vs Claude.ai

**Use Claude Code for**:
- Multi-document updates ("Update terminology across all 3 docs")
- Batch operations ("Ensure cross-references are correct")
- Applying standards ("Make all docs follow formatting guidelines")
- Large restructuring of existing files

**Use Claude.ai for**:
- Drafting new content (iterate, then copy final version)
- Research and synthesis (explore ideas, attach documents)
- Brainstorming and ideation
- Iterative refinement of messaging

**Typical workflow**:
1. Claude.ai: Research, explore, iterate, draft new content
2. Copy final version to Cursor (one-time copy/paste is fine)
3. Claude Code: Later maintenance, multi-file updates, consistency checks

## Instructions for Claude Code

### What to Do
- **Read only files I explicitly specify** - never auto-scan
- **Search for files if exact path unknown** - use pattern matching
- **Ask before making assumptions** about what I want updated
- **Show me what you plan to change** before changing files
- **Use operational transparency** - show me every file operation
- **Preserve my writing voice** - match tone and style of existing content

### What NOT to Do
- **Don't auto-read files** without being asked
- **Don't assume I want all documents updated** (ask which ones)
- **Don't scan directories** without explicit instruction
- **Don't reformat or rewrap** existing paragraphs unnecessarily
- **Don't add content not requested** (stay focused on the task)

## Critical Terminology

**Project-specific terms** (add your key terms here):
- "[Your Term]" **NEVER** "[Alternative you want to avoid]"
- "[Another Term]" **NOT** "[Common mistake]"

**Example**:
- "Knowledge Authority" **NEVER** "Generator"
- "Protocol Infrastructure" **NOT** "platform"

## Writing Style

### Voice and Tone
[Describe your desired voice - professional? conversational? academic? casual?]

**Examples**:
- Professional but conversational
- Data-driven but accessible
- Authentic and personal
- Strategic, not buzzword-heavy

### Avoid AI Patterns and Watermarks

**Never use these AI-typical phrases**:
- "delve into" / "delve deeper"
- "navigate the landscape"
- "it's important to note that"
- "dive deeper"
- "at the end of the day"
- "leverage" (unless discussing actual leverage/debt)
- "robust" (unless discussing technical robustness)
- "utilize" (use "use" instead)
- "paradigm shift"
- "ecosystem" (unless discussing actual ecosystems)

**No em-dashes** - Use commas, semicolons, or periods instead

**No excessive adverbs**:
- Avoid: very, really, quite, extremely, incredibly
- Use specific language instead

**No hedging language** (unless genuinely uncertain):
- Avoid: "seems to," "appears to," "might suggest"
- Be direct: "shows," "indicates," "demonstrates"

## Document Standards

### Structure
[Describe typical document structure for this project]

**Example**:
All strategy documents follow this structure:
- Executive Summary (2-3 pages)
- Context and Background
- Analysis (detailed sections)
- Recommendations
- Appendices (if needed)

### Formatting
- **Version format**: [Your format, e.g., vX.Y.Z]
- **Cross-references**: [Your format, e.g., "See [Document Name] Section X.Y"]
- **Headings**: [Your standard, e.g., markdown headers ##, ###]
- **Other standards**: [Add project-specific formatting rules]

## Common Mistakes I've Made

[This section starts empty and grows over time]

### Terminology
- [Add mistakes here as they happen]

### Formatting
- [Add mistakes here as they happen]

### Assumptions
- [Add mistakes here as they happen]

## Working with Me

### When Starting a Task
1. Confirm you understand the task
2. Tell me which files you'll need to read (search if needed)
3. Outline your approach
4. Ask any clarifying questions
5. Wait for my go-ahead

### When Making Changes
1. Show me what you're about to change
2. Explain your reasoning
3. Highlight any decisions you made
4. Ask if I want to proceed differently

### When Complete
1. Summarize what you changed
2. Note any issues or questions
3. Suggest next steps (if relevant)
4. Let me review before moving on

## Project Evolution Notes

### Changes Log
- [Date]: Initial CLAUDE.md created
- [Future updates here]

### Lessons Learned
[Add patterns and preferences as we work together]
[Each mistake becomes a rule to prevent recurrence]

---

**Remember**: This is a living document. Update it whenever you discover a pattern, make a mistake, or learn something about how we work together effectively.
```

---

## Template 2: Operations Repository

 **Use for** : Business operations, SOPs, templates, processes, runbooks

```markdown
# [Project/Company Name] Operations Guide

## Project Context
[What this operations repo manages - 1-2 sentences]

**Content types**:
- Standard Operating Procedures (SOPs)
- Templates and forms
- Process documentation
- [Other operational content]

## Repository Structure

**Active work**:
- `/sops` - Standard operating procedures
- `/templates` - Reusable document templates
- `/forms` - Intake forms, checklists, worksheets
- `/processes` - Process flows and documentation

## Instructions for Claude Code

### What to Do
- **Read only files I explicitly specify** - never auto-scan
- **Ask before making assumptions** - business operations are specific
- **Show me what you plan to change** before changing files
- **Use operational transparency** - show me every file operation
- **Keep procedures clear and actionable** - step-by-step format

### What NOT to Do
- **Don't auto-read files** - operations may contain sensitive info
- **Don't assume I want all docs updated** - ask which ones
- **Don't scan directories** without explicit instruction
- **Don't use passive voice** in procedures - use active voice
- **Don't add steps I didn't request** - keep procedures lean

## Document Standards

### Standard Operating Procedures (SOPs)

**Structure**:
1. **Purpose** - Why this procedure exists (1 paragraph)
2. **Scope** - Who this applies to, when to use it
3. **Procedure** - Numbered steps (imperative voice)
4. **Related Documents** - Links to templates, forms, other SOPs
5. **Revision History** - Track changes over time

**Writing style**:
- **Active voice** - "Upload the file" not "The file is uploaded"
- **Imperative mood** - Give direct instructions
- **Clear steps** - One action per step
- **Include screenshots** - Where helpful for clarity
- **Note exceptions** - "If X, then do Y instead"

### Templates and Forms

**Templates include**:
- **[BRACKETED PLACEHOLDERS]** - For user to fill in
- **Instructions in italics** - At the top of document
- **Version number** - In footer (v1.0, v1.1, etc.)
- **Last updated date** - In header

### File Naming
- **SOPs**: `sop-[description].md` (e.g., `sop-client-onboarding.md`)
- **Templates**: `template-[description].md` (e.g., `template-invoice.md`)
- **Forms**: `form-[description].md` (e.g., `form-client-intake.md`)

## Terminology

[Add operations-specific terms here]

**Example**:
- "SOP" - Standard Operating Procedure
- "Template" - Reusable document with placeholders
- "Form" - Document for collecting information

## Common Mistakes to Avoid

### SOPs
- ❌ Don't skip the "Purpose" section (context matters)
- ❌ Don't forget to update revision history
- ❌ Don't use passive voice
- ❌ Don't create overly complex procedures (keep it simple)

### Templates
- ❌ Don't forget [BRACKETED PLACEHOLDERS]
- ❌ Don't skip version numbers
- ❌ Don't use company-specific info in templates (use placeholders)

## Working with Me

### When Creating SOPs
1. Ask about the process I want to document
2. Confirm who will use this SOP
3. Outline the steps you understand
4. Ask about exceptions or edge cases
5. Show me draft, iterate based on feedback

### When Creating Templates
1. Ask what the template is for
2. Identify what needs to be customizable
3. Create placeholders for variable content
4. Include helpful instructions
5. Show me example of template filled in

## Project Evolution Notes

### Changes Log
- [Date]: Initial CLAUDE.md created
- [Future updates here]

### Lessons Learned
[Add patterns for good operational documentation]
[Document mistakes in process documentation]

---

**Remember**: Good operational documentation is clear, actionable, and maintained. Write for the team member who'll use this six months from now.
```

---

## Template 3: Development Repository

 **Use for** : Software projects, APIs, web applications, code repositories

```markdown
# [Project Name] Development Guide

## Project Context
[What this codebase does - 1-2 sentences]

**Current phase**: [Planning / Active development / Production / etc.]

**Tech stack**:
- [Language/framework, e.g., TypeScript + React]
- [Database, e.g., PostgreSQL]
- [Key dependencies]

## Repository Structure

**Code organization**:
- `/src` - [What's here]
- `/tests` - [Testing approach]
- `/docs` - [Documentation]
- [Other key directories]

## Instructions for Claude Code

### What to Do
- **Read only files I explicitly specify** - never auto-scan
- **Ask before making assumptions** about architecture decisions
- **Show me what you plan to change** before changing files
- **Use operational transparency** - show me every file operation
- **Follow established patterns** - match existing code style

### What NOT to Do
- **Don't auto-read files** without being asked
- **Don't assume I want all files updated** (ask which ones)
- **Don't scan directories** without explicit instruction
- **Don't skip error handling** - always handle errors explicitly
- **Don't commit without tests** - tests required for all features

## Code Standards

### Language/Framework Standards
[Add language-specific standards here]

**Example for TypeScript**:
- **Strict mode**: Always enabled
- **No `any` type**: Use `unknown` or specific types
- **Explicit return types**: All functions must declare return type
- **Naming conventions**:
  - Files: kebab-case (`user-service.ts`)
  - Classes: PascalCase (`UserService`)
  - Functions: camelCase (`getUserById`)
  - Constants: SCREAMING_SNAKE_CASE (`API_VERSION`)

### File Structure
- `/src/[feature]` - [Organization pattern]
- Max [X] lines per file - split if longer
- [Other structural rules]

### Testing Requirements
- Unit tests for [what needs unit tests]
- Integration tests for [what needs integration tests]
- Minimum [X]% code coverage
- Test file naming: `*.test.[ext]`

## Security Requirements

### Authentication/Authorization
[Your auth standards]

### Input Validation
[Validation requirements]

### Data Protection
[How to handle sensitive data]

## Common Mistakes to Avoid

### Code Quality
- ❌ [Common mistake 1]
- ❌ [Common mistake 2]
- ❌ [Common mistake 3]

### Testing
- ❌ [Testing mistake 1]
- ❌ [Testing mistake 2]

### Security
- ❌ [Security mistake 1]
- ❌ [Security mistake 2]

## Working with Me

### When Starting Development
1. Confirm the feature requirements
2. Propose architecture/approach
3. List files you'll create/modify
4. Ask about edge cases and error scenarios
5. Wait for approval before implementing

### When Writing Code
1. Follow all standards above
2. Include error handling
3. Add inline comments for complex logic
4. Write tests alongside implementation
5. Update this CLAUDE.md if new patterns emerge

### When Complete
1. Summarize what you implemented
2. List files created/modified
3. Confirm tests are passing
4. Note any technical debt or future improvements
5. Ask if I want to review before committing

## Project Evolution Notes

### Changes Log
- [Date]: Initial CLAUDE.md created
- [Future updates here]

### Lessons Learned
[Add mistakes and corrections here as development progresses]
[Each mistake becomes a rule to prevent recurrence]

---

**Remember**: This is a living document. Update it as we develop and learn what works best for this project.
```

---

## Template 4: Hybrid Repository

 **Use for** : Repos serving multiple purposes (e.g., documentation + configuration templates)

```markdown
# [Project Name] Guide

## Project Context
This repository serves multiple purposes:

**1. [Purpose 1, e.g., Writing and content creation]** (Documentation)
- [What content type 1]
- [What content type 2]

**2. [Purpose 2, e.g., Personal infrastructure]** (Operations)
- [What operational content 1]
- [What operational content 2]

## Repository Structure

**[Purpose 1] content**:
- `/[folder]` - [What's here]

**[Purpose 2] content**:
- `/[folder]` - [What's here]

## Instructions for Claude

### For [Purpose 1] Work

**What to Do**:
- [Guidelines specific to purpose 1]

**What NOT to Do**:
- [Anti-patterns for purpose 1]

### For [Purpose 2] Work

**What to Do**:
- [Guidelines specific to purpose 2]

**What NOT to Do**:
- [Anti-patterns for purpose 2]

## Standards for [Purpose 1] Work

[Include relevant sections from Documentation or Development template]

### Writing Style / Code Style
[Purpose 1 specific standards]

### Avoid AI Patterns (if documentation work)
[Include AI pattern avoidance list if doing writing]

## Standards for [Purpose 2] Work

[Include relevant sections from Operations or Development template]

### [Templates / Code / Processes]
[Purpose 2 specific standards]

## Common Standards (All Work)

**General principles that apply across both purposes**:
- [Universal standard 1]
- [Universal standard 2]

## Common Mistakes

### For [Purpose 1]
- [Mistakes specific to purpose 1]

### For [Purpose 2]
- [Mistakes specific to purpose 2]

## Working with Me

### When working on [Purpose 1]
[Workflow for purpose 1]

### When working on [Purpose 2]
[Workflow for purpose 2]

## Project Evolution Notes

### Changes Log
- [Date]: Initial CLAUDE.md created
- [Future updates here]

### Lessons Learned
[Add patterns and preferences as we work together]

---

**Remember**: This repo serves multiple purposes. Make sure to follow the right standards for the type of work you're doing.
```

---

## Customization Guide

### How to Use These Templates

**Step 1: Choose the right template**

* Pure documentation work → Template 1 (Documentation)
* Pure operations work → Template 2 (Operations)
* Pure development work → Template 3 (Development)
* Multiple purposes → Template 4 (Hybrid)

**Step 2: Copy template to your repo**

```bash
# Navigate to your repo
cd ~/git/your-project

# Create CLAUDE.md file
# Copy template content, paste, save

# Commit
git add CLAUDE.md
git commit -m "docs: Add CLAUDE.md with project standards"
```

**Step 3: Customize sections marked with [brackets]**

* Replace all `[Project Name]` with your actual project name
* Replace all `[bracketed instructions]` with your specific content
* Delete placeholder examples, add your real examples

**Step 4: Start minimal, grow organically**

* Don't fill in everything day 1
* Start with:
  * Project Context (2-3 sentences)
  * Critical Terminology (3-5 key terms)
  * Basic Instructions (do's and don'ts)
* Common Mistakes section starts **empty**
* Add to it as you discover patterns and mistakes

**Step 5: Update after mistakes**
Every time Claude does something you didn't want:

1. Add it to "Common Mistakes" section
2. Commit the update
3. Next session, read CLAUDE.md - Claude knows not to repeat it

### What to Customize First

**Critical sections** (customize day 1):

1. ✅ Project Context - What is this project?
2. ✅ Critical Terminology - Your 3-5 most important terms
3. ✅ Instructions for Claude - Basic do's and don'ts

**Important sections** (customize week 1):
4. ✅ Writing Style / Code Style - Your preferences
5. ✅ Avoid AI Patterns - Copy the universal list, customize if needed

**Optional sections** (customize as needed):
6. Repository Structure - If complex or non-obvious
7. Document/Code Standards - As patterns emerge
8. Working with Me - If you have specific workflow preferences

 **Always grows over time** :
9. Common Mistakes - Starts empty, grows with each mistake
10. Lessons Learned - Starts empty, documents what works

### Don't Over-Document

 **Don't document** :

* ❌ Every file path (document patterns instead)
* ❌ Things Claude already knows (how to code, write, etc.)
* ❌ Things that change frequently (file locations that move monthly)
* ❌ General best practices (be specific to YOUR project)

 **Do document** :

* ✅ Project-specific terminology
* ✅ Organizational patterns (how files are structured)
* ✅ Your preferences (voice, style, standards)
* ✅ Mistakes Claude has made in THIS project
* ✅ Things only you know (project context, goals)

### Maintaining Your CLAUDE.md

 **After each mistake** :

```bash
# Immediately update CLAUDE.md
nano CLAUDE.md
# Add mistake to "Common Mistakes" section
# Commit
git add CLAUDE.md
git commit -m "docs: Add [mistake] to common mistakes"
```

 **Monthly review** :

* Read through entire CLAUDE.md
* Remove outdated guidance
* Consolidate duplicate points
* Prune if over 200 lines

 **Quarterly cleanup** :

* Check if terminology changed
* Update file structure if reorganized
* Verify all examples still accurate
* Celebrate growth (your CLAUDE.md is institutional memory!)

---

## Real Examples

### Example 1: WorkCorp Strategy (Documentation)

 **Project Context** :

```markdown
WorkCorp is building protocol infrastructure for decentralized knowledge networks.
This repository contains strategic positioning, market analysis, and business model documentation.

**Current phase**: Strategy and vision development (pre-software implementation).
```

 **Critical Terminology** :

```markdown
- "Knowledge Authority" **NEVER** "Generator"
- "Knowledge Publisher" **NEVER** "Packager"
- "Protocol Infrastructure" **NOT** "platform" (unless discussing platforms specifically)
```

 **Common Mistake Example** :

```markdown
### Terminology
- Don't apply "Knowledge Authority" term too literally (context matters)
- Distinguish between technical protocol discussion and product naming
```

### Example 2: Personal Infrastructure (Hybrid)

 **Project Context** :

```markdown
Personal repository serving two purposes:
1. Writing and content creation (Documentation)
2. Personal infrastructure (Operations)
```

 **For Writing Work** :

```markdown
### Voice
- Authentic and personal - write like I talk
- Use "I" freely - this is my perspective
- Keep personality and humor
```

 **For Operations Work** :

```markdown
### Configuration Files
- Follow established patterns
- Include helpful comments
- Use placeholders for project-specific values
```

### Example 3: Company Ops (Operations)

 **SOP Structure** :

```markdown
1. **Purpose** - Why this procedure exists (1 paragraph)
2. **Scope** - Who this applies to, when to use it
3. **Procedure** - Numbered steps (imperative voice)
4. **Related Documents** - Links to templates, forms, other SOPs
5. **Revision History** - Track changes over time
```

 **Common Mistake** :

```markdown
### SOPs
- ❌ Don't use passive voice ("Click the button" not "The button is clicked")
```

---

## Quick Reference

### Template Selection

| Your Repo Type             | Use Template  | Key Sections to Customize                        |
| -------------------------- | ------------- | ------------------------------------------------ |
| Strategy docs, writing     | Documentation | Writing Style, Terminology, Avoid AI Patterns    |
| SOPs, templates, processes | Operations    | Document Standards, SOP Structure, File Naming   |
| Code, software, APIs       | Development   | Tech Stack, Code Standards, Testing Requirements |
| Multiple purposes          | Hybrid        | Separate standards for each purpose              |

### Minimum Viable CLAUDE.md (20 lines)

```markdown
# [Project Name]

## Project Context
[2-3 sentences: what is this project?]

## Critical Terminology
- "[Term]" **NEVER** "[Avoid]"
- "[Term]" **NOT** "[Avoid]"

## Instructions for Claude
- Read only files I explicitly specify
- Ask before making assumptions
- Show me what you plan to change

## Common Mistakes
[Starts empty, grows over time]

## Changes Log
- [Date]: Initial CLAUDE.md created
```

**This is enough to start.** Grow it organically as you work.

---

## Document Version History

| Version         | Date             | Summary of Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Author             |
| --------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **1.0.0** | January 17, 2026 | Initial creation of CLAUDE.md Templates document. Provides four ready-to-use templates (Documentation, Operations, Development, Hybrid) with complete structure and examples. Includes universal AI Pattern Avoidance list (reusable across all projects). Added comprehensive customization guide showing what to customize day 1 vs. week 1 vs. as-needed. Includes real examples from actual CLAUDE.md files (WorkCorp strategy, personal infrastructure, Vannan ops). Provides "Don't Over-Document" guidance and maintenance recommendations. Created as 8th document in comprehensive Claude Code documentation set. Total length: ~950 lines including all four complete templates. | Chevan Nanayakkara |

---

## Conclusion

**Start with the appropriate template** - copy, customize minimally, begin using.

**Grow organically** - add to "Common Mistakes" after each mistake, update standards as they emerge.

**Keep it under 200 lines** - if longer, you're over-documenting.

**This saves time** - 30-60 minutes creating CLAUDE.md from scratch, 2-3 minutes per session by not repeating yourself.

Your CLAUDE.md becomes **institutional memory** - knowledge that persists across sessions and team members.
