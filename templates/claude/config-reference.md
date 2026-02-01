# Claude Code config.json Reference Guide

| Metadata | Details |
|----------|---------|
| **Version** | 1.0.0 |
| **Date** | January 18, 2026 |
| **Author** | Chevan Nanayakkara |
| **Purpose** | Reference documentation for Claude Code config.json parameters |
| **Config Location** | `~/.claude/config.json` |
| **Claude Code Version** | Compatible with latest (as of Jan 2026) |

---

## Overview

The `config.json` file controls Claude Code's behavior at the user level. It lives at `~/.claude/config.json` and applies to all projects unless overridden by project-specific settings.

**Hierarchy:**
1. `~/.claude/config.json` (user-level, this file)
2. `.claude/settings.json` (project-level, overrides user config)
3. `.claude/settings.local.json` (local project overrides, git-ignored)

---

## Configuration Parameters

### autoReadFiles

**Type:** Array of strings (file paths/patterns)

**Purpose:** Automatically read specified files at the start of every Claude Code session

**Default:** `[]` (empty array, nothing auto-read)

**Valid Values:**
```json
"autoReadFiles": []                          // No auto-read (default)
"autoReadFiles": ["CLAUDE.md"]              // Single file
"autoReadFiles": ["CLAUDE.md", "README.md"] // Multiple files
"autoReadFiles": ["docs/*.md"]              // Pattern (if supported)
```

**When to use:**

**Auto-read when:**
- File contains project context you always need (CLAUDE.md, README.md)
- Working on long-term projects with established patterns
- Want consistent behavior across all sessions in a project
- File is small (<5k tokens) and provides high value

**Don't auto-read when:**
- Files are large (uses tokens on every session start)
- Working on quick one-off tasks
- Different sessions need different context
- File changes frequently and could be stale

**Token cost:** Each auto-read file counts against your context window at session start

**Example for your workflow:**
```json
"autoReadFiles": ["CLAUDE.md", "README.md"]
```
Rationale: You maintain CLAUDE.md as institutional memory. Auto-reading leverages that investment.

**Pro tip:** Keep auto-read files under 5k tokens total. For large reference docs, read them explicitly when needed.

---

### explicitReadOnly

**Type:** Boolean

**Purpose:** Controls whether Claude Code requires explicit permission before writing/editing files

**Default:** `false` (auto-execute file writes)

**Valid Values:**
```json
"explicitReadOnly": true   // Require permission for all writes (safety mode)
"explicitReadOnly": false  // Auto-execute writes (speed mode)
```

**When to use:**

