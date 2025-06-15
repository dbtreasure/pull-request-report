# Quick Setup Guide

Welcome! This tool helps you analyze your pull request feedback patterns. Let's get you set up in 2 minutes.

## Prerequisites

1. **Claude Code** - Install from [claude.ai/code](https://claude.ai/code)
2. **GitHub CLI** - Install with:
   - macOS: `brew install gh`
   - Ubuntu/Debian: `sudo apt install gh`
   - Other: [See installation guide](https://github.com/cli/cli#installation)

## Setup Steps

### 1. Authenticate GitHub CLI
```bash
gh auth login
```

### 2. Open in Claude Code
```bash
claude code .
```

### 3. Run Setup
Just tell Claude: **"Set me up"**

Claude will:
- Ask you about the repositories you want to analyze
- Create your personalized config.json
- Verify your GitHub access
- Create your first analysis report

## What Claude Will Ask You

1. **Your GitHub username**
2. **Which repositories to analyze** (you can add multiple)
3. **Your role** in each repository (e.g., "Frontend engineer", "API developer")
4. **What you want to improve** (e.g., "async patterns", "code organization")

## Your First Analysis

After setup, just say: **"Analyze my recent PRs"**

Claude will create detailed reports in the `reports/` folder showing:
- What reviewers commented on
- Patterns in the feedback
- Specific ways to improve

## Common Commands

- **"Set me up"** - Initial configuration
- **"Analyze my recent PRs"** - Run analysis on configured repos
- **"Show me my improvement areas"** - See summary of feedback patterns
- **"Add another repository"** - Add more repos to analyze
- **"Analyze just [repo-name]"** - Analyze specific repository

## Tips

- Start with analyzing your last 5-10 PRs
- Focus on repos where you contribute most
- Review reports regularly to track improvement
- Share learnings with your team!

Ready? Open this folder in Claude Code and say "Set me up"! 🚀