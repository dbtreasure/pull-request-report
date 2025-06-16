# Pull Request Report

An AI-powered tool for analyzing code review feedback patterns to help developers improve their code quality.

## 🚀 Quick Start (1 minute)

### Prerequisites
- **[uvx](https://github.com/astral-sh/uv)** - Python package runner (for easy execution)
- **GitHub CLI** - `brew install gh` (macOS) or [see installation](https://github.com/cli/cli#installation)

### One-Command Setup
```bash
# 1. Clone and run setup
git clone https://github.com/dbtreasure/pull-request-report && cd pull-request-report
./scripts/setup.sh
```

That's it! The setup script will check prerequisites and guide you through configuration. 🎉

## 🔧 Alternative: Using Claude Code

If you prefer AI-guided setup:
```bash
# Open in Claude Code and say: "Set me up"
claude code .
```

## 📖 Detailed Setup

For manual setup or troubleshooting, see [SETUP.md](SETUP.md).

## 🎯 What This Does

This tool analyzes your pull request comments to help you:
- **Identify patterns** in code review feedback
- **Track improvement** over time
- **Focus learning** on specific areas (async, API design, testing, etc.)
- **Level up** your code quality

## 💬 How to Use

### Option 1: Convenience Scripts
```bash
# Analyze your PRs
./scripts/analyze.sh

# Convert reports to PDF
./scripts/convert.sh

# Run tests
./scripts/test.sh
```

### Option 2: Direct uvx Commands
```bash
# Setup and configuration
uvx --from . pr-report setup

# Analyze PRs (10 by default)
uvx --from . pr-report analyze --repo owner/repo --count 20

# Convert markdown to styled PDF
uvx --from . pr-report convert --pdf

# Run comprehensive tests
uvx --from . --with pytest python test/run_tests.py
```

### Option 3: Using Claude Code
Tell Claude any of these:
- **"Analyze my recent PRs"** - Run analysis on all configured repos
- **"Show me my improvement areas"** - See feedback patterns
- **"Add another repository"** - Expand your analysis
- **"Convert reports to PDF"** - Generate professional PDFs

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
