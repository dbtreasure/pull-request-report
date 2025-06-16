#!/bin/bash
# Health check script to verify installation

set -e

echo "🔍 Pull Request Report - System Check"
echo "====================================="

errors=0

# Check uvx
echo -n "• uvx: "
if command -v uvx &> /dev/null; then
    echo "✅ $(uvx --version)"
else
    echo "❌ Not found"
    errors=$((errors + 1))
fi

# Check GitHub CLI
echo -n "• GitHub CLI: "
if command -v gh &> /dev/null; then
    echo "✅ $(gh --version | head -1)"
else
    echo "❌ Not found"
    errors=$((errors + 1))
fi

# Check GitHub auth
echo -n "• GitHub Auth: "
if gh auth status &> /dev/null; then
    echo "✅ Authenticated"
else
    echo "⚠️  Not authenticated (run: gh auth login)"
    errors=$((errors + 1))
fi

# Check wkhtmltopdf (optional)
echo -n "• wkhtmltopdf: "
if command -v wkhtmltopdf &> /dev/null; then
    echo "✅ Available"
else
    echo "⚠️  Not found (PDF generation will use weasyprint)"
fi

# Test our tool
echo -n "• pr-report tool: "
if uvx --from . pr-report --help &> /dev/null; then
    echo "✅ Working"
else
    echo "❌ Failed to run"
    errors=$((errors + 1))
fi

# Check if config exists
echo -n "• Configuration: "
if [ -f "config.json" ]; then
    echo "✅ config.json exists"
else
    echo "⚠️  No config.json (run: ./scripts/setup.sh)"
fi

echo ""
if [ $errors -eq 0 ]; then
    echo "🎉 All checks passed! You're ready to go."
    echo ""
    echo "Quick start:"
    echo "  ./scripts/analyze.sh     # Analyze PRs"
    echo "  ./scripts/convert.sh     # Convert to PDF"
else
    echo "❌ $errors error(s) found. Please fix the issues above."
    echo ""
    echo "Common fixes:"
    echo "  • Install uvx: curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "  • Install GitHub CLI: brew install gh"
    echo "  • Authenticate: gh auth login"
    exit 1
fi