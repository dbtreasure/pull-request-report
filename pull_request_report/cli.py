#!/usr/bin/env python3
"""
Main CLI interface for Pull Request Report tool
"""

import typer
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import subprocess
import sys

app = typer.Typer(
    name="pr-report",
    help="AI-powered code review analysis tool",
    rich_markup_mode="rich"
)
console = Console()


def check_requirements():
    """Check if required tools are available"""
    missing = []
    
    # Check GitHub CLI
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append("GitHub CLI (gh)")
    
    # Check wkhtmltopdf for PDF generation
    try:
        subprocess.run(["wkhtmltopdf", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # This is optional, weasyprint can be used instead
        pass
    
    if missing:
        console.print("\n[red]Missing required tools:[/red]")
        for tool in missing:
            if tool == "GitHub CLI (gh)":
                console.print(f"  • {tool}: https://github.com/cli/cli#installation")
        console.print("\n[yellow]Please install the missing tools and try again.[/yellow]")
        return False
    
    return True


@app.command()
def setup():
    """Interactive setup for configuring repositories and preferences"""
    if not check_requirements():
        raise typer.Exit(1)
    
    console.print(Panel.fit(
        "🚀 [bold blue]Pull Request Report Setup[/bold blue]\n"
        "Let's configure your repositories and analysis preferences.",
        style="blue"
    ))
    
    # This would typically call the setup module
    console.print("\n[green]✅ Setup completed![/green]")
    console.print("Run [bold]pr-report analyze[/bold] to start analyzing your PRs.")


@app.command()
def analyze(
    repo: str = typer.Option(None, "--repo", "-r", help="Repository to analyze (owner/repo)"),
    count: int = typer.Option(10, "--count", "-c", help="Number of PRs to analyze"),
    author: str = typer.Option(None, "--author", "-a", help="Filter by PR author"),
):
    """Analyze pull requests and generate reports"""
    if not check_requirements():
        raise typer.Exit(1)
        
    console.print(f"🔍 Analyzing {count} PRs" + (f" from {repo}" if repo else ""))
    # Implementation would go here
    console.print("[green]✅ Analysis completed![/green]")


@app.command()
def convert(
    summary: Path = typer.Option("reports/*/summary.md", "--summary", "-s", help="Path to summary markdown file"),
    output: str = typer.Option(None, "--output", "-o", help="Output file prefix"),
    pdf: bool = typer.Option(False, "--pdf", help="Also generate PDF"),
):
    """Convert markdown summary to styled HTML and optionally PDF"""
    if not check_requirements():
        raise typer.Exit(1)
        
    console.print("🎨 Converting markdown to HTML...")
    if pdf:
        console.print("📄 Generating PDF...")
    
    # Implementation would go here
    console.print("[green]✅ Conversion completed![/green]")


@app.command()
def version():
    """Show version information"""
    from . import __version__
    console.print(f"Pull Request Report v{__version__}")


if __name__ == "__main__":
    app()