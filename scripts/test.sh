#!/bin/bash
# Test runner script using uvx

set -e

echo "🧪 Pull Request Report - Test Suite"
echo "==================================="

# Check uvx
if ! command -v uvx &> /dev/null; then
    echo "❌ uvx is required. See ./scripts/setup.sh for installation."
    exit 1
fi

# Run tests using uvx to ensure consistent environment
echo "🔬 Running tests with uvx..."
echo ""

uvx --from . --with pytest --with tomli python test/run_tests.py

echo ""
echo "🔍 Additional Checks:"

# Test that CLI works
echo -n "• CLI functionality: "
if uvx --from . pr-report --help &> /dev/null; then
    echo "✅"
else
    echo "❌"
fi

# Test that scripts are executable
echo -n "• Script permissions: "
if [ -x "scripts/setup.sh" ] && [ -x "scripts/analyze.sh" ] && [ -x "scripts/convert.sh" ]; then
    echo "✅"
else
    echo "❌"
fi

# Test that fixtures exist
echo -n "• Test fixtures: "
if [ -f "test/fixtures/sample_config.json" ] && [ -f "test/fixtures/sample_pr_data.json" ]; then
    echo "✅"
else
    echo "❌"
fi

echo ""
echo "🎯 To run individual test categories:"
echo "  python test/run_tests.py           # All tests"
echo "  python test/unit/test_config.py    # Just config tests"
echo "  python test/integration/test_full_workflow.py  # Just integration tests"