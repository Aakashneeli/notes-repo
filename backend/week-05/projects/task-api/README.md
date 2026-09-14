# Week 5 Task API — learner persistence project
Source: roadmap article week-5. This extends the Week 4 Task API concept.
At authoring, ../relative predecessor [Week 4](../../../week-04/projects/task-api/README.md)
had unfinished schemas, routes and TaskService. Nothing was overwritten.
The supplied app.py/schemas.py form a minimal prerequisite bridge, not completed Week 4 work.
If you later finish Week 4, bring your own adapters here deliberately and retain the persistence checks.
Document adapted behavior; do not reset either workspace.

## Contract (teaching choices supporting the source)
Use SQLAlchemy 2.0 synchronous sessions and PostgreSQL. SQLModel is an alternative in
the source; studying both is not required. Keep Pydantic transport models distinct from ORM rows.
Implement models.py and repository.py; create Alembic revisions.
Tables: tasks (id, title, done), task_events (id, task_id, kind).
IDs are positive database-generated integers; gaps are allowed, never assume restart at 1.
Title is trimmed, 1–80 characters, unique case-sensitively; database constraint name uq_tasks_title.
Database rejects null/blank titles, null done, and events referencing absent tasks.
Create inserts task and a 'created' event in ONE transaction. Update appends 'updated' in the
same transaction; duplicate-title failure leaves both data and events unchanged.
Choose and justify event deletion policy (cascade is acceptable for this lab, unlike immutable audit).
Explain primary/foreign keys, nullability, delete policy and why the event table exists.

Return {id,title,done} for create/get/update. page returns {items,total,offset,limit};
filter done before count/pagination; order by id ascending; limit 1..100, offset >=0.
POST /tasks =>201; GET list/item and PATCH =>200; DELETE =>204 with no body.
Unknown positive ID =>404; conflicting title =>409; empty PATCH=>400.
Omitted PATCH field unchanged; explicit null invalid; false is a real supplied value.
Dummy X-API-Key local-study-key can write, local-read-key can read. /health is public.
Bridge HTTP errors use FastAPI detail, not Week 4's full uniform error envelope.
Retain your full Week 4 contract if extending your own implementation instead.

## Run locally (learner completes evidence)
From repository root: cd backend/week-05. Follow lesson 2 to run the local database.
From that weekly root:
```sh
uv sync --locked
source practice/local.env.example
uv run alembic -c projects/task-api/alembic.ini upgrade head
uv run uvicorn --app-dir projects/task-api app:create_app --factory --port 8055
```
Migrations and CRUD intentionally need your implementation.
In another terminal at backend/week-05:
```sh
curl -i -H 'X-API-Key: local-study-key' -H 'Content-Type: application/json' --data @projects/task-api/data/create.json http://127.0.0.1:8055/tasks
```
Record returned ID; use it for GET/PATCH/DELETE (lesson 10). Restart the API and
verify the row is still present before deleting it. Stop only this API with Ctrl-C.

## Tests
From backend/week-05, after source practice/local.env.example:
`uv run pytest projects/task-api/tests -q`.
Tests need w5_test and create one random w5_<hex> schema per test; migrations build it,
and teardown drops only that generated schema. No project database reset is required.
Do not modify guards to point at personal or shared data.
Read supplied test_contract.py; add your own test_learner.py cases.
Before migrations exist, failures explicitly say EXPECTED STARTER.
After migrations exist, missing ORM/query implementation must fail; don't xfail/skip it.

## Learner deliverables
- Local run instructions confirmed on your machine, versions, start/stop/reuse instructions.
- Models, repository operations, initial and follow-up migration, filter index rationale.
- Passing tests plus a new regression with failing-before/passing-after evidence.
- At least 20 independently written SQL queries in ../../practice/queries.sql and sql-notes.md.
- Schema diagram (draw.io or Excalidraw editable source plus export), migration notes.
- Explain-back and delayed variation in ../../weekly-logs/week-05.md.

## Decisions and evidence — learner fills
Relationships/delete policy:
Transaction boundaries:
Endpoint-to-SQL mapping:
Index choice and measured before/after plans:
Migration upgrade/rollback risks:
Local startup/restart evidence:
Tests and remaining limitations:
