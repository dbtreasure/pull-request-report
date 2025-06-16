#!/usr/bin/env python3
"""
Pull Request Analysis Report Converter
Converts markdown summary reports to styled HTML and PDF format.
"""

import re
import json
import argparse
from pathlib import Path
from datetime import datetime
import subprocess
import sys

def parse_markdown_summary(content: str) -> dict:
    """Parse the markdown summary into structured data."""
    data = {
        'title': 'Pull Request Analysis Summary',
        'overview': '',
        'pr_list': [],
        'patterns': [],
        'standards_compliance': '',
        'strengths': [],
        'recommendations': {
            'critical': [],
            'immediate': [],
            'development': [],
            'architecture': []
        },
        'focus_areas': {
            'clean_code': [],
            'fastapi': [],
            'api_construction': []
        },
        'conclusion': ''
    }
    
    lines = content.split('\n')
    current_section = None
    current_subsection = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Main sections
        if line.startswith('# '):
            data['title'] = line[2:]
        elif line.startswith('## Overview'):
            current_section = 'overview'
            current_content = []
        elif line.startswith('## Key Patterns'):
            current_section = 'patterns'
            current_content = []
        elif line.startswith('## Standards Compliance'):
            current_section = 'standards_compliance'
            current_content = []
        elif line.startswith('## Strengths'):
            current_section = 'strengths'
            current_content = []
        elif line.startswith('## Top Recommendations'):
            current_section = 'recommendations'
            current_content = []
        elif line.startswith('## Focus Areas'):
            current_section = 'focus_areas'
            current_content = []
        elif line.startswith('## Conclusion'):
            current_section = 'conclusion'
            current_content = []
        # Subsections
        elif line.startswith('### ') and current_section == 'recommendations':
            if 'Critical Actions' in line:
                current_subsection = 'critical'
            elif 'Immediate Actions' in line:
                current_subsection = 'immediate'
            elif 'Development Process' in line:
                current_subsection = 'development'
            elif 'Architecture Improvements' in line:
                current_subsection = 'architecture'
        elif line.startswith('### ') and current_section == 'focus_areas':
            if 'Clean Code' in line:
                current_subsection = 'clean_code'
            elif 'FastAPI' in line:
                current_subsection = 'fastapi'
            elif 'API Construction' in line:
                current_subsection = 'api_construction'
            else:
                current_subsection = None
        else:
            # Content lines
            current_content.append(line)
            
            # Process content based on current section
            if current_section == 'overview':
                if line.startswith('- PR #'):
                    data['pr_list'].append(line[2:])
                elif not line.startswith('**PRs Analyzed:**') and not line.startswith('- PR #'):
                    data['overview'] += line + ' '
            elif current_section == 'patterns':
                if line.startswith('### '):
                    # New pattern section
                    pattern_name = line[4:].split('**')[1] if '**' in line else line[4:]
                    data['patterns'].append({
                        'name': pattern_name,
                        'issues': [],
                        'improvements': []
                    })
                elif line.startswith('- **') and data['patterns']:
                    # Issue or improvement item
                    if '**Recurring Issues:**' in '\n'.join(current_content[-5:]):
                        data['patterns'][-1]['issues'].append(line[2:])
                    elif '**Improvement Actions:**' in '\n'.join(current_content[-5:]):
                        data['patterns'][-1]['improvements'].append(line[2:])
            elif current_section == 'standards_compliance':
                data['standards_compliance'] += line + '\n'
            elif current_section == 'strengths':
                if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.')):
                    data['strengths'].append(line)
            elif current_section == 'recommendations' and current_subsection:
                if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.')):
                    data['recommendations'][current_subsection].append(line)
            elif current_section == 'focus_areas' and current_subsection and current_subsection in data['focus_areas']:
                if line.startswith('- '):
                    data['focus_areas'][current_subsection].append(line[2:])
            elif current_section == 'conclusion':
                data['conclusion'] += line + ' '
    
    return data

