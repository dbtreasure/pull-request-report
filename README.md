# Pull Request Report

A tool for analyzing code review feedback patterns to help developers improve their code quality.

## 🚀 Quick Start (2 minutes)

### Prerequisites
- **[Claude Code](https://claude.ai/code)** - AI coding assistant (required)
- **GitHub CLI** - `brew install gh` (macOS) or [see other platforms](https://github.com/cli/cli#installation)

### Setup
```bash
# 1. Clone and enter the repository
git clone <this-repo-url>
cd pull-request-report

# 2. Authenticate GitHub (if needed)
gh auth login

# 3. Open in Claude Code
claude code .

# 4. Tell Claude:
"Set me up"
```

That's it! Claude will guide you through the rest. 🎉

## 📖 Detailed Setup

For manual setup or troubleshooting, see [SETUP.md](SETUP.md).

## 🎯 What This Does

This tool analyzes your pull request comments to help you:
- **Identify patterns** in code review feedback
- **Track improvement** over time
- **Focus learning** on specific areas (async, API design, testing, etc.)
- **Level up** your code quality

## 💬 How to Use

Once set up, just tell Claude:

- **"Analyze my recent PRs"** - Run analysis on all configured repos
- **"Show me my improvement areas"** - See feedback patterns
- **"Add another repository"** - Expand your analysis
- **"Analyze just [repo-name]"** - Focus on specific repo

## 📊 Example Output

Claude creates detailed reports showing:
```
reports/
└── my-api-project/
    └── pull-requests/
        ├── PR-123-add-auth.md      # What reviewers said
        ├── PR-125-refactor-db.md   # How to improve
        └── summary.md              # Your patterns
```

## 🔒 Privacy

- All reports stay local (gitignored)
- Your code never leaves your machine
- Each developer gets their own private analysis

## What Gets Analyzed

For each pull request, the tool examines:
- Review comments and suggestions
- Requested code changes
- Approval status and conditions
- Common themes across reviews

The analysis produces:
- Detailed breakdowns of each PR's feedback
- Key takeaways for improvement
- Actionable steps to avoid similar issues
- Progress tracking over time

## Privacy

- All analysis reports are stored locally in the `reports/` directory
- The `reports/` directory is gitignored by default
- Your code and review comments never leave your machine
- Only you can see your analysis results

## Example Output

After analysis, you'll find reports like:

```
reports/
└── my-api-project/
    ├── intro.md
    └── pull-requests/
        ├── PR-123-add-user-auth.md
        ├── PR-125-refactor-database.md
        └── summary.md
```

Each report includes:
- PR overview and purpose
- Detailed review feedback
- Specific improvement recommendations
- Patterns to watch for in future PRs

## Contributing

Feel free to submit issues or PRs to improve this tool!