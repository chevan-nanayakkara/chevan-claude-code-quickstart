# Windows WSL Development Setup Guide

## Document Metadata

| Field                    | Value                                                           |
| ------------------------ | --------------------------------------------------------------- |
| **Document Title** | Windows WSL Development Setup Guide                             |
| **Version**        | 2.1.0                                                           |
| **Author**         | Chevan Nanayakkara                                              |
| **Date Created**   | December 7, 2025                                                |
| **Last Updated**   | January 18, 2026                                                |
| **Platform**       | Windows 10 (2004+) / Windows 11 with WSL 2                      |
| **Distribution**   | Ubuntu 24.04 LTS                                                |
| **Status**         | Production - Complete and Tested                                |
| **Purpose**        | Standard setup instructions for Windows development environment |

---

## 1. Overview

This document provides comprehensive, step-by-step instructions for setting up a professional development environment on Windows using Windows Subsystem for Linux (WSL). The setup mirrors macOS development workflows using bash, providing consistency across platforms and enabling AI-assisted development.

**What you'll get:**

* Complete Linux development environment within Windows
* Native bash shell with enhanced configuration
* Multiple GitHub account support with SSH keys
* Claude Code for AI-powered development with complete configuration
  * Optimized config.json with 4-hour session timeout
  * Custom status line showing project, session ID, and token usage
  * Session backup and restore system (OneDrive integration)
  * Custom skills for content workflows
* Cursor IDE with seamless WSL integration
* OneDrive and Windows filesystem access from Linux
* Document processing tools (Pandoc, LaTeX)
* Organized git repository structure
* Comprehensive shell functions (navigation, session management, backup/restore)

**Key benefits of this setup:**

* Consistent bash environment across Windows and Mac
* Native Linux tools and package managers (apt, nvm, pip)
* Better performance for development workflows
* Seamless integration with Windows applications
* Access to both Linux and Windows file systems

**Estimated setup time:** 70-95 minutes

---

## 2. Setup Steps

Follow these steps in order. Each step depends on previous steps being completed.

### 2.1. Install Windows Subsystem for Linux

**Required first** - enables Linux environment within Windows.

#### 2.1.1. Install Ubuntu Distribution

Open PowerShell as Administrator (right-click → Run as administrator):

```powershell
wsl --install -d Ubuntu-24.04
```

This command will:

* Enable WSL feature on Windows
* Download and install Ubuntu 24.04 LTS
* Set up the Virtual Machine Platform
* Install the WSL kernel update

**Note:** If installation fails, enable WSL manually:

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Then restart your computer and run the install command again.

#### 2.1.2. Initial Ubuntu Setup

After installation completes, launch WSL from regular PowerShell (no admin needed):

```powershell
wsl
```

On first launch, you'll be prompted to:

