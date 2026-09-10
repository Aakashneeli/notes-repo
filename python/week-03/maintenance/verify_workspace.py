"""Read-only author checks; never complete learner files or mark progress.

Run from week root: python maintenance/verify_workspace.py
Generated caches/environment and unmodified upstream links are not learning content.
"""

import ast
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".venv", ".pytest_cache", ".ruff_cache", "__pycache__", ".git", "output"}


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.ids = set()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


def files():
    for folder, dirs, names in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in SKIP]
        for name in names:
            yield Path(folder) / name


def main():
    errors = []
    all_files = list(files())
    map_doc = Document((ROOT / "plan/file-map.html").read_text())
    mapped = {(ROOT / "plan" / urlsplit(link).path).resolve() for link in map_doc.links}
    for path in all_files:
        relative = path.relative_to(ROOT)
        # These files are intentionally created by the learner in lessons 9/11.
        learner_created = str(relative) in {
            "practice/async_attempt.py",
            "projects/text-workbench/module-diagram.drawio",
        }
        if path.resolve() not in mapped and not learner_created:
            errors.append(f"Unmapped file: {relative}")
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text())
            except SyntaxError as exc:
                errors.append(f"Syntax: {relative}: {exc}")
        # Preserve upstream documentation literally; validate our links TO it only.
        if "sampleproject" in relative.parts:
            continue
        if path.suffix not in {".html", ".md"}:
            continue
        source = path.read_text()
        if path.suffix == ".html":
            document = Document(source)
            links = document.links
            if 'lang="en"' not in source or 'name="viewport"' not in source:
                errors.append(f"Missing language/viewport: {relative}")
            if "h1" not in document.tags or "nav" not in document.tags:
                errors.append(f"Missing page title/navigation: {relative}")
        else:
            links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", source)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.exists():
                errors.append(f"Broken link: {relative} -> {link}")
            elif parsed.fragment and target.suffix == ".html":
                if parsed.fragment not in Document(target.read_text()).ids:
                    errors.append(f"Broken fragment: {relative} -> {link}")
    if errors:
        print("\n".join(errors))
        return 1
    print(
        f"PASS: {len(all_files)} supplied files mapped; local links, fragments, HTML essentials and Python syntax"
    )
    py = ROOT / "projects/text-workbench/.venv/bin/python"
    if not py.exists():
        print("NOT RUN: example tests; first follow lesson 2 environment setup")
        return 2
    result = subprocess.run(
        [
            str(py),
            "-m",
            "pytest",
            str(ROOT / "practice/test_examples.py"),
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT / "projects/text-workbench",
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if result.returncode:
        return result.returncode
    for argument, expected in [
        ([], ["A start", "B start", "A end", "B end"]),
        (["--blocking"], ["A start", "A end", "B start", "B end"]),
    ]:
        result = subprocess.run(
            [str(py), str(ROOT / "practice/async_demo.py"), *argument],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode or result.stdout.splitlines() != expected:
            print("FAIL: async observation", result.stdout, result.stderr)
            return 1
    print("PASS: completed teaching examples and two local async observations")
    starter_files = [
        ROOT / "practice/exercises.py",
        *(ROOT / "projects/text-workbench/src/text_workbench").glob("*.py"),
    ]
    pending = [
        str(p.relative_to(ROOT))
        for p in starter_files
        if "raise NotImplementedError" in p.read_text()
    ]
    print("Starter markers (informational, not a pass/fail assessment):", len(pending))
    print("Run project pytest separately to assess current behavior; no learner progress changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
