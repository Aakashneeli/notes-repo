# Author verification — 2026-09-14

This is tutor evidence about supplied materials, not learner mastery. Source mapping:
TARGET_WEEK=6 → /home/an10/Downloads/ai-backend-roadmap.html#week-6 →
Backend Architecture, Auth, Security Basics, File Ingestion, Redis, and Jobs → backend/week-06/.

## Runnable results
From the weekly root:
- `uv sync --locked`: resolved environment and lock verified. Python 3.14.7, uv 0.12.10;
  FastAPI 0.141.1, Starlette 1.6.0, Pydantic 2.13.5, python-multipart 0.0.32,
  pytest 9.1.1, HTTPX 0.28.1. Optional RQ 2.12.0 / Redis client 7.4.1 installed for API checks.
- `uv run pytest practice/test_examples.py maintenance/test_author_checks.py -q`:
  **18 passed** (12 completed-example/fixture checks and 6 checker-quality checks).
  Verified bytes and exact limits, auth rejection without task effects, background ordering,
  multipart parsing, response schema, settings, state edges, SQLite persistence/parameter binding/
  atomic sequential claim, sample counts, and explained beginner answers in isolated patches.
  Deliberately wrong unbounded reads, auth bypass, permissive state graph, empty text acceptance
  and unlimited retries were rejected by the checks. Learner files were never filled in.
- `uv run python practice/examples.py`: expected b'abcd', then True False.
  hello.txt is 34 bytes/characters and five words; sample count also tested.
- `uv run pytest practice/test_exercises.py projects/ingestion/tests -q`:
  **8 expected failures and 15 expected setup errors**, all due to unfinished learner code.
  Five beginner cases remain TODOs; the main project has three direct TODO-related failures
  and fifteen router-factory setup errors. No xfail/skip masks the unfinished implementation.
  Fixed a false positive where broad RuntimeError matching accepted NotImplementedError:
  the compensation check now requires the simulated metadata failure message.
- RQ imports and `uv run --locked --extra rq rq worker --help` verified from practice/;
  --url and --with-scheduler supported. Optional commands retain --extra rq so uv can select it.
- Five local Postman requests/environment parse as JSON; test JavaScript compiles. Requests
  use the local base_url variable, cover upload, missing/invalid auth, invalid file and status.
  This does not prove import/run behavior in the Postman application.

The restricted sandbox hung at TestClient's local async/thread coordination and prevented
Chromium startup. Scoped verification reruns outside it succeeded; the hanging run was stopped.
Dependency fetching also needed permitted network access. No application code workaround was added.
The suite emits two dependency deprecation warnings (HTTPX TestClient integration and AnyIO
BlockingPortal alias). Current locked behavior passes; warnings were not suppressed.

## Navigation and presentation
`python maintenance/verify.py`: **70 supplied files mapped**, HTML links/anchors and local CSS
imports resolve; Markdown file links, Python syntax, JSON and lesson catalog checked.
The unsupported sample invalid.html is test data, not an HTML study page. Environments, caches,
ignored .env and runtime output are categorized in lessons rather than mapped file by file.
Topic README/index link Week 6; earlier weeks and existing learner work were preserved.

Headless Chromium checked **all 17 study HTML pages at 1280px and 390px**: one main heading,
expected local stylesheet loaded, no document-width overflow. Sampled study desk, upload lesson,
RQ lesson and file map screenshots were generated; mobile desk and desktop upload lesson were
visually inspected. Disclosure opening was checked. A representative upload lesson printed to A4;
its first page was visually inspected and extracted print text confirmed hints/answers are present.
Not every printed page or assistive technology was visually/manually audited. Screenshots/PDF were
temporary QA output under /tmp, not new learner deliverables. Local links are checked statically;
Markdown rendering depends on the learner's browser/editor.

## Teaching sufficiency review (separate from tests and coverage)
- Lessons 1–4 provide baseline probes, conditional bridges, package/data-flow traces,
  dependency execution and beginner logging practice before project auth work.
- Lessons 5–7 add byte accumulation, a runnable multipart preview, safe-write reasoning,
  partial failure, parameter binding and claim traces before integration.
- Lessons 8–11 distinguish the five domain states, retry classification, repeat effects,
  process lifetime and response-schema validation before independent assembly.
- Lessons 12–13 connect client observations to security evidence, manual QA, code reading,
  debugging, explain-back, variation, Git review and delayed retrieval.
Each lesson includes an outcome, failure reasoning, action/check/evidence path and independent
variation. Beginner answers use disclosures; main implementation and assessed design notes remain
learner-owned. File-map entries were reviewed against first-use lesson instructions.
See plan/coverage.md for requirement coverage, separately from this teaching review.

## Practical limits
No completed learner ingestion implementation was fabricated for a positive full-project run.
Contract tests are collected and inspected, but their full positive end-to-end path must be
verified against the learner's implementation. TestClient results do not prove real response timing,
worker-kill recovery, durable dispatch, production security or PostgreSQL behavior.
Redis server/CLI are absent, so live Redis/RQ processing/retries were not performed. The roadmap's
required chosen path is BackgroundTasks plus a substantive learner RQ migration note; live RQ is optional.
No live S3, Postman GUI, published service, cloud provisioning, account changes, messages or Git
commit were performed. No mastery or progress checkbox was recorded as completed.
