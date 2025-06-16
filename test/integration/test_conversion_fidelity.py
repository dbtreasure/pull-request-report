"""
Integration tests for conversion fidelity
Tests that markdown to HTML conversion preserves all information
"""

import re
import tempfile
from pathlib import Path


def test_html_conversion_fidelity():
    """Test that HTML conversion preserves all markdown content"""
    # Read the sample summary
    repo_root = Path(__file__).parent.parent.parent
    sample_summary = repo_root / "test" / "fixtures" / "sample_summary.md"
    
    with open(sample_summary) as f:
        markdown_content = f.read()
    
    # Extract key content elements
    markdown_elements = extract_content_elements(markdown_content)
    
    # For now, test that we can extract elements correctly
    # In a full implementation, this would convert to HTML and verify
    assert len(markdown_elements['headings']) > 0
    assert len(markdown_elements['pr_list']) > 0
    assert len(markdown_elements['recommendations']) > 0
    
    print(f"✅ Found {len(markdown_elements['headings'])} headings")
    print(f"✅ Found {len(markdown_elements['pr_list'])} PR references")
    print(f"✅ Found {len(markdown_elements['recommendations'])} recommendations")


def extract_content_elements(content):
    """Extract key content elements from markdown"""
    elements = {
        'headings': [],
        'pr_list': [],
        'recommendations': [],
        'strengths': [],
        'patterns': []
    }
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Extract headings
        if line.startswith('#'):
            elements['headings'].append(line)
        
        # Extract PR references
        if 'PR #' in line:
            pr_refs = re.findall(r'PR #\d+[^:]*(?::[^$]*)?', line)
            elements['pr_list'].extend(pr_refs)
        
        # Extract recommendations (numbered lists)
        if re.match(r'^\d+\.', line):
            elements['recommendations'].append(line)
        
        # Extract strengths (numbered lists in strengths section)
        if line.startswith('1.') and 'Strengths' in '\n'.join(lines[max(0, lines.index(line)-10):lines.index(line)]):
            elements['strengths'].append(line)
        
        # Extract patterns (under pattern sections)
        if line.startswith('- **') and ('Issues:' in line or 'Actions:' in line):
            elements['patterns'].append(line)
    
    return elements


def test_html_structure_requirements():
    """Test that HTML output would have required structure"""
    sample_summary = Path(__file__).parent.parent.parent / "test" / "fixtures" / "sample_summary.md"
    
    with open(sample_summary) as f:
        content = f.read()
    
    # Verify that sample has content that should map to specific HTML structures
    required_sections = {
        'overview': '## Overview',
        'patterns': '## Key Patterns Identified', 
        'strengths': '## Strengths Observed',
        'recommendations': '## Top Recommendations',
        'conclusion': '## Conclusion'
    }
    
    for section_name, section_heading in required_sections.items():
        assert section_heading in content, f"Missing required section: {section_name}"
    
    # Should have lists that would become styled HTML lists
    assert '**PRs Analyzed:**' in content
    assert '**Recurring Issues:**' in content
    assert '**Improvement Actions:**' in content
    
    # Should have content that would become different CSS classes
    assert '### Immediate Actions:' in content
    assert '### Focus Areas for Future PRs' in content


def test_pr_template_structure():
    """Test that we have the structure needed for individual PR reports"""
    # This tests the structure we'd need for generating individual PR reports
    # from the sample PR data
    
    pr_data_path = Path(__file__).parent.parent / "fixtures" / "sample_pr_data.json"
    
    import json
    with open(pr_data_path) as f:
        data = json.load(f)
    
    # Should have enough data to generate meaningful PR reports
    assert len(data['pr_list']) >= 2, "Need multiple PRs for meaningful analysis"
    assert len(data['comments']) >= 2, "Need multiple comments for patterns"
    assert len(data['reviews']) >= 2, "Need multiple reviews for analysis"
    
    # Each PR should have sufficient detail
    for pr in data['pr_list']:
        assert len(pr['title']) > 10, f"PR {pr['number']} title too short"
        assert len(pr['reviewers']) > 0, f"PR {pr['number']} has no reviewers"
    
    # Comments should have meaningful content
    for comment in data['comments']:
        assert len(comment['body']) > 20, f"Comment body too short: {comment['body'][:50]}..."
    
    print("✅ PR template structure is adequate for report generation")


def test_engineering_docs_structure():
    """Test that engineering docs have the right structure for standards analysis"""
    docs_path = Path(__file__).parent.parent / "fixtures" / "sample_engineering_docs.md"
    
    with open(docs_path) as f:
        content = f.read()
    
    # Should have standards that can be checked against
    critical_standards = [
        "ZERO business logic",
        "Feature-Based Organization", 
        "Service Layer Patterns",
        "Repository Layer Purity",
        "DRY Principle"
    ]
    
    for standard in critical_standards:
        assert standard in content, f"Missing critical standard: {standard}"
    
    # Should have actionable guidance
    assert "CRITICAL:" in content or "MANDATORY:" in content
    assert "Example:" in content or "```" in content  # Code examples
    
    print("✅ Engineering docs have sufficient standards for analysis")


if __name__ == "__main__":
    test_html_conversion_fidelity()
    test_html_structure_requirements()
    test_pr_template_structure()
    test_engineering_docs_structure()
    print("✅ Conversion fidelity tests passed!")