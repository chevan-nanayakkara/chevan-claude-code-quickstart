#!/bin/bash

# ============================================
# Claude Code Custom Status Line
# ============================================
# Version: 1.1.0
# Last Updated: January 18, 2026
#
# Changelog:
# v1.1.0 (2026-01-18) - Changed to show session ID (first 8 chars) + static /rename tip
#                     - Format: [project] [session-id • /rename] tokens
#                     - Removed session name detection (not available in JSON)
# v1.0.0 (2026-01-18) - Initial version showing project name, session name attempt, token usage
# ============================================

# Read JSON input from stdin
input=$(cat)

# Extract project name from current directory
PROJECT_DIR=$(echo "$input" | jq -r '.workspace.project_dir // .cwd // "unknown"')
PROJECT_NAME=$(basename "$PROJECT_DIR")

# Extract token usage
TOKENS_USED=$(echo "$input" | jq -r '.context_window.total_input_tokens // 0')
TOKENS_TOTAL=$(echo "$input" | jq -r '.context_window.context_window_size // 200000')

# Format tokens in k (thousands)
TOKENS_USED_K=$(echo "scale=0; $TOKENS_USED / 1000" | bc 2>/dev/null || echo "0")
TOKENS_TOTAL_K=$(echo "scale=0; $TOKENS_TOTAL / 1000" | bc 2>/dev/null || echo "200")

# Extract session ID (Claude Code provides this in JSON)
SESSION_ID=$(echo "$input" | jq -r '.session_id // ""')

# Format session display: show first 8 chars of session ID + static tip
if [ -n "$SESSION_ID" ] && [ "$SESSION_ID" != "null" ] && [ "$SESSION_ID" != "" ]; then
    SESSION_SHORT="${SESSION_ID:0:8}"
    SESSION_DISPLAY="[$SESSION_SHORT • /rename]"
else
    SESSION_DISPLAY="[NEW • /rename]"
fi

# Format and output the status line
# Format: [project-name] [session-id • /rename] 45k/200k tokens
echo "[$PROJECT_NAME] $SESSION_DISPLAY ${TOKENS_USED_K}k/${TOKENS_TOTAL_K}k tokens"
