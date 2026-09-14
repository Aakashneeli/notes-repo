# Week 04 — FastAPI

**Source title:** HTTP, REST, FastAPI, API Design, Postman, and API Tests.
**Authority:** `/home/an10/Downloads/ai-backend-roadmap.html`, exact article `#week-4`.
**Workspace:** `backend/week-04/`; existing backend topic, no prior matching workspace or naming exception.
See [source extraction and sequence context](roadmap/source-week-04.md).

Open the [study desk](index.html), then [Lesson 1](lessons/0001-start-and-bridge.html).
Terminal starting directory: `/home/an10/code/notes-repo/backend/week-04`.
Lessons explicitly identify the few transitions into/out of the project directory.

## Main deliverables

- Learner-built in-memory Task CRUD API; validation, pagination, filtering, errors and API-key dependency.
- Router/schema/service separation, API tests for endpoints and negative cases.
- Learner-exported Postman collection with manual QA evidence.
- API README with curl examples/status behavior, request lifecycle note and sequence diagram.

## Use the workspace

[Sequence](plan/README.md) · [coverage](plan/coverage.md) · [all files and first uses](plan/file-map.html)
· [assessment](plan/assessment.md) · [progress](plan/progress.md) · [verification](VALIDATION.md).

Read lessons/reference; leave infrastructure intact; implement practice/exercises.py
and the learner-owned project modules. Append real evidence to weekly-logs/week-04.md
and codebase-reading/week-04.md. Main project code intentionally starts incomplete.
The two completed instructor example tests are separate from the unfinished drills/API.

Everything uses local dummy data. Install requires internet; serving/testing does not
require a paid service, account or GPU. Swagger's default assets can require internet.
Postman installation, import, actual runs, export and re-import remain learner actions.
No database, deployment, DSA or interview practice is taught here.

## Depth and pace

Lessons 3–12 now include expanded worked mechanisms, traces and debugging exercises.
Use two passes: understand/predict, then run/modify/explain. The completed mechanism
lab is separate from your Task API and introduces validation, state ownership and
dependency replacement before asking you to transfer those ideas. Pause between
sections; the lesson number is not a fixed sitting length.
