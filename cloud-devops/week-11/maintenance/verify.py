"""Tutor-maintained offline links/syntax/file-map check. Run from week root."""

import ast
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "generated"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.add(data["id"])
        for key in ("href", "src"):
            if key in data:
                self.links.append(data[key])


def files():
    return [
        p
        for p in ROOT.rglob("*")
        if p.is_file() and not any(part in SKIP for part in p.relative_to(ROOT).parts) and p.name != ".env"
    ]


def main():
    errors = []
    count = 0
    for path in files():
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
        links = []
        if path.suffix == ".html":
            page = Page()
            page.feed(path.read_text())
            links = page.links
            if "viewport" not in path.read_text() or 'lang="en"' not in path.read_text():
                errors.append(f"missing HTML metadata: {path}")
        elif path.suffix == ".md":
            links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text())
        elif path.suffix == ".css":
            links = re.findall(r'url\(["\x27]?([^)"\x27]+)', path.read_text())
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            count += 1
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing {link}")
            elif parsed.fragment and target.suffix == ".html":
                page = Page()
                page.feed(target.read_text())
                if unquote(parsed.fragment) not in page.ids:
                    errors.append(f"{path.relative_to(ROOT)}: missing anchor {link}")
    mapping = (ROOT / "plan/file-map.html").read_text()
    for path in files():
        rel = path.relative_to(ROOT).as_posix()
        if rel not in mapping:
            errors.append(f"unmapped file: {rel}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(files())} supplied files mapped; {count} local links; Python syntax")


if __name__ == "__main__":
    main()
