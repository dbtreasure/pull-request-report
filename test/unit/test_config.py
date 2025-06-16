"""
Unit tests for configuration handling
"""

import json
import pytest
from pathlib import Path


def test_config_validation():
    """Test that sample config is valid JSON and has required fields"""
    config_path = Path(__file__).parent.parent / "fixtures" / "sample_config.json"
    
    # Should be valid JSON
    with open(config_path) as f:
        config = json.load(f)
    
    # Should have required top-level fields
    assert "repositories" in config
    assert "analysis_settings" in config
    assert isinstance(config["repositories"], list)
    assert len(config["repositories"]) > 0
    
    # Each repository should have required fields
    for repo in config["repositories"]:
        assert "name" in repo
        assert "github_url" in repo
        assert "description" in repo
        assert "learning_goals" in repo
        assert "focus_areas" in repo
        
        # URLs should be valid GitHub URLs
        assert repo["github_url"].startswith("https://github.com/")
        
        # Lists should not be empty
        assert len(repo["learning_goals"]) > 0
        assert len(repo["focus_areas"]) > 0
    
    # Analysis settings should have required fields
    settings = config["analysis_settings"]
    assert "author" in settings
    assert "pr_limit" in settings
    assert isinstance(settings["pr_limit"], int)
    assert settings["pr_limit"] > 0


def test_engineering_docs_config():
    """Test engineering docs configuration"""
    config_path = Path(__file__).parent.parent / "fixtures" / "sample_config.json"
    
    with open(config_path) as f:
        config = json.load(f)
    
    if "engineering_docs" in config:
        docs = config["engineering_docs"]
        assert "github_url" in docs
        assert "enabled" in docs
        assert isinstance(docs["enabled"], bool)
        
        if docs["enabled"]:
            assert docs["github_url"].startswith("https://github.com/")


if __name__ == "__main__":
    test_config_validation()
    test_engineering_docs_config()
    print("✅ Config tests passed!")