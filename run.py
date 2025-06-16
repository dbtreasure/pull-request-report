#!/usr/bin/env python3
"""
Standalone runner for Pull Request Report tool using uvx
This script can be executed directly with uvx without installing the package globally.
"""

import subprocess
import sys
import os
from pathlib import Path

# Add the current directory to Python path so we can import local modules
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """Main entry point that delegates to the CLI"""
    try:
        from pull_request_report.cli import app
        app()
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Make sure you're running this with uvx or have the dependencies installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()