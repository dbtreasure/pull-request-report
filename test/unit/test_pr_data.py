"""
Unit tests for PR data parsing and validation
"""

import json
from pathlib import Path
from datetime import datetime


def test_pr_data_structure():
    """Test that sample PR data has correct structure"""
    data_path = Path(__file__).parent.parent / "fixtures" / "sample_pr_data.json"
    
    with open(data_path) as f:
        data = json.load(f)
    
    # Should have main sections
    assert "pr_list" in data
    assert "comments" in data
    assert "reviews" in data
    
    # PR list validation
    assert isinstance(data["pr_list"], list)
    assert len(data["pr_list"]) > 0
    
    for pr in data["pr_list"]:
        # Required fields
        assert "number" in pr
        assert "title" in pr
        assert "state" in pr
        assert "author" in pr
        assert "created_at" in pr
        assert "reviewers" in pr
        
        # Data types
        assert isinstance(pr["number"], int)
        assert isinstance(pr["title"], str)
        assert pr["state"] in ["OPEN", "CLOSED", "MERGED"]
        assert isinstance(pr["reviewers"], list)
        
        # Date format validation
        datetime.fromisoformat(pr["created_at"].replace('Z', '+00:00'))
        
        # Reviewers structure
        for reviewer in pr["reviewers"]:
            assert "login" in reviewer
            assert "state" in reviewer
            assert reviewer["state"] in ["APPROVED", "CHANGES_REQUESTED", "COMMENTED"]


def test_comments_structure():
    """Test PR comments structure"""
    data_path = Path(__file__).parent.parent / "fixtures" / "sample_pr_data.json"
    
    with open(data_path) as f:
        data = json.load(f)
    
    for comment in data["comments"]:
        assert "pr_number" in comment
        assert "user" in comment
        assert "body" in comment
        assert "file" in comment
        assert "line" in comment
        
        assert isinstance(comment["pr_number"], int)
        assert isinstance(comment["line"], int)
        assert len(comment["body"]) > 0


def test_reviews_structure():
    """Test PR reviews structure"""
    data_path = Path(__file__).parent.parent / "fixtures" / "sample_pr_data.json"
    
    with open(data_path) as f:
        data = json.load(f)
    
    for review in data["reviews"]:
        assert "pr_number" in review
        assert "user" in review
        assert "state" in review
        assert "body" in review
        
        assert isinstance(review["pr_number"], int)
        assert review["state"] in ["APPROVED", "CHANGES_REQUESTED", "COMMENTED"]


def test_data_consistency():
    """Test that PR numbers are consistent across data structures"""
    data_path = Path(__file__).parent.parent / "fixtures" / "sample_pr_data.json"
    
    with open(data_path) as f:
        data = json.load(f)
    
    # Get all PR numbers
    pr_numbers = {pr["number"] for pr in data["pr_list"]}
    comment_prs = {comment["pr_number"] for comment in data["comments"]}
    review_prs = {review["pr_number"] for review in data["reviews"]}
    
    # Comments and reviews should only reference existing PRs
    assert comment_prs.issubset(pr_numbers), f"Comments reference non-existent PRs: {comment_prs - pr_numbers}"
    assert review_prs.issubset(pr_numbers), f"Reviews reference non-existent PRs: {review_prs - pr_numbers}"


if __name__ == "__main__":
    test_pr_data_structure()
    test_comments_structure()
    test_reviews_structure()
    test_data_consistency()
    print("✅ PR data tests passed!")