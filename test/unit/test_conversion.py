"""
Unit tests for markdown to HTML conversion
"""

import re
from pathlib import Path


def test_sample_markdown_structure():
    """Test that sample summary has proper markdown structure"""
    summary_path = Path(__file__).parent.parent / "fixtures" / "sample_summary.md"
    
    with open(summary_path) as f:
        content = f.read()
    
    # Should have main sections
    assert "# Pull Request Analysis Summary" in content
    assert "## Overview" in content
    assert "## Key Patterns Identified" in content
    assert "## Strengths Observed" in content
    assert "## Top Recommendations for Improvement" in content
    assert "## Conclusion" in content
    
    # Should have PR list
    assert "**PRs Analyzed:**" in content
    assert "- PR #" in content
    
    # Should have pattern subsections
    assert "**Recurring Issues:**" in content
    assert "**Improvement Actions:**" in content
    
    # Should have structured recommendations
    assert "### Immediate Actions:" in content
    assert "### Focus Areas for Future PRs" in content


def test_markdown_list_structure():
    """Test that markdown lists are properly formatted"""
    summary_path = Path(__file__).parent.parent / "fixtures" / "sample_summary.md"
    
    with open(summary_path) as f:
        content = f.read()
    
    # Check for proper list formatting
    lines = content.split('\n')
    
    # Find list items and validate formatting
    list_items = [line for line in lines if line.strip().startswith('- ')]
    assert len(list_items) > 0, "Should have bullet list items"
    
    numbered_items = [line for line in lines if re.match(r'^\s*\d+\.', line.strip())]
    assert len(numbered_items) > 0, "Should have numbered list items"
    
    # Check for bold formatting
    bold_items = re.findall(r'\*\*[^*]+\*\*', content)
    assert len(bold_items) > 0, "Should have bold text formatting"


def test_content_completeness():
    """Test that sample content covers all expected analysis areas"""
    summary_path = Path(__file__).parent.parent / "fixtures" / "sample_summary.md"
    
    with open(summary_path) as f:
        content = f.read()
    
    # Should cover key technical areas
    technical_areas = [
        "Code Organization",
        "Error Handling", 
        "Resource Management",
        "Configuration",
        "API Design"
    ]
    
    for area in technical_areas:
        assert area in content, f"Should mention {area}"
    
    # Should have actionable recommendations
    action_words = ["implement", "use", "add", "extract", "ensure"]
    content_lower = content.lower()
    found_actions = [word for word in action_words if word in content_lower]
    assert len(found_actions) >= 3, f"Should have actionable language, found: {found_actions}"


def test_pr_references():
    """Test that PR references are properly formatted"""
    summary_path = Path(__file__).parent.parent / "fixtures" / "sample_summary.md"
    
    with open(summary_path) as f:
        content = f.read()
    
    # Find PR references
    pr_refs = re.findall(r'PR #\d+', content)
    assert len(pr_refs) > 0, "Should reference specific PRs"
    
    # PR numbers should be consistent with sample data
    expected_prs = ["PR #123", "PR #124"]
    for expected in expected_prs:
        assert expected in content, f"Should reference {expected}"


if __name__ == "__main__":
    test_sample_markdown_structure()
    test_markdown_list_structure()
    test_content_completeness()
    test_pr_references()
    print("✅ Conversion tests passed!")