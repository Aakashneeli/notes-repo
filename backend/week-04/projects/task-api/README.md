# Week 4 Task API — learner project

Status: supplied infrastructure and unfinished learner implementation. This directory
is a package inside the existing notes Git repository; do not create nested Git history.
Start with ../../lessons/0004-routes-and-input-locations.html and progress through the lessons.

## Contract (supplied; keep stable)

All task operations require X-API-Key. Public /health returns 200 {"status":"ok"}.
OpenAPI is public; document security on task operations. Dummy writer key is
local-study-key; dummy reader is local-read-key. Missing/wrong -> 401 unauthorized
with WWW-Authenticate: APIKey; reader writes -> 403 forbidden. These are local-only
teaching values configured through TASK_API_KEY/TASK_READ_KEY before app construction.
.env.example documents them and is NOT loaded automatically. Do not use real secrets.

| Method/path | Input | Success |
| --- | --- | --- |
| POST /tasks | TaskCreate JSON | 201 TaskRead |
| GET /tasks | offset=0, limit=20, optional done | 200 TaskPage |
| GET /tasks/{task_id} | positive integer ID | 200 TaskRead |
| PATCH /tasks/{task_id} | partial TaskUpdate JSON | 200 TaskRead |
| DELETE /tasks/{task_id} | positive integer ID | 204, empty body |

TaskCreate: title string, trimmed length 1..80; done strict JSON boolean, default false.
Reject extra fields, null, numeric title, coercible non-booleans and whitespace-only title.
TaskRead: exactly id/title/done, positive integer server ID, validated title and bool.
TaskUpdate: title and done may be omitted individually; supplied null is rejected;
empty object is 400 empty_update. Preserve omitted fields and explicitly supplied false.
TaskPage: {"items": [TaskRead...], "total": filtered_count, "offset": n, "limit": n}.
Filter done before pagination; order ascending id. offset >= 0, limit 1..100. Query
booleans use FastAPI's normal text parsing; invalid query -> 422. No filter means all.
Empty/past-end page is 200 with items=[]; total remains the filtered count.

Every app instance starts empty. IDs increase from 1 without reuse after deletion.
Title uniqueness compares trimmed, case-sensitive titles. POST/update duplicates ->
409 conflict; unchanged own title is allowed. Missing positive ID -> 404 not_found.
Apply validation/conflict checks before mutation. No partial state changes on failure.
Read/list must not mutate. Use one server worker; protect compound thread-level state
operations if synchronous handlers can run concurrently. No durability guarantee.

Every HTTP error uses {"error":{"code":string,"message":nonempty_string}} and JSON.
400 empty_update; 401 unauthorized; 403 forbidden; 404 not_found; 409 conflict;
422 validation_error; 500 internal_error (generic, no tracebacks or private details).
Malformed JSON, invalid body/path/query -> 422. Unknown routes -> 404.
Unsupported methods -> 405 method_not_allowed, preserving Allow header.
Use valid auth when testing input failures; simultaneous-defect precedence is not assessed.

## Files you implement

src/task_api/schemas.py, service.py, routes.py, dependencies.py, errors.py, plus
wiring in main.py. __init__.py is a supplied inert package marker. Tests use only
create_app and the public HTTP contract; internal method signatures are your decision.
Add your regression/variation tests in tests/test_learner.py. Supplied contract tests
are read/run infrastructure, not learner code to disable. No finished main API is hidden here.

## Reproduce locally

Starting directory: backend/week-04/projects/task-api within this repository.

```bash
UV_CACHE_DIR=/tmp/week4-uv-cache uv sync --locked
UV_CACHE_DIR=/tmp/week4-uv-cache uv run --locked pytest -q
TASK_API_KEY=local-study-key TASK_READ_KEY=local-read-key UV_CACHE_DIR=/tmp/week4-uv-cache uv run --locked uvicorn task_api.main:create_app --factory --host 127.0.0.1 --port 8004
```

Starter: health works, task checks fail. Use one worker. Stop with Ctrl-C. Restart
clears memory. Python 3.11–3.14 declared; author-tested interpreter is in ../../VALIDATION.md.
No GPU, database or paid service required. Installation downloads dependencies.

## curl examples (supplied expected contract; learner verifies)

Second terminal, same project starting directory. Use a fresh process for ID 1,
otherwise replace 1 with the ID returned from POST.

```bash
curl -i -X POST http://127.0.0.1:8004/tasks -H 'X-API-Key: local-study-key' -H 'Content-Type: application/json' --data-binary @data/create.json
curl -i 'http://127.0.0.1:8004/tasks?done=false&offset=0&limit=2' -H 'X-API-Key: local-read-key'
curl -i http://127.0.0.1:8004/tasks/1 -H 'X-API-Key: local-read-key'
curl -i -X PATCH http://127.0.0.1:8004/tasks/1 -H 'X-API-Key: local-study-key' -H 'Content-Type: application/json' --data-binary @data/update.json
curl -i -X POST http://127.0.0.1:8004/tasks -H 'X-API-Key: local-study-key' -H 'Content-Type: application/json' --data-binary @data/invalid.json
curl -i http://127.0.0.1:8004/tasks
curl -i http://127.0.0.1:8004/tasks/999 -H 'X-API-Key: local-read-key'
curl -i -X DELETE http://127.0.0.1:8004/tasks/1 -H 'X-API-Key: local-study-key'
```

Expected statuses in order: 201, 200, 200, 200, 422, 401, 404, 204. Data fixtures
are supplied and stable. Add separate files for your variations. Run Postman using
lesson 12 and the supplied starter collection/environment. The starter is not your export.

## Learner completion (append real evidence)

Observed setup and versions:
Your architecture decisions and thread/state assumptions:
Observed endpoint examples and failure responses:
Tests, real regression and result:
Postman final export path (create postman/task-api.postman_collection.json), re-import/run evidence:
Request lifecycle note (create request-lifecycle.md) and sequence diagram (create request-sequence.mmd):
Independent variation and delayed retrieval:
Known limitations and help used:

Return to the weekly root with cd ../.. after stopping the server.
