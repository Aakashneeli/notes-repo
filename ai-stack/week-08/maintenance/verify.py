"""Read-only course navigation/map/syntax verification. Run from weekly root."""
import ast
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".venv", ".cache", "runtime", "__pycache__", ".pytest_cache"}
LEARNER_OUTPUTS = {
    "projects/manual-rag/tests/test_variations.py",
    "projects/manual-rag/run_semantic.py",
    "projects/manual-rag/data/golden.json",
}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("href","src"):
            if k in a:
                self.links.append(a[k])

def main():
    files=[p for p in ROOT.rglob("*") if p.is_file() and not (set(p.relative_to(ROOT).parts)&SKIP)]
    pages={}
    errors=[]
    for p in files:
        if p.suffix==".html":
            page=Page()
            page.feed(p.read_text())
            pages[p.resolve()]=page
            text=p.read_text()
            for required in ['lang="en"','name="viewport"','<title>','stylesheet']:
                if required not in text:
                    errors.append(f"{p}: missing {required}")
        if p.suffix==".py":
            ast.parse(p.read_text(),filename=str(p))
        if p.suffix==".json":
            json.loads(p.read_text())
    for p in files:
        if p.suffix==".html":
            links=pages[p.resolve()].links
        elif p.suffix==".md":
            links=re.findall(r"\]\(([^)]+)\)",p.read_text())
        elif p.suffix==".css":
            links=re.findall(r'url\(["\']?([^"\')]+)',p.read_text())
        else:
            continue
        for url in links:
            part=urlsplit(url)
            if part.scheme or part.netloc:
                continue
            target=(p.parent/unquote(part.path)).resolve() if part.path else p.resolve()
            if not target.exists():
                errors.append(f"{p.relative_to(ROOT)}: missing {url}")
            elif part.fragment and target.suffix==".html":
                if target not in pages:
                    parsed=Page()
                    parsed.feed(target.read_text())
                    pages[target]=parsed
                if unquote(part.fragment) not in pages[target].ids:
                    errors.append(f"{p.relative_to(ROOT)}: missing anchor {url}")
    filemap=(ROOT/"plan/file-map.html").read_text()
    mapped=set(re.findall(r'data-file="([^"]+)"',filemap))
    actual={str(p.relative_to(ROOT)) for p in files}
    # Future learner artifacts are not tutor-supplied inventory; report separately.
    missing=actual-mapped-LEARNER_OUTPUTS
    if missing:
        errors.append("Files without map entry: "+", ".join(sorted(missing)))
    stale=mapped-actual
    if stale:
        errors.append("Map entries without file: "+", ".join(sorted(stale)))
    for item in errors:
        print(item)
    if errors:
        raise SystemExit(1)
    print(f"PASS: {len(files)} supplied files, HTML/Markdown/CSS local links, anchors, Python/JSON syntax, file map.")
    print("No live service, browser layout, learner mastery or semantic quality asserted.")

if __name__=="__main__":
    main()
