# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a reusable pull request analysis tool designed to help developers identify patterns in code review feedback and improve their code quality. Engineers can configure it to analyze their own pull requests from any GitHub repository they have access to.

## Setup Commands

When a user says any of these phrases, initiate the setup process:
- "Set me up"
- "Setup"
- "Configure"
- "Get started"
- "Initialize"

### Setup Process

1. **Check Prerequisites**:
   ```bash
   # Check if gh is installed
   which gh || echo "GitHub CLI not found. Please install: https://github.com/cli/cli#installation"
   
   # Check GitHub auth
   gh auth status || echo "Please run: gh auth login"
   ```

2. **Interactive Configuration**:
   Ask the user:
   - "What's your GitHub username?"
   - "Which repository would you like to analyze? (format: owner/repo)"
   - "How would you describe your role or contributions to this repository?"
   - "What specific areas would you like to improve? (e.g., async patterns, API design, testing)"
   - "Would you like to add another repository? (yes/no)"

3. **Create config.json**:
   Based on their answers, generate a config.json file. Example:
   ```json
   {
     "repositories": [
       {
         "name": "repo-name",
         "github_url": "https://github.com/owner/repo",
         "description": "User's role description",
         "learning_goals": ["Goal 1", "Goal 2"],
         "focus_areas": ["Area 1", "Area 2"]
       }
     ],
     "analysis_settings": {
       "author": "their-username",
       "pr_limit": 10,
       "include_closed_prs": true
     }
   }
   ```

4. **Verify Setup**:
   - Test repository access: `gh repo view {repo}`
   - Create reports directory: `mkdir -p reports`
   - Confirm: "Setup complete! Would you like me to analyze your recent PRs now?"

## Repository Structure

```
pull-request-report/
├── CLAUDE.md                    # This file - project documentation
├── README.md                    # Quick start guide
├── SETUP.md                     # Detailed setup instructions
├── config.template.json         # Template for repository configuration
├── config.json                  # User's actual configuration (gitignored)
├── .gitignore                   # Excludes private reports and configs
└── reports/                     # Generated analysis reports (gitignored)
    └── {repo-name}/
        ├── intro.md             # Auto-generated context file
        └── pull-requests/
            └── PR-{number}-{title}.md
```

## Initial Setup for Users

Users should follow the quick start in README.md:
1. Clone the repository
2. Run `gh auth login` if needed
3. Open in Claude Code
4. Say "Set me up" - Claude will handle the rest interactively

## How to Use This Tool

### Step 1: Read User Configuration

When starting an analysis session, first read the user's config.json to understand:
- Which repositories to analyze
- The user's GitHub username
- Learning goals and focus areas
- Analysis settings (PR limits, etc.)

```bash
# Read the configuration
cat config.json
```

### Step 2: Create Repository Structure

For each repository in the config:

1. Create the directory structure:
   ```bash
   mkdir -p reports/{repo-name}/pull-requests
   ```

2. Generate an intro.md file in `reports/{repo-name}/intro.md` using the config data:
   ```markdown
   Github Repo Location: {github_url}
   Local location: {local_path}
   Me: {description}
   Goals: {learning_goals}
   Focus Areas: {focus_areas}
   ```

### Step 3: Analyze Pull Requests

1. **Authenticate with GitHub CLI**: `gh auth status`

2. **List PRs for analysis**:
   ```bash
   gh pr list --repo {github_url} --author {username} --state all --limit {pr_limit}
   ```

3. **For each PR, gather**:
   - PR overview: `gh pr view {pr-number} --repo {repo} --comments`
   - Review comments: `gh api repos/{owner}/{repo}/pulls/{pr-number}/comments`
   - Review summaries: `gh api repos/{owner}/{repo}/pulls/{pr-number}/reviews`

### Step 4: Generate Analysis Reports

Create reports in `reports/{repo-name}/pull-requests/PR-{number}-{title}.md` following this template:

```markdown
# PR #{number}: {title}

## PR Synopsis

**Pull Request**: #{number}  
**Title**: {Full PR title}  
**Author**: {username}  
**Status**: {MERGED|CLOSED|OPEN}  
**Date**: {merge/close date}  
**Reviewer(s)**: {reviewers and their decisions}  
**Changes**: {files modified, additions, deletions}  

### Purpose
{Brief description of what the PR accomplished}

### Technical Implementation
{List of key files modified and changes made}

## Code Review Comments

### Comment {N}: {Brief Summary}
**Reviewer**: {username}  
**File**: {file path}  
**Line**: {line number}  

**Comment Details**:
> {Quote the exact reviewer comment}

**Code Context**:
```{language}
{Relevant code snippet}
```

**What Was Requested**:
{Clear explanation of the change requested}

## Key Takeaways for Self-Improvement

### {N}. **{Improvement Theme}**
- **Issue**: {What problem was identified}
- **Learning**: {What principle or best practice this relates to}
- **Action**: {Specific action to take in future PRs}

## Future Improvements
{List of concrete steps based on this PR's feedback}
```

### Step 5: Generate Summary Reports (Optional)

After analyzing multiple PRs, create a summary report at `reports/{repo-name}/summary.md` that identifies:
- Common feedback patterns across PRs
- Progress over time
- Top areas for improvement
- Positive patterns to continue

## Analysis Best Practices

1. **Respect Privacy**: Never commit actual code snippets or detailed comments to public repos
2. **Focus on Patterns**: Look for recurring themes across multiple PRs
3. **Be Constructive**: Frame insights as opportunities for growth
4. **Track Progress**: Compare newer PRs to older ones to see improvement
5. **Prioritize Actionable Feedback**: Focus on concrete changes the developer can make

## Common User Commands

When users say these phrases, take the corresponding action:

- **"Analyze my recent PRs"** / **"Run analysis"** - Analyze all configured repositories
- **"Show me my improvement areas"** / **"Summary"** - Generate or show summary reports
- **"Add another repository"** / **"Add repo"** - Add a new repository to config.json
- **"Analyze just [repo-name]"** - Analyze only the specified repository
- **"Update my config"** / **"Change settings"** - Modify existing configuration

## Common Analysis Commands

```bash
# Check GitHub authentication
gh auth status

# List user's recent PRs
gh pr list --repo {owner}/{repo} --author {username} --state all --limit 10

# View specific PR with comments
gh pr view {pr-number} --repo {owner}/{repo} --comments

# Get detailed review comments
gh api repos/{owner}/{repo}/pulls/{pr-number}/comments

# Get review summaries
gh api repos/{owner}/{repo}/pulls/{pr-number}/reviews
```

## Working with Multiple Repositories

When analyzing multiple repositories from the config:

1. Process them sequentially or ask the user which to analyze
2. Create separate report directories for each
3. Consider creating a cross-repository summary if patterns emerge
4. Maintain consistent report formatting across all repos

## Error Handling

- If a repository is inaccessible, note it and continue with others
- If config.json is missing, prompt user to create it from template
- Handle rate limiting from GitHub API gracefully
- Provide clear error messages for authentication issues