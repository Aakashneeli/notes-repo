# Prerequisite fixture boundary

## Established by tutor
Inspected backend/week-06/projects/ingestion/ingestion/service.py and worker.py on 2026-09-14: both contain unimplemented learner functions. Week 6 progress is unassessed. No learner code was moved or overwritten.

This local-stack fixture is a smaller raw-text ingestion backend to keep the Week 7 runtime lessons accessible. It stores small text and status in PostgreSQL, queues an importable function through Redis/RQ and counts characters in a worker. It has public local API-key configuration and input checks. It does not recreate multipart uploads, safe local file storage, migrations or full state/retry policy.

The schema is created by an explicit bootstrap command, not import side effects. API and worker share Postgres state; there is no shared Python memory. Redis enqueue and SQL commit are not atomic. An ambiguous enqueue failure can still place a job on the queue; the fixture marks its row failed and extraction ignores non-pending rows. A crash before enqueue can leave pending work. No automatic reconciliation/outbox/retry or production recovery is claimed. Row locking protects repeated extraction; mid-extraction failure rolls back that transaction but requires deliberate recovery.

## Learner fills before adaptation
Chosen path (fixture / independently completed Week 6 copy):
Evidence for earlier implementation if using it:
Original path preserved:
Actual storage and worker process requirements:
Tests establishing prerequisites:
Remaining differences/limits:

If adapting a real completed earlier project later, create a separate copy inside this workspace after inventorying its files; do not overwrite either project. Retain its dependencies and tests, map its actual entrypoint/storage paths, and update Docker COPY/environment/volume settings accordingly. Do not claim this fixture was that earlier implementation.
