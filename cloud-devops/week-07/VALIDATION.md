# Week 7 author verification

Prepared 2026-09-14; final checks completed 2026-09-15 (Asia/Kolkata). These are **material-quality checks**, not learner achievement. Progress and evidence templates remain unassessed.

## Source and preservation
- Read the roadmap's agreement, sequence context, numbered weeks, adjacent Week 6/8 sections, and relevant continuous reading/DevOps context. Exact Week 7 title, rationale, seven subtopic groups, five labs, four deliverables, four explain-backs and source-resource categories are mapped in plan/coverage.md.
- Inspected topic organization, shared CSS/print assets, existing missions/notes, the baseline learning record, earlier progress/logs and unfinished Week 6 code. Selected existing cloud-devops topic; no Week 7 conflict or numbering exception.
- Created only cloud-devops topic navigation and week-07 materials, plus an additive Week 7 entry in WORKSPACE-STRUCTURE.md. No earlier learner files, progress, Git index or history were changed by this task.

## Local Python checks — passed
Environment: CPython 3.12.14, FastAPI 0.141.1, Starlette 1.6.0, pytest 9.1.1, Ruff 0.16.7, psycopg 3.3.5, Redis client 7.4.1, RQ 2.12.0. Full dependency versions are in requirements.lock.

Commands below start in cloud-devops/week-07:

```bash
.venv/bin/python -m pytest -q practice/test_mechanisms.py maintenance/test_fixture.py maintenance/test_checks.py
.venv/bin/python -m ruff check .
.venv/bin/python -m compileall -q practice projects/local-stack maintenance
.venv/bin/python practice/mechanisms.py
.venv/bin/python maintenance/verify.py
```

- 13 supplied example/fixture/checker tests passed. Readiness examples exercise empty/mixed/true inputs; demo HTTP middleware preserves an error response and adds a header. Fixture tests exercise auth, size, empty/invalid UTF-8, pending status and missing jobs. Checker tests accept small valid rule fragments and reject meaningful configuration mistakes; they do not contain a solved main stack.
- Ruff and compilation passed. Example output: `503`, then `{"event": "example", "method": "GET", "status": 503}`.
- Two upstream deprecation warnings remain: Starlette's httpx TestClient compatibility and the AnyIO BlockingPortal alias. They did not prevent tests passing with the resolved lock. A future dependency refresh should recheck them rather than hide warnings.
- Initial sandbox TestClient runs stalled because local event-loop sockets were restricted; those runs were interrupted and rerun successfully outside the sandbox. This is distinct from an exercise failure.
- The repository-local .venv is backed by a generated Python interpreter under ignored artifacts/python, not /tmp. Both are local generated artifacts and excluded from the learning file map and Git. A fresh clone needs its own Python 3.12 only for host-side checks; container startup does not need a host venv. Installing packages initially required network access.

## Expected learner failures — confirmed
- Default `.venv/bin/python -m pytest -q`: **14 failed, 5 passed**. All 14 failures are the explicitly unfinished project/exercise functions raising NotImplementedError. No assertion was weakened and no learner solution was inserted.
- `.venv/bin/python maintenance/check_project.py`: **21 unfinished configuration requirements**. Empty Dockerfile/Compose/workflow starters are intentional. The structural gate is a convenience, not a Dockerfile interpreter, full Actions validator, semantic middleware audit or live integration test.
- Docker Compose parsed both the completed two-service example and the incomplete main mapping. A successful parse of `services: {}` does not prove syllabus completion.

## Live author checks — passed, with narrow boundaries
Docker Engine/client 29.7.2 and Compose 5.5.1. Initial daemon denial was confined to the sandbox; the host daemon was accessible for authorized checks. No daemon settings or socket permissions were changed.

1. Built the completed practice/tiny-image Dockerfile as isolated author tag `week7-author-hello:20260914`. Runs printed `hello reader` and, with LESSON_NAME=builder, `hello builder`.
2. Ran practice/two-services.yaml under isolated project `week7-author-network-20260914`: the client resolved cache and returned **PONG**. Its temporary containers/network were stopped and removed using project-scoped down; no learner volumes were used.
3. Exercised only the **supplied prerequisite fixture** against disposable PostgreSQL, Redis and Qdrant containers. The API router ran in TestClient and the RQ worker ran as a real separate host process using the repository environment. POST accepted the sample, the database showed pending, the worker changed it to completed with **17 characters**, repeated extraction left the result unchanged, wrong auth returned 401 and wrong type returned 415. Postgres/Redis probes returned true; Qdrant /readyz was reachable. Disposable database/vector storage and only newly created containers were used and stopped afterward.

Observed image digests:
- python:3.12-slim — sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea
- postgres:16-alpine — sha256:cf78e76683b9ca8c5733cbbdce6c9262b45b6767934dd0a95e671f9a0fc20685
- redis:7-alpine — sha256:ff02b58f971e7d7d156a1267e283fcbbeee91773b6aa36c49dac28ecfe28eadf
- qdrant/qdrant:v1.13.6 — sha256:bd67306b6cc77c98122cada2321eb60b20d00b19d26cb61c86681e7bd5951498

These checks **do not verify the learner's five-service Compose topology**, containerized API image, middleware implementation, health policy, startup gates, named-volume persistence/recreation, dependency-fault runbook or fresh-clone behavior. Those remain intentional learner tasks with explicit contracts and live checks. The prerequisite fixture has narrower storage/recovery behavior than Week 6; see bridge-notes.md.

Docker retains downloaded images/build cache for the example runs. No unrelated containers, images, volumes or data were pruned.

## Navigation and visual checks — passed
- 76 supplied files mapped to first relevant lessons and actions. Local HTML/Markdown/CSS links and HTML fragment targets resolve; the sample length agrees with lessons and smoke checks. Generated environments/caches/artifacts are excluded by category.
- Headless Chromium checked all 17 HTML pages (desk, 13 lessons, two references, file map) at 1280px and 390px: **34 page/viewport checks**, no page-level horizontal overflow and no failed local asset requests.
- Inspected rendered mobile desk, desktop middleware lesson and a middleware print-page image. Generated an A4 middleware print PDF and verified expanded answer text in extracted output. Print spacing was tightened after spotting an almost-empty trailing page, then rerendered. Not every lesson's printed page was individually inspected; no screen-reader or physical-printer test was performed.
- Shared style and print-helper paths were verified without altering the earlier week's files. Keyboard-focus styles, skip links and an accessible scroll region support navigation; browser checks do not constitute a full accessibility audit.

## Teaching sufficiency review — separate from coverage and code
Reviewed each lesson for a specific outcome, vocabulary at first use, a worked trace/expected result, a relevant failure, supported practice and an independent variation. The hardest transitions were explicitly bridged: build context versus file location; host interpolation versus runtime environment; process startup versus dependency readiness; liveness versus business completion; JSON serialization versus logger plumbing; response errors versus raised exceptions; run-step working directory versus checkout location.

Density is split across thirteen lessons; full stack startup is explicitly deferred until health/logging hooks exist. Progressive answer disclosures support small beginner exercises without shipping the assessed implementation. Evidence destinations, paths and folder ownership are taught in lessons and checked against the file map. Repeated recall after roughly two days/one week is scheduled; no mastery is inferred.

## Remaining verification limits
No finished learner project, committed fresh-clone trial, hosted GitHub Actions run, deployment, cloud integration, GPU/model service, screen-reader session or learner assessment occurred. A hosted CI result needs the learner's repository, reviewed installation and actual run/commit evidence. Local/author tests cannot stand in for that. No external account settings, messages, publishing or paid provisioning were performed.
