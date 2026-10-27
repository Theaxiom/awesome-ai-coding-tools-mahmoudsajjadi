import sys, re, json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / 'README.md'
TOOLS_JSON = REPO_ROOT / 'docs' / 'tools.json'

def main():
    print('Checking awesome-ai-coding-tools catalog integrity...')
    with open(README_PATH, 'r', encoding='utf-8') as f:
        text = f.read()

    categories = [
        'Standalone Agentic IDEs',
        '1-Click Editor Extensions',
        'Terminal & CLI Pair Programmers',
        'Running Agents in Parallel',
        'Model Context Protocol (MCP) Servers for Coding',
        'Top Open-Weight Coding Models',
        'Local Execution Engines (Private & Offline)',
        'Automated Testing, QA & Code Review',
        'Autonomous Software Engineers (SWE-bench)'
    ]

    extracted = []
    for cat in categories:
        pattern = rf'### (?:.*?\s)?{re.escape(cat)}.*?\n(.*?)(?=\n### |\n## |\n---|\Z)'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            for line in match.group(1).split('\n'):
                line = line.strip()
                if line.startswith('- ['):
                    m = re.match(r'- \[([^\]]+)\]\(([^)]+)\)\s*[-—–]\s*(.*)', line)
                    if m:
                        extracted.append({
                            'name': m.group(1).strip(),
                            'url': m.group(2).strip(),
                            'category': cat,
                            'description': m.group(3).strip()
                        })

    print(f'Total tools validated across core categories: {len(extracted)}')
    assert len(extracted) >= 50, f'Expected >= 50 tools, found {len(extracted)}'

    # Check that URLs use https
    insecure = [t for t in extracted if not t['url'].startswith('https://')]
    if insecure:
        print(f'WARNING: Found non-HTTPS URLs: {insecure}')
    else:
        print('All tool URLs use secure HTTPS.')

    # Sync tools.json
    payload = {
        'schemaVersion': 1,
        'toolCount': len(extracted),
        'tools': extracted
    }
    with open(TOOLS_JSON, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    print(f'Synchronized {TOOLS_JSON} successfully.')

if __name__ == '__main__':
    main()
