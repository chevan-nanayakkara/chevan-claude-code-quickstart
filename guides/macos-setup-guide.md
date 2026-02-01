# macOS Setup Guide

## Document Metadata

| Field                    | Value                                           |
| ------------------------ | ----------------------------------------------- |
| **Document Title** | macOS Setup Guide                               |
| **Version**        | 2.1.0                                           |
| **Author**         | Chevan Nanayakkara                              |
| **Date Created**   | December 22, 2025                               |
| **Last Updated**   | January 18, 2026                                |
| **macOS Version**  | Current (2025+)                                 |
| **Status**         | Production - Complete and Tested                |
| **Purpose**        | Standard setup instructions for new Mac devices |

---

## 1. Overview

This document provides comprehensive, step-by-step instructions for setting up a new Mac for development work. All steps are ordered by dependency and have been tested on macOS 2025+.

**What you'll get:**

* Complete development environment (Node.js, Python, Git, Docker)
* Enhanced terminal with Oh My Zsh (colorful prompts, auto-suggestions, syntax highlighting)
* Multiple GitHub account support with SSH keys
* Claude Code for AI-powered development with complete configuration
  * Optimized config.json with 4-hour session timeout
  * Custom status line showing project, session ID, and token usage
  * Session backup and restore system (OneDrive integration)
  * Custom skills for content workflows
* Cursor IDE with essential plugins
* Document processing tools (Pandoc, LaTeX)
* Organized git repository structure
* Comprehensive shell functions (navigation, session management, backup/restore)

**Estimated setup time:** 85-110 minutes

---

## 2. Setup Steps

Follow these steps in order. Each step depends on previous steps being completed.

### 2.1. Install Xcode Command Line Tools

**Required first** - provides foundation for all development tools.

```bash
xcode-select --install
```

Click "Install" in the dialog that appears.

**Verify installation:**

```bash
xcode-select -p
# Output: /Library/Developer/CommandLineTools

git --version
# Should show git version
```

---

### 2.2. Install Homebrew

**Package manager for macOS** - required for installing most development tools.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Add Homebrew to PATH** (run the commands Homebrew displays after installation):

For Apple Silicon (M1/M2/M3):

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Verify:**

```bash
brew --version
brew doctor
```

---

### 2.3. Install Essential Development Tools

**Basic utilities needed throughout setup.**

```bash
brew install wget curl tree jq
```

---

### 2.4. Install Oh My Zsh and Configure Terminal

**Enhanced terminal framework** - provides colorful prompts, plugins, and quality-of-life improvements.

#### 2.4.1. Install Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**This will:**

* Backup your current `.zshrc` to `.zshrc.pre-oh-my-zsh`
* Create a new `.zshrc` with Oh My Zsh configuration
* Set up a colorful, informative prompt

#### 2.4.2. Install Essential Plugins

```bash
# Auto-suggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Syntax highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Reload to activate
source ~/.zshrc
```

#### 2.4.3. Install Alternative Themes

**Note:** These themes are for testing later. The default theme will be replaced with agnoster in step 2.4.6.

```bash
# Spaceship theme
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# Powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

**Note:** Pure theme requires Node.js (installed in step 2.12). Install it later with:

```bash
npm install --global pure-prompt
```

#### 2.4.4. Install Meslo Nerd Font

**Required for agnoster and powerlevel10k themes** - provides special characters and symbols.

```bash
brew tap homebrew/cask-fonts
brew install font-meslo-lg-nerd-font
```

#### 2.4.5. Configure Terminal Font

1. Terminal → Settings (or Preferences)
2. Profiles → Select your profile
3. Font → Click "Change"
4. Select: **MesloLGS NF**
5. Size: 12 or 13
6. Close settings and restart terminal

#### 2.4.6. Replace .zshrc with Complete Configuration

**This provides your complete terminal setup** with all aliases, functions, and helpers.

```bash
# Backup existing .zshrc
cp ~/.zshrc ~/.zshrc.backup

# Edit .zshrc
nano ~/.zshrc
```

**Use the template from this repository:**

The complete .zshrc configuration is available as a template in this repo.

**Template location:** `templates/shell/.zshrc-template`

**Copy the template:**

```bash
# Copy template to your home directory
cp templates/shell/.zshrc-template ~/.zshrc

