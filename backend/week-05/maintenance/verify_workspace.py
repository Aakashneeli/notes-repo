"""Tutor-maintained static checks. Run from weekly root; no database mutations."""
import ast
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
IGNORE = {".venv", ".local", "__pycache__", ".pytest_cache"}
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.files = set()
        self.title = False
        self.viewport = False
        self.lang = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.title |= tag == "title"
        self.viewport |= tag == "meta" and a.get("name") == "viewport"
        self.lang |= tag == "html" and a.get("lang") == "en"
        if "id" in a:
            self.ids.add(a["id"])
        if "data-file" in a:
            self.files.add(a["data-file"])
        for key in ("href", "src"):
            if key in a:
                self.links.append(a[key])

def files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and not (set(p.relative_to(ROOT).parts) & IGNORE))

def main():
    errors = []
    inventory = files()
    pages = {}
    for p in inventory:
        if p.suffix == ".html":
            page = Page()
            page.feed(p.read_text())
            pages[p] = page
            if not (page.title and page.viewport and page.lang):
                errors.append(f"Missing title/viewport/lang: {p.relative_to(ROOT)}")
        if p.suffix == ".py":
            ast.parse(p.read_text(), filename=str(p))
    for p in inventory:
        links = []
        if p.suffix == ".html":
            links = pages[p].links
        elif p.suffix == ".md":
            links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", p.read_text())
        elif p.suffix == ".css":
            links = re.findall(r'url\(["\x27]?([^)"\x27]+)', p.read_text())
        for link in links:
            u = urlsplit(link)
            if u.scheme or u.netloc:
                continue
            dest = (p.parent / unquote(u.path)).resolve() if u.path else p
            if not dest.is_relative_to(REPO):
                errors.append(f"Link escapes repository: {p}: {link}")
            elif not dest.exists():
                errors.append(f"Missing link: {p.relative_to(ROOT)} -> {link}")
            elif u.fragment and dest.suffix == ".html":
                page = pages.get(dest)
                if page is None:
                    page = Page()
                    page.feed(dest.read_text())
                if unquote(u.fragment) not in page.ids:
                    errors.append(f"Missing anchor: {p.relative_to(ROOT)} -> {link}")
    mapped = pages[ROOT / "plan/file-map.html"].files
    expected = {str(p.relative_to(ROOT)) for p in inventory}
    for path in sorted(expected - mapped):
        errors.append(f"Unmapped supplied file: {path}")
    for path in sorted(mapped - expected):
        errors.append(f"Map points to absent file: {path}")
    assert not errors, "\n".join(errors)
    print(f"PASS: {len(inventory)} supplied files; {len(pages)} HTML pages; local links, anchors, CSS imports, Python syntax and complete file map")
    print("LIMIT: no learner mastery, database behavior, external-link availability or visual layout is inferred.")

if __name__ == "__main__":
    main()
