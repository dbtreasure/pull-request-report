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

If you prefer AI-guided setup with Claude Code:

### Installing Claude Code
```bash
# 1. Install Claude Code (requires Node.js 18+)
npm install -g @anthropic-ai/claude-code

# 2. Navigate to your project directory
cd pull-request-report

# 3. Start Claude Code
claude

# 4. Tell Claude: "Set me up"
```

**System Requirements:**
- macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows via WSL
- Node.js 18+ 
- 4GB RAM minimum
- Claude Pro/Max plan or Anthropic Console access

**📖 Full Installation Guide:** [docs.anthropic.com/claude-code/getting-started](https://docs.anthropic.com/en/docs/claude-code/getting-started)

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

## 📄 License

This project is licensed under the MIT License - see below for details.

### MIT License

```
MIT License

Copyright (c) 2025 Pull Request Report Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Usage and Attribution

This software is free to use, modify, and distribute. When using or modifying this tool:

- ✅ **Use for any purpose** (personal, commercial, educational)
- ✅ **Modify and distribute** freely
- ✅ **No attribution required** (but appreciated!)
- ✅ **Include in larger projects** without restriction

**Optional Attribution:** If you find this tool helpful, consider linking back to the original repository or mentioning it in your project documentation.
