# Contributing to Pull Request Report

Thank you for your interest in contributing to Pull Request Report! This document provides guidelines and information for contributors.

## 🚀 Quick Start for Contributors

1. **Fork the repository** and clone your fork
2. **Install dependencies**: `./scripts/setup.sh` 
3. **Run tests**: `./scripts/test.sh`
4. **Make your changes** following the guidelines below
5. **Test thoroughly** and ensure all tests pass
6. **Submit a pull request** with a clear description

## 📋 Types of Contributions

We welcome various types of contributions:

### 🐛 Bug Reports
- Use the bug report issue template
- Include steps to reproduce
- Provide system information (OS, Python version, etc.)
- Include relevant error messages or logs

### ✨ Feature Requests
- Use the feature request issue template
- Explain the problem you're trying to solve
- Describe your proposed solution
- Consider implementation complexity and maintenance burden

### 📖 Documentation Improvements
- Fix typos, clarify instructions
- Add examples or use cases
- Improve installation guides
- Update outdated information

### 🔧 Code Contributions
- Bug fixes
- New features (discuss in issues first)
- Performance improvements
- Test coverage improvements
- Refactoring for maintainability

## 🛠️ Development Setup

### Prerequisites
- **uvx**: For dependency management (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- **GitHub CLI**: For repository access (`brew install gh` or [other platforms](https://github.com/cli/cli#installation))
- **Node.js 18+**: If using Claude Code
- **wkhtmltopdf** (optional): For PDF generation

### Local Development
```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR-USERNAME/pull-request-report
cd pull-request-report

# 2. Set up development environment
./scripts/setup.sh

# 3. Run tests to ensure everything works
./scripts/test.sh

# 4. Make your changes
# Edit files as needed

# 5. Test your changes
./scripts/test.sh
uvx --from . pr-report --help  # Test CLI
```

## 📝 Code Guidelines

### Code Style
- **Python**: Follow PEP 8, use type hints where appropriate
- **Shell Scripts**: Use `set -e` for error handling, quote variables
- **Markdown**: Use consistent formatting, check links
- **Tests**: Write tests for new functionality, maintain existing test structure

### File Organization
- **Core functionality**: `pull_request_report/` directory
- **Scripts**: `scripts/` directory with executable permissions
- **Tests**: `test/` directory with realistic fixtures
- **Documentation**: Root level markdown files

### Testing Requirements
All contributions must include appropriate tests:
- **Unit tests**: For individual functions and components
- **Integration tests**: For full workflow testing
- **Test fixtures**: Realistic sample data when needed
- **All existing tests must pass**

### Commit Guidelines
Follow conventional commit format:
```
type(scope): description

Examples:
feat: add support for GitLab repositories
fix: resolve PDF generation on Windows
docs: update installation instructions
test: add tests for configuration validation
```

## 🔄 Pull Request Process

### Before Submitting
1. **Create an issue** for significant changes (discuss first)
2. **Fork the repository** and create a feature branch
3. **Write tests** for your changes
4. **Run the full test suite**: `./scripts/test.sh`
5. **Update documentation** if needed
6. **Check that scripts still work**: `./scripts/check.sh`

### Pull Request Requirements
- **Clear title and description** explaining the change
- **Reference related issues** (e.g., "Fixes #123")
- **Include test coverage** for new functionality
- **All CI checks passing**
- **No merge conflicts** with main branch
- **Updated documentation** if API or usage changes

### Review Process
1. **Automated checks** must pass (tests, linting)
2. **Maintainer review** for code quality and design
3. **Community feedback** may be requested for significant changes
4. **Approval and merge** by project maintainers

## 🐛 Reporting Issues

### Security Issues
For security vulnerabilities, please follow our [Security Policy](SECURITY.md).

### Bug Reports
When reporting bugs, please include:
- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **System information**: OS, Python version, package versions
- **Error messages** and relevant logs
- **Sample configuration** if applicable (sanitized)

### Feature Requests
For feature requests, please provide:
- **Problem description**: What issue are you trying to solve?
- **Proposed solution**: How should this be implemented?
- **Alternatives considered**: Other ways to solve the problem
- **Implementation complexity**: Your assessment of difficulty
- **Backward compatibility**: Impact on existing users

## 📚 Documentation Standards

### README Updates
- Keep installation instructions current
- Update feature lists when adding capabilities
- Ensure examples work with current version
- Maintain consistent formatting and style

### Code Documentation
- **Docstrings**: Use clear, concise descriptions
- **Comments**: Explain complex logic, not obvious code
- **Type hints**: Include for function parameters and returns
- **Examples**: Provide usage examples in docstrings

### Test Documentation
- **Test names**: Should clearly describe what's being tested
- **Test fixtures**: Include realistic, representative data
- **Test coverage**: Aim for high coverage of critical paths
- **Test documentation**: Explain complex test scenarios

## 🏷️ Release Process

### Versioning
We follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **Major**: Breaking changes
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, backward compatible

### Release Checklist
- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md` with release notes
- [ ] Ensure all tests pass
- [ ] Tag release with version number
- [ ] Create GitHub release with notes
- [ ] Announce in discussions/README if significant

## ❓ Getting Help

### Community Support
- **GitHub Issues**: For bugs, feature requests, and questions
- **GitHub Discussions**: For general questions and community interaction
- **Documentation**: Check existing documentation first

### Maintainer Contact
- **Response time**: We aim to respond to issues within 48 hours
- **Review time**: Pull requests typically reviewed within 1 week
- **Complex changes**: May require longer discussion and review

## 🎯 Project Goals

When contributing, please keep these project goals in mind:
- **User-friendly**: Easy setup and usage for developers
- **Privacy-focused**: All analysis runs locally, no data transmission
- **Cross-platform**: Works on macOS, Linux, and Windows (WSL)
- **Maintainable**: Clean, tested, well-documented code
- **Extensible**: Easy to add new features and analysis types

## 🙏 Recognition

Contributors will be:
- **Acknowledged** in release notes for significant contributions
- **Listed** in repository contributors
- **Credited** in commit messages with Co-Authored-By tags
- **Appreciated** by the community for their efforts

Thank you for contributing to Pull Request Report! Your efforts help make code review analysis accessible to developers everywhere. 🚀