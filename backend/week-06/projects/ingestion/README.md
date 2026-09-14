# Document ingestion — learner project contract

This is the source Week 6 main lab inside the existing notes Git repository.
Start at `/home/an10/code/notes-repo/backend/week-06`; all paths below are relative to it.
Read lessons 3–11 before independent assembly. Completed infrastructure: config.py,
repository.py, app.py, package marker and contract tests. Implement auth.py, validation.py,
storage.py, schemas.py, service.py, worker.py, routes.py. No completed main solution is supplied.

## Scope and interfaces
One local shared API key; UTF-8 plain text only; one job per accepted upload. The SQLite jobs
repository is a prerequisite fixture because earlier persistence is unfinished. It is not
PostgreSQL verification or production schema/migration design. Original filename is metadata;
there is no public file download or multi-tenant authorization in this contract.

- POST /documents: multipart field `file`, X-API-Key required. Missing/invalid key → 401 before
  service side effects. Validate name (no slash, backslash, control characters, or empty name → 400),
  .txt suffix case-insensitive and content type text/plain (otherwise 415), nonempty bytes (400),
  max_bytes inclusive (overflow 413), strict UTF-8/no NUL (415). Missing multipart field → 422.
- Success → 202 `{ "job_id": "<generated UUID hex>", "state": "pending" }`. Save bytes and metadata
  before scheduling extraction with BackgroundTasks. The returned body describes acceptance.
- GET /jobs/{job_id}: same auth; unknown → 404. Public response has exactly job_id, state, attempts,
  characters, words, error_code. Before completion counts are null. Completed has correct Unicode
  character and whitespace-separated word counts. Never expose storage key/path/name or credential.
- Storage key is uuid4().hex + `.txt`. Validate internal keys as 32 lowercase hex + `.txt` for every
  operation. Exclusive create prevents overwrites; deletion is idempotent for an absent valid key.
  Remove a newly created blob if metadata creation fails. Unexpected internal failures stay visible.
- Worker claims pending→running atomically. Only a successful claim increments attempts. Duplicate
  running/completed calls do not re-extract. Missing blob → failed/storage_missing. Invalid saved
  text → failed/invalid_text. Other anticipated storage OSError → failed/storage_error.
  Success commits counts and completed together. Log safe state events with job ID; no raw secrets,
  contents or arbitrary exception messages. Base path does not automatically recover abandoned running.
- Service functions take adapters, not HTTP request objects. get_status maps the fixture row to
  the public response dict or None. accept returns job ID and preserves compensation failures for diagnosis.

## Setup and run (after implementing the starter)
```sh
cd /home/an10/code/notes-repo/backend/week-06
uv sync --locked
export INGEST_API_KEY=local-study-only
export INGEST_ROOT=runtime/dev
uv run uvicorn ingestion.app:create_app --factory --app-dir projects/ingestion --host 127.0.0.1 --port 8006
```
Uvicorn imports the module using --app-dir and calls create_app because of --factory.
Settings read the environment; `.env` is not auto-loaded. The example key is a harmless public
local placeholder, not a production credential. runtime/dev is generated, private, ignored and
retained across restarts. Tests use fresh temporary paths and never target it. No GPU or paid
service required. Dependency download needs internet once; SQLite needs no server.

## Checks and evidence
`uv run pytest projects/ingestion/tests -q` — expected TODO failures until implemented.
Read tests/test_contract.py for provided cases. Add independent regressions to test_learner.py.
The TestClient runs background tasks before returning to the test; this is not wire-timing proof.
Follow lesson 12 for curl/Postman. hello.txt is 34 bytes/characters, five words including its final
newline in the character count. invalid.html is a harmless unsupported sample; never execute it.
Fill design.md, security-checklist.md, failure-modes.md, job-state.mmd, storage-migration.md and
rq-migration.md as the relevant lessons request. Put test/manual evidence in ../../weekly-logs/week-06.md.

## Implementation slices
1. Auth, validation and storage helpers, each with a focused check.
2. Public schemas, service persistence/compensation and protected routes.
3. Worker claim, extraction, failed outcomes, safe logs and repeat execution.
4. End-to-end negative tests, graceful restart, Postman, diagrams and explain-back.
5. Required RQ migration note; optional real RQ queue exercise in lesson 10.

Do not claim durable dispatch from BackgroundTasks. A process can die after commit but before
scheduling; a worker can die in running; local files must be shared or replaced for remote workers.
Document these as limitations rather than hiding them with automatically successful statuses.
