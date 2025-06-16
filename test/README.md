# Test Suite

This directory contains comprehensive tests for the Pull Request Report tool, including sample data and test artifacts for validating each step of the analysis process.

## 🧪 Test Structure

```
test/
├── fixtures/           # Sample data for testing
│   ├── sample_config.json           # Example configuration
│   ├── sample_pr_data.json          # Mock GitHub API responses
│   ├── sample_engineering_docs.md   # Example team standards
│   └── sample_summary.md            # Expected analysis output
├── unit/              # Unit tests for individual components
│   ├── test_config.py               # Configuration validation
│   ├── test_pr_data.py              # PR data parsing
│   └── test_conversion.py           # Markdown processing
├── integration/       # Integration tests for full workflows
│   ├── test_full_workflow.py        # End-to-end CLI testing
│   └── test_conversion_fidelity.py  # HTML conversion accuracy
├── outputs/           # Generated test outputs (gitignored)
└── run_tests.py       # Main test runner
```

## 🚀 Running Tests

### Quick Test (Recommended)
```bash
# Run all tests with uvx
./scripts/test.sh
```

### Manual Test Execution
```bash
# Run all tests
python test/run_tests.py

# Run specific test categories
python test/unit/test_config.py
python test/integration/test_full_workflow.py

# Run with verbose output
python -v test/run_tests.py
```

### Individual Test Files
```bash
cd test
python unit/test_config.py        # Configuration tests
python unit/test_pr_data.py       # PR data validation
python unit/test_conversion.py    # Markdown structure tests
python integration/test_full_workflow.py     # CLI integration
python integration/test_conversion_fidelity.py  # HTML fidelity
```

## 📋 What Gets Tested

### Unit Tests

**Configuration Tests (`test_config.py`)**
- JSON structure validation
- Required field presence
- GitHub URL format validation
- Learning goals and focus areas validation
- Engineering docs configuration

**PR Data Tests (`test_pr_data.py`)**
- GitHub API response structure
- PR metadata completeness
- Comment and review data integrity
- Cross-reference consistency (PR numbers)
- Date format validation

**Conversion Tests (`test_conversion.py`)**
- Markdown structure validation
- Section completeness
- List formatting
- Content coverage of technical areas
- PR reference formatting

### Integration Tests

**Full Workflow Tests (`test_full_workflow.py`)**
- CLI command execution
- Script permissions and executability
- Package configuration validity
- End-to-end command flow

**Conversion Fidelity Tests (`test_conversion_fidelity.py`)**
- Markdown to HTML content preservation
- HTML structure requirements
- PR template adequacy
- Engineering docs standards coverage

## 📄 Test Fixtures

### `sample_config.json`
- **Purpose**: Valid configuration for testing setup process
- **Contains**: 2 repositories, engineering docs, analysis settings
- **Use**: Validates configuration parsing and structure

### `sample_pr_data.json`
- **Purpose**: Mock GitHub API responses for PR analysis
- **Contains**: 2 PRs with comments, reviews, and metadata
- **Use**: Tests PR data processing without GitHub API calls

### `sample_engineering_docs.md`
- **Purpose**: Example team coding standards document
- **Contains**: Critical standards like "ZERO business logic" rule
- **Use**: Tests standards compliance analysis features

### `sample_summary.md`
- **Purpose**: Expected analysis output format
- **Contains**: Structured analysis with patterns and recommendations
- **Use**: Tests report generation and HTML conversion

## ✅ Test Coverage

The test suite validates:

**✅ Configuration Management**
- Config file structure and validation
- Repository and settings parsing
- Engineering docs integration

**✅ Data Processing**
- GitHub API response parsing
- PR metadata extraction
- Comment and review processing
- Data consistency validation

**✅ Report Generation**
- Markdown structure creation
- Content organization
- Pattern identification
- Standards compliance analysis

**✅ HTML Conversion**
- Markdown to HTML transformation
- CSS styling application
- Content fidelity preservation
- PDF generation capability

**✅ CLI Interface**
- Command execution
- Parameter handling
- Error reporting
- Script functionality

**✅ Integration Workflow**
- End-to-end process flow
- File permissions
- Package configuration
- Cross-platform compatibility

## 🐛 Debugging Failed Tests

### Common Issues and Solutions

**"uvx command not found"**
```bash
# Install uvx first
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
brew install uv
```

**"Permission denied" on scripts**
```bash
chmod +x scripts/*.sh
chmod +x test/run_tests.py
```

**Import errors in tests**
```bash
# Make sure you're in the repo root
cd /path/to/pull-request-report
python test/run_tests.py
```

**GitHub CLI tests failing**
```bash
# Install and authenticate GitHub CLI
brew install gh
gh auth login
```

### Verbose Test Output
```bash
# Run with Python's verbose flag
python -v test/run_tests.py

# Run specific test with detailed output
python -u test/unit/test_config.py
```

## 📊 Success Criteria

Tests pass when:
- ✅ All fixture files are valid (JSON parseable, proper structure)
- ✅ Configuration validation works correctly
- ✅ PR data processing handles all edge cases
- ✅ Markdown output has required sections and formatting
- ✅ CLI commands execute without errors
- ✅ HTML conversion preserves all original content
- ✅ Scripts have proper permissions and execute successfully

## 🔄 Adding New Tests

### For New Features
1. **Add fixtures**: Create sample data in `test/fixtures/`
2. **Unit tests**: Test individual functions in `test/unit/`
3. **Integration**: Test full workflow in `test/integration/`
4. **Update runner**: Tests are auto-discovered by `run_tests.py`

### Test Naming Convention
- `test_*.py` for test files (auto-discovered)
- `sample_*.json/md` for fixture files
- Descriptive function names: `test_config_validation_with_invalid_urls()`

## 🎯 Continuous Testing

### During Development
```bash
# Quick validation
./scripts/test.sh

# Watch for changes and re-run (if using watchdog)
# pip install watchdog
# watchmedo auto-restart --patterns="*.py" --recursive -- python test/run_tests.py
```

### Before Commits
```bash
# Full test suite
./scripts/test.sh

# Check system requirements
./scripts/check.sh

# Validate all scripts work
./scripts/setup.sh --dry-run  # if implemented
```