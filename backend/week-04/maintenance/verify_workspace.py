"""Read-only standard-library checks for teaching artifacts, not learner mastery."""
import argparse
import ast
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".venv", "__pycache__", ".pytest_cache", ".ruff_cache"}


def supplied_files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and not any(x in IGNORED or x.endswith(".egg-info") for x in p.parts))


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.mapped = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for name in ("href", "src"):
            if name in a:
                self.links.append(a[name])
        if "id" in a:
            self.ids.add(a["id"])
        if "data-file" in a:
            self.mapped.add(a["data-file"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Author audit: also reject unmapped new files")
    args = parser.parse_args()
    files = supplied_files()
    problems = []
    count = 0
    for p in files:
        if p.suffix == ".py":
            ast.parse(p.read_text(), filename=str(p))
        if p.suffix == ".json":
            json.loads(p.read_text())
        if p.suffix not in {".html", ".md"}:
            continue
        doc = p.read_text()
        if p.suffix == ".html":
            parser = Links()
            parser.feed(doc)
            links = parser.links
            if 'name="viewport"' not in doc or 'lang="en"' not in doc:
                problems.append(f"Missing responsive/language metadata: {p}")
        else:
            links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", doc)
        for link in links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (p.parent / unquote(url.path)).resolve() if url.path else p
            count += 1
            if not target.exists():
                problems.append(f"Broken link in {p.relative_to(ROOT)}: {link}")
            elif url.fragment and target.suffix == ".html":
                dest = Links()
                dest.feed(target.read_text())
                if unquote(url.fragment) not in dest.ids:
                    problems.append(f"Missing anchor in {p}: {link}")
    guide = Links()
    guide.feed((ROOT / "plan/file-map.html").read_text())
    actual = {str(p.relative_to(ROOT)) for p in files}
    extra = actual - guide.mapped
    stale = guide.mapped - actual
    if stale or (args.strict and extra):
        problems.append(f"Map missing={sorted(extra)}; stale={sorted(stale)}")
    elif extra:
        print(f"Additional learner files (link from project README): {sorted(extra)}")
    collection = json.loads((ROOT / "projects/task-api/postman/task-api.starter.postman_collection.json").read_text())
    assert collection["info"]["schema"].endswith("/v2.1.0/collection.json")
    assert len(collection["item"]) == 11
    for item in collection["item"]:
        assert item["request"]["url"].startswith("{{base_url}}/")
        assert item["event"][0]["listen"] == "test"
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"PASS: {len(files)} supplied files, {count} local links, mapped-file coverage, Python syntax and JSON checks")
    print("No learner mastery, live Postman run, external link availability or visual correctness inferred.")


if __name__ == "__main__":
    main()
