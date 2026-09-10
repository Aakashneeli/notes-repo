# Instructor validation — 2026-09-10

This records teaching-material quality, never learner mastery. All learner progress remains unassessed.

## Verified

- 32 HTML pages: 28 lesson pages, three printable references and the study desk. All 459 local HTML links and anchors resolve; Markdown links also resolve. Every HTML page has a viewport declaration, a heading and the shared stylesheet.
- 44 recognizable shell code blocks pass `bash -n` without executing their mutations. Supplied Python files compile.
- Eleven worked Python traces were executed and matched their documented output exactly. All 30 beginner checks pass against the answers disclosed in lessons 18–21.
- The completed greeting example passes its two tests. Success, blank argument, omitted argument and help command paths were exercised.
- Terminal checks cover relative/absolute reads, head/tail, content and filename search, dummy environment inheritance and permission mode 600. GNU/Bash command help was consulted.
- Staging, conflict resolution, local clone/push/fetch/pull and fresh-clone rehearsals passed in disposable repositories under this workspace. No learner Git history was created.
- `uv sync --locked` succeeds with Python 3.14.7 and uv 0.12.10. Dependencies and the editable package install correctly. The first restricted download failed; the authorized network retry succeeded. The cache is inside `.validation/`.
- All 41 project checks pass in a separate disposable instructor implementation and again from its fresh clone. Those instructor implementations and repositories were removed afterward.
- The unchanged learner starter deliberately produces **30 failures and 11 passes**: failures arise from unfinished core functions; passing cases check supplied argument parsing and read-error handling. The beginner starter reports **0/30 with TODO feedback**. These are expected starting results.
- Shared quiz code was checked for unanswered, incorrect and correct selections. Print behavior was checked for opening answer disclosures and restoring their previous state. Neither component records learning progress.

## Limits

The browser preview connection reports no available browser. No desktop/mobile screenshots or printed-page visual inspection are claimed. The HTML has shared responsive rules, scrollable code/tables, focus states, long-path wrapping, and A4 print styles; print disclosures have a CSS fallback plus before/after-print behavior.

Tests prove supplied cases, not every possible input. In particular, the suite does not claim exhaustive filesystem permissions/platform behavior or concurrent filesystem changes. JSON follows Python's documented defaults; log input uses text newline normalization. Read the project's precise boundaries.

External primary sources are linked in RESOURCES and lessons. This is not a comprehensive availability check of every external URL.

## Recheck the workspace

From the course root:

```bash
python maintenance/verify_workspace.py
```

The verifier reads links and syntax; it does not run learner code, change files or update progress. Its source explains its HTML parser and shell syntax checks. Development caches, environments and temporary QA outputs are ignored. No existing file in `os-python-tooling` was edited.
