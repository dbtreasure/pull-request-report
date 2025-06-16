# Installation Guide

This document provides detailed installation instructions for different platforms and scenarios.

## 🚀 Quick Installation (Recommended)

### 1. Install uvx (Python package runner)

Choose one method:

**macOS (Homebrew):**
```bash
brew install uv
```

**Linux/macOS (curl):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (if you have pipx):**
```bash
pipx install uv
```

### 2. Install GitHub CLI

**macOS:**
```bash
brew install gh
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install gh
```

**Windows:**
```bash
winget install GitHub.cli
```

**Other platforms:** See [GitHub CLI installation guide](https://github.com/cli/cli#installation)

### 3. Clone and Setup

```bash
git clone <repo-url>
cd pull-request-report
./scripts/setup.sh
```

## 🔧 Alternative Installation Methods

### Option 1: Traditional Python Virtual Environment

If you prefer not to use uvx:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Run directly
python -m pull_request_report.cli setup
```

### Option 2: Using pip install

```bash
# Install from local directory
pip install .

# Run the installed commands
pr-report setup
pr-analyze --help
pr-convert --help
```

### Option 3: Development Setup

For contributors:

```bash
# Clone and setup development environment
git clone <repo-url>
cd pull-request-report

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check .
black --check .
```

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.9 or higher
- **Operating System**: macOS, Linux, or Windows
- **Memory**: 100MB free space
- **Network**: Internet access for GitHub API

### Required External Tools
- **GitHub CLI (gh)**: For accessing GitHub repositories
- **wkhtmltopdf** (optional): For PDF generation
  - macOS: `brew install wkhtmltopdf`
  - Ubuntu: `sudo apt install wkhtmltopdf`
  - Windows: Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)

Note: If wkhtmltopdf is not available, the tool will use weasyprint for PDF generation.

## ⚠️ Troubleshooting

### "uvx command not found"

After installing uv, restart your terminal or run:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### "gh command not found"

Make sure GitHub CLI is installed and in your PATH:
```bash
which gh
gh --version
```

### "Permission denied" on scripts

Make sure scripts are executable:
```bash
chmod +x scripts/*.sh
```

### Python dependency conflicts

Use uvx to avoid conflicts:
```bash
uvx --from . run.py --help
```

Or create a clean virtual environment:
```bash
python -m venv clean-env
source clean-env/bin/activate
pip install .
```

### GitHub authentication issues

Authenticate with GitHub CLI:
```bash
gh auth login
gh auth status
```

## 🐳 Docker (Optional)

For completely isolated execution:

```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

# Install GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt update \
    && apt install gh -y

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

WORKDIR /app
COPY . .

# Install the package
RUN pip install .

CMD ["pr-report", "--help"]
```

Build and run:
```bash
docker build -t pr-report .
docker run -v $(pwd)/reports:/app/reports pr-report
```

## 🎯 Verification

After installation, verify everything works:

```bash
# Check uvx
uvx --version

# Check GitHub CLI
gh --version
gh auth status

# Check the tool
uvx --from . run.py --help

# Run a quick test
./scripts/setup.sh --dry-run  # If available
```

## 🆘 Getting Help

If you encounter issues:

1. **Check the troubleshooting section above**
2. **Verify all prerequisites are installed**
3. **Check your Python version**: `python --version`
4. **Try the alternative installation methods**
5. **Open an issue** with your error message and system details

## 🔄 Updating

To update to the latest version:

```bash
cd pull-request-report
git pull origin main

# If using uvx, no additional steps needed
# If using pip install:
pip install -e . --upgrade
```