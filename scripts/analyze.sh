#!/bin/bash
# Convenience script for analyzing pull requests

set -e

echo "🔍 Pull Request Analysis"
echo "======================="

# Check if config exists
if [ ! -f "config.json" ]; then
    echo "❌ No config.json found. Please run setup first:"
    echo "   ./scripts/setup.sh"
    exit 1
fi

# Check uvx
if ! command -v uvx &> /dev/null; then
    echo "❌ uvx is required. See ./scripts/setup.sh for installation."
    exit 1
fi

# Run analysis
echo "📊 Starting PR analysis..."
uvx --from . pr-report analyze "$@"

echo ""
echo "✅ Analysis complete!"
echo ""
echo "Next steps:"
echo "  • View reports in: reports/"
echo "  • Convert to PDF: ./scripts/convert.sh"