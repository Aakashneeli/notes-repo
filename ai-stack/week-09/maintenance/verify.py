"""Read-only audit: syntax, local HTML/Markdown/CSS links and file-map coverage."""
import ast
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parents[1]
IGNORED={'.venv','.model-venv','runtime','__pycache__','.pytest_cache'}
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.ids=set(); self.lang=False; self.viewport=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ('href','src'):
            if key in a: self.refs.append(a[key])
        if 'id' in a: self.ids.add(a['id'])
        if tag=='html' and a.get('lang'): self.lang=True
        if tag=='meta' and a.get('name')=='viewport': self.viewport=True

def audit():
    files=[p for p in ROOT.rglob('*') if p.is_file() and not any(s in IGNORED for s in p.relative_to(ROOT).parts)]
    errors=[]; links=0; pages={}
    def page(p):
        if p not in pages:
            parser=Page();parser.feed(p.read_text());pages[p]=parser
        return pages[p]
    for p in files:
        refs=[]
        if p.suffix=='.py': ast.parse(p.read_text(),filename=str(p))
        if p.suffix=='.html':
            parsed=page(p);refs=parsed.refs
            if not parsed.lang or not parsed.viewport: errors.append(f'{p}: missing lang/viewport')
        if p.suffix=='.md': refs=re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text())
        if p.suffix=='.css': refs=re.findall(r'url\(["\']?([^"\')]+)',p.read_text())
        for ref in refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc: continue
            links+=1;dest=(p.parent/unquote(u.path)).resolve() if u.path else p
            if not dest.exists(): errors.append(f'{p.relative_to(ROOT)} -> missing {ref}')
            elif u.fragment and dest.suffix=='.html' and unquote(u.fragment) not in page(dest).ids:
                errors.append(f'{p.relative_to(ROOT)} -> missing anchor {ref}')
    mapped={str((ROOT/'plan'/urlsplit(r).path).resolve()) for r in page(ROOT/'plan/file-map.html').refs if not urlsplit(r).scheme}
    for p in files:
        if p.parent.name=='lessons': continue
        if str(p.resolve()) not in mapped: errors.append(f'Unmapped supplied file: {p.relative_to(ROOT)}')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(files)} supplied files, {links} local links, Python syntax, HTML anchors and file-map coverage')
if __name__=='__main__':audit()
