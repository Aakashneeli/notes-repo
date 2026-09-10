"""Read-only link, structure, Python syntax and shell-snippet checks.

Run from any directory: python /path/to/week-01/maintenance/verify_workspace.py
This verifies teaching material, never learner mastery. It does not execute
lesson commands or learner code. HTMLParser extracts actual links and code;
bash -n parses recognizable shell blocks without performing their actions.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = []
        self.blocks = []
        self.in_pre = False
        self.block = ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs:
                self.links.append(attrs[attr])
        if tag == 'pre':
            self.in_pre = True
            self.block = ''

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.blocks.append(self.block)
            self.in_pre = False

    def handle_data(self, data):
        if self.in_pre:
            self.block += data


def main():
    documents = {p: Document(p.read_text()) for p in ROOT.rglob('*.html')
                 if not any(x.startswith('.') for x in p.relative_to(ROOT).parts)}
    failures = []
    links = 0
    shell_blocks = 0
    for path, doc in documents.items():
        text = path.read_text()
        if len(doc.ids) != len(set(doc.ids)):
            failures.append(f'{path}: duplicate ids')
        for needed in ('<h1>', 'name="viewport"', 'course.css'):
            if needed not in text:
                failures.append(f'{path}: missing {needed}')
        for link in doc.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            links += 1
            if not target.exists():
                failures.append(f'{path.relative_to(ROOT)}: missing {link}')
            elif parsed.fragment and target.suffix == '.html':
                target_doc = documents.get(target) or Document(target.read_text())
                if unquote(parsed.fragment) not in target_doc.ids:
                    failures.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
        for block in doc.blocks:
            first = block.strip().splitlines()[0] if block.strip() else ''
            if re.match(r'^(cd |python |uv |git |cat |cp |printf |export |rg |mkdir |command )', first):
                result = subprocess.run(['bash', '-n'], input=block, text=True, capture_output=True)
                shell_blocks += 1
                if result.returncode:
                    failures.append(f'{path.name}: shell syntax: {result.stderr.strip()}')
    for path in ROOT.rglob('*.py'):
        if any(x.startswith('.') or x == '__pycache__' for x in path.relative_to(ROOT).parts):
            continue
        try:
            compile(path.read_text(), str(path), 'exec')
        except SyntaxError as error:
            failures.append(str(error))
    for path in ROOT.rglob('*.md'):
        if any(x.startswith('.') for x in path.relative_to(ROOT).parts):
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if urlsplit(link).scheme or link.startswith('#'):
                continue
            if not (path.parent / unquote(link.split('#')[0])).exists():
                failures.append(f'{path.relative_to(ROOT)}: missing Markdown link {link}')
    for failure in failures:
        print('FIX', failure)
    print(f'{len(documents)} HTML pages; {links} local HTML links; {shell_blocks} shell blocks parsed; {len(failures)} errors.')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
