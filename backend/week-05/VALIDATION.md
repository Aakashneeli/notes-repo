# Author verification — 2026-09-14

Tutor-maintained evidence, never learner completion. Exact source mapping:
Week 5, article week-5, PostgreSQL, SQL, SQLAlchemy/SQLModel, Alembic, and Data Modeling,
workspace backend/week-05. Earlier work was preserved.

## Environment
Python 3.14.7; PostgreSQL client/server 18.6; SQLAlchemy 2.0.52;
psycopg 3.3.5; Alembic 1.20.0; FastAPI 0.141.1; Pydantic 2.13.5;
pytest 9.1.1; httpx 0.28.1; uvicorn 0.53.0. Exact resolutions are in uv.lock.
uv sync completed; uv sync --locked --offline subsequently passed.
Official PostgreSQL, SQLAlchemy, Alembic, FastAPI and Git documentation was checked.

## Verified
- Static audit: 74 supplied files, 18 HTML pages; all local HTML/Markdown links,
  anchors, CSS imports and Python syntax pass. Every file is in plan/file-map.html.
  Lesson starting directories and project paths were reviewed against the real tree.
  Git whitespace check passes. Topic README/index and shared organization link Week 5.
- Seven completed-example checks pass: label mapping/session trace, label CRUD/page
  trace, PostgreSQL left-join counts, partial-write rollback, parameter-as-data,
  selective index plan, and two-connection increment/unique-conflict behavior.
- All twenty SQL lab expected results were independently executed on temporary sample
  tables. No answers were saved into the learner's queries.sql or sql-notes.md.
  worked.sql and index-lab.sql ran through psql successfully; blank queries.sql
  executes setup/rollback safely but does not satisfy the query deliverable.
- Correct beginner query implementations were injected in memory for author checks:
  both accepted. Missing-filter and COUNT(*) mutations were rejected.
  Learner exercises.py remains unchanged and raises two expected NotImplementedErrors.
- Completed label migrations were applied to a fresh w5_demo, with a row inserted before
  the second revision. Required color became gray; current reported demo2.
  Downgrade retained name but removed color; re-upgrade lost a customized blue value
  and restored gray, matching the lesson's loss warning. Revision template renders
  valid Python; the lesson's ORM reference/relationship declarations configure.
- All eleven project tests collect and enter real PostgreSQL isolation setup.
  They stop with EXPECTED STARTER: missing learner migration history. Each temporary
  schema was cleaned up. They are not reported as passing implementation tests.
- Minimal HTTP bridge checked separately: health, missing key, read-only denial,
  invalid title, omitted-vs-false PATCH handling. A valid create reaches the unfinished
  repository and fails as expected. This is not PostgreSQL-backed API completion.
- Chromium layout checks visited all 18 HTML pages at 390px and 1440px widths with
  no document-wide horizontal overflow. Mobile desk and desktop session lesson
  screenshots were visually inspected. A four-page A4 session-lesson PDF was generated
  with disclosures expanded; its first rendered page was visually inspected.
  Generated screenshots/print sample remain ignored under .local/qa/.

## Teaching sufficiency review (separate from test correctness)
Reviewed each lesson for a mechanism explanation, worked trace, failure case,
guided attempt, feedback, reduced-help variation, evidence destination and next step.
Added explicit ORM count/page/update/delete teaching before repository implementation,
table-constraint/relationship syntax before modeling, and the migration demo before
learner revisions. Moved the concurrency table to w5_test so Alembic's dev-schema
comparison cannot propose removing it. Dense session/migration lessons have stopping
points and can span sittings. This is author review, not measured learner comprehension.

## Limits and remaining learner work
- Models, repository, Task migrations, 20 query attempts, schema diagram, actual
  migration/design decisions, regression/concurrency tests and explain-back remain
  learner-owned and unfinished. No learner progress boxes or mastery records were filled.
- The project contract suite has not passed against a finished Task implementation;
  such an implementation was deliberately not hidden in the scaffolding.
- Author database used an isolated container with temporary storage. Real PostgreSQL
  behavior was tested, but the learner's persistent bind-mount setup, API restart
  durability and personal draw.io/Excalidraw save/export workflow remain learner actions.
  No cloud, deployment, external-account or live remote-service test was performed.
- Browser overflow was checked for every page, but not every page was visually inspected
  in full. Only one lesson was print-rendered and its first page visually inspected;
  physical printing, other browsers, keyboard-only and screen-reader audits were not run.
- Current Starlette emits a deprecation warning about httpx in TestClient (and its
  AnyIO portal alias); the declared combination works in the executed bridge checks.
  It is recorded rather than suppressed. Keep the lockfile during study.
- Sandbox restrictions initially blocked dependency downloads, loopback PostgreSQL,
  and Chromium/TestClient. Scoped author checks succeeded outside those restrictions.
  A psycopg raw-percent placeholder defect was found and fixed using SQLAlchemy text().

## Author environment cleanup
Stopped notes-week05-author-20260914 after verification, releasing port 55435.
Its temporary database rows were discarded; no learner data was removed.
The stopped container and downloaded postgres:18.6 image remain reusable local artifacts.
The learner's notes-week05-db container was not created or changed.

## Repeat relevant checks
From backend/week-05 after lesson 2's local setup:
```sh
python maintenance/verify_workspace.py
uv run pytest practice/test_examples.py -q
source practice/local.env.example
uv run pytest practice/test_postgres.py -q
uv run pytest practice/test_exercises.py -q
uv run pytest projects/task-api/tests -q
```
Last two commands intentionally fail until learner work is implemented. Migration demo
commands and destructive-downgrade precautions are in lesson 9. Do not reset learner
data or fill exercises merely to turn author verification green.