**Set to `true` (safety mode) when:**
- Learning Claude Code (want to see what it's doing)
- Working with critical files
- Want granular control over changes
- Prefer verification before execution
- Working with unfamiliar codebases

**Set to `false` (speed mode) when:**
- You trust the workflow (proven pattern)
- Working with low-stakes content
- Speed matters more than oversight
- Doing repetitive operations
- Working in test/dev environment

**Trade-offs:**

| Mode | Pro | Con |
|------|-----|-----|
| `true` (safety) | Full control, learning opportunity, prevents errors | Slower, requires approvals, can be tedious |
| `false` (speed) | Fast execution, fewer interruptions | Less oversight, harder to catch errors |

**Example for your workflow:**
```json
"explicitReadOnly": true
```
Rationale: You value control and verification. You want to see what's happening. During the reading list workflow, this provided valuable checkpoints.

**Can override per-session:** Use `--dangerously-skip-permissions` flag to bypass temporarily

---

### ignorePatterns

**Type:** Array of strings (glob patterns)

**Purpose:** Exclude files/directories from Claude Code's file operations (reading, searching, editing)

**Default:** Basic patterns (node_modules, .git)

**Valid Values:**
```json
"ignorePatterns": [
  "**/node_modules/**",      // Dependency directories
  "**/.git/**",              // Version control
  "**/dist/**",              // Build outputs
  "**/.DS_Store",            // System files
  "**/*.log",                // Log files
  "**/.claude.working.*/**", // Intermediate work folders
  "**/OneDrive/**",          // Cloud sync folders
  "**/*.csv"                 // Large data files
]
```

**Pattern syntax:**
- `**/` - Match in any subdirectory
- `*` - Match any characters (except `/`)
- `**` - Match any number of directories
- `*.ext` - Match any file with extension

**Common patterns to ignore:**

**Development:**
```json
"**/node_modules/**",
"**/dist/**",
"**/build/**",
"**/.venv/**",
"**/__pycache__/**",
"**/target/**"  // Rust
```

**System/Editor:**
```json
"**/.DS_Store",
"**/.vscode/**",
"**/.cursor/**",
"**/.idea/**",
"**/tmp/**",
"**/*.log"
```

**Your workflow patterns:**
```json
"**/.claude.working.*/**",  // Your intermediate files convention
"**/OneDrive/**",           // Backup location
"**/*.csv",                 // Large exports (Goodreads)
"**/*.jsonl",              // Session logs
"**/.backup/**",
"**/archive/**"
```

**Why ignore these?**
- **Performance**: Skip scanning thousands of dependency files
- **Relevance**: Build artifacts aren't source code
- **Safety**: Don't accidentally edit generated files
- **Token efficiency**: Don't load large irrelevant files

**Example for your workflow:**
```json
"ignorePatterns": [
  "**/node_modules/**",
  "**/.git/**",
  "**/dist/**",
  "**/build/**",
  "**/.DS_Store",
  "**/*.log",
  "**/.vscode/**",
  "**/.cursor/**",
  "**/tmp/**",
  "**/.claude.working.*/**",
  "**/OneDrive/**",
  "**/*.csv",
  "**/*.jsonl",
  "**/.backup/**",
  "**/archive/**"
]
```

**Pro tip:** If Claude Code seems slow searching files, check if your ignore patterns are comprehensive enough.

---

### maxFileSize

**Type:** Number (bytes)

**Purpose:** Maximum file size Claude Code will attempt to read

**Default:** `10485760` (10MB)

**Valid Values:**
```json
"maxFileSize": 1048576     // 1MB (conservative)
"maxFileSize": 10485760    // 10MB (default, recommended)
"maxFileSize": 52428800    // 50MB (generous, risky)
```

**Why this matters:**

**Token limits:**
- 1MB text file ≈ 250k tokens (exceeds most context windows)
- 10MB file = 2.5M tokens (will fail to read)
- Large files need explicit chunking strategy

**Recommendations by file type:**

| File Type | Typical Size | Strategy |
|-----------|--------------|----------|
| Markdown, code | <100KB | Auto-read fine |
| CSVs, exports | >1MB | Explicit chunking required |
| Logs | >10MB | Use grep/head/tail, don't read full file |
| Images, binaries | Varies | Claude Code can read images but they're token-heavy |

**Example for your workflow:**
```json
"maxFileSize": 10485760  // 10MB, keep as default
```

Rationale: Large files (like your 995-book CSV) need intentional chunking anyway. This prevents accidentally trying to load huge files.

**Lesson from reading list workflow:**
- Goodreads CSV was ~400KB (99k tokens)
- Exceeded practical reading limit
- Having maxFileSize as guardrail forced explicit chunking strategy
- Good default, keep it

---

### contextWindow

**Type:** String

**Purpose:** Controls the size of Claude Code's context window for operations

**Default:** `"large"`

**Valid Values:**
```json
"contextWindow": "small"   // ~32k tokens (faster, cheaper)
"contextWindow": "medium"  // ~100k tokens (balanced)
"contextWindow": "large"   // ~200k tokens (default, most capable)
```

**When to use each:**

**"small" (32k tokens):**
- Quick one-file edits
- Simple questions
- Low-stakes operations
- Cost-sensitive workflows
- Older models (if specified)

**"medium" (100k tokens):**
- Multi-file operations (2-5 files)
- Moderate complexity tasks
- Balance between cost and capability

**"large" (200k tokens):**
- Complex multi-file workflows
- Large-scale analysis
- Heavy content generation
- Multi-session projects
- Your default for substantial work

**Trade-offs:**

| Size | Pro | Con |
|------|-----|-----|
| Small | Fast, cheap | Limited context, can't handle complex tasks |
| Medium | Balanced | May hit limits on complex workflows |
| Large | Most capable | Higher cost, potentially slower |

**Example for your workflow:**
```json
"contextWindow": "large"
```

Rationale: Your work involves heavy content generation, multi-document workflows, and iteration. Large context supports this. Cost is worth capability for your use cases.

**Note:** This is your default. Can override per-session with flags if needed for quick tasks.

---

### sessionTimeout

**Type:** Number (seconds)

**Purpose:** How long a session can be inactive before it times out

**Default:** `7200` (2 hours)

**Valid Values:**
```json
"sessionTimeout": 3600   // 1 hour (short sessions)
"sessionTimeout": 7200   // 2 hours (default)
"sessionTimeout": 14400  // 4 hours (recommended for your workflow)
"sessionTimeout": 28800  // 8 hours (very long sessions)
```

**When to increase:**

**Use longer timeout (4-8 hours) when:**
- Working on multi-hour projects (like your 4.3 hour reading list)
- Taking breaks to think/research
- Switching between Claude Code and Claude.ai mid-workflow
- Pausing to review intermediate results
- Working across interruptions (meetings, etc.)

**Use shorter timeout (1-2 hours) when:**
- Quick iterative tasks
- Want to force session cleanup
- Working on time-boxed tasks
- Security-sensitive environments

**Lesson from reading list workflow:**
- Actual workflow: 4.3 hours
- Default timeout: 2 hours
- Risk: Session could expire mid-workflow
- Recommendation: 4 hours minimum

**Example for your workflow:**
```json
"sessionTimeout": 14400  // 4 hours
```

Rationale: Your workflows span multiple hours. You take breaks to research in Claude.ai. You review progress. 4 hours gives breathing room.

**Pro tip:** Even with long timeout, use `cb` (claude-backup) wrapper to save work regularly.

---

### saveSessionHistory

**Type:** Boolean

**Purpose:** Whether to save session transcripts for later resume/analysis

**Default:** `true`

**Valid Values:**
```json
"saveSessionHistory": true   // Save sessions (recommended)
"saveSessionHistory": false  // Don't save sessions (privacy mode)
```

**When to use:**

**Set to `true` (save) when:**
- Want to resume sessions later (default behavior)
- Building long-term projects
- Value audit trail of what was done
- Want to review conversations
- Using session backup strategy

**Set to `false` (don't save) when:**
- Privacy concerns (sensitive data)
- Temporary/throwaway sessions
- Don't want session accumulation
- Storage constraints

**What gets saved:**
- Full conversation transcript (`.jsonl` files)
- File operations performed
- Session metadata
- Located at `sessionHistoryPath`

**Storage location:** See `sessionHistoryPath` below

**Example for your workflow:**
```json
"saveSessionHistory": true
```

Rationale: You've built backup/restore infrastructure (`claude-backup`, `claude-restore`). This enables it. You value being able to resume work.

**Pairs with:** Your `claude-backup` function backs up `~/.claude/` to OneDrive, which includes session history.

---

### sessionHistoryPath

**Type:** String (file path)

**Purpose:** Where to store session transcripts

**Default:** `"~/.claude/sessions"` or `"~/.claude/projects"`

**Valid Values:**
```json
"sessionHistoryPath": "~/.claude/sessions"        // Default location
"sessionHistoryPath": "~/Documents/claude-logs"   // Custom location
"sessionHistoryPath": "/Volumes/External/claude"  // External drive
```

**When to customize:**

**Use custom path when:**
- Want sessions on different drive
- Organizing alongside other work
- Storage constraints on home directory
- Backup strategy requires specific location

**Keep default when:**
- Standard setup works fine
- Using backup strategy (like your OneDrive backup)
- Want consistent location across machines

**Example for your workflow:**
```json
"sessionHistoryPath": "~/.claude/sessions"  // Keep default
```

Rationale: Your `claude-backup` function already handles backup by copying entire `~/.claude/` to OneDrive. No need to change default path - your backup strategy covers it.

**Note:** Your backup copies:
```
~/.claude/ → /Users/you/Documents/claude-code/backups/current/
```
This includes session history, so changing this path isn't necessary.

---

## Complete Example Configuration

Here's your optimized configuration with all parameters explained:

```json
{
  "autoReadFiles": [
    "CLAUDE.md",
    "README.md"
  ],
  "explicitReadOnly": true,
  "ignorePatterns": [
    "**/node_modules/**",
    "**/.git/**",
    "**/dist/**",
    "**/build/**",
    "**/.DS_Store",
    "**/*.log",
    "**/.vscode/**",
    "**/.cursor/**",
    "**/tmp/**",
    "**/.claude.working.*/**",
    "**/OneDrive/**",
    "**/*.csv",
    "**/*.jsonl",
    "**/.backup/**",
    "**/archive/**"
  ],
  "maxFileSize": 10485760,
  "contextWindow": "large",
  "sessionTimeout": 14400,
  "saveSessionHistory": true,
  "sessionHistoryPath": "~/.claude/sessions"
}
```

---

## Configuration Strategies by Use Case

### For Heavy Content Generation (Your Primary Use Case)

```json
{
  "autoReadFiles": ["CLAUDE.md", "README.md"],  // Context on every session
  "explicitReadOnly": true,                      // Verify changes
  "contextWindow": "large",                      // Support complex work
  "sessionTimeout": 14400,                       // 4 hours for long sessions
  "ignorePatterns": [                            // Skip intermediate/backup files
    "**/.claude.working.*/**",
    "**/OneDrive/**",
    "**/*.csv",
    "**/archive/**"
  ]
}
```

### For Quick Development Tasks

```json
{
  "autoReadFiles": [],                   // No auto-read (faster startup)
  "explicitReadOnly": false,            // Auto-execute (speed)
  "contextWindow": "medium",            // Balanced
  "sessionTimeout": 7200,               // 2 hours sufficient
  "ignorePatterns": [                   // Standard dev patterns
    "**/node_modules/**",
    "**/.git/**",
    "**/dist/**"
  ]
}
```

### For Learning/Exploration

```json
{
  "autoReadFiles": ["README.md"],       // Project overview
  "explicitReadOnly": true,             // See everything
  "contextWindow": "large",             // Full capability
  "sessionTimeout": 7200,               // Standard timeout
  "saveSessionHistory": true            // Review later
}
```

---

## Troubleshooting Common Issues

### "Claude Code is slow to start"

**Check:**
- `autoReadFiles`: Are you reading large files on every startup?
- `ignorePatterns`: Are you missing common large directories?

**Fix:**
- Remove large files from `autoReadFiles`
- Add `**/node_modules/**`, `**/dist/**` to ignore patterns

### "Session timed out mid-workflow"

**Check:**
- `sessionTimeout`: Is it too short for your actual workflows?

**Fix:**
- Increase to 14400 (4 hours) or higher
- Use `cb` (claude-backup) to save work periodically

### "Claude Code tried to read a huge file"

**Check:**
- `maxFileSize`: Is it set too high?
- `ignorePatterns`: Are large file types excluded?

**Fix:**
- Keep `maxFileSize` at 10MB
- Add file patterns to `ignorePatterns`: `"**/*.csv"`, `"**/*.log"`

### "Too many permission prompts"

**Check:**
- `explicitReadOnly`: Set to `true`?

**Fix (if appropriate):**
- Set to `false` for trusted workflows
- Or batch approve patterns instead of per-operation approvals
- Keep `true` for learning/critical work

### "Can't find CLAUDE.md in searches"

**Check:**
- `ignorePatterns`: Is it accidentally excluded?

**Fix:**
- Ensure no pattern matches `CLAUDE.md`
- Check `.gitignore` isn't interfering

---

## Configuration Validation

**After editing config.json, validate:**

1. **JSON syntax:** Use a JSON validator or:
   ```bash
   cat ~/.claude/config.json | jq .
   ```
   Should output formatted JSON without errors

2. **Path existence:** Verify paths exist:
   ```bash
   ls -la ~/.claude/sessions
   ```

3. **Pattern testing:** Test ignore patterns:
   ```bash
   # In a project directory
   claude --debug | grep "Ignoring"
   ```

4. **Test session:** Start Claude Code, check behavior matches expectations

---

## Backup Your Configuration

**Before making changes:**

```bash
# Backup current config
cp ~/.claude/config.json ~/.claude/config.json.backup

# Or with timestamp
cp ~/.claude/config.json ~/.claude/config.json.$(date +%Y%m%d)
```

**To restore:**

```bash
cp ~/.claude/config.json.backup ~/.claude/config.json
```

**Your backup strategy already covers this:**
- `claude-backup` copies entire `~/.claude/` to OneDrive
- Includes `config.json`
- Can restore with `claude-restore`

---

## Project-Level Overrides

**For project-specific settings:**

Create `.claude/settings.json` in project root:

```json
{
  "autoReadFiles": ["PROJECT-SPECIFIC.md"],
  "explicitReadOnly": false
}
```

**Hierarchy:**
1. `~/.claude/config.json` (this file, user-level defaults)
2. `.claude/settings.json` (project-level, overrides user config)
3. `.claude/settings.local.json` (local overrides, git-ignored)

**Use project overrides when:**
- Project has unique requirements
- Different team members have different preferences
- Testing configuration changes before global adoption

---

## Related Documentation

**Other configuration files:**

- `~/.claude/settings.json` - Additional settings (model, statusLine)
- `.claude/settings.json` - Project-level overrides
- `.claude/settings.local.json` - Local git-ignored overrides
- `CLAUDE.md` - Project context and instructions

**Your infrastructure:**

- `.zshrc` - Session management functions (claude-backup, claude-restore)
- `statusline.sh` - Custom status line configuration
- Backup location: `/Users/you/Documents/claude-code/backups/`

---

## Document History

| Version | Date | Summary of Changes | Author |
|---------|------|-------------------|--------|
| 1.0.0 | 2026-01-18 | Initial reference documentation for config.json parameters. Documented all 8 configuration parameters (autoReadFiles, explicitReadOnly, ignorePatterns, maxFileSize, contextWindow, sessionTimeout, saveSessionHistory, sessionHistoryPath) with purpose, valid values, usage guidance, and examples tailored to content generation workflow. Included troubleshooting, validation, and configuration strategies. | Chevan Nanayakkara |
