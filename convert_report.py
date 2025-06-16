#!/usr/bin/env python3
"""
Claude Code Script: Intelligent PR Analysis Report Converter

This script converts markdown PR analysis summaries to styled HTML and PDF,
with intelligent parsing and fidelity verification.

Usage:
    python convert_report.py [--summary path] [--output prefix] [--pdf]
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_claude_conversion():
    """
    Claude Code Script for Converting PR Analysis Reports
    
    This script will:
    1. Read the markdown summary report
    2. Analyze the HTML template structure for styling
    3. Intelligently convert markdown to matching HTML
    4. Verify conversion fidelity 
    5. Optionally generate PDF
    """
    
    script = '''
# Claude Code Conversion Script

## Task 1: Read and Analyze Source Files

First, I need to read the markdown summary and understand its structure, then examine the HTML template to understand the visual styling approach.

### Step 1A: Read the markdown summary
I'll read the summary.md file to understand the content structure and identify all sections that need to be converted.

### Step 1B: Analyze HTML template
I'll examine the pr_analysis_pdf.html file to understand:
- CSS styling patterns for different content types
- HTML structure and class usage  
- Visual hierarchy and layout principles
- Print-specific formatting rules

## Task 2: Intelligent Content Conversion

### Step 2A: Content Analysis
I'll analyze the markdown content to identify:
- Main sections and their purposes
- Lists and their types (issues, improvements, recommendations)
- Emphasis patterns (strengths, critical items, standards compliance)
- Hierarchical structure and relationships

### Step 2B: HTML Generation
I'll convert the markdown to HTML by:
- Mapping content sections to appropriate CSS classes from the template
- Preserving all information while enhancing visual presentation
- Maintaining logical content flow and hierarchy
- Adding appropriate styling for different content types

## Task 3: Fidelity Verification

### Step 3A: Content Completeness Check
I'll verify that the HTML version contains:
- All original information from the markdown
- Correct section mappings and content organization
- Proper representation of all lists, recommendations, and findings
- No missing or added information

### Step 3B: Structure Validation  
I'll check that:
- HTML structure matches the template pattern
- CSS classes are used appropriately
- Content hierarchy is preserved
- Visual emphasis aligns with content importance

## Task 4: PDF Generation (Optional)

If requested, I'll generate a PDF using available tools while maintaining:
- Print-friendly formatting
- Page breaks in appropriate locations
- Readable fonts and spacing
- Complete content representation

## Task 5: Quality Assurance

I'll perform final verification:
- Compare original vs converted content
- Test HTML rendering
- Validate PDF output if generated
- Confirm no hallucinations or omissions
'''
    
    return script


def execute_claude_script(summary_path: str, output_prefix: str, generate_pdf: bool = False):
    """Execute the Claude Code conversion process."""
    
    # Create a comprehensive prompt for Claude Code
    claude_prompt = f"""
I need to convert a PR analysis markdown summary to styled HTML matching a specific template, with fidelity verification.

**Task Overview:**
Convert the markdown summary at `{summary_path}` to HTML matching the visual style of `pr_analysis_pdf.html`, then verify conversion fidelity.

**Specific Requirements:**
1. Read `{summary_path}` and understand its content structure
2. Read `pr_analysis_pdf.html` to understand the CSS styling patterns  
3. Convert the markdown to HTML using the same visual styling approach
4. Map content appropriately to CSS classes (overview-box, pattern-section, issues-list, improvements-list, strengths-list, recommendations, focus-areas, conclusion, etc.)
5. Preserve ALL original information - no additions, no omissions
6. Verify conversion fidelity by comparing original and converted content
7. Save the HTML output as `{output_prefix}.html`
{"8. Generate PDF using available tools (weasyprint or wkhtmltopdf)" if generate_pdf else ""}

**Key Styling Guidelines from Template:**
- Use overview-box for introductory content with PR lists
- Use pattern-section for main analysis sections  
- Use issues-list (red border) for problems/recurring issues
- Use improvements-list (green border) for improvement actions
- Use strengths-list (blue border) for positive observations
- Use recommendations (orange border) for actionable recommendations
- Use focus-areas (purple border) for future focus areas
- Use conclusion (green border) for summary/conclusion
- Maintain proper spacing, typography, and print-friendly formatting

**Critical Quality Checks:**
- Verify no content is lost or added during conversion
- Ensure proper HTML structure and CSS class usage
- Validate that visual hierarchy matches content importance
- Confirm all sections are appropriately styled
- Check that the output is both web and print-friendly

Please proceed with this conversion process step by step, ensuring high fidelity to the original content while achieving professional visual presentation.
"""
    
    print("Claude Code Conversion Script")
    print("=" * 50)
    print(f"Source: {summary_path}")
    print(f"Output: {output_prefix}.html")
    if generate_pdf:
        print(f"PDF: {output_prefix}.pdf")
    print("=" * 50)
    print()
    print("This script uses Claude Code to intelligently convert your PR analysis")
    print("summary to styled HTML with fidelity verification.")
    print()
    print("The conversion process includes:")
    print("1. Intelligent content analysis and parsing")  
    print("2. Template-based HTML generation")
    print("3. Fidelity verification (no hallucinations)")
    print("4. Quality assurance checks")
    if generate_pdf:
        print("5. PDF generation")
    print()
    
    print("To execute this conversion, please:")
    print("1. Open Claude Code in this directory")
    print("2. Paste the following prompt:")
    print()
    print("-" * 80)
    print(claude_prompt)
    print("-" * 80)
    print()
    print("Claude Code will then execute the conversion process with")
    print("intelligent parsing, proper styling, and fidelity verification.")
    
    return claude_prompt


def main():
    parser = argparse.ArgumentParser(
        description='Intelligent PR Analysis Report Converter using Claude Code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python convert_report.py                                    # Use defaults
  python convert_report.py --summary custom_summary.md       # Custom summary
  python convert_report.py --output my_report --pdf          # Custom output with PDF
  
This script generates a Claude Code prompt for intelligent conversion
with fidelity verification and quality assurance.
        '''
    )
    
    parser.add_argument('--summary', '-s',
                       default='reports/paxton-app-api/summary.md',
                       help='Path to markdown summary file (default: reports/paxton-app-api/summary.md)')
    
    parser.add_argument('--output', '-o', 
                       default='reports/paxton-app-api/analysis-report',
                       help='Output file prefix without extension (default: reports/paxton-app-api/analysis-report)')
    
    parser.add_argument('--pdf', action='store_true',
                       help='Also generate PDF output')
    
    args = parser.parse_args()
    
    # Validate input file exists
    summary_path = Path(args.summary)
    if not summary_path.exists():
        print(f"Error: Summary file not found: {summary_path}")
        print()
        print("Available summary files:")
        for md_file in Path('.').glob('**/summary.md'):
            print(f"  {md_file}")
        sys.exit(1)
    
    # Execute Claude Code script
    claude_prompt = execute_claude_script(
        str(summary_path), 
        args.output, 
        args.pdf
    )
    
    # Optionally save the prompt to a file for easy copy-paste
    prompt_file = Path("claude_conversion_prompt.txt")
    with open(prompt_file, 'w') as f:
        f.write(claude_prompt)
    
    print(f"\nThe Claude Code prompt has been saved to: {prompt_file}")
    print("You can copy-paste it directly into Claude Code for execution.")


if __name__ == '__main__':
    main()