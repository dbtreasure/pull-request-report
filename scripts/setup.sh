#!/bin/bash
# Convenience script for setting up the Pull Request Report tool

set -e

echo "🚀 Pull Request Report Setup"
echo "=============================="

# Check if uvx is available
if ! command -v uvx &> /dev/null; then
    echo "❌ uvx is required but not installed."
    echo "📦 Install uvx with one of these methods:"
    echo "   • pipx install uv"
    echo "   • curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "   • brew install uv (macOS)"
    echo ""
    echo "Then restart your shell and run this script again."
    exit 1
fi

# Check GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is required but not installed."
    echo "📦 Install GitHub CLI:"
    echo "   • https://github.com/cli/cli#installation"
    echo "   • brew install gh (macOS)"
    echo "   • sudo apt install gh (Ubuntu/Debian)"
    echo ""
    exit 1
fi

# Check GitHub authentication
if ! gh auth status &> /dev/null; then
    echo "🔐 GitHub CLI needs authentication"
    echo "Run: gh auth login"
    echo ""
    exit 1
fi

echo "✅ Prerequisites check passed!"
echo ""

# Run the setup using uvx
echo "🔧 Running interactive setup..."
uvx --from . pr-report setup

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "  • Run: ./scripts/analyze.sh (to analyze PRs)"
echo "  • Run: ./scripts/convert.sh (to convert reports to PDF)"
echo "  • Or use uvx directly: uvx --from . run.py --help"