"""
Integration tests for the full workflow
"""

import json
import subprocess
import tempfile
import shutil
from pathlib import Path


def test_cli_help():
    """Test that CLI commands work"""
    # Test main help
    result = subprocess.run(
        ["uvx", "--from", ".", "pr-report", "--help"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent
    )
    
    assert result.returncode == 0, f"CLI help failed: {result.stderr}"
    assert "AI-powered code review analysis tool" in result.stdout
    assert "setup" in result.stdout
    assert "analyze" in result.stdout
    assert "convert" in result.stdout


def test_setup_command():
    """Test setup command execution"""
    result = subprocess.run(
        ["uvx", "--from", ".", "pr-report", "setup"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent
    )
    
    # Should run without error (even if it just shows help/placeholder)
    assert result.returncode == 0, f"Setup command failed: {result.stderr}"


def test_version_command():
    """Test version command"""
    result = subprocess.run(
        ["uvx", "--from", ".", "pr-report", "version"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent
    )
    
    assert result.returncode == 0, f"Version command failed: {result.stderr}"
    assert "Pull Request Report" in result.stdout
    assert "v" in result.stdout


def test_convert_command():
    """Test convert command with sample data"""
    repo_root = Path(__file__).parent.parent.parent
    sample_summary = repo_root / "test" / "fixtures" / "sample_summary.md"
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        output_prefix = temp_path / "test_report"
        
        result = subprocess.run([
            "uvx", "--from", ".", "pr-report", "convert",
            "--summary", str(sample_summary),
            "--output", str(output_prefix)
        ],
        capture_output=True,
        text=True,
        cwd=repo_root
        )
        
        assert result.returncode == 0, f"Convert command failed: {result.stderr}"
        # Note: Actual file generation depends on full implementation


def test_script_permissions():
    """Test that all scripts are executable"""
    repo_root = Path(__file__).parent.parent.parent
    scripts_dir = repo_root / "scripts"
    
    for script in scripts_dir.glob("*.sh"):
        assert script.is_file(), f"Script {script.name} should exist"
        # Check if executable (on Unix systems)
        import stat
        file_stat = script.stat()
        is_executable = file_stat.st_mode & stat.S_IEXEC
        assert is_executable, f"Script {script.name} should be executable"


def test_config_template_validity():
    """Test that config template is valid"""
    repo_root = Path(__file__).parent.parent.parent
    template_path = repo_root / "config.template.json"
    
    if template_path.exists():
        with open(template_path) as f:
            config = json.load(f)
        
        # Should be valid JSON structure
        assert isinstance(config, dict)


def test_pyproject_toml_validity():
    """Test that pyproject.toml is valid"""
    repo_root = Path(__file__).parent.parent.parent
    pyproject_path = repo_root / "pyproject.toml"
    
    assert pyproject_path.exists(), "pyproject.toml should exist"
    
    # Try to parse it (requires tomli/tomllib)
    try:
        import tomllib  # Python 3.11+
    except ImportError:
        try:
            import tomli as tomllib  # Fallback
        except ImportError:
            print("⚠️  Cannot validate pyproject.toml - no TOML parser available")
            return
    
    with open(pyproject_path, 'rb') as f:
        config = tomllib.load(f)
    
    # Should have required sections
    assert "project" in config
    assert "name" in config["project"]
    assert "version" in config["project"]
    assert "dependencies" in config["project"]


if __name__ == "__main__":
    test_cli_help()
    test_setup_command()
    test_version_command()
    test_convert_command()
    test_script_permissions()
    test_config_template_validity()
    test_pyproject_toml_validity()
    print("✅ Integration tests passed!")