def generate_html(data: dict, config: dict) -> str:
    """Generate HTML from parsed data using the template style."""
    
    # Read the template CSS from the example file
    css_content = """
        @page {
            margin: 1in;
            size: letter;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 8.5in;
            margin: 0 auto;
            background: white;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            font-size: 28px;
            margin-bottom: 30px;
        }
        
        h2 {
            color: #34495e;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 8px;
            margin-top: 35px;
            margin-bottom: 20px;
            font-size: 22px;
        }
        
        h3 {
            color: #2c3e50;
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 18px;
        }
        
        h4 {
            color: #34495e;
            margin-top: 20px;
            margin-bottom: 12px;
            font-size: 16px;
            font-weight: 600;
        }
        
        p {
            margin-bottom: 15px;
            text-align: justify;
        }
        
        ul, ol {
            margin-bottom: 20px;
            padding-left: 25px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        strong {
            color: #2c3e50;
            font-weight: 600;
        }
        
        .overview-box {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .pr-list {
            background: #ffffff;
            border-left: 4px solid #3498db;
            padding: 15px 20px;
            margin: 15px 0;
        }
        
        .pattern-section {
            background: #fefefe;
            border: 1px solid #e1e8ed;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .issues-list {
            background: #fff5f5;
            border-left: 4px solid #e74c3c;
            padding: 15px 20px;
            margin: 15px 0;
        }
        
        .improvements-list {
            background: #f0fff4;
            border-left: 4px solid #27ae60;
            padding: 15px 20px;
            margin: 15px 0;
        }
        
        .strengths-list {
            background: #f0f8ff;
            border-left: 4px solid #3498db;
            padding: 15px 20px;
            margin: 15px 0;
        }
        
        .recommendations {
            background: #fffbf0;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        
        .focus-areas {
            background: #f8f0ff;
            border: 2px solid #9b59b6;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        
        .conclusion {
            background: #f0f8f0;
            border: 2px solid #27ae60;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        
        .standards-compliance {
            background: #f0f8ff;
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        
        .page-break {
            page-break-before: always;
        }
        
        @media print {
            body {
                font-size: 12px;
                line-height: 1.4;
            }
            
            h1 { font-size: 24px; }
            h2 { font-size: 18px; }
            h3 { font-size: 16px; }
            h4 { font-size: 14px; }
            
            .pattern-section,
            .recommendations,
            .focus-areas,
            .conclusion,
            .standards-compliance {
                break-inside: avoid;
            }
        }
    """
    
    # Generate repository info from config
    repo_info = ""
    if config.get('repositories'):
        repo = config['repositories'][0]  # Use first repo
        repo_info = f"Analyzed {len(data['pr_list'])} recent pull requests from the {repo['name']} repository"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <style>{css_content}</style>
</head>
<body>
    <h1>{data['title']}</h1>
    
    <div class="overview-box">
        <h2>Overview</h2>
        <p>{repo_info} to identify patterns in code review feedback and opportunities for improvement in FastAPI and API construction patterns.</p>
        
        <div class="pr-list">
            <strong>PRs Analyzed:</strong>
            <ul>"""
    
    # Add PR list
    for pr in data['pr_list']:
        html += f"\n                <li>{pr}</li>"
    
    html += """
            </ul>
        </div>
    </div>

    <h2>Key Patterns Identified</h2>
"""
    
    # Add patterns
    for i, pattern in enumerate(data['patterns']):
        html += f"""
    <div class="pattern-section">
        <h3>{i+1}. {pattern['name']}</h3>
        
        <div class="issues-list">
            <h4>Recurring Issues:</h4>
            <ul>"""
        
        for issue in pattern['issues']:
            html += f"\n                <li>{issue}</li>"
        
        html += """
            </ul>
        </div>

        <div class="improvements-list">
            <h4>Improvement Actions:</h4>
            <ul>"""
        
        for improvement in pattern['improvements']:
            html += f"\n                <li>{improvement}</li>"
        
        html += """
            </ul>
        </div>
    </div>"""
    
    # Add page break
    html += '\n\n    <div class="page-break"></div>'
    
    # Add standards compliance if available
    if data['standards_compliance'].strip():
        html += f"""
    
    <div class="standards-compliance">
        <h2>Standards Compliance Analysis</h2>
        <div>{data['standards_compliance'].replace('**', '<strong>').replace('**', '</strong>')}</div>
    </div>"""
    
    # Add strengths
    html += """

    <div class="strengths-list">
        <h2>Strengths Observed</h2>
        <ol>"""
    
    for strength in data['strengths']:
        html += f"\n            <li>{strength}</li>"
    
    html += """
        </ol>
    </div>

    <div class="page-break"></div>

    <div class="recommendations">
        <h2>Top Recommendations for Improvement</h2>"""
    
    # Add recommendation sections
    rec_sections = [
        ('critical', 'Critical Actions'),
        ('immediate', 'Immediate Actions'),
        ('development', 'Development Process'),
        ('architecture', 'Architecture Improvements')
    ]
    
    for key, title in rec_sections:
        if data['recommendations'][key]:
            html += f"""
        
        <h3>{title}:</h3>
        <ol>"""
            for rec in data['recommendations'][key]:
                html += f"\n            <li>{rec}</li>"
            html += """
        </ol>"""
    
    html += """
    </div>

    <div class="focus-areas">
        <h2>Focus Areas for Future PRs</h2>
        <p>Based on your learning goals of clean code and FastAPI patterns:</p>"""
    
    # Add focus areas
    focus_sections = [
        ('clean_code', 'Clean Code Principles'),
        ('fastapi', 'FastAPI Best Practices'),
        ('api_construction', 'API Construction Patterns')
    ]
    
    for key, title in focus_sections:
        if data['focus_areas'][key]:
            html += f"""

        <h3>{title}:</h3>
        <ul>"""
            for item in data['focus_areas'][key]:
                html += f"\n            <li>{item}</li>"
            html += """
        </ul>"""
    
    html += """
    </div>

    <div class="conclusion">
        <h2>Conclusion</h2>"""
    
    if data['conclusion'].strip():
        html += f"\n        <p>{data['conclusion'].strip()}</p>"
    else:
        html += """
        <p>The analysis shows strong technical implementation skills with room for improvement in code organization, consistency, and leveraging existing patterns. The team provides excellent feedback that, when systematically applied, will lead to cleaner, more maintainable FastAPI code.</p>

        <h3>Next Steps:</h3>
        <ol>
            <li>Implement the immediate actions listed above</li>
            <li>Apply these patterns to future PRs</li>
            <li>Consider creating a team coding standards document based on these patterns</li>
        </ol>"""
    
    html += """
    </div>
