"""Read-only author check. Run from the weekly root: python maintenance/verify.py.
Checks HTML links/anchors, local CSS imports, catalog and exact file-map coverage.
Does not execute learner work, mark mastery, or verify external services.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import ast
import json
import re
ROOT=Path(__file__).resolve().parents[1]
IGNORE={'.venv','__pycache__','.pytest_cache','.uv-cache','runtime'}
def supplied():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not any(part in IGNORE for part in p.relative_to(ROOT).parts)
                  and p.name != '.env')
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.refs=[]; self.ids=set(); self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href','src'):
            if key in attrs: self.refs.append(attrs[key])
errors=[]
files=supplied()
for path in files:
    if path.suffix=='.py': ast.parse(path.read_text(),filename=str(path))
    if path.suffix=='.json': json.loads(path.read_text())
    if path.suffix=='.md':
        for ref in re.findall(r'\[[^\]]+\]\(([^)]+)\)',path.read_text()):
            u=urlsplit(ref)
            if not u.scheme and not u.netloc and u.path and not (path.parent/unquote(u.path)).resolve().is_file():
                errors.append(f'{path.relative_to(ROOT)} -> missing Markdown target {ref}')
    if path.suffix=='.html' and 'data' not in path.relative_to(ROOT).parts:
        page=Page(path.read_text())
        for ref in page.refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc: continue
            target=(path.parent/unquote(u.path)).resolve() if u.path else path
            if not target.is_file(): errors.append(f'{path.relative_to(ROOT)} -> missing {ref}')
            elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in Page(target.read_text()).ids:
                errors.append(f'{path.name} -> missing anchor {ref}')
        if 'name="viewport"' not in path.read_text(): errors.append(f'No viewport: {path}')
        if 'lang="en"' not in path.read_text(): errors.append(f'No language: {path}')
    if path.suffix=='.css':
        for ref in re.findall(r'url\(["\']?([^"\')]+)',path.read_text()):
            if not urlsplit(ref).scheme and not (path.parent/ref).resolve().is_file():
                errors.append(f'Broken CSS import: {ref}')
map_page=Page((ROOT/'plan/file-map.html').read_text())
mapped={(ROOT/'plan'/urlsplit(ref).path).resolve() for ref in map_page.refs
        if not urlsplit(ref).scheme and urlsplit(ref).path}
for path in files:
    if path.resolve() not in mapped: errors.append(f'Unmapped: {path.relative_to(ROOT)}')
for row in json.loads((ROOT/'maintenance/lesson-catalog.json').read_text()):
    if not (ROOT/'lessons'/row['file']).is_file(): errors.append(f'Catalog missing lesson: {row}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(files)} supplied files mapped; HTML links/anchors, local CSS, Python syntax, JSON and catalog checked.')