# Reload shell
source ~/.zshrc
```

**Template features (v2.4.0):**
- Oh My Zsh with agnoster theme
- Git-aware prompt with colors
- Claude Code session management (claude-backup, claude-restore, cb alias)
- Navigation functions with CLAUDE.md reminders
- Comprehensive myhelp reference
- Right-side timestamp prompt

**For reference:** See `templates/shell/.zshrc-template` for the full configuration.

**Your terminal now has:**

* ✅ Colorful agnoster theme with git branch and status
* ✅ Command auto-suggestions as you type (press → to accept)
* ✅ Syntax highlighting (green = valid, red = invalid)
* ✅ Git-aware prompt showing repository and branch
* ✅ Navigation helpers for all your repos
* ✅ Quick reference with `myhelp` command

**Test your setup:**

```bash
# Try the help command
myhelp

# Navigate to a repo (should show colorful prompt)
personal-content
```

---

### 2.5. Delete Old SSH Keys (If Replacing a Device)

**IMPORTANT:** Only do this if you're replacing an old device. Skip if this is your first Mac setup or if you're keeping your old device active.

#### 2.5.1. Delete Local SSH Key Files

```bash
# Navigate to SSH directory
cd ~/.ssh

# List all SSH keys
ls -la

# Delete old keys (adjust names as needed)
rm id_ed25519_personal*
rm id_ed25519_work*
rm id_ed25519_company*
```

#### 2.5.2. Delete SSH Keys from GitHub

Remove old SSH keys from your GitHub account and organizations:

1. Go to https://github.com/settings/keys
2. Delete ALL old SSH keys from the previous device
3. Check organization settings for WorkCorp and CompanyCorp
4. Delete any old keys there too

**Why this matters:** Prevents unauthorized access to repositories from old/lost devices.

---

### 2.6. Configure Git

**Global git configuration** - sets your identity for all git operations.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@personal.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

**Verify:**

```bash
git config --list
```

---

### 2.7. Generate SSH Keys

**Create separate SSH keys for each GitHub account** - enables multi-account workflow.

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cd ~/.ssh

# Personal account (your-username)
ssh-keygen -t ed25519 -C "you@personal.com" -f ~/.ssh/id_ed25519_personal

# WorkCorp organization
ssh-keygen -t ed25519 -C "you@work.com" -f ~/.ssh/id_ed25519_work

# CompanyCorp organization
ssh-keygen -t ed25519 -C "you@company.com" -f ~/.ssh/id_ed25519_company
```

**Note:** Press Enter when asked for passphrase (no passphrase for convenience on personal dev machine).

---

### 2.8. Configure SSH

**SSH config file** - tells SSH which key to use for each GitHub account.

```bash
nano ~/.ssh/config
```

**Add this configuration:**

```
# Personal GitHub
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes
    AddKeysToAgent yes
    UseKeychain yes

# WorkCorp
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes
    AddKeysToAgent yes
    UseKeychain yes

# CompanyCorp
Host github.com-company
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company
    IdentitiesOnly yes
    AddKeysToAgent yes
    UseKeychain yes
```

**Save (Ctrl+X, then Y, then Enter) and set permissions:**

```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_*
```

---

### 2.9. Add SSH Keys to macOS Keychain

**Store SSH keys in macOS Keychain** - prevents needing to re-enter passphrase.

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_personal
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_work
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_company
```

---

### 2.10. Add SSH Keys to GitHub

**Upload public keys to GitHub** - enables authentication.

**Display public keys:**

```bash
cat ~/.ssh/id_ed25519_personal.pub
cat ~/.ssh/id_ed25519_work.pub
cat ~/.ssh/id_ed25519_company.pub
```

**For each key:**

1. Copy the public key (starts with `ssh-ed25519`)
2. Go to https://github.com/settings/keys
3. Click "New SSH key"
4. Title: "MacBook Air - Personal" (or "WorkCorp", "CompanyCorp")
5. Paste the key
6. Click "Add SSH key"

---

### 2.11. Test SSH Connections

**Verify SSH authentication works** for all accounts.

```bash
ssh -T github.com-personal
ssh -T github.com-work
ssh -T github.com-company
```

**Expected response for each:** "Hi [username]! You've successfully authenticated..."

**Note:** Type "yes" when asked about fingerprint on first connection.

---

### 2.12. Install Node.js with NVM

**NVM (Node Version Manager)** - allows installing and switching between Node.js versions.

```bash
# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# NVM configuration was already added to .zshrc in step 2.4.6
# Just reload shell to activate it
source ~/.zshrc

# Install Node.js LTS
nvm install --lts