1. Create a UNIX username (lowercase, no spaces recommended)
2. Set a password (won't display as you type - this is normal)
3. Confirm the password

**Important notes:**

* This username/password is separate from your Windows login
* You'll need the password for sudo commands
* The password can be simple for a personal dev machine

#### 2.1.3. Verify Installation

```bash
# Check Ubuntu version
cat /etc/os-release

# Navigate to Linux home directory
cd ~
pwd
# Should show: /home/your-username

# Check WSL version
wsl.exe --list --verbose
# Should show Ubuntu-24.04 with version 2
```

---

### 2.2. System Updates and Essential Tools

**Update the package system** and install foundational development tools.

#### 2.2.1. Update Package System

```bash
sudo apt update
sudo apt upgrade -y
```

#### 2.2.2. Install Build Essentials

```bash
sudo apt install -y build-essential curl wget unzip zip tree jq
```

**What these provide:**

* **build-essential** : C/C++ compilers, make, and development libraries
* **curl/wget** : Tools for downloading files
* **unzip/zip** : Archive utilities
* **tree** : Directory structure visualization
* **jq** : JSON processor

#### 2.2.3. Install Git

```bash
sudo apt install -y git
```

**Verify:**

```bash
git --version
```

---

### 2.3. Enhanced Bash Configuration

**Configure bash with git-aware prompt and helpful aliases** - similar to Oh My Zsh on macOS.

#### 2.3.1. Backup Existing .bashrc

```bash
cp ~/.bashrc ~/.bashrc.backup
```

#### 2.3.2. Replace .bashrc with Enhanced Configuration

**Use the template from this repository:**

The complete .bashrc configuration is available as a template in this repo.

**Template location:** `templates/shell/.bashrc-template`

**Copy the template:**

```bash
# Copy template to your home directory
cp templates/shell/.bashrc-template ~/.bashrc

# Reload shell
source ~/.bashrc
```

**Template features (v2.4.0):**
- Git-aware prompt with colors showing branch and status
- Claude Code session management (claude-backup, claude-restore, cb alias)
- Navigation functions with CLAUDE.md reminders
- Comprehensive myhelp reference
- SSH agent auto-start

**For reference:** See `templates/shell/.bashrc-template` for the full configuration.

**Your terminal now has:**

* ✅ Colorful git-aware prompt showing branch and status
* ✅ Git branch displayed in yellow
* ✅ Uncommitted changes indicator (*)
* ✅ Navigation helpers for all your repos
* ✅ Quick reference with `myhelp` command
* ✅ SSH agent auto-start

**Test your setup:**

```bash
# Try the help command
myhelp

# Navigate to a repo (should show colorful prompt)
personal-content
```


---

### 2.4. Configure Git

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

### 2.5. Generate SSH Keys

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

### 2.6. Configure SSH

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

# WorkCorp
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes

# CompanyCorp
Host github.com-company
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company
    IdentitiesOnly yes
```

**Save (Ctrl+X, then Y, then Enter) and set permissions:**

```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_*
```

**Note:** SSH keys are automatically loaded by the SSH agent (configured in .bashrc in step 2.3.2).

---

### 2.7. Add SSH Keys to GitHub

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
4. Title: "Windows WSL - Personal" (or "WorkCorp", "CompanyCorp")
5. Paste the key
6. Click "Add SSH key"

**Important:** If replacing a device, delete old SSH keys from GitHub first for security.

---

### 2.8. Test SSH Connections

**Verify SSH authentication works** for all accounts.

```bash
ssh -T github.com-personal
ssh -T github.com-work
ssh -T github.com-company
```

**Expected response for each:** "Hi [username]! You've successfully authenticated..."

**Note:** Type "yes" when asked about fingerprint on first connection.

---

### 2.9. Install Node.js with NVM

**NVM (Node Version Manager)** - allows installing and switching between Node.js versions.

```bash
# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# NVM configuration was already added to .bashrc in step 2.3.2
# Just reload shell to activate it
source ~/.bashrc

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

---

### 2.10. Install Python Tools

**Python 3.12.3** comes pre-installed with Ubuntu 24.04.

#### 2.10.1. Install pip

```bash
sudo apt install -y python3-pip python3-venv
```

#### 2.10.2. Verify Installation

```bash
python3 --version
pip3 --version
```

**Note:** Always use `--break-system-packages` flag when installing packages globally with pip:

```bash
pip3 install package-name --break-system-packages
```

Or use virtual environments (recommended for projects):

```bash
python3 -m venv venv
source venv/bin/activate
pip install package-name
```

---

### 2.11. Create Git Directory Structure

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

### 2.12. Install Cursor IDE

**Cursor** - AI-powered code editor with WSL support.

#### 2.12.1. Download and Install

1. Download from https://cursor.com
2. Run the Windows installer
3. During installation, Cursor will detect WSL automatically

#### 2.12.2. Install WSL Extension

If not automatically installed:

1. Open Cursor
2. Press Ctrl+Shift+X
3. Search for "WSL"
4. Install the official WSL extension

#### 2.12.3. Connect to WSL

**Method 1: From WSL terminal (recommended):**

```bash
cd ~
cursor .
```

If 'cursor' command is not found, use 'code .' instead (Cursor uses VSCode command structure).

**Method 2: From Cursor UI:**

1. Open Cursor
2. Click the green button in bottom-left corner (looks like ><)
3. Select "Connect to WSL"
4. File → Open Folder
5. Navigate to /home/your-username/git/...

---

### 2.13. Install and Configure Claude Code

**Claude Code** - command-line tool for AI-powered development with Claude.

**Requires Node.js/npm from step 2.9.**

#### 2.13.1. Install Claude Code

```bash
# Install Claude Code globally via npm
npm install -g @anthropic-ai/claude-code
```

**Verify installation:**

```bash
claude --version
```

#### 2.13.2. Create Configuration Directory and Skills Folder

```bash
# Create .claude directory structure
mkdir -p ~/.claude
mkdir -p ~/.claude/skills
```

#### 2.13.3. Create config.json (Optimized Configuration)

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

#### 2.13.4. Create settings.json (Model and Status Line Configuration)

**Use the template from this repository:**

**Template location:** `templates/claude/settings.json-template`

**Copy the template:**

```bash
cp templates/claude/settings.json-template ~/.claude/settings.json
```

**Template includes:**
- Model: claude-sonnet-4-5-20250929
- Status line configuration (verbose format with type, command, padding)

#### 2.13.5. Create Custom Status Line Script

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

#### 2.13.6. Add API Key to config.json

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

#### 2.13.7. Test Claude Code Installation

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

#### 2.13.8. Test Custom Status Line

When Claude Code runs, you should see a status line at the bottom showing:

```
[example-repo] [abc12345 • /rename] 5k/200k tokens
```

This shows:
- **Project name** (current directory)
- **Session ID** (first 8 characters) with reminder to use `/rename`
- **Token usage** (current usage / total available)

#### 2.13.9. Reference Documentation

For complete configuration reference and workflow tips:
- `templates/claude/config-reference.md` - Detailed parameter documentation
- `~/git/personal/example-repo/13-operations/claude-code-cheat-sheet.md` - Comprehensive workflow guide

**Note:** These references will be available after cloning your personal-content repository in step 2.14.

---

### 2.14. Clone All Repositories

**Clone your repositories** into the organized structure created in step 2.11.

**Requires SSH setup from steps 2.5-2.8.**

#### 2.14.1. Personal Repositories

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

#### 2.14.2. WorkCorp Repositories

```bash
cd ~/git/work

# Clone strategy-vision
git clone git@github.com-work:workcorp-org/strategy-vision.git
cd strategy-vision
git config user.email "you@work.com"
cd ..
```

#### 2.14.3. CompanyCorp Repositories

```bash
cd ~/git/company

# Clone ops
git clone git@github.com-company:companyhq/ops.git
cd ops
git config user.email "you@company.com"
cd ..
```

#### 2.14.4. Mark Repositories as Safe for Cursor

```bash
# Mark all repos in ~/git as safe
git config --global --add safe.directory '~/git/*'
```

**Test opening a repository in Cursor:**

```bash
cd ~/git/personal/example-repo
cursor .
```

**Success!** Repository should open in Cursor.

---

### 2.15. Set Up CLAUDE.md Files

**CLAUDE.md files** provide institutional memory for Claude Code in each repository.

**Requires repositories to be cloned (step 2.14).**

#### 2.15.1. If You Have Existing CLAUDE.md Files

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

#### 2.15.2. If Creating New CLAUDE.md Files

Refer to the **Claude Code Documentation** (your 8 reference documents):

* **CLAUDE.md Guide** - How to create effective CLAUDE.md files
* **CLAUDE.md Templates** - Ready-to-use templates

**Key repos that need CLAUDE.md:**

1. `personal/example-repo` - Personal writing and content
2. `personal/another-project` - Political/economic activism
3. `work/strategy-vision` - WorkCorp strategy and vision
4. `company/ops` - CompanyCorp operations and SOPs

#### 2.15.3. Test CLAUDE.md Works

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

### 2.16. Backup .bashrc to Version Control

**Store your .bashrc** in version control for future reference and portability.

**Requires personal-content repo to be cloned (step 2.14.1).**

```bash
# Navigate to personal-content repo
personal-content

# Copy .bashrc to repo
cp ~/.bashrc .bashrc

# Verify it looks correct
tail -10 .bashrc
# Should end with bash completion code

# If correct, commit it
git add .bashrc
git commit -m "config: Add .bashrc v2.0.0 with git-aware prompt and helpers"
git push
```

**Why backup .bashrc:**

* ✅ Easy to restore on new machines
* ✅ Version controlled - track changes over time
* ✅ Shareable with team members
* ✅ Documents your terminal configuration

---

### 2.17. OneDrive and Windows File System Integration

**Access Windows files and OneDrive from WSL** - bridges Linux and Windows environments.

#### 2.17.1. Understanding File System Access

Windows drives are mounted in WSL at `/mnt/`:

* C: drive → `/mnt/c/`
* D: drive → `/mnt/d/`
* etc.

#### 2.17.2. Identify OneDrive Folders

```bash
# List OneDrive folders
ls /mnt/c/Users/$USER/ | grep -i onedrive
```

Replace `$USER` with your actual Windows username if different from WSL username.

#### 2.17.3. Create Symbolic Links

**For easy access to OneDrive and Windows folders:**

```bash
# Personal OneDrive
ln -s "/mnt/c/Users/YOUR-WINDOWS-USERNAME/OneDrive" ~/OneDrive

# Work OneDrive (adjust name as needed)
ln -s "/mnt/c/Users/YOUR-WINDOWS-USERNAME/OneDrive - Company" ~/OneDrive-Company

# Common Windows folders
ln -s "/mnt/c/Users/YOUR-WINDOWS-USERNAME/Documents" ~/Documents
ln -s "/mnt/c/Users/YOUR-WINDOWS-USERNAME/Downloads" ~/Downloads
ln -s "/mnt/c/Users/YOUR-WINDOWS-USERNAME/Desktop" ~/Desktop
```

**Replace `YOUR-WINDOWS-USERNAME` with your actual Windows username.**

**Test access:**

```bash
onedrive  # Using alias from .bashrc
cd ~/Documents
cd ~/Downloads
```

#### 2.17.4. Performance Considerations

**Important:** Files on `/mnt/c/` (Windows filesystem) are slower than files in WSL's native filesystem (`~`).

**Best practices:**

**For active development:**

* Work in `~/git/` (WSL filesystem) - FAST
* Git operations are much faster here

**For backup/sharing:**

* Copy completed projects to OneDrive
* Access OneDrive files for quick edits

**Example workflow:**

```bash
# Copy project from OneDrive to work on it
cp -r ~/OneDrive/Project ~/git/personal/Project
cd ~/git/personal/Project
# Do your work here (fast performance)

# When done, copy back to OneDrive
cp -r ~/git/personal/Project ~/OneDrive/Project
```

---

### 2.18. Install Additional Development Tools

#### 2.18.1. Pandoc for Document Conversion

```bash
sudo apt install -y pandoc
```

**Verify:**

```bash
pandoc --version
```

#### 2.18.2. LaTeX for PDF Generation

**Install BasicTeX equivalent:**

```bash
sudo apt install -y texlive-latex-base texlive-fonts-recommended texlive-latex-extra
```

**Test pandoc PDF generation:**

```bash
echo "# Test Document

This is **bold** text." | pandoc -o test.pdf
```

**Open the PDF** (from Windows):

```bash
explorer.exe test.pdf
```

**Clean up:**

```bash
rm test.pdf
```

#### 2.18.3. Useful CLI Utilities

```bash
sudo apt install -y htop ripgrep bat
```

**What they do:**

* **htop** : System monitoring
* **ripgrep** : Fast grep alternative
* **bat** : Better cat with syntax highlighting

**Note:** On Ubuntu, `bat` is installed as `batcat`. Create an alias:

```bash
echo 'alias bat="batcat"' >> ~/.bashrc
source ~/.bashrc
```

---

### 2.19. Configure Cursor Settings

**Custom Cursor configuration** - sets up formatting, terminal, and editor preferences.

**Requires Cursor to be installed and connected to WSL (step 2.12).**

#### 2.19.1. Open Cursor Settings

1. Open Cursor
2. Connect to WSL (if not already connected)
3. Cmd+, (or File → Preferences → Settings)
4. Click the file icon in top-right (Open Settings JSON)

#### 2.19.2. Key Settings to Add/Update

```json
{
  "terminal.integrated.defaultProfile.linux": "bash",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "prettier.singleQuote": true,
  "prettier.semi": true,
  "eslint.format.enable": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "gitlens.currentLine.enabled": true,
  "remote.WSL.useShellEnvironment": true
}
```

**Save and close.**

#### 2.19.3. Install Cursor Extensions (Optional)

**Recommended extensions:**

1. **Office Viewer** (vscode-office) - Preview .docx, .xlsx, .pptx files
2. **Prettier** - Code formatter
3. **ESLint** - JavaScript/TypeScript linting
4. **GitLens** - Enhanced Git visualization

**Install via:** Ctrl+Shift+X → Search → Install

---

### 2.20. Create Claude Code Custom Skills (Optional but Recommended)

**Custom Skills** - Create slash commands for common content workflows.

**Requires Claude Code to be installed (step 2.13).**

Skills provide reusable prompts you can invoke with slash commands like `/outline` or `/polish`.

#### 2.20.1. Skills Directory

Skills are stored in `~/.claude/skills/` (already created in step 2.13.2)

#### 2.20.2. Create Four Essential Skills for Content Work

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

#### 2.20.3. Verify Skills Are Loaded

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

#### 2.20.4. Reference for Additional Skills

For more examples and workflow patterns, see:
- `~/git/personal/example-repo/13-operations/claude-code-cheat-sheet.md` (after cloning repo in step 2.14)

**Skills make your workflow faster:**
- `/outline` → Get structure before drafting
- `/expand section-name` → Develop specific sections
- `/polish` → Final quality check
- `/check-patterns` → Remove AI tells

---

## 3. Reference Information

### 3.1. Complete Tool Stack

#### Core Development

| Tool        | Version/Source       | Purpose                         |
| ----------- | -------------------- | ------------------------------- |
| WSL 2       | Latest               | Linux environment on Windows    |
| Ubuntu      | 24.04 LTS            | Linux distribution              |
| Bash        | 5.2+ (with Ubuntu)   | Shell with custom configuration |
| Git         | via apt              | Version control                 |
| Cursor IDE  | Latest               | Primary IDE with WSL support    |
| Claude Code | Latest (via npm)     | AI-powered development CLI      |
| Node.js     | via nvm (LTS)        | JavaScript runtime              |
| Python      | 3.12.3 (with Ubuntu) | Python development              |

#### Document Tools

| Tool    | Purpose                      |
| ------- | ---------------------------- |
| Pandoc  | Universal document converter |
| TeXLive | LaTeX for PDF generation     |

#### CLI Utilities

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| wget, curl | Download tools          |
| tree       | Directory visualization |
| jq         | JSON processor          |
| bat        | Better cat              |
| ripgrep    | Fast grep               |
| htop       | System monitoring       |

#### Bash Enhancements

| Component                    | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| **Git-aware prompt**   | Shows current branch and status           |
| **Color prompt**       | User, host, and path in different colors  |
| **SSH agent**          | Auto-starts and loads keys                |
| **Navigation aliases** | Quick access to repos and Windows folders |
| **Git helpers**        | Short aliases for common git commands     |
| **myhelp function**    | Quick reference guide                     |

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

### 3.4. File System Paths

| Path            | Description                             |
| --------------- | --------------------------------------- |
| `~`           | Linux home (/home/username)             |
| `~/git`       | Git repositories (fast, WSL filesystem) |
| `/mnt/c/`     | Windows C: drive                        |
| `/mnt/d/`     | Windows D: drive (if exists)            |
| `~/OneDrive`  | OneDrive symlink (if created)           |
| `~/Documents` | Windows Documents symlink (if created)  |
| `~/Downloads` | Windows Downloads symlink (if created)  |
| `~/.bashrc`   | Bash configuration file                 |
| `~/.ssh/`     | SSH keys and configuration              |

---

### 3.5. Windows Integration

#### Accessing Windows Files from WSL

```bash
# Windows C: drive
cd /mnt/c/

# User folder
cd /mnt/c/Users/YOUR-USERNAME/

# Via symlinks (if created in step 2.17.3)
cd ~/OneDrive
cd ~/Documents
cd ~/Downloads
```

#### Accessing WSL Files from Windows

**In Windows File Explorer, type:**

```
\\wsl$\Ubuntu-24.04\home\your-username
```

**Or use the WSL shortcut:**

* Open File Explorer
* Look for "Linux" in the left sidebar
* Navigate to Ubuntu → home → your-username

#### Opening Windows Applications from WSL

```bash
# Open file in default Windows app
explorer.exe file.pdf

# Open current directory in Windows Explorer
explorer.exe .

# Open URL in Windows default browser
cmd.exe /c start https://github.com
```

#### Copy/Paste in WSL Terminal

* **Copy** : Ctrl+Shift+C (or right-click selected text)
* **Paste** : Ctrl+Shift+V (or right-click)
* **Note** : Text is auto-copied when selected

---

## 4. Post-Setup Verification

### 4.1. Post-Setup Checklist

After completing all setup steps, verify:

**WSL & System:**

* [ ] WSL 2 is installed and running
* [ ] Ubuntu 24.04 launches successfully
* [ ] System packages are updated

**Terminal & Shell:**

* [ ] Bash shows colorful git-aware prompt
* [ ] Git branch displays in prompt when in repo
* [ ] `myhelp` command displays reference guide
* [ ] SSH agent auto-starts and loads keys (`ssh-add -l`)

**Development Tools:**

* [ ] Git is configured with correct settings
* [ ] SSH connections work for all three GitHub accounts
* [ ] Node.js and npm are working (`node --version`, `npm --version`)
* [ ] Python and pip are working (`python3 --version`, `pip3 --version`)
* [ ] Claude Code is installed (`claude --version`)
* [ ] Claude Code config file exists (`cat ~/.claude/config.json`)
* [ ] Pandoc can generate PDFs (tested in step 2.18.2)

**Repository Setup:**

* [ ] Repository structure created (`~/git/personal`, `~/git/work`, `~/git/company`)
* [ ] All repositories cloned:
  * [ ] `personal/example-repo`
  * [ ] `personal/another-project`
  * [ ] `work/strategy-vision`
  * [ ] `company/ops`
* [ ] Repositories marked as safe for Cursor
* [ ] CLAUDE.md files are in place in each repository
* [ ] .bashrc is backed up to version control

**IDE Setup:**

* [ ] Cursor is installed on Windows
* [ ] Cursor connects to WSL successfully
* [ ] Cursor can open WSL repositories
* [ ] Cursor terminal uses bash in WSL
* [ ] Cursor settings.json is configured

**Windows Integration:**

* [ ] OneDrive symlinks work (if created)
* [ ] Can access Windows files from WSL (`/mnt/c/`)
* [ ] Can access WSL files from Windows Explorer (`\\wsl$\`)
* [ ] Can open Windows apps from WSL (`explorer.exe`)

---

### 4.2. Troubleshooting Reference

#### WSL Hangs on Startup

**Symptom:** WSL hangs when launching, requires Ctrl+C to get bash prompt.

**Solution:**

Test if .bashrc is causing the issue:

```powershell
wsl bash --norc --noprofile
```

If this launches immediately, edit .bashrc:

```bash
nano ~/.bashrc
```

Look for duplicate sections or problematic code. Common issue: multiple SSH agent sections.

#### Git 'Unsafe Repository' Warning

**Symptom:** Cursor shows 'potentially unsafe repository' warning.

**Solution:**

```bash
git config --global --add safe.directory '~/git/*'
```

#### SSH Key Not Working

**Symptom:** Permission denied when trying to clone or push.

**Solutions:**

1. Verify SSH key is added to GitHub
2. Test connection: `ssh -T github.com-personal -v`
3. Check SSH config: `cat ~/.ssh/config`
4. Check key permissions: `ls -la ~/.ssh/`
5. Reload SSH agent: `source ~/.bashrc`
6. Verify keys loaded: `ssh-add -l`

#### Node/npm Commands Not Found

**Symptom:** 'node' or 'npm' commands not recognized.

**Solution:**

```bash
source ~/.bashrc
nvm install --lts
nvm use --lts
```

#### Cursor Can't Find Repositories

**Symptom:** Cursor can't see repositories in WSL.

**Solution:**

1. Ensure Cursor is connected to WSL (green icon in bottom-left)
2. Click green icon → "Connect to WSL"
3. File → Open Folder → navigate to `/home/your-username/git/...`

#### Claude Code Not Working

**Symptom:** `claude: command not found`

**Solution:**

```bash
# Reinstall
npm install -g @anthropic-ai/claude-code

# Reload shell
source ~/.bashrc

# Verify
claude --version
```

#### Can't Access OneDrive from WSL

**Symptom:** OneDrive symlink doesn't work or permission denied.

**Solution:**

1. Verify OneDrive path in Windows:

```bash
ls /mnt/c/Users/YOUR-USERNAME/ | grep -i onedrive
```

2. Recreate symlink with correct path:

```bash
ln -sf "/mnt/c/Users/YOUR-USERNAME/OneDrive" ~/OneDrive
```

#### WSL Filesystem Slow

**Symptom:** Git operations or file access very slow.

**Solution:**

* **Problem** : Working on `/mnt/c/` (Windows filesystem)
* **Fix** : Move work to `~/git/` (WSL filesystem)

```bash
# Check where you are
pwd

# If in /mnt/c/, move to WSL filesystem
cd ~/git/personal/your-repo
```

---

## 5. Appendices

### 5.1. Key Decisions Made

#### 5.1.1. WSL 2 vs WSL 1

**Decision:** WSL 2

**Reason:** Better performance, full Linux kernel, Docker support

#### 5.1.2. Ubuntu 24.04 vs Other Distributions

**Decision:** Ubuntu 24.04 LTS

**Reason:** Long-term support, widely used, excellent documentation, native Python 3.12.3

#### 5.1.3. Bash vs Zsh

**Decision:** Bash with custom configuration

**Reason:** Default on Ubuntu, simpler configuration, sufficient with custom prompt and aliases

#### 5.1.4. Work in WSL Filesystem vs Windows Filesystem

**Decision:** Work in `~/git/` (WSL filesystem)

**Reason:** 10x+ faster file operations, better git performance, still accessible from Windows

#### 5.1.5. SSH Passphrase

**Decision:** No passphrase on SSH keys

**Reason:** Personal dev machine, convenience, auto-loaded by SSH agent

#### 5.1.6. Python pip Installation Method

**Decision:** Use `--break-system-packages` or virtual environments

**Reason:** Ubuntu 24.04 enforces PEP 668 to prevent system package conflicts

---

### 5.2. Security Best Practices

**When setting up SSH keys:**

1. ✅ Delete old SSH keys from GitHub if replacing a device
2. ✅ Generate new SSH keys for each device
3. ✅ Verify keys are added correctly to GitHub
4. ✅ Test authentication before relying on SSH access
5. ✅ Use descriptive key titles (e.g., "Windows WSL - Personal")

**If a device is lost/stolen:**

1. **Immediately** delete SSH keys from GitHub (personal and organization accounts)
2. Revoke any personal access tokens
3. Change passwords if stored locally
4. Review recent repository activity for unauthorized access
5. Enable 2FA on GitHub if not already enabled

**SSH Key Management:**

* Use separate SSH keys for each device
* Use separate SSH keys for each GitHub account
* Never share private keys
* Regularly review and remove unused keys from GitHub settings

---

### 5.3. Time Estimates

**Total setup time:** 70-95 minutes

**Detailed breakdown:**

| Step    | Task                                                 | Time      |
| ------- | ---------------------------------------------------- | --------- |
| 2.1     | WSL and Ubuntu installation                          | 10-15 min |
| 2.2     | System updates and essential tools                   | 5 min     |
| 2.3     | Enhanced bash configuration (with v2.4.0 .bashrc)    | 10-15 min |
| 2.4     | Configure Git                                        | 2 min     |
| 2.5-2.8 | SSH setup (generate, configure, add to GitHub, test) | 10-15 min |
| 2.9     | Node.js (NVM)                                        | 5 min     |
| 2.10    | Python tools                                         | 3 min     |
| 2.11    | Create Git directory structure                       | 2 min     |
| 2.12    | Cursor installation and WSL connection               | 5-10 min  |
| 2.13    | Claude Code installation and configuration           | 10-15 min |
|         | - Install Claude Code                                | 2 min     |
|         | - Create config.json (optimized)                     | 2 min     |
|         | - Create settings.json                               | 1 min     |
|         | - Create statusline.sh                               | 2 min     |
|         | - Add API key                                        | 2 min     |
|         | - Test installation and status line                  | 3-5 min   |
| 2.14    | Clone all repositories                               | 10-15 min |
| 2.15    | Set up CLAUDE.md files                               | 5-10 min  |
| 2.16    | Backup .bashrc                                       | 2 min     |
| 2.17    | OneDrive and Windows integration                     | 5-10 min  |
| 2.18    | Additional development tools                         | 5-10 min  |
| 2.19    | Configure Cursor settings                            | 5 min     |
| 2.20    | Claude Code custom skills (optional)                 | 5-10 min  |

---

### 5.4. Differences from macOS

**Key differences when comparing to macOS setup:**

| Aspect                    | macOS                    | Windows WSL              |
| ------------------------- | ------------------------ | ------------------------ |
| **Package manager** | Homebrew (`brew`)      | apt (`sudo apt`)       |
| **Shell framework** | Oh My Zsh                | Custom .bashrc           |
| **File paths**      | `/Users/username`      | `/home/username`       |
| **Terminal**        | Terminal.app             | WSL terminal             |
| **Copy/paste**      | Cmd+C/V                  | Ctrl+Shift+C/V           |
| **External drives** | `/Volumes/`            | `/mnt/c/`,`/mnt/d/`  |
| **Cloud storage**   | iCloud in `~/Library/` | OneDrive via `/mnt/c/` |
| **Python**          | Install via pyenv        | Pre-installed (3.12.3)   |
| **LaTeX**           | BasicTeX (100MB)         | TeXLive packages         |

**What's the same:**

* ✅ Git configuration and SSH setup
* ✅ Node.js via NVM
* ✅ Repository structure and workflow
* ✅ Cursor IDE integration
* ✅ Claude Code installation and usage
* ✅ Navigation aliases and git helpers
* ✅ CLAUDE.md setup and workflow

---

### 5.5. Performance Tips

#### Maximize Performance

**Do:**

* ✅ Store active projects in `~/git/` (WSL filesystem)
* ✅ Run git operations in WSL filesystem
* ✅ Use WSL-native tools (apt, not Windows apps)
* ✅ Keep OneDrive for backup/sharing only

**Don't:**

* ❌ Work directly on `/mnt/c/` for development
* ❌ Keep node_modules in Windows filesystem
* ❌ Run git operations on OneDrive-synced folders
* ❌ Mix Windows and WSL line endings

#### File Sync Strategy

**Recommended workflow:**

```bash
# Morning: Pull from OneDrive to WSL (if needed)
cp -r ~/OneDrive/Project ~/git/personal/Project

# Day: Work in WSL (fast)
cd ~/git/personal/Project
# Do all your work here

# Evening: Push to OneDrive (backup)
cp -r ~/git/personal/Project ~/OneDrive/Project

# Always: Git push (version control)
git push
```

---

### 5.6. Related Documentation

* **macOS Setup Guide** - Equivalent setup for Mac devices
* **Claude Code Documentation** - 8 comprehensive reference documents
  * Core Guide - Tool selection and workflows
  * Software Supplement - Web development specifics
  * Ecosystem Guide - Advanced capabilities
  * Teams Guide - Organizational patterns
  * CLAUDE.md Guide - Institutional memory best practices
  * Git Operations Guide - Version control workflows
  * CLAUDE.md Templates - Ready-to-use templates
  * README - Navigation hub

---

## Document History

| Version         | Date                 | Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Author             |
| --------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **2.1.0** | **2026-01-18** | **MAJOR UPDATE: Claude Code Session Management.** Updated .bashrc to v2.4.0 with claude-backup, claude-restore, and claude-backup-status functions (OneDrive integration for WSL). Completely rewrote step 2.13 to include comprehensive Claude Code configuration: optimized config.json with 4-hour timeout, settings.json with model and statusline, custom statusline.sh script showing session ID and tokens. Added new step 2.20 for creating custom skills (outline, expand, polish, check-patterns). Updated overview to highlight session management infrastructure. Updated time estimates to 70-95 minutes. Document now provides complete Claude Code setup with backup/restore system, custom status line, and content workflow skills. Total: 20 numbered setup steps. | Chevan Nanayakkara |
| **2.0.0** | **2026-01-17** | **FINAL PRODUCTION RELEASE.** Complete restructure matching macOS setup guide quality. Added proper section numbering (1-5 with subsections). Added critical missing content: enhanced bash configuration with git-aware prompt (2.3), Claude Code installation (2.13), clone all repositories with proper organization (2.14), CLAUDE.md setup (2.15), backup .bashrc (2.16). Improved existing content: expanded OneDrive integration (2.17), added comprehensive development tools (2.18), added Cursor configuration (2.19). New sections: Complete tool stack (3.1), repository structure (3.2), SSH config summary (3.3), file system paths (3.4), Windows integration guide (3.5), comprehensive post-setup checklist (4.1), troubleshooting reference (4.2), appendices with decisions, security, time estimates, macOS differences, performance tips (5.1-5.6). Document now matches macOS guide in structure, completeness, and professional quality. Total: 19 numbered setup steps across 5 major sections. | Chevan Nanayakkara |
| 1.0             | 2025-12-07           | Initial version documenting complete WSL development environment setup. Covered WSL installation, Git with multiple SSH keys, Node.js, OneDrive integration, Cursor IDE setup. Basic structure with 10 main sections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Chevan Nanayakkara |
