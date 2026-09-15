"""Author local navigation, HTML anchors, file-map and basic artifact consistency."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EXCLUDED = {".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "artifacts"}


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            if name in attrs:
                self.links.append(attrs[name])


def main():
    errors = []
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and
                   not EXCLUDED.intersection(p.relative_to(ROOT).parts))
    for file in files:
        if file.suffix not in (".html", ".md", ".css"):
            continue
        text = file.read_text()
        if file.suffix == ".html":
            links = Page(text).links
            for required in ('lang="en"', 'name="viewport"', '<title>'):
                if required not in text:
                    errors.append(f"{file.relative_to(ROOT)}: missing {required}")
        elif file.suffix == ".md":
            links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', text)
        else:
            links = re.findall(r'url\(["\']?([^\)"\']+)', text)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file
            if not target.exists():
                errors.append(f"{file.relative_to(ROOT)} -> missing {link}")
            elif parsed.fragment and target.suffix == ".html":
                if unquote(parsed.fragment) not in Page(target.read_text()).ids:
                    errors.append(f"{file.relative_to(ROOT)} -> missing anchor {link}")
    catalog = json.loads((ROOT / "maintenance/catalog.json").read_text())
    mapped = {row["path"] for row in catalog}
    actual = {str(p.relative_to(ROOT)) for p in files}
    if mapped != actual:
        errors.append(f"file map mismatch: unmapped={sorted(actual-mapped)}, missing={sorted(mapped-actual)}")
    for row in catalog:
        lesson = ROOT / row["lesson"]
        if not lesson.exists():
            errors.append(f"missing first-use lesson for {row['path']}")
        elif row["path"] != row["lesson"] and row["path"] not in lesson.read_text() and Path(row["path"]).name not in lesson.read_text():
            errors.append(f"first-use lesson does not name {row['path']}")
    sample = ROOT / "projects/local-stack/data/hello.txt"
    if len(sample.read_text()) != 17:
        errors.append("sample character count differs from lesson/smoke contract")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Verified {len(files)} supplied files, local links/anchors and file introductions.")
    print("No learning or live-service claims follow from this static check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