# Set as default
nvm use --lts
```

**Verify:**

```bash
node --version
npm --version
nvm --version
```

**Optional - Install pure theme now that Node.js is available:**

```bash
npm install --global pure-prompt
```

---

### 2.13. Create Git Directory Structure

**Organized repository structure** - separates personal, company, and organization repos.

```bash
mkdir -p ~/git/personal
mkdir -p ~/git/work
mkdir -p ~/git/company
```

**Verify:**

```bash
ls -la ~/git/
# Should show: work, personal, company
```

---

### 2.14. Install Cursor IDE

**Cursor** - AI-powered code editor based on VSCode.

1. Download from https://cursor.com
2. Open .dmg file
3. Drag Cursor to Applications
4. Open Cursor
5. Install CLI command: Cmd+Shift+P → type "shell command" → select "Install 'cursor' command in PATH"

**Verify:**

```bash
cursor --version
```

---

### 2.15. Install and Configure Claude Code

**Claude Code** - command-line tool for AI-powered development with Claude.

**Requires Node.js/npm from step 2.12.**

#### 2.15.1. Install Claude Code

```bash
# Install Claude Code globally via npm
npm install -g @anthropic-ai/claude-code
```

**Verify installation:**

```bash
claude --version
```

#### 2.15.2. Create Configuration Directory and Skills Folder

```bash
# Create .claude directory structure
mkdir -p ~/.claude
mkdir -p ~/.claude/skills
```

#### 2.15.3. Create config.json (Optimized Configuration)

**Use the template from this repository:**

**Template location:** `templates/claude/config.json-template`

**Copy the template:**

```bash
cp templates/claude/config.json-template ~/.claude/config.json
```

**Key settings in the template:**
- `autoReadFiles`: Automatically reads CLAUDE.md and README.md at session start
- `explicitReadOnly: true`: Requires approval before file writes (safety mode)
- `sessionTimeout: 14400`: 4-hour timeout (matches typical long sessions)
- `contextWindow: "large"`: 200k tokens
- `ignorePatterns`: Excludes node_modules, build artifacts, OneDrive, etc.

#### 2.15.4. Create settings.json (Model and Status Line Configuration)

**Use the template from this repository:**

**Template location:** `templates/claude/settings.json-template`

**Copy the template:**

```bash
cp templates/claude/settings.json-template ~/.claude/settings.json
```

**Template includes:**
- Model: claude-sonnet-4-5-20250929
- Status line configuration (verbose format with type, command, padding)

#### 2.15.5. Create Custom Status Line Script

**Use the statusline script from this repository:**

**Template location:** `templates/claude/statusline.sh`

**Copy the script:**

```bash
cp templates/claude/statusline.sh ~/.claude/statusline.sh
chmod +x ~/.claude/statusline.sh
```

**Status line format (v1.1.0):**
- `[project-name] [session-id • /rename] 45k/200k tokens`
- Shows project name, first 8 chars of session ID, static /rename reminder, token usage

#### 2.15.6. Add API Key to config.json

**Important:** You need to add your Anthropic API key to the config.json file.

```bash
# Open config.json in nano
nano ~/.claude/config.json
```

Add this line at the top of the JSON file (after the opening `{`):

```json
  "apiKey": "YOUR_API_KEY_HERE",
```

**Your config.json should now look like:**

```json
{
  "apiKey": "YOUR_API_KEY_HERE",
  "autoReadFiles": [
    "CLAUDE.md",
    "README.md"
  ],
  ...
}
```

**Save (Ctrl+X, then Y, then Enter)**

**Get your API key from:** https://console.anthropic.com/settings/keys

#### 2.15.7. Test Claude Code Installation

```bash
# Navigate to any directory
cd ~

# Start Claude Code
claude

# Type: Hello
# Claude should respond
# Exit: type 'exit' or press Ctrl+D

# If it responds, installation successful!
```

#### 2.15.8. Test Custom Status Line

When Claude Code runs, you should see a status line at the bottom showing:

```
[example-repo] [abc12345 • /rename] 5k/200k tokens
```

This shows:
- **Project name** (current directory)
- **Session ID** (first 8 characters) with reminder to use `/rename`
- **Token usage** (current usage / total available)

#### 2.15.9. Reference Documentation

For complete configuration reference and workflow tips:
- `templates/claude/config-reference.md` - Detailed parameter documentation
- `~/git/personal/example-repo/13-operations/claude-code-cheat-sheet.md` - Comprehensive workflow guide

**Note:** These references will be available after cloning your personal-content repository in step 2.16.

---

### 2.16. Clone All Repositories

**Clone your repositories** into the organized structure created in step 2.13.

**Requires SSH setup from steps 2.7-2.11.**

#### 2.16.1. Personal Repositories

```bash
cd ~/git/personal

# Clone personal-content
git clone git@github.com-personal:your-username/example-repo.git
cd example-repo
git config user.email "you@personal.com"
cd ..

# Clone another-project
git clone git@github.com-personal:your-username/another-project.git
cd another-project
git config user.email "you@personal.com"
cd ..
```

#### 2.16.2. WorkCorp Repositories

```bash
cd ~/git/work

# Clone strategy-vision
git clone git@github.com-work:workcorp-org/strategy-vision.git
cd strategy-vision
git config user.email "you@work.com"
cd ..
```

#### 2.16.3. CompanyCorp Repositories

```bash
cd ~/git/company

# Clone ops
git clone git@github.com-company:companyhq/ops.git
cd ops
git config user.email "you@company.com"
cd ..
```

**Test opening a repository in Cursor:**

```bash
cd ~/git/personal/example-repo
cursor .
```

**Success!** Repository should open in Cursor.

---

### 2.17. Set Up CLAUDE.md Files

**CLAUDE.md files** provide institutional memory for Claude Code in each repository.

**Requires repositories to be cloned (step 2.16).**

#### 2.17.1. If You Have Existing CLAUDE.md Files

Copy them to the appropriate repositories:

```bash
# Example for personal-content:
cd ~/git/personal/example-repo
# Copy your CLAUDE.md file here

# Repeat for other repos:
# - ~/git/personal/another-project
# - ~/git/work/strategy-vision
# - ~/git/company/ops
```

#### 2.17.2. If Creating New CLAUDE.md Files

Refer to the **Claude Code Documentation** (your 8 reference documents):

* **CLAUDE.md Guide** - How to create effective CLAUDE.md files
* **CLAUDE.md Templates** - Ready-to-use templates

**Key repos that need CLAUDE.md:**

1. `personal/example-repo` - Personal writing and content
2. `personal/another-project` - Political/economic activism
3. `work/strategy-vision` - WorkCorp strategy and vision
4. `company/ops` - CompanyCorp operations and SOPs

#### 2.17.3. Test CLAUDE.md Works

```bash
# Navigate to repo with CLAUDE.md
personal-content

# Start Claude Code
claude

# In Claude Code:
You: "Read CLAUDE.md"

# Claude should successfully read and understand the file
# Exit when done: exit
```

---

### 2.18. Backup .zshrc to Version Control

**Store your .zshrc** in version control for future reference and portability.

**Requires personal-content repo to be cloned (step 2.16.1).**

```bash
# Navigate to personal-content repo (or wherever you want to store it)
personal-content

# Copy .zshrc to repo
cp ~/.zshrc .zshrc

# Verify it looks correct (no terminal prompt at end)
tail -5 .zshrc
# Should end with:
# Set in Terminal → Preferences → Profiles → Font → MesloLGS NF

# If correct, commit it
git add .zshrc
git commit -m "config: Add .zshrc v2.0.0 with Oh My Zsh and agnoster theme"
git push
```

**Why backup .zshrc:**

* ✅ Easy to restore on new machines
* ✅ Version controlled - track changes over time
* ✅ Shareable with team members
* ✅ Documents your terminal configuration

**Alternative locations:**

* `~/git/personal/example-repo` - With other personal documentation
* `~/git/personal/dotfiles` - Dedicated dotfiles repository (create if needed)

---

### 2.19. Install Python with pyenv

**Pyenv** - Python version manager (similar to NVM for Node.js).

```bash
# Install pyenv
brew install pyenv

# Pyenv configuration was already added to .zshrc in step 2.4.6
# Just reload shell to activate it
source ~/.zshrc

# Install latest Python
pyenv install 3.12.8

# Set as global default
pyenv global 3.12.8
```

**Verify:**

```bash
python --version
pip --version
pyenv --version
```

---

### 2.20. Install Additional Development Tools

#### 2.20.1. GitHub CLI

```bash
brew install gh

# Authenticate when needed
gh auth login
```

#### 2.20.2. Docker Desktop

```bash
brew install --cask docker
```

**Note:** Open Docker Desktop from Applications to complete setup.

**Verify:**

```bash
docker --version
docker run hello-world
```

#### 2.20.3. Useful CLI Utilities

```bash
brew install bat ripgrep htop
```

**What they do:**

* **bat** : Better `cat` with syntax highlighting
* **ripgrep** : Fast grep alternative
* **htop** : System monitoring

---

### 2.21. Install Pandoc for Document Conversion

**Pandoc** - universal document converter.

```bash
brew install pandoc
```

**Verify:**

```bash
pandoc --version
```

---

### 2.22. Install LaTeX (BasicTeX)

**BasicTeX** - lightweight LaTeX distribution for PDF generation.

**Decision:** BasicTeX (100MB) instead of MacTeX (~4GB) - sufficient for pandoc PDF generation.

```bash
# Install BasicTeX
brew install --cask basictex

# BasicTeX PATH was already added to .zshrc in step 2.4.6
# Just reload shell to activate it
source ~/.zshrc

# Update and install essentials
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended
```

**Test pandoc PDF generation:**

```bash
echo "# Test Document

This is **bold** text." | pandoc -o test.pdf
open test.pdf
```

**Success!** PDF should open correctly.

**Clean up test file:**

```bash
rm test.pdf
```

---

### 2.23. Install Cursor Plugins

**Install via Cursor Extensions** (Cmd+Shift+X):

**Requires Cursor to be installed (step 2.14).**

1. **Office Viewer** (vscode-office) - Preview .docx, .xlsx, .pptx files
2. **Prettier** - Code formatter
3. **ESLint** - JavaScript/TypeScript linting
4. **GitLens** - Enhanced Git visualization

**Search for each in the Extensions marketplace and click Install.**

---

### 2.24. Configure Cursor Settings

**Custom Cursor configuration** - sets up formatting, terminal, and editor preferences.

**Requires Cursor to be installed (step 2.14).**

**Open Cursor Settings:**

1. Cmd+, (or Code → Settings → Settings)
2. Click the file icon in top-right (Open Settings JSON)

**Key settings to add/update:**

```json
{
  "terminal.integrated.defaultProfile.osx": "zsh",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "prettier.singleQuote": true,
  "prettier.semi": true,
  "eslint.format.enable": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "gitlens.currentLine.enabled": true
}
```

**Save and close.**

---

### 2.25. Create Claude Code Custom Skills (Optional but Recommended)

**Custom Skills** - Create slash commands for common content workflows.

**Requires Claude Code to be installed (step 2.15).**

Skills provide reusable prompts you can invoke with slash commands like `/outline` or `/polish`.

#### 2.25.1. Skills Directory

Skills are stored in `~/.claude/skills/` (already created in step 2.15.2)

#### 2.25.2. Create Four Essential Skills for Content Work

**Use the skill templates from this repository:**

**Template location:** `templates/skills/`

**Copy all skill templates:**

```bash
cp templates/skills/*.md ~/.claude/skills/
```

**Four essential skills included:**

**1. Outline** (`/outline`) - Create structured outlines for content
- Creates detailed outline with thesis, supporting arguments, evidence needed
- Usage: `/outline [paste rough idea]`

**2. Expand** (`/expand`) - Expand specific sections with depth and examples
- Develops sections with supporting evidence, examples, counterarguments
- Usage: `/expand section 3` or `/expand the introduction`

**3. Polish** (`/polish`) - Final refinement pass for publishing
- Checks clarity, flow, evidence quality, tone consistency, AI patterns
- Usage: `/polish`

**4. Check Patterns** (`/check-patterns`) - Scan for AI watermark phrases
- Scans for AI tells per CLAUDE.md guidelines
- Usage: `/check-patterns`

#### 2.25.3. Verify Skills Are Loaded

```bash
# Start Claude Code
claude

# Inside Claude, type:
/help

# You should see your four custom skills listed:
# /outline - Create structured outline for content
# /expand - Expand a specific section with depth and examples
# /polish - Final refinement pass for publishing
# /check-patterns - Scan for AI watermark phrases

# Exit Claude
exit
```

#### 2.25.4. Reference for Additional Skills

For more examples and workflow patterns, see:
- `~/git/personal/example-repo/13-operations/claude-code-cheat-sheet.md` (after cloning repo in step 2.16)

**Skills make your workflow faster:**
- `/outline` → Get structure before drafting
- `/expand section-name` → Develop specific sections
- `/polish` → Final quality check
- `/check-patterns` → Remove AI tells

---

## 3. Reference Information

### 3.1. Complete Tool Stack

#### Core Development

| Tool            | Version/Source     | Purpose                          |
| --------------- | ------------------ | -------------------------------- |
| Xcode CLI Tools | Latest             | Foundation for development tools |
| Homebrew        | Latest             | Package manager                  |
| Oh My Zsh       | Latest             | Enhanced terminal framework      |
| Git             | via Xcode          | Version control                  |
| Cursor IDE      | Latest             | Primary IDE                      |
| Claude Code     | Latest (via npm)   | AI-powered development CLI       |
| Node.js         | via nvm (LTS)      | JavaScript runtime               |
| Python          | via pyenv (3.12.8) | Python development               |
| Docker Desktop  | Latest             | Containerization                 |

#### Document Tools

| Tool     | Purpose                          |
| -------- | -------------------------------- |
| Pandoc   | Universal document converter     |
| BasicTeX | LaTeX for PDF generation (100MB) |

#### CLI Utilities

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| wget, curl | Download tools          |
| tree       | Directory visualization |
| jq         | JSON processor          |
| bat        | Better cat              |
| ripgrep    | Fast grep               |
| htop       | System monitoring       |
| gh         | GitHub CLI              |

#### Terminal Enhancements (Oh My Zsh)

| Component                | Purpose                                |
| ------------------------ | -------------------------------------- |
| **Agnoster theme** | Powerline-style prompt with git status |
| zsh-autosuggestions      | Command suggestions as you type        |
| zsh-syntax-highlighting  | Real-time command validation           |
| git plugin               | Git aliases and shortcuts              |
| node plugin              | Node.js aliases                        |
| npm plugin               | npm aliases                            |
| macos plugin             | macOS-specific shortcuts               |

**Alternative themes installed** (ready to test):

* robbyrussell (default, minimal)
* powerlevel10k (most customizable)
* spaceship (shows tool versions)
* pure (ultra minimal, installed after Node.js)

 **Font** : MesloLGS NF (Meslo Nerd Font)

#### Cursor Plugins

| Plugin        | Purpose                  |
| ------------- | ------------------------ |
| Office Viewer | Preview Office documents |
| Prettier      | Code formatting          |
| ESLint        | JavaScript linting       |
| GitLens       | Git superpowers          |

---

### 3.2. Repository Structure

```
~/git/
├── personal/              # Personal repos (your-username)
│   ├── example-repo/    # Personal writing and content
│   └── another-project/ # Political/economic activism
├── work/            # WorkCorp organization repos
│   └── strategy-vision/  # Strategy and vision documents
└── company/               # CompanyCorp organization repos
    └── ops/              # Operations and SOPs
```

---

### 3.3. SSH Configuration Summary

**Three SSH identities configured:**

| Identity   | Host                 | Email               | Key File             |
| ---------- | -------------------- | ------------------- | -------------------- |
| Personal   | github.com-personal  | you@personal.com  | id_ed25519_personal  |
| WorkCorp | github.com-work | you@work.com | id_ed25519_work |
| CompanyCorp     | github.com-company    | you@company.com    | id_ed25519_company    |

**Clone syntax:**

```bash
# Personal
git clone git@github.com-personal:your-username/repo.git

# WorkCorp
git clone git@github.com-work:workcorp-org/repo.git

# CompanyCorp
git clone git@github.com-company:companyhq/repo.git
```

---

## 4. Post-Setup Verification

### 4.1. Post-Setup Checklist

After completing all setup steps, verify:

**Terminal & Shell:**

* [ ] SSH connections work for all three GitHub accounts
* [ ] Git is configured with correct global settings
* [ ] Oh My Zsh is installed with plugins working
* [ ] Terminal shows colorful agnoster prompt with git status
* [ ] Command auto-suggestions work (start typing, see gray suggestions)
* [ ] Syntax highlighting works (green/red commands)
* [ ] `myhelp` command displays reference guide
* [ ] Terminal font is set to MesloLGS NF

**Development Tools:**

* [ ] Node.js and npm are working (`node --version`, `npm --version`)
* [ ] Python and pip are working (`python --version`, `pip --version`)
* [ ] Claude Code is installed (`claude --version` works)
* [ ] Claude Code config file exists (`cat ~/.claude/config.json`)
* [ ] Docker Desktop is running (`docker --version`)
* [ ] Pandoc can generate PDFs (tested in step 2.22)
* [ ] Cursor opens and can access repositories

**Repository Setup:**

* [ ] Repository structure created (`~/git/personal`, `~/git/work`, `~/git/company`)
* [ ] All repositories cloned:
  * [ ] `personal/example-repo`
  * [ ] `personal/another-project`
  * [ ] `work/strategy-vision`
  * [ ] `company/ops`
* [ ] CLAUDE.md files are in place in each repository
* [ ] .zshrc is backed up to version control

**IDE Setup:**

* [ ] All Cursor plugins are installed (Office Viewer, Prettier, ESLint, GitLens)
* [ ] Cursor settings.json is configured

---

### 4.2. Troubleshooting Reference

#### SSH Connection Issues

```bash
# Test connection with verbose output
ssh -T github.com-personal -v

# List keys in SSH agent
ssh-add -l

# Re-add keys to keychain
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_personal
```

#### Homebrew Issues

```bash
# Run diagnostics
brew doctor

# Update Homebrew
brew update

# Fix permissions (Apple Silicon)
sudo chown -R $(whoami) /opt/homebrew
```

#### Node/npm Not Found

```bash
# Reload shell
source ~/.zshrc

# Reinstall Node
nvm install --lts
nvm use --lts
```

#### Python Not Found

```bash
# Reload shell
source ~/.zshrc

# Check pyenv
pyenv versions
pyenv global 3.12.8
```

#### Oh My Zsh Not Loading

```bash
# Check if .zshrc exists
cat ~/.zshrc | grep "oh-my-zsh"

# Reload shell configuration
source ~/.zshrc

# Reinstall if needed
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

#### Plugins Not Working

```bash
# Verify plugins are installed
ls ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/

# Reinstall auto-suggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Reinstall syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Reload
source ~/.zshrc
```

#### Claude Code Issues

```bash
# Check if installed
claude --version

# Check config file exists
cat ~/.claude/config.json

# Reinstall if needed
npm install -g @anthropic-ai/claude-code
```

---

## 5. Appendices

### 5.1. Key Decisions Made

#### 5.1.1. BasicTeX vs MacTeX

**Decision:** BasicTeX (100MB)

**Reason:** Sufficient for pandoc PDF generation, saves 3.9GB

#### 5.1.2. pyenv vs Homebrew Python

**Decision:** pyenv

**Reason:** Version management similar to nvm, more flexible for multiple Python versions

#### 5.1.3. SSH Passphrase

**Decision:** No passphrase on SSH keys

**Reason:** Personal dev machine, convenience over security. For work machines, use passphrases.

#### 5.1.4. Oh My Zsh

**Decision:** Install as core part of setup with agnoster theme

**Reason:** Essential quality-of-life improvement for terminal work. Agnoster provides excellent git status visibility without complexity of powerlevel10k configuration wizard.

#### 5.1.5. Claude Code via npm

**Decision:** Install globally via npm

**Reason:** Makes `claude` command available everywhere, consistent with how other CLI tools are installed

---

### 5.2. Security Best Practices

**When setting up SSH keys:**

1. ✅ Delete old SSH keys from GitHub if replacing a device
2. ✅ Generate new SSH keys for each device
3. ✅ Verify keys are added correctly to GitHub
4. ✅ Test authentication before relying on SSH access
5. ✅ Use descriptive key titles (e.g., "MacBook Air - Personal")

**If a device is lost/stolen:**

1. **Immediately** delete SSH keys from GitHub (personal and organization accounts)
2. Revoke any personal access tokens
3. Change passwords if stored locally
4. Review recent repository activity for unauthorized access
5. Enable 2FA on GitHub if not already enabled

**SSH Key Management:**

* Use separate SSH keys for each device
* Use separate SSH keys for each GitHub account (personal, work, organizations)
* Never share private keys
* Regularly review and remove unused keys from GitHub settings

---

### 5.3. Time Estimates

**Total setup time:** 85-110 minutes

**Detailed breakdown:**

| Step     | Task                                                 | Time      |
| -------- | ---------------------------------------------------- | --------- |
| 2.1      | Xcode Command Line Tools                             | 5-10 min  |
| 2.2      | Homebrew                                             | 5 min     |
| 2.3      | Essential development tools                          | 2 min     |
| 2.4      | Oh My Zsh complete setup (with v2.4.0 .zshrc)        | 15-20 min |
|          | - Install Oh My Zsh                                  | 2 min     |
|          | - Install plugins                                    | 2 min     |
|          | - Install themes                                     | 3 min     |
|          | - Install font                                       | 2 min     |
|          | - Configure .zshrc v2.4.0 (with backup functions)    | 5-10 min  |
| 2.5      | Delete old SSH keys (optional)                       | 2 min     |
| 2.6      | Configure Git                                        | 2 min     |
| 2.7-2.11 | SSH setup (generate, configure, add to GitHub, test) | 10-15 min |
| 2.12     | Node.js (NVM)                                        | 5 min     |
| 2.13     | Create Git directory structure                       | 2 min     |
| 2.14     | Cursor installation                                  | 5 min     |
| 2.15     | Claude Code installation and configuration           | 10-15 min |
|          | - Install Claude Code                                | 2 min     |
|          | - Create config.json (optimized)                     | 2 min     |
|          | - Create settings.json                               | 1 min     |
|          | - Create statusline.sh                               | 2 min     |
|          | - Add API key                                        | 2 min     |
|          | - Test installation and status line                  | 3-5 min   |
| 2.16     | Clone all repositories                               | 10-15 min |
| 2.17     | Set up CLAUDE.md files                               | 5-10 min  |
| 2.18     | Backup .zshrc                                        | 2 min     |
| 2.19     | Python (pyenv)                                       | 5 min     |
| 2.20     | Additional tools (Docker, GitHub CLI, utilities)     | 10-15 min |
| 2.21     | Pandoc                                               | 2 min     |
| 2.22     | LaTeX (BasicTeX)                                     | 5 min     |
| 2.23     | Cursor plugins                                       | 5 min     |
| 2.24     | Cursor settings                                      | 5 min     |
| 2.25     | Claude Code custom skills (optional)                 | 5-10 min  |

---

### 5.4. Future Setup Improvements

**Consider for next time:**

1. **Create a dotfiles repository** with:
   * `.zshrc` (with Oh My Zsh configuration)
   * `.gitconfig`
   * `.ssh/config`
   * Cursor `settings.json`
2. **Create setup script** to automate:
   * Homebrew installation
   * Oh My Zsh installation
   * Tool installations
   * Directory structure creation
3. **Document project-specific tools** needed for:
   * WorkCorp development
   * CompanyCorp operations
   * Any specialized workflows
4. **Create CLAUDE.md template** specific to your needs for quick repo setup

---

### 5.5. Related Documentation

* **Claude Code Documentation** - 8 comprehensive reference documents
  * Core Guide - Tool selection and workflows
  * Software Supplement - Web development specifics
  * Ecosystem Guide - Advanced capabilities
  * Teams Guide - Organizational patterns
  * CLAUDE.md Guide - Institutional memory best practices
  * Git Operations Guide - Version control workflows
  * CLAUDE.md Templates - Ready-to-use templates
  * README - Navigation hub
* **Windows WSL Setup Guide** - For Windows development setup (if needed)
* **Cursor settings.json** - Latest configuration file

---

## Document History

| Version         | Date                 | Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Author             |
| --------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **2.1.0** | **2026-01-18** | **MAJOR UPDATE: Claude Code Session Management.** Updated .zshrc to v2.4.0 with claude-backup, claude-restore, and claude-backup-status functions. Completely rewrote step 2.15 to include comprehensive Claude Code configuration: optimized config.json with 4-hour timeout, settings.json with model and statusline, custom statusline.sh script showing session ID and tokens. Added new step 2.25 for creating custom skills (outline, expand, polish, check-patterns). Updated overview to highlight session management infrastructure. Updated time estimates to 85-110 minutes. Document now provides complete Claude Code setup with backup/restore system, custom status line, and content workflow skills. Total: 25 numbered setup steps. | Chevan Nanayakkara |
| **2.0.0** | **2026-01-17** | **FINAL PRODUCTION RELEASE.** Complete restructure with proper section numbering (1-5 with subsections). Fixed dependency ordering: moved pure-prompt installation note to after Node.js step. Verified all commands are accurate and tested. Updated metadata to reflect production status. Enhanced documentation with: comprehensive overview, detailed step-by-step instructions with subsection numbering (2.1, 2.2, 2.4.1, etc.), complete reference information (tool stack, repo structure, SSH config), comprehensive post-setup verification checklist, troubleshooting guide, security best practices, time estimates with detailed breakdown, future improvements section. Document is now a complete, production-ready setup guide suitable for repeated use and team sharing. Total: 24 numbered setup steps across 5 major sections. | Chevan Nanayakkara |
| 1.4             | 2026-01-17           | Added 4 critical missing steps: (15) Claude Code installation and configuration, (16) Clone ALL repositories instead of just first, (17) Set up CLAUDE.md files, (18) Backup .zshrc to version control. Updated Post-Setup Checklist and time estimates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Chevan Nanayakkara |
| 1.3             | 2026-01-17           | MAJOR UPDATE: Complete Oh My Zsh configuration with full .zshrc v2.0.0, all plugins, themes, and Terminal setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Chevan Nanayakkara |
| 1.2             | 2026-01-17           | Updated to standard setup guide format. Removed device-specific context. Updated Security Notes to general best practices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chevan Nanayakkara |
| 1.1             | 2026-01-17           | Integrated Oh My Zsh into core setup flow. Added Terminal Enhancements section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Chevan Nanayakkara |
| 1.0             | 2025-12-22           | Initial version documenting actual Mac setup steps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Chevan Nanayakkara |
