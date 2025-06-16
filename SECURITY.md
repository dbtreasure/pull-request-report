# Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions of Pull Request Report:

| Version | Supported          | Notes                    |
| ------- | ------------------ | ------------------------ |
| 1.x.x   | :white_check_mark: | Current stable release   |
| main    | :white_check_mark: | Development branch       |

## Security Considerations

### Data Privacy
- **Local Operation**: All analysis runs locally on your machine
- **No Data Transmission**: Your code and PR data never leave your environment
- **GitHub API**: Only uses GitHub's official API with your authenticated access
- **Reports Storage**: Generated reports are stored locally and gitignored by default

### Dependencies
- **Python Packages**: Uses well-maintained packages (weasyprint, typer, rich)
- **uvx Execution**: Leverages uv's secure package isolation
- **GitHub CLI**: Relies on official GitHub CLI for API access
- **No Secrets**: Tool doesn't handle or store authentication secrets directly

### File System Access
- **Read-Only GitHub Data**: Only reads PR data via GitHub API
- **Local Write Access**: Writes reports to local `reports/` directory only
- **Script Execution**: Shell scripts have minimal system interaction
- **No Elevated Privileges**: Runs with standard user permissions

## Reporting a Vulnerability

If you discover a security vulnerability in Pull Request Report, please help us maintain a secure environment by reporting it responsibly.

### How to Report

**Email**: Create an issue at [github.com/dbtreasure/pull-request-report/issues](https://github.com/dbtreasure/pull-request-report/issues) and mark it as a security concern, or contact the maintainers directly if the issue is sensitive.

**Please Include**:
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested fix (if you have one)

### What to Expect

- **Initial Response**: Within 48 hours
- **Assessment**: Security team will evaluate within 5 business days
- **Fix Timeline**: Critical issues will be addressed within 2 weeks
- **Public Disclosure**: After fix is released and users have time to update

### Security Best Practices for Users

**Environment Setup**:
- ✅ Keep Node.js and npm updated
- ✅ Use latest version of GitHub CLI
- ✅ Run in trusted development environments only
- ✅ Review scripts before execution (all are open source)

**GitHub Authentication**:
- ✅ Use GitHub CLI's official authentication (`gh auth login`)
- ✅ Limit repository access to what you need to analyze
- ✅ Regularly audit GitHub personal access tokens
- ✅ Use organizational access controls as appropriate

**Report Handling**:
- ✅ Keep generated reports in secure, private locations
- ✅ Don't commit reports to public repositories
- ✅ Be mindful of sensitive information in PR comments
- ✅ Use gitignore patterns to prevent accidental exposure

### Not a Security Issue

The following are **not** considered security vulnerabilities:
- Issues requiring physical access to the user's machine
- Problems with third-party dependencies (report to upstream projects)
- GitHub API rate limiting or access restrictions
- Cosmetic issues in generated reports
- Configuration errors or user setup mistakes

### Vulnerability Disclosure Policy

We follow responsible disclosure principles:
1. **Private Reporting**: Initial report kept confidential
2. **Collaborative Fix**: Work with reporter to develop fix
3. **Testing**: Validate fix doesn't introduce new issues
4. **Release**: Deploy fix in patch release
5. **Public Disclosure**: Announce fix after users can update

### Security Updates

- **Critical**: Released immediately as patch versions
- **High**: Released within 2 weeks
- **Medium/Low**: Included in next regular release
- **Notifications**: Posted in GitHub Releases and README

## Contact

For security-related questions or concerns:
- **GitHub Issues**: [github.com/dbtreasure/pull-request-report/issues](https://github.com/dbtreasure/pull-request-report/issues)
- **General Questions**: See project README for support information

Thank you for helping keep Pull Request Report secure! 🔒
