# Source mapping: numbered Week 03

Source: /home/an10/Downloads/ai-backend-roadmap.html, HTML anchor `week-3`.
Resolved 2026-09-10. Marker: **03 — Pro Python**.
Title: **Professional Python Structure, Pydantic, Logging, and Practical LLD**.
Workspace: `python/week-03/`. No Week 3 collision or naming exception exists.

Purpose: move from scripts to maintainable Python that supports backend and AI systems.
Rationale: type hints, Pydantic, dependency boundaries, config and imports precede FastAPI.

## Exact in-scope requirements (transcribed)

- Package layout: src, tests, modules, imports, public vs internal helpers.
- Type hints: unions, optionals, collection types, typed return values.
- Dataclasses vs Pydantic models: when each is useful.
- Config management: env vars, settings object, .env.example.
- Logging: levels, message structure, avoiding secrets in logs.
- Practical LLD: functions vs classes, service boundaries, dependency direction.
- Async basics: I/O-bound work, blocking calls, why FastAPI can be async.
- Build a small text-processing package that can split, normalize, and summarize text metadata.
- Add Pydantic validation for input config and output records.
- Add structured logging and a settings module.
- Add tests for normal cases, invalid input, empty files, and large files.
- Read one small Python repo and write an architecture note.
- Deliver a professional Python package repo with src layout.
- Deliver .env.example, README, tests, ruff, typed function signatures.
- Deliver one codebase-reading note: entrypoints, modules, tests, config.
- Deliver one draw.io/Excalidraw module diagram.
- Explain: Why did you split the code into these modules?
- Explain: Which functions are pure and which cause side effects?
- Explain: Where is configuration loaded, and why there?
- Explain: What would become hard to test if you moved code into the wrong layer?
- Resources: Pydantic docs (models/validation), Python logging docs,
  A Philosophy of Software Design (selected chapters on complexity and modules).

## Scope decisions

All DSA/NeetCode, algorithm interview exercises, complexity drills and their logs are
excluded by user instruction, including the source's Week 3 pointer/window practice.
Ordinary text collections remain. No detailed later-week lessons are provided.
Source Week 2 is Python Core; the existing python/week-02 instead teaches Foundation
under a historical explicit exception. It is preserved, not treated as proof of Python
Core mastery. Lessons 1 and 3 supply only the missing prerequisite bridges.
Source Week 4 introduces HTTP/FastAPI. This week prepares its Python boundaries only.
The source does not require extending an earlier app: the text package is new.

The source's separate-project-repo convention is adapted to an independently packaged
project directory inside this notes repo to honor the user's repository-only constraint.
Git tasks use this repository; no nested Git repository or publishing is required.
Specific text rules, size limit and CLI contract are teaching choices, not roadmap quotes.

Source HTML SHA-256 at resolution: `70466aa6c6ecb8ed7ca94c84882faa54f26147d180c9de17d5bf095fc945579e`.
