"""Read-only author checks. Run from any directory; no learner completion claim."""
import ast
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if 'id' in attrs:
            self.ids.append(attrs['id'])


def main():
    files = [p for p in ROOT.rglob('*') if p.is_file()
             and not any(x in p.parts for x in ('__pycache__', 'runtime', '.venv'))]
    file_map = (ROOT / 'plan/file-map.md').read_text()
    checked = 0
    for path in files:
        relative = str(path.relative_to(ROOT))
        assert f'({"../" + relative})' in file_map, f'Unmapped file: {relative}'
        if path.suffix == '.py':
            ast.parse(path.read_text(), filename=str(path))
        if path.suffix not in ('.html', '.md', '.css'):
            continue
        text = path.read_text()
        parser = Links()
        if path.suffix == '.html':
            parser.feed(text)
            assert len(parser.ids) == len(set(parser.ids)), f'Duplicate id: {path}'
            assert '<html lang="en">' in text and 'name="viewport"' in text
            assert '<h1>' in text and 'rel="stylesheet"' in text
            links = parser.links
        elif path.suffix == '.md':
            links = re.findall(r'\]\(([^)]+)\)', text)
        else:
            links = re.findall(r'url\([\"\x27]?([^\"\x27)]+)', text)
        for link in links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(REPO), f'Link escapes repo: {path}: {link}'
            assert target.exists(), f'Broken link: {path}: {link}'
            if url.fragment and target.suffix == '.html':
                target_parser = Links()
                target_parser.feed(target.read_text())
                assert unquote(url.fragment) in target_parser.ids, f'Broken anchor: {link}'
            checked += 1
    diagram = ET.parse(ROOT / 'projects/architecture-review/diagrams/architecture.drawio')
    assert [p.attrib['name'] for p in diagram.findall('diagram')] == [
        'Context', 'Containers', 'Sequence', 'Data flow', 'Deployment']
    for page in diagram.findall('diagram'):
        assert page.find('mxGraphModel/root') is not None
    lessons = sorted((ROOT / 'lessons').glob('*.html'))
    assert len(lessons) == 13
    for path in lessons:
        text = path.read_text()
        assert 'Primary reading:' in text and 'follow-up' in text
        assert 'id="materials"' in text
        assert 'Next lesson' in text or 'Assessment' in text
    print(f'PASS: {len(files)} files mapped; {checked} local links/anchors; 13 lessons; 5 diagram pages; Python syntax')
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s',
                    str(ROOT / 'maintenance'), '-p', 'test_infrastructure.py', '-v'], check=True)
    print('Author infrastructure passed. Learner implementation and assessment remain separate.')


if __name__ == '__main__':
    main()
