#!/bin/bash
# Convenience script for converting reports to PDF

set -e

echo "🎨 Report Conversion"
echo "==================="

# Check uvx
if ! command -v uvx &> /dev/null; then
    echo "❌ uvx is required. See ./scripts/setup.sh for installation."
    exit 1
fi

# Find summary files if no specific file provided
if [ $# -eq 0 ]; then
    summaries=$(find reports -name "summary.md" 2>/dev/null || true)
    if [ -z "$summaries" ]; then
        echo "❌ No summary.md files found in reports/"
        echo "Run analysis first: ./scripts/analyze.sh"
        exit 1
    fi
    
    echo "📄 Found summary files:"
    echo "$summaries"
    echo ""
fi

# Run conversion
echo "🔄 Converting to HTML and PDF..."
uvx --from . pr-report convert --pdf "$@"

echo ""
echo "✅ Conversion complete!"
echo ""
echo "📋 Generated files:"
find reports -name "*.html" -o -name "*.pdf" 2>/dev/null | head -10