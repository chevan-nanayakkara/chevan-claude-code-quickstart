# Claude Code: Best Practices & Reference Guide

| Metadata | Details |
|----------|---------|
| **Version** | 1.3.0 |
| **Date** | January 18, 2026 |
| **Author** | Chevan Nanayakkara |
| **Purpose** | Best practices, workflow patterns, and comprehensive reference for Claude Code |
| **For** | Heavy content generation, multi-file workflows, session management, and AI-augmented development |

---

## Table of Contents

1. [Quick Reference Card](#1-quick-reference-card)
2. [Understanding Claude Code Modes](#2-understanding-claude-code-modes)
   - 2.1 [Plan Mode](#21-plan-mode)
   - 2.2 [Permission Modes (File Operations)](#22-permission-modes-file-operations)
   - 2.3 [Extended Thinking Mode](#23-extended-thinking-mode-optiont)
   - 2.4 [How the Modes Work Together](#24-how-the-modes-work-together)
   - 2.5 [Quick Decision Guide](#25-quick-decision-guide)
   - 2.6 [Mode Status Indicators](#26-mode-status-indicators)
3. [Keyboard Shortcuts](#3-keyboard-shortcuts)
   - 3.1 [Essential Shortcuts (Use Daily)](#31-essential-shortcuts-use-daily)
   - 3.2 [Efficiency Shortcuts](#32-efficiency-shortcuts)
   - 3.3 [Word Navigation (Requires Option as Meta)](#33-word-navigation-requires-option-as-meta)
   - 3.4 [Setup Multiline Input](#34-setup-multiline-input)
4. [Slash Commands (Built-in)](#4-slash-commands-built-in)
   - 4.1 [Session Management](#41-session-management)
   - 4.2 [Cost & Context Management](#42-cost--context-management)
   - 4.3 [Advanced Features](#43-advanced-features)
   - 4.4 [File References](#44-file-references)
5. [CLI Flags & Options](#5-cli-flags--options)
   - 5.1 [Starting Claude Code](#51-starting-claude-code)
   - 5.2 [Common Patterns](#52-common-patterns)
6. [Custom Skills for Content Workflow](#6-custom-skills-for-content-workflow)
   - 6.1 [Skills You Should Create](#61-skills-you-should-create)
   - 6.2 [Creating Skills](#62-creating-skills)
7. [Session Management Workflow](#7-session-management-workflow)
   - 7.1 [Optimal Session Pattern](#71-optimal-session-pattern)
   - 7.2 [Session Backup & Restore](#72-session-backup--restore)
8. [Session Lifecycle & Context Management](#8-session-lifecycle--context-management)
   - 8.1 [Understanding Token Usage and Context Windows](#81-understanding-token-usage-and-context-windows)
   - 8.2 [When to Continue Current Conversation](#82-when-to-continue-current-conversation)
   - 8.3 [When to Start New Conversation](#83-when-to-start-new-conversation)
   - 8.4 [Context Management Best Practices](#84-context-management-best-practices)
   - 8.5 [Session Continuation Decision Tree](#85-session-continuation-decision-tree)
   - 8.6 [Checking Context Status](#86-checking-context-status)
   - 8.7 [Recovery from Context Overflow](#87-recovery-from-context-overflow)
9. [Content Workflow Patterns](#9-content-workflow-patterns)
   - 9.1 [Phase 1: Planning (Thinking ON)](#91-phase-1-planning-thinking-on)
   - 9.2 [Phase 2: Drafting (Thinking OFF)](#92-phase-2-drafting-thinking-off)
   - 9.3 [Phase 3: Revision (Thinking ON)](#93-phase-3-revision-thinking-on)
   - 9.4 [Phase 4: Polish (Thinking OFF, Opus)](#94-phase-4-polish-thinking-off-opus)
10. [Multi-File Operations](#10-multi-file-operations)
    - 10.1 [Working Across Multiple Files](#101-working-across-multiple-files)
    - 10.2 [Working Folder Convention](#102-working-folder-convention)
11. [Cost Management](#11-cost-management)
    - 11.1 [Tracking & Controlling Costs](#111-tracking--controlling-costs)
12. [Working with Subagents](#12-working-with-subagents)
    - 12.1 [When to Use Subagents](#121-when-to-use-subagents)
    - 12.2 [Spawning Subagents](#122-spawning-subagents)
13. [Config Files Reference](#13-config-files-reference)
    - 13.1 [Primary Configs](#131-primary-configs)
    - 13.2 [Custom Status Line](#132-custom-status-line)
14. [File Organization Patterns](#14-file-organization-patterns)
    - 14.1 [Project Structure](#141-project-structure)
    - 14.2 [CLAUDE.md Template](#142-claudemd-template)
15. [Troubleshooting Quick Reference](#15-troubleshooting-quick-reference)
    - 15.1 [Common Issues](#151-common-issues)
    - 15.2 [Debug Commands](#152-debug-commands)
16. [Integration with Other Tools](#16-integration-with-other-tools)
    - 16.1 [Claude Code + Claude.ai Workflow](#161-claude-code--claude-app-workflow)
    - 16.2 [Claude Code + Git Workflow](#162-claude-code--git-workflow)
    - 16.3 [Claude Code + Cursor Workflow](#163-claude-code--cursor-workflow)
17. [Pro Tips](#17-pro-tips)
    - 17.1 [Efficiency Tips](#171-efficiency-tips)
    - 17.2 [Content Quality Tips](#172-content-quality-tips)
    - 17.3 [Cost Optimization Tips](#173-cost-optimization-tips)
    - 17.4 [Session Management Tips](#174-session-management-tips)
18. [Quick Start Checklist](#18-quick-start-checklist)
    - 18.1 [First Time Setup](#181-first-time-setup)
    - 18.2 [Daily Workflow](#182-daily-workflow)
19. [Learning Resources](#19-learning-resources)
20. [Version History](#20-version-history)

---

## 1. Quick Reference Card

**Most Used (Print This):**
```
Session Start:      cb                    # Start with backup
                    cb --thinking         # Start with thinking mode
                    /rename project-name  # Name session immediately

While Working:      Option+T              # Toggle thinking
                    Option+P              # Switch models (Sonnet ↔ Opus)
                    Shift+Enter           # Multiline prompts
                    /cost                 # Check spending (every hour)

Session End:        Ctrl+D or exit        # Auto-backup on exit

Find Sessions:      claude -r             # Resume picker
                    cb --continue         # Resume most recent
```

---

## 2. Understanding Claude Code Modes

Claude Code has several different "modes" that control how it operates. Understanding these helps you use the right tool for each situation.

### 2.1. Plan Mode

**What it is:** A planning phase where Claude explores your codebase and creates an implementation plan before making changes.

**When it activates:**
- Complex, multi-step tasks that need strategic planning
- You'll see a system message: "Entered Plan Mode"

**What Claude can do in Plan Mode:**
- Read files, search, research
- Write a plan document
- Ask questions to clarify requirements

**What Claude cannot do in Plan Mode:**
- Edit or write actual code files
- Make any changes to your files

**How it ends:**
- Claude uses ExitPlanMode tool
- You review the plan and approve/reject
- After approval: Claude exits plan mode and can start making actual changes

**Example workflow:**
```
You: "Add authentication to the app"
Claude: [Enters Plan Mode automatically]
Claude: [Reads files, researches patterns, writes plan]
Claude: "Here's my implementation plan..." [Exits Plan Mode]
You: [Review plan] Approve
Claude: [Now can make actual file changes]
```

### 2.2. Permission Modes (File Operations)

These control whether Claude asks permission before writing/editing files.

#### 2.2.1. Safety Mode (explicitReadOnly: true)
- **What it does:** Claude shows you proposed changes and waits for approval
- **Use when:** Working with configuration files, infrastructure, unfamiliar code
- **Advantage:** Complete control over every change
- **Disadvantage:** More approval prompts in batch operations

#### 2.2.2. Auto-Accept Mode (explicitReadOnly: false)
- **What it does:** Claude makes changes without asking each time
- **Use when:** Content drafting, batch operations, well-established patterns
- **Advantage:** Faster workflows, fewer interruptions
- **Disadvantage:** Less granular control

#### 2.2.3. Toggle Between Modes: **Shift+Tab** or **Alt+M**
- **Press during session** to switch modes
- **Your config.json** sets the default mode when you start
- **Best practice:** Start in Safety Mode, toggle to Auto-Accept for specific workflows, toggle back when done

**Recommended workflow:**
```
Start session → Safety Mode (default)
                ↓
[Working on content]
                ↓
Press Shift+Tab → Auto-Accept Mode
                ↓
[Claude makes multiple edits automatically]
[You review final output]
                ↓
Press Shift+Tab → Back to Safety Mode
                ↓
[Working on infrastructure files]
[Claude asks permission for each change]
```

### 2.3. Extended Thinking Mode (Option+T)

**What it does:** Shows Claude's reasoning in `<thinking>` blocks before responses

**When to use:**
- **Planning and strategy:** "Should this be one essay or two?"
- **Complex decisions:** "Which architecture pattern fits best?"
- **Understanding problems:** "This feels off but I don't know why"
- **Trade-off analysis:** See pros/cons of different approaches

**When to turn OFF:**
- **Execution tasks:** Drafting, expanding, routine edits
- **Speed matters:** Thinking adds latency
- **Clear instructions:** "Just do X" doesn't need reasoning

**Toggle:** Press **Option+T** at any time during session

**Example:**
```
# Planning phase - thinking ON
Option+T (enable)
You: "Should I lead with the anecdote or the thesis?"
Claude: <thinking>The anecdote hooks readers but...</thinking>
        "Lead with the anecdote because..."

# Execution phase - thinking OFF
Option+T (disable)
You: "Draft section 2"
Claude: [Writes section without showing reasoning]
```

### 2.4. How the Modes Work Together

**Typical multi-phase session:**
```
1. Start session
   └─ Default: Safety Mode (from config.json)
   └─ Thinking: OFF (unless cb --thinking)

2. Planning Phase
   └─ Enable thinking: Option+T
   └─ Claude may enter Plan Mode for complex tasks
   └─ Stay in Safety Mode

3. Execution Phase
   └─ Disable thinking: Option+T
   └─ Toggle to Auto-Accept: Shift+Tab
   └─ Claude makes changes automatically

4. Review Phase
   └─ Enable thinking: Option+T
   └─ Stay in Auto-Accept or return to Safety Mode

5. Infrastructure Work
   └─ Return to Safety Mode: Shift+Tab
   └─ Thinking ON or OFF based on complexity
```

### 2.5. Quick Decision Guide

| Situation | Plan Mode | Permission Mode | Thinking Mode |
|-----------|-----------|-----------------|---------------|
| Complex new feature | May activate automatically | Safety | ON for planning |
| Content drafting | No | Auto-Accept | OFF for speed |
| Batch file processing | No | Auto-Accept | OFF |
| Config file edits | No | Safety | ON if complex |
| Strategic decisions | May activate | Either | ON |
| Routine edits | No | Auto-Accept | OFF |
| Debugging issues | No | Safety | ON |

### 2.6. Mode Status Indicators

**Plan Mode:**
- System messages: "Entered Plan Mode" / "Exited Plan Mode"
- Claude tells you explicitly

**Permission Mode:**
- Changes when you press Shift+Tab or Alt+M
- No persistent indicator (but you'll notice approval prompts or lack thereof)

**Thinking Mode:**
- You see `<thinking>...</thinking>` blocks when ON
- No blocks when OFF
- Status line doesn't show thinking mode (visual blocks are the indicator)

**Session Info:**
- Status line shows: `[project] [session-id • /rename] 128k/200k`
- Use `/cost` to check spending
- Use `/help` to see available commands

---

## 3. Keyboard Shortcuts

### 3.1. Essential Shortcuts (Use Daily)

| Shortcut | Action | Use Case |
|----------|--------|----------|
| **Option+T** | Toggle extended thinking | Planning, strategic decisions, "why" questions |
| **Option+P** | Switch models mid-session | Sonnet (routine) ↔ Opus (complex reasoning) |
| **Shift+Enter** | Multiline prompt | Write detailed prompts without submitting |
| **Ctrl+R** | Reverse search history | Find previous prompts in long sessions |
| **Esc+Esc** | Rewind/undo changes | Rollback Claude's last edit |

### 3.2. Efficiency Shortcuts

| Shortcut | Action | Use Case |
|----------|--------|----------|
| **Shift+Tab** or **Alt+M** | Toggle permission modes | Auto-Accept for batch operations |
| **Ctrl+L** | Clear screen | Reduce clutter, keep history |
| **Ctrl+O** | Toggle verbose output | Debug multi-file operations |
| **?** | Show all shortcuts | Quick reference |

### 3.3. Word Navigation (Requires Option as Meta)

| Shortcut | Action | Setup Required |
|----------|--------|----------------|
| **Option+B** | Back one word | iTerm: Settings → Keys → Left Option = "Esc+" |
| **Option+F** | Forward one word | Terminal: Settings → Keyboard → "Use Option as Meta" |

### 3.4. Setup Multiline Input

```bash
# Run once in Claude Code:
/terminal-setup

# Or configure manually in terminal settings
```

---

## 4. Slash Commands (Built-in)

### 4.1. Session Management

| Command | Purpose | Example |
|---------|---------|---------|
| `/rename <name>` | Name current session | `/rename blog-post-ai-ethics` |
| `/resume [search]` | Interactive session picker | `/resume` or `/resume reading` |
| `/continue` or `-c` | Resume most recent session | `cb --continue` |
| `/memory` | Session-specific notes | `/memory Research: CSV format changed 2024` |

**Best Practice:** Name sessions immediately with `/rename {type}-{topic}-{date}`

### 4.2. Cost & Context Management

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/cost` | Show session spending | Every hour in long sessions |
| `/help` | List all commands & skills | Discover what's available |

### 4.3. Advanced Features

| Command | Purpose | Use Case |
|---------|---------|----------|
| `/agents` | Spawn subagent for task | Research across files, batch processing |
| `/config` | Toggle settings | Change thinking, permissions |

### 4.4. File References

| Syntax | Purpose | Example |
|--------|---------|---------|
| `@filename` | Reference without reading | `@outline.md structure looks good` |
| `@directory/` | Show directory structure | `@blog-posts/ what's here?` |

---

## 5. CLI Flags & Options

### 5.1. Starting Claude Code

```bash
# Basic start (with backup)
cb

# With thinking enabled
cb --thinking

# Resume specific session
cb --resume essay-draft

# Continue most recent
cb --continue

# Use different model
cb --model haiku              # Cheaper for routine tasks
cb --model opus               # Better for complex reasoning

# Cost control
cb --max-budget-usd 5.00      # Set spending limit

# Fork session (branch off without affecting original)
cb --resume reading-list --fork-session
```

### 5.2. Common Patterns

```bash
# Long content session with cost control
cb --thinking --max-budget-usd 10.00

# Quick task with Haiku
claude -p --model haiku "Quick question"

# Resume and continue immediately
cb --continue -p "Next step: polish the conclusion"
```

---

## 6. Custom Skills for Content Workflow

### 6.1. Skills You Should Create

**Location:** `~/.claude/skills/`

#### 6.1.1. Outline Skill

**File:** `~/.claude/skills/outline.md`

```markdown
---
name: outline
description: Create structured outline for content
---

Create a detailed outline for the content idea provided.

Include:
1. Main thesis in one sentence
2. Supporting arguments (3-5 sections)
3. Key points under each section
4. Evidence/examples needed
5. Potential counterarguments

Use markdown hierarchy. Keep it actionable for drafting.
```

**Usage:** `/outline [paste rough idea]`

#### 6.1.2. Expand Skill

**File:** `~/.claude/skills/expand.md`

```markdown
---
name: expand
description: Expand a specific section with depth and examples
---

Expand the section: $ARGUMENTS

Approach:
1. Identify core claim
2. Add supporting evidence
3. Include concrete examples
4. Address counterarguments
5. Maintain voice consistency

Keep proportional to existing content. Avoid AI patterns (no "delve," "leverage," "robust").
```

**Usage:** `/expand section 3` or `/expand the capability gains paragraph`

#### 6.1.3. Polish Skill

**File:** `~/.claude/skills/polish.md`

```markdown
---
name: polish
description: Final refinement pass for publishing
---

Polish the content for publication.

Check:
- Clarity and accessibility
- Flow and transitions
- Evidence quality and completeness
- Redundancies or gaps
- Tone consistency
- AI watermark phrases (per CLAUDE.md)

Suggest specific improvements without rewriting unless necessary.
```

**Usage:** `/polish`

#### 6.1.4. Check Patterns Skill

**File:** `~/.claude/skills/check-patterns.md`

```markdown
---
name: check-patterns
description: Scan for AI watermark phrases
---

Scan content for AI watermark patterns from CLAUDE.md:

**Phrases to avoid:**
- "delve into," "navigate the landscape," "it's important to note"
- "dive deeper," "at the end of the day," "leverage"
- "robust," "utilize," "paradigm shift," "ecosystem"
- Rhetorical turnarounds: "It's not just X, it's Y"
- False bridges: "Here's the thing," "But here's the kicker"
- Framing devices: "At its core," "The key is"
- Stiff transitions: "Moreover," "Furthermore," "What's more"

List any found with line numbers, suggest natural alternatives.
```

**Usage:** `/check-patterns`

### 6.2. Creating Skills

```bash
# Create skills directory
mkdir -p ~/.claude/skills

# Create a skill file
cat > ~/.claude/skills/outline.md << 'EOF'
---
name: outline
description: Create structured outline
---
[Your prompt here]
EOF

# Reload Claude Code (or start new session)
# Type /help to verify skill appears
```

---

## 7. Session Management Workflow

### 7.1. Optimal Session Pattern

```bash
# 1. Start session with backup wrapper
cb --thinking

# 2. Immediately name the session
/rename essay-ai-capability-gains

# 3. Check initial context
[example-repo] [abc12345 • /rename] 5k/200k

# 4. Work in phases
#    - Planning: thinking ON (Option+T shows thinking blocks)
#    - Execution: thinking OFF (faster)
#    - Review: thinking ON (see reasoning)

# 5. Check cost every hour
/cost

# 6. Add session notes as you work
/memory Key decisions: Led with anecdote, moved thesis to para 2

# 7. Switch models when needed
Option+P → Opus (complex strategy)
Option+P → Sonnet (execution)

# 8. Exit (auto-backup triggers)
Ctrl+D or exit
```

### 7.2. Session Backup & Restore

**Automatic backup on exit:**
```bash
cb              # Backs up to OneDrive when you exit
cb --continue   # Also backs up on exit
```

**Restore from backup:**
```bash
claude-restore  # Interactive menu: latest or specific snapshot
```

**View backup status:**
```bash
claude-backup-status
```

**Backup location:**
```
/Users/you/Documents/claude-code/backups/
├── current/           # Latest backup (overwrites)
└── snapshots/         # Timestamped snapshots
```

---

## 8. Session Lifecycle & Context Management

### 8.1. Understanding Token Usage and Context Windows

Claude Code has a **200,000 token context window** (with "contextWindow": "large" setting). Understanding when your context is filling up helps you decide when to continue a session vs. start fresh.

**Current token usage shows in status line:**
```
[project-name] [session-id • /rename] 73k/200k tokens
                                      ↑    ↑
                                   Used  Total
```

**What uses tokens:**
- **Your prompts** - Every message you send
- **Claude's responses** - All text, thinking blocks, tool results
- **File reads** - Contents of files Claude reads
- **Conversation history** - Full context maintained throughout session
- **System messages** - Mode changes, tool confirmations

**Rough estimates:**
- 1 page of text ≈ 500-750 tokens
- Long file read (500 lines) ≈ 2,000-4,000 tokens
- Typical conversation turn ≈ 1,000-3,000 tokens
- 4-hour content session ≈ 60,000-120,000 tokens

### 8.2. When to Continue Current Conversation

**Continue when (under ~150k tokens):**

1. **Related work in same domain**
   - Still working on same project/files
   - Building on previous decisions
   - Context from earlier in session is valuable

2. **Sequential tasks**
   - "Now polish the introduction"
   - "Apply same pattern to chapter 2"
   - "Check for similar issues in other files"

3. **Iterative refinement**
   - Multiple revision passes
   - Incremental improvements
   - Building on feedback

4. **Plenty of context remaining**
   - Under 120k tokens used
   - Session has valuable accumulated context
   - Would be inefficient to re-explain

**Example scenarios:**
```
✓ "Now update the Windows guide with same changes"
✓ "Polish the conclusion section we just drafted"
✓ "Apply this refactoring pattern to the other templates"
✓ "Check if we missed anything in the setup guides"
```

### 8.3. When to Start New Conversation

**Start fresh when:**

1. **Context window getting full (150k+ tokens)**
   - You'll see automatic summarization warnings
   - Responses may get slower
   - Risk of context overflow

2. **Major topic shift**
   - Finished infrastructure work, now writing blog post
   - Switching from one project to completely different one
   - Different type of work (development → content → operations)

3. **Want clean slate**
   - Previous session has lots of trial/error to leave behind
   - Starting new approach to a problem
   - Fresh context ensures Claude doesn't carry over old assumptions

4. **Performance degradation**
   - Responses getting noticeably slower
   - Claude seems to "forget" earlier context
   - Session feels sluggish

5. **Natural breakpoint**
   - Completed a major milestone
   - End of work day, want fresh start tomorrow
   - Finished one phase, starting another

**Example scenarios:**
```
✓ Context at 165k - time to start fresh
✓ Finished setup guides, now working on blog post
✓ Tried 3 approaches that didn't work, want clean slate
✓ End of day - will resume tomorrow with fresh session
✓ Completed infrastructure, switching to content creation
```

### 8.4. Context Management Best Practices

**1. Monitor token usage:**
```bash
# Status line shows usage
[project] [session] 73k/200k tokens

# General guidelines:
0-80k:    Fresh session, plenty of room
80-120k:  Healthy usage, continue freely
120-150k: Getting full, consider wrapping up
150k+:    Start thinking about new session
180k+:    High risk, start new session
```

**2. Use session forking for branching:**
```bash
# Fork creates new session with same context
cb --resume essay-draft --fork-session

# Use when:
# - Want to try different approach without losing original
# - Experiment while keeping main session clean
# - Branch exploration from main work
```

**3. Summarize and start fresh:**
```
# Before starting new session, ask Claude to summarize:
"Summarize key decisions and current state for handoff to next session"

# Copy summary, start fresh:
cb
/rename essay-draft-continued

# Paste summary as first prompt:
"Continuing from previous session. Context: [paste summary]"
```

**4. Use /memory for session notes:**
```bash
/memory Key decisions: Led with anecdote, thesis in para 2, avoiding "delve"
/memory Research sources: Smith 2024, Jones 2023
/memory Next session: Polish conclusion, run check-patterns

# Memory persists with session for future resumes
```

**5. Break large tasks into multiple sessions:**
```
Session 1 (cb): Planning and outline (60k tokens)
Session 2 (cb): Draft sections 1-3 (80k tokens)
Session 3 (cb): Draft sections 4-6 (75k tokens)
Session 4 (cb): Revision and polish (65k tokens)

Total: 280k tokens across 4 sessions
Better than: One 280k session that would overflow
```

### 8.5. Session Continuation Decision Tree

```
Current session < 120k tokens?
├─ Yes: Continue if working on related tasks
│  └─ Use same session for sequential work
│
└─ No: Context > 120k?
   ├─ 120-150k: Wrap up current task, then start new session
   │  └─ Finish what you're doing, don't start new work
   │
   └─ 150k+: Start new session now
      └─ Summarize if needed, then fresh start
```

### 8.6. Checking Context Status

**Unfortunately, there's no built-in `/tokens` command**, but you can estimate:

**Method 1: Status line**
```
[project] [session-id] 128k/200k tokens
                       ↑ Current usage
```

**Method 2: Rough calculation**
- Count conversation turns × ~2,000 tokens/turn
- Count file reads × file size estimate
- Long session (2+ hours) ≈ 60-100k tokens
- Very long session (4+ hours) ≈ 120-180k tokens

**Method 3: Performance indicators**
- Fast responses: Under 100k
- Slight delay: 100-150k
- Noticeable slowdown: 150k+
- System summarization messages: Approaching limit

### 8.7. Recovery from Context Overflow

**If session hits context limit:**

1. **Don't panic** - Your work is saved
2. **Exit session** - `Ctrl+D` or `exit`
3. **Start fresh** - `cb`
4. **Summarize previous work** - "Review changes from last session"
5. **Continue** - Build on previous work in new session

**Your backups protect you:**
```bash
claude-restore    # If needed, restore from snapshot
```

---

## 9. Content Workflow Patterns

### 9.1. Phase 1: Planning (Thinking ON)

```bash
# Start with thinking to see reasoning
Option+T (enable thinking)

/outline [rough idea]

# Ask strategic questions
"Should this be one essay or split into two?"
"Lead with anecdote or thesis?"

# See thinking blocks showing trade-offs
```

### 9.2. Phase 2: Drafting (Thinking OFF)

```bash
# Turn off thinking for faster execution
Option+T (disable thinking)

# Use multiline prompts
Shift+Enter to structure requests:
"Draft section 1 covering:
- Point A
- Point B
- Example C"

# Expand sections as needed
/expand introduction
/expand section 3
```

### 9.3. Phase 3: Revision (Thinking ON)

```bash
# Enable thinking to understand problems
Option+T (enable thinking)

"This paragraph feels off but I can't say why"

# See reasoning about what's wrong
# Get specific fixes
```

### 9.4. Phase 4: Polish (Thinking OFF, Opus)

```bash
# Switch to Opus for final quality check
Option+P → Opus

/polish
/check-patterns

# Get final review
"Ready to publish?"

# Switch back to Sonnet
Option+P → Sonnet
```

---

## 10. Multi-File Operations

### 10.1. Working Across Multiple Files

```bash
# Reference files without loading
"Check @blog-posts/2025/ for related content"
"Review structure of @outline.md"

# Edit multiple related files
"Update chapter-1.md introduction to align with outline.md changes"

# Search across files with subagent
/agents
"Use Explore agent to find all mentions of 'capability gain' across my writing"
```

### 10.2. Working Folder Convention

```bash
# Use .claude.working.{project}/ for intermediate work
.claude.working.essay-ai-ethics/
├── research-notes.md
├── outline-v1.md
├── outline-v2.md
├── draft-sections/
└── references.md
```

**Why:** Separates work-in-progress from final output, easy cleanup when done

---

## 11. Cost Management

### 11.1. Tracking & Controlling Costs

**Check cost regularly:**
```bash
/cost                    # Shows cumulative session cost
```

**Set budget limits:**
```bash
cb --max-budget-usd 5.00    # Hard limit for session
```

**Model selection by task:**

| Task Type | Model | Cost | When to Use |
|-----------|-------|------|-------------|
| Routine drafting | Sonnet | ~$3-5/hr | Default for most work |
| Complex strategy | Opus | ~$15-20/hr | Major decisions, complex reasoning |
| Simple tasks | Haiku | ~$0.50/hr | Quick questions, formatting |

**Switch models mid-session:**
```bash
Option+P                    # Keyboard shortcut
# or
--model opus                # CLI flag on start
```

**Estimated costs (4-hour session):**
- Sonnet only: ~$12-20
- Mixed (mostly Sonnet, some Opus): ~$20-35
- Opus heavy: ~$60-80

---

## 12. Working with Subagents

### 12.1. When to Use Subagents

**Use subagents for:**
- Research across many files (Explore agent)
- Batch data processing (general-purpose agent)
- Background tasks while you work

**Don't use for:**
- Content drafting (needs your voice)
- Iterative revision (needs context)
- Strategic decisions (needs your judgment)

### 12.2. Spawning Subagents

```bash
/agents

# Select agent type:
# - Explore: Read-only research, fast (Haiku)
# - general-purpose: Multi-step tasks, full access

# Example prompts:
"Use Explore agent to find all blog posts mentioning AI ethics"
"Use general-purpose agent to process this CSV in chunks"
```

**Result:** Agent works in background, returns summary only

---

## 13. Config Files Reference

### 13.1. Primary Configs

**User-level config:**
```
~/.claude/config.json         # Main configuration
~/.claude/settings.json       # Additional settings (model, statusline)
```

**Project-level overrides:**
```
.claude/settings.json         # Project-specific settings
.claude/settings.local.json   # Local overrides (git-ignored)
```

**Your current setup:**
```json
{
  "explicitReadOnly": true,        // Require approval for writes
  "contextWindow": "large",        // 200k tokens
  "sessionTimeout": 7200,          // 2 hours (consider increasing to 14400)
  "autoReadFiles": [],             // Consider adding ["CLAUDE.md", "README.md"]
  "ignorePatterns": [...]          // Skip node_modules, dist, etc.
}
```

**See:** `config-reference.md` for detailed parameter documentation

### 13.2. Custom Status Line

**Location:** `~/.claude/statusline.sh`

**Shows:**
```
[project-name] [session-id • /rename] 128k/200k
```

**Customize:** Edit statusline.sh to add/remove information

---

## 14. File Organization Patterns

### 14.1. Project Structure

```
project-root/
├── CLAUDE.md                      # Auto-read context
├── README.md                      # Project overview
├── .claude/
│   ├── settings.json              # Project config
│   └── skills/                    # Project-specific skills
├── .claude.working.{project}/     # Intermediate work
│   ├── research/
│   ├── drafts/
│   └── outlines/
├── content/                       # Final outputs
└── archive/                       # Completed work
```

### 14.2. CLAUDE.md Template

```markdown
# Project Context

**Project:** [Name and purpose]

**Voice:** [Tone, style, audience]

**Patterns to avoid:**
- AI watermarks (delve, leverage, robust)
- [Project-specific patterns]

**Key decisions:**
- [Document important choices made]

**Resources:**
- [Links to references]
```

---

## 15. Troubleshooting Quick Reference

### 15.1. Common Issues

| Problem | Solution |
|---------|----------|
| Session timed out | Increase `sessionTimeout` in config.json to 14400 (4 hours) |
| Too many permission prompts | Use `Shift+Tab` for Auto-Accept, or set `explicitReadOnly: false` |
| Can't find old session | Use `claude -r [search-term]` or `cb --resume` |
| Multiline input not working | Run `/terminal-setup` or configure Option as Meta |
| High costs in long sessions | Check `/cost` hourly, switch to Haiku for routine tasks |
| Context window filling up | Session > 150k tokens? See "Session Lifecycle & Context Management" section for when to start fresh |
| Skill not appearing | Check file in `~/.claude/skills/`, restart Claude Code |
| Lost work | `claude-restore` from OneDrive backup |

### 15.2. Debug Commands

```bash
# Check Claude version
claude --version

# View config
cat ~/.claude/config.json | jq .

# See active sessions
claude -r

# View backup status
claude-backup-status

# Check session files
ls -la ~/.claude/projects/

# View history
cat ~/.claude/history.jsonl | tail -10
```

---

## 16. Integration with Other Tools

### 16.1. Claude Code + Claude.ai Workflow

**Pattern:**

1. **Ideate in Claude.ai**
   - Fast brainstorming
   - Artifacts for previews
   - Attach research PDFs

2. **Execute in Claude Code**
   - Multi-file operations
   - Version control integration
   - Iterative refinement

3. **Quick checks in Claude.ai**
   - "Does this hook work?"
   - One-off questions

**Example:**
```
Claude.ai: Brainstorm 5 blog post angles (30 min)
Claude Code: Write and refine chosen post (2 hours)
Claude.ai: Final check - "Does this opening grab you?"
```

### 16.2. Claude Code + Git Workflow

```bash
# Before major changes
git status                          # Check clean state
git branch feature-new-section      # Branch for safety

# Work in Claude Code
cb --thinking
[Make changes via Claude]

# Review changes
git diff                           # See what Claude changed

# Commit if good
git add .
git commit -m "Add new section on capability gains

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Rollback if needed
git reset --hard                   # Undo everything
```

### 16.3. Claude Code + Cursor Workflow

**Cursor for:**
- Real-time visual verification
- File tree navigation
- Quick manual edits

**Claude Code for:**
- AI-assisted operations
- Multi-file coordination
- Complex transformations

**Run simultaneously:**
- Claude Code in terminal
- Cursor IDE showing files
- See changes in real-time

---

## 17. Pro Tips

### 17.1. Efficiency Tips

1. **Name sessions immediately** - `/rename` before you forget
2. **Check cost hourly** - `/cost` every 60 minutes in long sessions
3. **Use multiline prompts** - Shift+Enter for structured requests
4. **Switch models strategically** - Option+P: Sonnet (routine) ↔ Opus (strategy)
5. **Search don't scroll** - Ctrl+R to find old prompts
6. **Batch operations** - Shift+Tab to Auto-Accept for repetitive tasks

### 17.2. Content Quality Tips

1. **Toggle thinking for decisions** - Option+T when you need reasoning
2. **Use skills for consistency** - `/polish`, `/check-patterns` every time
3. **Reference, don't load** - `@filename` instead of "read this file"
4. **Keep context clean** - Use `/memory` for session notes, not main conversation
5. **Verify with Cursor** - Visual check of changes in IDE

### 17.3. Cost Optimization Tips

1. **Default to Sonnet** - Use Opus only when needed
2. **Haiku for simple tasks** - `claude -p --model haiku "quick question"`
3. **Set budget limits** - `--max-budget-usd` prevents surprises
4. **Monitor token usage** - Status line shows 128k/200k
5. **Batch similar work** - Do all expansions at once, not spread across sessions

### 17.4. Session Management Tips

1. **Naming convention** - `{type}-{topic}-{date}` like `essay-ai-ethics-20260118`
2. **Use working folders** - `.claude.working.{project}/` for intermediate files
3. **Session notes** - `/memory` for research sources, decisions made
4. **Pause/resume freely** - 4-hour timeout gives breathing room
5. **Backup is automatic** - `cb` wrapper handles it on exit

---

## 18. Quick Start Checklist

### 18.1. First Time Setup

- [ ] Configure terminal for multiline input: `/terminal-setup`
- [ ] Set Option as Meta (for Option+P, Option+T): Terminal settings
- [ ] Increase session timeout: `~/.claude/config.json` → `"sessionTimeout": 14400`
- [ ] Create skills directory: `mkdir -p ~/.claude/skills`
- [ ] Create 4 content skills: outline, expand, polish, check-patterns
- [ ] Add CLAUDE.md to projects: Describes context, voice, patterns to avoid
- [ ] Test backup/restore: `cb` → exit → `claude-restore`

### 18.2. Daily Workflow

- [ ] Start with `cb` (or `cb --thinking` for planning sessions)
- [ ] Immediately `/rename {type}-{topic}-{date}`
- [ ] Check status line: project, session ID, token usage
- [ ] Work in phases: planning (thinking ON) → execution (OFF) → review (ON)
- [ ] Check `/cost` every hour
- [ ] Switch models with Option+P when needed
- [ ] Use skills for consistency: `/outline`, `/expand`, `/polish`, `/check-patterns`
- [ ] Exit normally - auto-backup triggers

---

## 19. Learning Resources

**In Claude Code:**
- Type `?` - Show all keyboard shortcuts
- Type `/help` - List all commands and skills
- Type `/terminal-setup` - Configure multiline input

**Documentation:**
- `config-reference.md` - Detailed config documentation
- `CLAUDE.md` - Project context and voice guidelines
- Reading list post-mortem - Full workflow analysis

**Practice:**
- Create one custom skill this week
- Use multiline prompts (Shift+Enter) in next session
- Try Option+P to switch models mid-session
- Check `/cost` hourly during long session

---

## 20. Version History

| Version | Date | Summary of Changes | Author |
|---------|------|-------------------|--------|
| 1.3.0 | 2026-01-18 | Added comprehensive table of contents and section numbering throughout document. All 20 major sections now numbered (1-20) with subsections using hierarchical numbering (e.g., 2.1, 2.2.1, 8.4). TOC provides clickable navigation links to all sections and subsections. Improves document navigation and reference usability for 1,200+ line guide. | Chevan Nanayakkara |
| 1.2.0 | 2026-01-18 | Evolved from cheat sheet to "Best Practices & Reference Guide". Added comprehensive "Session Lifecycle & Context Management" section covering: when to continue vs start new conversations, token usage understanding, context window monitoring (0-80k fresh, 80-120k healthy, 120-150k getting full, 150k+ time for new session), context management best practices (forking, summarizing, /memory usage, breaking large tasks), session continuation decision tree, checking context status methods, recovery from overflow. Document now serves as both quick reference and comprehensive best practices guide. | Chevan Nanayakkara |
| 1.1.0 | 2026-01-18 | Added comprehensive "Understanding Claude Code Modes" section explaining Plan Mode, Permission Modes (Safety vs Auto-Accept), Extended Thinking Mode, how they work together, quick decision guide, and mode status indicators. Positioned early in document for foundational understanding. | Chevan Nanayakkara |
| 1.0.0 | 2026-01-18 | Initial cheat sheet created. Comprehensive reference covering keyboard shortcuts, slash commands, CLI flags, custom skills, session management, content workflow patterns, cost management, troubleshooting, and integration with other tools. Organized by category for quick lookup. Includes quick reference card, pro tips, and first-time setup checklist. | Chevan Nanayakkara |