</body>
</html>"""
    
    return html

def convert_html_to_pdf(html_file: Path, pdf_file: Path) -> bool:
    """Convert HTML to PDF using weasyprint or wkhtmltopdf."""
    
    # Try weasyprint first (better CSS support)
    try:
        import weasyprint
        weasyprint.HTML(filename=str(html_file)).write_pdf(str(pdf_file))
        return True
    except ImportError:
        pass
    
    # Try wkhtmltopdf as fallback
    try:
        result = subprocess.run([
            'wkhtmltopdf',
            '--page-size', 'Letter',
            '--margin-top', '1in',
            '--margin-bottom', '1in',
            '--margin-left', '1in',
            '--margin-right', '1in',
            '--print-media-type',
            str(html_file),
            str(pdf_file)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
        else:
            print(f"wkhtmltopdf error: {result.stderr}")
            return False
    except FileNotFoundError:
        pass
    
    print("Error: Neither weasyprint nor wkhtmltopdf is available")
    print("Install weasyprint with: pip install weasyprint")
    print("Or install wkhtmltopdf from: https://wkhtmltopdf.org/downloads.html")
    return False

def main():
    parser = argparse.ArgumentParser(description='Convert PR analysis summary to HTML and PDF')
    parser.add_argument('--summary', '-s', 
                       default='reports/paxton-app-api/summary.md',
                       help='Path to markdown summary file')
    parser.add_argument('--config', '-c',
                       default='config.json',
                       help='Path to config.json file')
    parser.add_argument('--output', '-o',
                       default='reports/paxton-app-api/analysis-report',
                       help='Output file prefix (without extension)')
    parser.add_argument('--html-only', action='store_true',
                       help='Generate only HTML, skip PDF conversion')
    
    args = parser.parse_args()
    
    # Read input files
    summary_path = Path(args.summary)
    config_path = Path(args.config)
    
    if not summary_path.exists():
        print(f"Error: Summary file not found: {summary_path}")
        sys.exit(1)
    
    if not config_path.exists():
        print(f"Warning: Config file not found: {config_path}")
        config = {}
    else:
        with open(config_path) as f:
            config = json.load(f)
    
    # Parse markdown
    with open(summary_path) as f:
        content = f.read()
    
    data = parse_markdown_summary(content)
    
    # Generate HTML
    html_content = generate_html(data, config)
    
    # Write HTML file
    html_path = Path(f"{args.output}.html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    print(f"HTML report generated: {html_path}")
    
    # Generate PDF
    if not args.html_only:
        pdf_path = Path(f"{args.output}.pdf")
        if convert_html_to_pdf(html_path, pdf_path):
            print(f"PDF report generated: {pdf_path}")
        else:
            print("PDF generation failed. HTML report is available.")
            sys.exit(1)

if __name__ == '__main__':
    main()