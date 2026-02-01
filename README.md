# Claude Code Quickstart: Complete Setup Guide

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](CHANGELOG.md)

**Version:** 1.0.0
**Last Updated:** February 1, 2026
**Purpose:** Comprehensive guides and production-ready templates for Claude Code CLI
**Time Investment:** 20 minutes (quick start) to 90 minutes (full environment)

**🎯 Everything you need in one repository!** Comprehensive setup guides, battle-tested configuration templates, and production-proven best practices refined over 6+ months of real-world use.

---

## Table of Contents

- [What This Repository Provides](#what-this-repository-provides)
- [Understanding the Components](#understanding-the-components)
- [Prerequisites](#prerequisites)
- [Ready-to-Use Configurations (Just Copy!)](#ready-to-use-configurations-just-copy)
- [Quick Start: 20-Minute Setup](#quick-start-20-minute-setup)
- [Full Setup Guides](#full-setup-guides)
- [Essential Configurations](#essential-configurations)
  - [CLAUDE.md - Institutional Memory](#claudemd---institutional-memory)
  - [Custom Skills](#custom-skills-optional-but-powerful)
- [Tool Selection: When to Use What](#tool-selection-when-to-use-what)
- [Essential Best Practices](#essential-best-practices)
- [Common Patterns](#common-patterns)
- [Troubleshooting](#troubleshooting)
- [Next Steps: Going Deeper](#next-steps-going-deeper)
- [Repository Structure](#repository-structure)
- [Cost and Usage](#cost-and-usage)
- [Getting Help](#getting-help)
- [Success Checklist](#success-checklist)
- [What Makes This Different](#what-makes-this-different)
- [License and Attribution](#license-and-attribution)
- [Appendix: File Locations Reference](#appendix-file-locations-reference)

---

## What This Repository Provides

**Everything you need for professional Claude Code setup:**

- **Comprehensive guides** - Platform-specific setup, keyboard shortcuts, CLAUDE.md best practices, tool selection
- **Shell configurations** - Git-aware prompts, navigation shortcuts, Claude integration (macOS/Windows WSL)
- **Claude Code configs** - Optimized settings with multiple template options
- **Custom skills** - Reusable prompt templates for common workflows
- **CLAUDE.md template** - Institutional memory starter for your projects
- **Real-world learnings** - 6+ months of production experience distilled into guides and templates

**What you'll achieve:**

- Natural language interface to your codebase from the command line
- AI that maintains context about your projects (via CLAUDE.md)
- Multi-file operations through conversation
- Git integration with AI-generated commit messages

---

## Understanding the Components

Before diving into setup, let's understand what makes this environment powerful.

### The Core Idea: AI-Powered Command Line

Traditional development means learning specific tools and clicking through interfaces. With Claude Code, you describe what you want in plain English from your terminal, and the AI figures out how to do it. Instead of "I need to click File → New → Component → Enter name → Configure settings," you type "Create a new React component for user profiles" and Claude handles the details.

This setup requires five key components working together:

### 1. Claude Code (The Engine)

Claude Code is a CLI tool that brings AI assistance directly into your terminal. Unlike web interfaces, it can:

- Read and write files in your project
- Execute commands and scripts
- Understand your entire codebase context
- Maintain conversation history across operations
- Integrate with Git for version control

**Think of it as:** An AI pair programmer that lives in your terminal and can actually modify files, not just suggest changes.

### 2. CLAUDE.md Files (Institutional Memory)

Every project accumulates knowledge: naming conventions, architectural decisions, common pitfalls, preferred patterns. Normally this lives in people's heads or scattered across documentation.

CLAUDE.md is a simple markdown file you place in each repository that tells Claude about your project. When Claude starts working in that directory, it automatically reads this file to understand context.

**Example CLAUDE.md content:**

- "We use TypeScript with strict mode"
- "Database queries go in /services, never in components"
- "Always write tests alongside new features"
- "Use our custom logger, not console.log"

**Think of it as:** A briefing document for every new team member, except the team member is an AI that reads it every single session.

### 3. Configuration Files (How Claude Behaves)

Just like you configure your code editor, you configure Claude Code:

**config.json** - The main configuration file

- Your API key (required)
- Model preferences (faster vs more capable)
- Default behaviors and safety settings
- Integration settings

**settings.json** - Display and interface settings

- Which model to use (Sonnet vs Opus)
- Status line configuration
- Session management preferences

**statusline.sh** - Custom status display

- Shows current context (project, tokens used, etc.)
- Updates in real-time as you work
- Customizable to show what matters to you

**Think of it as:** VS Code's settings.json, but for your AI assistant.

### 4. Skills (Reusable Prompt Templates)

Skills are saved prompts you can invoke with slash commands. Instead of typing out the same instructions repeatedly, you create a skill once and reuse it.

**Example skills included:**

- `/outline` - "Create a structured outline for this content"
- `/expand section 3` - "Take section 3 and develop it with more depth and examples"
- `/polish` - "Final editing pass: fix grammar, improve clarity, check flow"
- `/check-patterns` - "Scan this file for common AI writing patterns and suggest improvements"

Skills can take arguments, reference files, and chain operations together.

**Think of it as:** Text expansion or snippets, but they trigger AI workflows instead of static text.

### 5. Shell Configuration (Your Command Center)

Your terminal becomes your primary interface. The shell configuration gives you:

- **Git-aware prompt** - See branch, status, and changes at a glance
- **Navigation shortcuts** - Jump to projects instantly
- **Git helpers** - `gs` for status, `gc` for commit, etc.
- **Claude integration** - Quick commands to backup/restore sessions
- **Context awareness** - Terminal title shows where you are

**Think of it as:** Making your terminal as informative and efficient as a modern IDE.

### How They Work Together

1. You open a terminal and navigate to a project
2. The shell shows you git status and context
3. You type `claude` to start
4. Claude reads CLAUDE.md to understand the project
5. You describe what you want in natural language
6. Claude uses its configuration to decide how to help
7. You can invoke skills for common workflows
8. Changes are made, you review, commit with AI-generated messages

**The result:** You work at a higher level of abstraction. Instead of managing tools, you describe intent.

---

## Prerequisites

**Before you start, you need:**

1. **macOS or Windows WSL** - These templates support both platforms
2. **Claude Code installed** - `npm install -g @anthropic/claude-code`
3. **Anthropic API key** - Get from console.anthropic.com (~$20-30/month typical usage)
4. **Basic command line familiarity** - Comfortable with terminal commands
5. **20 minutes** - To copy templates and configure

**Official Claude Code documentation:** https://docs.anthropic.com/claude/docs/intro-to-claude-code

---

## Ready-to-Use Configurations (Just Copy!)

**This repository includes production-ready configuration files.** You don't need to create these from scratch - just copy and customize.

All templates are in the `/templates` folder organized by type (shell, claude, skills).

### What's Included

**Shell Configuration (Choose Your Platform):**

- **macOS:** `.zshrc-template` (19KB) - Git-aware prompt, navigation functions, Claude aliases
- **Windows WSL:** `.bashrc-template` (15KB) - Same features, bash implementation

**Claude Code Configuration:**

- `config.json-template` - Optimized starter (recommended)
- `config.json-full-template` - All available options
- `config.json-full-template-commented` - Fully documented with explanations
- `settings.json-template` - Model and status line settings
- `statusline.sh` - Custom status line script

**Skills (Reusable Prompt Templates):**

- `outline.md` - Create structured outlines
- `expand.md` - Expand sections with depth
- `polish.md` - Final refinement for publishing
- `check-patterns.md` - Scan for AI watermark phrases

**Other Templates:**

- `claude-md-template.md` - CLAUDE.md institutional memory template
- `config-reference.md` - Configuration documentation

### File Locations

```
templates/
├── shell/
│   ├── .bashrc-template                          # Windows WSL shell config
│   └── .zshrc-template                           # macOS shell config
├── claude/
│   ├── config.json-template                      # Claude Code config (START HERE)
│   ├── config.json-full-template                 # All options
│   ├── config.json-full-template-commented       # Documented
│   ├── settings.json-template                    # Model settings
│   ├── statusline.sh                             # Status line script
│   └── claude-md-template.md                     # CLAUDE.md template
└── skills/
    ├── outline.md                                # /outline skill
    ├── expand.md                                 # /expand skill
    ├── polish.md                                 # /polish skill
    └── check-patterns.md                         # /check-patterns skill
```

### Quick Copy Commands

**First, clone this repository:**

```bash
git clone https://github.com/chevan-nanayakkara/chevan-claude-code-quickstart.git
cd chevan-claude-code-quickstart
```

**Then run the appropriate commands for your platform:**

**For macOS:**

```bash
# Shell configuration
cp templates/shell/.zshrc-template ~/.zshrc
source ~/.zshrc

# Claude Code configuration
mkdir -p ~/.claude/skills
cp templates/claude/config.json-template ~/.claude/config.json
cp templates/claude/settings.json-template ~/.claude/settings.json
cp templates/claude/statusline.sh ~/.claude/statusline.sh
chmod +x ~/.claude/statusline.sh

# Skills
cp templates/skills/*.md ~/.claude/skills/

# Edit to add your API key
nano ~/.claude/config.json
```

**For Windows WSL:**

```bash
# Shell configuration
cp templates/shell/.bashrc-template ~/.bashrc
source ~/.bashrc

# Claude Code configuration (same as macOS)
mkdir -p ~/.claude/skills
cp templates/claude/config.json-template ~/.claude/config.json
cp templates/claude/settings.json-template ~/.claude/settings.json
cp templates/claude/statusline.sh ~/.claude/statusline.sh
chmod +x ~/.claude/statusline.sh

# Skills
cp templates/skills/*.md ~/.claude/skills/

# Edit to add your API key
nano ~/.claude/config.json
```

**That's it! You now have:**

- ✅ Professional shell with git-aware prompt
- ✅ Claude Code configured and ready
- ✅ Custom skills available
- ✅ Status line showing context

**Just add your API key and you're running.**

### What These Configurations Give You

**Shell (.zshrc / .bashrc):**

- Git-aware prompt (shows branch, status, colors)
- Navigation shortcuts (customize for your repo structure)
- Git helper aliases (`gs`, `gd`, `gl`, `ga`, `gc`, `gp`)
- Claude session management (`claude-backup`, `claude-restore`, `cb`)
- `myhelp` command for quick reference
- SSH agent auto-start (WSL only)

**Note:** Shell templates include example navigation shortcuts that you'll want to customize for your own repositories and directory structure.

**Claude Code (config.json):**

- Optimized model settings
- Useful default prompts
- Performance tuning
- Security settings

**Skills (prompt templates):**

- `/outline` - Create content structure
- `/expand section 3` - Deepen specific parts
- `/polish` - Final publishing pass
- `/check-patterns` - Find AI watermarks

**You can modify any of these later.** They're starting points that work out of the box.

### Customization Required

**The shell templates include example navigation shortcuts** that reference a specific directory structure. You'll want to customize these for your own setup.

**In the shell config (.zshrc / .bashrc), look for:**

```bash
# Navigation shortcuts (CUSTOMIZE THESE)
alias gitroot="cd ~/git"                           # Change ~/git to your repos location
alias project1="cd ~/git/project1"                 # Replace with your actual projects
alias project2="cd ~/git/project2"
# ... add your own shortcuts

# Navigation with CLAUDE.md reminders (CUSTOMIZE THESE)
function project1-main() {
    cd ~/git/project1/main && echo "📋 Check CLAUDE.md"
}
# ... add functions for your repos
```

**What to change:**

- Replace example project names with your actual repository names
- Update paths to match your directory structure
- Modify the `myhelp` function to reference your shortcuts
- Keep the git aliases (`gs`, `gd`, `gl`, etc.) - those are universal

**Claude Code config (config.json):**

- Only needs your API key - everything else works as-is

**Skills:**

- Work as-is - no customization needed
- Create your own by adding `.md` files to `~/.claude/skills/`

---

## Quick Start: 20-Minute Setup

**Goal:** Get Claude Code running with production-ready configuration

**Prerequisites:** Claude Code installed (`npm install -g @anthropic/claude-code`) and API key ready.

### 1. Install Claude Code (5 min)

```bash
npm install -g @anthropic/claude-code
```

Verify installation:

```bash
claude --version
```

### 2. Copy Configuration Templates (10 min)

**Use the Quick Copy Commands from the previous section.**

The short version:

```bash
# Clone this repository
git clone https://github.com/chevan-nanayakkara/chevan-claude-code-quickstart.git
cd chevan-claude-code-quickstart

# Run the copy commands for your platform (see "Ready-to-Use Configurations" above)
# macOS: Use the macOS commands
# Windows WSL: Use the Windows WSL commands

# Then edit to add your API key
nano ~/.claude/config.json
```

Look for this in `config.json`:

```json
{
  "apiKey": "YOUR_API_KEY_HERE"
}
```

Replace `YOUR_API_KEY_HERE` with your actual API key from console.anthropic.com.

### 3. Test It (5 min)

```bash
cd ~/Desktop  # or any directory
claude
```

Try these commands:

- "Create a simple Python script that prints hello world"
- "Read this file and summarize it"
- "What files are in this directory?"

**If this works, you're operational!**

The rest is about making you productive and setting up institutional memory.

---

## Full Setup Guides

**Want a complete development environment?** This repository includes comprehensive platform-specific setup guides.

### Choose Your Platform

**macOS Users:**
- **Guide:** `guides/macos-setup-guide.md`
- **Time:** 75-95 minutes
- **Includes:** Homebrew, Oh My Zsh, Claude Code, Cursor IDE, Node.js, Python, Git multi-account setup

**Windows WSL Users:**
- **Guide:** `guides/windows-wsl-setup-guide.md`
- **Time:** 60-80 minutes
- **Includes:** WSL 2, Ubuntu 24.04, Custom bash, Claude Code, Cursor IDE, Node.js, Python, Git multi-account setup

**Both guides provide:**
- Step-by-step installation instructions
- Complete development environment setup
- Professional terminal configuration
- Integration with the templates in this repository

**Official Claude Code documentation:**
- **Main docs:** https://docs.anthropic.com/claude/docs/intro-to-claude-code
- **API reference:** https://docs.anthropic.com

---

## Essential Configurations

### CLAUDE.md - Institutional Memory

**What it is:** A markdown file in each repository that gives Claude context about your project.

**What it does:**

- Tells Claude about project purpose and structure
- Defines terminology and conventions
- Provides coding standards and patterns
- Maintains institutional knowledge across sessions

**Quick start:**

```bash
# In any repository:
nano CLAUDE.md
```

**Minimal template:**

```markdown
# Project Name

## Purpose
[What this project does]

## Structure
[Key directories and their purpose]

## Conventions
[Important patterns, naming, standards]

## Working with Claude
[Specific instructions for AI assistance]
```

**Templates and guides:**

- **Template:** `templates/claude/claude-md-template.md` - Starter template
- **Guide:** `guides/claude-md-guide.md` - Comprehensive CLAUDE.md guide
- **Best practices:** `guides/claude-md-best-practices.md` - Examples and patterns

### Custom Skills (Optional but Powerful)

**What they are:** Reusable prompt templates you invoke with slash commands

**Included skills:**

- `/outline [idea]` - Create structured outlines
- `/expand section 3` - Expand specific sections with depth
- `/polish` - Final refinement pass for publishing
- `/check-patterns` - Scan for AI watermark phrases

**Install:**

```bash
mkdir -p ~/.claude/skills
# Copy skill templates from this repository
cp templates/skills/*.md ~/.claude/skills/
```

**Create your own:**
Any `.md` file in `~/.claude/skills/` becomes a skill.

---

## Tool Selection: When to Use What

### Claude.ai (Web Interface)

**Use for:**

- Brainstorming and ideation
- Research and synthesis
- Drafting new content (iterate rapidly)
- Quick questions
- Attaching documents for analysis

**Don't use for:**

- Multi-file operations
- Git operations
- Maintaining project context

### Claude Code (CLI)

**Use for:**

- Multi-file updates
- Code generation and refactoring
- Git workflows
- Applying standards across files
- Maintaining institutional memory
- Large restructuring

**Don't use for:**

- Initial drafting (Claude.ai is better)
- Pure research (no files to modify)

### Cursor IDE (Editor)

**Use for:**

- AI pair programming
- In-editor AI assistance
- File editing with AI suggestions
- Visual workflow when needed

### Typical Workflow

1. **Claude.ai** - Research, explore, draft new content
2. **Copy to editor** - One-time copy/paste of final version
3. **Claude Code** - Later maintenance, multi-file updates, consistency checks
4. **Cursor** - Active coding/writing with AI assistance

**Full guide:** `guides/tool-selection-and-workflow-patterns.md` - Detailed workflows and decision framework

---

## Essential Best Practices

### 1. CLAUDE.md Discipline

**Every repository should have CLAUDE.md** - Even minimal context helps tremendously.

**Update CLAUDE.md when:**

- Project structure changes
- New conventions established
- Common mistakes discovered
- New team members join

### 2. Natural Language Work Style

**Think in outcomes, not steps:**

- ❌ "Use grep to find all TODO comments"
- ✅ "Find all TODO items across the codebase"

**Refine iteratively:**

- ❌ Try to specify everything upfront
- ✅ Start broad, refine through back-and-forth dialogue

### 3. Context Management

**Claude Code reads:**

- Files you explicitly mention
- CLAUDE.md in current directory
- Recent conversation history

**Provide context:**

- "Read X first, then Y"
- "This connects to the pattern in Z"
- Let Claude explore when uncertain

### 4. Git Integration

**Claude Code can:**

- Create commits with AI-generated messages
- Create branches and PRs
- Review diffs and suggest improvements
- Handle merge conflicts

**Best practice:**

- Let Claude generate commit messages
- Review changes before committing
- Use natural language: "Commit these changes" instead of manual git commands

**Learn more:** https://docs.anthropic.com/claude/docs/use-claude-code

### 5. Keyboard Shortcuts (Learn These First)

**Essential shortcuts:**

- `Cmd/Ctrl + K` - Start new conversation
- `Cmd/Ctrl + L` - Clear conversation
- `Cmd/Ctrl + /` - Command palette
- `↑` in empty prompt - Recall last message
- `Cmd/Ctrl + Enter` - Submit with newline

**Full reference:** `guides/claude-code-cheat-sheet.md` - Comprehensive keyboard shortcuts and commands

---

## Common Patterns

### Pattern 1: Content Creation

```bash
# In repository with CLAUDE.md:
claude

> "Create an outline for a blog post about [topic]"
> "Expand section 3 with more depth"
> "Check this for AI watermark phrases"
> "Polish for publication"
> "Create commit with these changes"
```

### Pattern 2: Code Refactoring

```bash
claude

> "Read src/components/UserProfile.tsx"
> "This component is too complex. Break it into smaller components."
> "Extract the form logic into a custom hook"
> "Update tests to match the new structure"
> "Show me what changed"
```

### Pattern 3: Documentation Maintenance

```bash
claude

> "Find all README.md files"
> "Ensure they follow the standard template"
> "Update version numbers to 2.0.0"
> "Check cross-references are valid"
```

### Pattern 4: Learning Codebases

```bash
claude

> "What's the overall structure of this codebase?"
> "How does authentication work?"
> "Where are API endpoints defined?"
> "Show me the data flow for user registration"
```

---

## Troubleshooting

### Claude Code Not Starting

**Check installation:**

```bash
which claude
npm list -g @anthropic/claude-code
```

**Reinstall if needed:**

```bash
npm uninstall -g @anthropic/claude-code
npm install -g @anthropic/claude-code
```

### API Key Issues

**Verify configuration:**

```bash
cat ~/.claude/config.json
```

**Check API key is valid:**

- Visit console.anthropic.com
- Check API keys section
- Regenerate if needed

### Permission Errors

**Common issue:** Script files need execute permission

**Fix:**

```bash
chmod +x ~/.claude/statusline.sh
```

### Slow Responses

**Check:**

- Internet connection
- Anthropic API status
- Token usage (context size)

**Reduce context:**

- Clear conversation: `Cmd/Ctrl + L`
- Be more specific about files to read

---

## Next Steps: Going Deeper

### Comprehensive Guides in This Repository

**Start here (recommended order):**

1. **`guides/claude-code-cheat-sheet.md`** - Master keyboard shortcuts and essential commands
2. **`guides/tool-selection-and-workflow-patterns.md`** - When to use Claude.ai vs Claude Code vs Cursor
3. **`guides/claude-md-guide.md`** - Create effective institutional memory with CLAUDE.md
4. **`guides/claude-md-best-practices.md`** - Real examples and patterns

**Platform-specific setup:**

- **macOS:** `guides/macos-setup-guide.md` (75-95 min complete environment)
- **Windows WSL:** `guides/windows-wsl-setup-guide.md` (60-80 min complete environment)

### Official Claude Code Resources

**Essential documentation:**

1. **Getting Started:** https://docs.anthropic.com/claude/docs/intro-to-claude-code
2. **Installation Guide:** https://docs.anthropic.com/claude/docs/install-claude-code
3. **Configuration Reference:** https://docs.anthropic.com/claude/docs/configure-claude-code
4. **Usage Guide:** https://docs.anthropic.com/claude/docs/use-claude-code

**Support and community:**

- **Documentation:** https://docs.anthropic.com
- **API Console:** https://console.anthropic.com
- **Community:** Anthropic Discord

### Templates in This Repository

**Location:** `templates/`

**Shell configurations:**
- `.zshrc-template` (macOS) - Git-aware prompt, navigation shortcuts
- `.bashrc-template` (Windows WSL) - Same features for bash

**Claude Code configurations:**
- `config.json-template` - Optimized starter (recommended)
- `config.json-full-template` - All available options
- `config.json-full-template-commented` - Fully documented
- `settings.json-template` - Model and statusline settings
- `statusline.sh` - Custom status line script

**Skills templates:**
- `outline.md` - Create structured outlines
- `expand.md` - Expand sections with depth
- `polish.md` - Final refinement pass
- `check-patterns.md` - Scan for AI watermarks

**Other templates:**
- `claude-md-template.md` - Institutional memory starter
- `config-reference.md` - Configuration documentation

---

## Repository Structure

```
claude-code-quickstart/
├── README.md                                      # This guide
├── LICENSE                                        # Unlicense (Public Domain)
├── guides/                                        # Comprehensive guides
│   ├── macos-setup-guide.md                      # Complete macOS setup
│   ├── windows-wsl-setup-guide.md                # Complete Windows WSL setup
│   ├── claude-code-cheat-sheet.md                # Keyboard shortcuts & commands
│   ├── claude-md-guide.md                        # CLAUDE.md guide
│   ├── claude-md-best-practices.md               # CLAUDE.md examples
│   └── tool-selection-and-workflow-patterns.md   # When to use what
└── templates/                                     # Configuration templates
    ├── shell/                                     # Shell configurations
    │   ├── .bashrc-template                      # Windows WSL bash config
    │   └── .zshrc-template                       # macOS zsh config
    ├── claude/                                    # Claude Code configurations
    │   ├── config.json-template                  # Starter config (recommended)
    │   ├── config.json-full-template             # All options
    │   ├── config.json-full-template-commented   # Documented
    │   ├── settings.json-template                # Model settings
    │   ├── statusline.sh                         # Status line script
    │   ├── claude-md-template.md                 # CLAUDE.md starter
    │   └── config-reference.md                   # Config docs
    └── skills/                                    # Reusable prompt templates
        ├── outline.md                            # /outline skill
        ├── expand.md                             # /expand skill
        ├── polish.md                             # /polish skill
        └── check-patterns.md                     # /check-patterns skill
```

### Quick Reference

**I need to...**

- **Set up from scratch** → `guides/macos-setup-guide.md` or `guides/windows-wsl-setup-guide.md`
- **Learn keyboard shortcuts** → `guides/claude-code-cheat-sheet.md`
- **Choose the right tool** → `guides/tool-selection-and-workflow-patterns.md`
- **Create CLAUDE.md** → `guides/claude-md-guide.md` (use template: `templates/claude/claude-md-template.md`)
- **CLAUDE.md best practices** → `guides/claude-md-best-practices.md`
- **Configure Claude Code** → `templates/claude/config-reference.md`
- **Add custom skills** → Copy from `templates/skills/` to `~/.claude/skills/`
- **Customize shell** → Edit templates in `templates/shell/` before copying

---

## Cost and Usage

### API Costs

**Typical usage:** $20-30/month for moderate use

**Cost factors:**

- Input tokens (reading files, CLAUDE.md)
- Output tokens (generated responses)
- Model selection (Sonnet vs Opus)

**Cost optimization:**

- Use `.claudeignore` to exclude irrelevant files
- Keep CLAUDE.md focused (under 40k characters)
- Clear conversation when context gets large
- Use Sonnet for most tasks (Opus for complex reasoning)

### Token Management

**CLAUDE.md performance tips:**

- Keep under 40k characters for optimal performance
- Externalize reference content to separate docs
- Keep session-critical info in CLAUDE.md
- Move historical notes to project documentation

**Learn more:** See `templates/claude/claude-md-template.md` for structure guidance

---

## Getting Help

### Official Resources

**Documentation:**
- **Claude Code Guide:** https://docs.anthropic.com/claude/docs/intro-to-claude-code
- **API Documentation:** https://docs.anthropic.com
- **API Console:** https://console.anthropic.com

**Support:**
- **Community Discord:** Anthropic Discord server
- **GitHub Issues:** Report bugs or request features for Claude Code

### From This Repository

**Comprehensive guides:**
- **Setup guides:** `guides/macos-setup-guide.md` or `guides/windows-wsl-setup-guide.md`
- **Keyboard shortcuts:** `guides/claude-code-cheat-sheet.md`
- **CLAUDE.md guide:** `guides/claude-md-guide.md`
- **Best practices:** `guides/claude-md-best-practices.md`
- **Tool selection:** `guides/tool-selection-and-workflow-patterns.md`

**Templates and configuration:**
- **Config documentation:** `templates/claude/config-reference.md`
- **CLAUDE.md template:** `templates/claude/claude-md-template.md`
- **Skills examples:** `templates/skills/` directory

### Common Questions

**Q: Do I need Claude.ai subscription AND API access?**
A: No. Claude Code uses API (pay-per-use). Claude.ai Pro ($20/month) is separate subscription for web interface. You can use one or both.

**Q: Can I use this for work/client projects?**
A: Yes. Check your organization's AI policy. You control the data (it's in your repos). Anthropic doesn't train on API data.

**Q: What if I run out of API credits?**
A: Add more credits at console.anthropic.com. Set up billing alerts to avoid surprises.

**Q: Can I use other AI models?**
A: Claude Code is Anthropic-specific. But the patterns (CLAUDE.md, Git workflows, semantic storage) work with any AI tool.

**Q: How do I back up configurations?**
A: Configuration files live in `~/.claude/`. The setup guides show how to version control them in a personal operations repository.

---

## Success Checklist

**After setup, you should be able to:**

- [ ] Launch `claude` command in any directory
- [ ] Have Claude read and summarize files
- [ ] Create multi-file updates through conversation
- [ ] Commit changes with AI-generated messages
- [ ] Use custom skills (if installed)
- [ ] Navigate your repositories with git-aware prompts
- [ ] Understand when to use Claude.ai vs Claude Code vs Cursor
- [ ] Have CLAUDE.md in at least one repository
- [ ] Know where to find detailed guides when needed

**If you can do these, you're ready to work with AI assistance from the command line.**

---

## What Makes This Different

**Why use this repository instead of starting from scratch?**

**Everything is production-tested:**
- Refined over 6+ months of real-world use
- Best practices discovered through experience
- Optimized configurations for performance
- Save hours (or days) of trial-and-error

**What you get:**
- **Comprehensive guides** - Step-by-step platform setup, keyboard shortcuts, workflow patterns
- **Shell configs** - Git-aware prompts that work across macOS and Windows WSL
- **Claude settings** - Performance-tuned configurations with sane defaults
- **Skills library** - Reusable prompt templates for common tasks
- **CLAUDE.md patterns** - Proven institutional memory structure with examples

**The difference:**
- **20-minute quick start** - Copy templates and start using Claude Code
- **Complete environment** - Follow platform guides for full professional setup
- **Ongoing reference** - Cheat sheets, best practices, and workflow guides

**From zero to productive in minutes, not days.**

---

## License and Attribution

**These templates are based on:**

- Production configuration refined over 6+ months
- Real-world usage across documentation, development, and operations projects
- Battle-tested patterns and best practices
- Performance optimization and usability improvements

**Version:** 1.0.0
**Released:** February 1, 2026
**License:** Unlicense (Public Domain)

**Feel free to:**

- Use in personal or commercial projects
- Modify and customize for your needs
- Share with friends and colleagues
- Fork and adapt for your organization

**Attribution appreciated but not required.**

---

**Found this useful? Star the repository and share with others who might benefit from production-ready Claude Code configuration.**

---

## Appendix: File Locations Reference

### In This Repository

**All templates are in:** `templates/`

**Shell configurations:**
- `templates/shell/.bashrc-template` - Windows WSL bash
- `templates/shell/.zshrc-template` - macOS zsh

**Claude Code templates:**
- `templates/claude/config.json-template` - Starter config
- `templates/claude/config.json-full-template` - All options
- `templates/claude/config.json-full-template-commented` - Documented
- `templates/claude/settings.json-template` - Model settings
- `templates/claude/statusline.sh` - Status line script
- `templates/claude/claude-md-template.md` - CLAUDE.md starter
- `templates/claude/config-reference.md` - Config docs

**Skills templates:**
- `templates/skills/outline.md` - Create outlines
- `templates/skills/expand.md` - Expand sections
- `templates/skills/polish.md` - Final refinement
- `templates/skills/check-patterns.md` - Scan for AI patterns

### After Installation (On Your System)

**Claude Code configuration:**
- `~/.claude/config.json` - Main configuration (copy from templates)
- `~/.claude/settings.json` - Model and statusline settings
- `~/.claude/statusline.sh` - Custom status line script
- `~/.claude/skills/` - Custom skills directory

**Shell configuration:**
- `~/.zshrc` (macOS) or `~/.bashrc` (Windows WSL)

**In your projects:**
- `[repository]/CLAUDE.md` - Institutional memory (one per repo)
- `[repository]/.claudeignore` - Files to exclude from context (optional)

---

## 🚀 Quick Start

**Ready to begin?** Choose your path:

### Fast Track (20 Minutes)

1. **Clone this repository**
   ```bash
   git clone https://github.com/chevan-nanayakkara/chevan-claude-code-quickstart.git
   cd chevan-claude-code-quickstart
   ```

2. **Copy templates** (see [Quick Start: 20-Minute Setup](#quick-start-20-minute-setup))
   ```bash
   # macOS
   cp templates/shell/.zshrc-template ~/.zshrc
   cp templates/claude/config.json-template ~/.claude/config.json
   # ... (see full commands in Quick Start section)
   ```

3. **Add your API key** and start using Claude Code!

### Full Setup (90 Minutes)

Complete professional environment with all tools:
- **macOS:** Follow [guides/macos-setup-guide.md](guides/macos-setup-guide.md)
- **Windows WSL:** Follow [guides/windows-wsl-setup-guide.md](guides/windows-wsl-setup-guide.md)

---

## ⭐ Found This Useful?

If this repository helped you set up Claude Code, please:

- **⭐ Star it on GitHub** - Helps others discover it
- **📢 Share it** - With colleagues, friends, or on social media
- **💬 Provide feedback** - Open an issue with suggestions or questions
- **🤝 Contribute** - Submit PRs to make it even better (see [CONTRIBUTING.md](CONTRIBUTING.md))

---

## 📬 Support & Community

### Questions or Issues?

- **📖 Check the guides** - Most questions are answered in the comprehensive guides
- **❓ Search issues** - Someone may have already asked your question
- **🐛 Report bugs** - Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- **💡 Request features** - Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)

### Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report issues
- How to suggest improvements
- How to submit pull requests
- Contribution guidelines

### Stay Updated

- **⭐ Watch this repository** - Get notified of updates
- **📋 Check [CHANGELOG.md](CHANGELOG.md)** - See what's new in each release

---

## 🔗 Related Resources

### Official Claude Code Documentation

- **Main Documentation:** https://docs.anthropic.com/claude/docs/intro-to-claude-code
- **Installation Guide:** https://docs.anthropic.com/claude/docs/install-claude-code
- **Configuration Reference:** https://docs.anthropic.com/claude/docs/configure-claude-code
- **API Documentation:** https://docs.anthropic.com
- **API Console:** https://console.anthropic.com

### Complementary Tools

- **Cursor IDE** - AI-powered code editor: https://cursor.sh
- **Claude.ai** - Web interface for Claude: https://claude.ai
- **Anthropic API** - Direct API access: https://console.anthropic.com

### Community Resources

- **Claude Code GitHub** - Official repository and issues
- **Anthropic Discord** - Community discussions and support
- **Documentation** - Comprehensive guides and references

---

## 🎉 You're All Set!

**Time investment:** 20 minutes to 90 minutes
**Return:** Professional AI-augmented development environment
**Benefit:** Work faster, smarter, and with institutional memory across all your projects

**Happy coding with Claude! 🚀**

---

*This repository is released into the public domain under the [Unlicense](LICENSE). Use it however you want, no attribution required (but appreciated!).*
