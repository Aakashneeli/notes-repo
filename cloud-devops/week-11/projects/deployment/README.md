# Deploy one backend — learner project

Read lessons 1–12 in order, using the flexible [sequence](../../plan/README.md).
Start all local commands at `cloud-devops/week-11` unless a lesson says otherwise.

## Starting state
Week 7 Dockerfile/Compose and operations are unfinished; Week 10 progress is unassessed.
`fixture/app.py` is a completed, deliberately tiny FastAPI prerequisite. It has no database,
uploads, RAG, or users. It does not represent a completed earlier project.
If your earlier backend later works, preserve it and use its verified image; record its path,
commit, dependencies, memory requirements, migrations and tests in selection.md.

## Your deliverables
Implement Dockerfile, ci/workflow.yml, release.py, and additional release tests.
Fill selection.md, cost-plan.md, access-plan.md, secrets.md, storage.md,
architecture.mmd, runbook.md, endpoint.md, rollback.md and shutdown.md.
Do not put credentials in any of them.
The deployment design, health gate and operational decisions are yours.
The supplied fixture and tests are infrastructure: read and run; do not change tests to hide failure.

## Contract
Container binds 0.0.0.0:8000 internally; host publishes 127.0.0.1:8000 only.
GET /health always returns 200 with alive=true and RELEASE (default dev).
GET /ready returns 200 iff API_KEY exists and FAIL_MODE is not dependency, else 503.
GET /message requires X-API-Key; missing/bad key → 401 (503 if server key absent);
good key → 200; FAIL_MODE=dependency plus good key → sanitized 500.
Every response has an X-Request-ID and safe JSON event; neither key nor request body is logged.
This readiness is only a configuration check; it does not probe a real database.
Use data/sample.txt only for the conditional S3 exercise; it contains no sensitive data.

## Passing is evidence-specific
Python tests prove fixture behavior and pure promotion decisions. Image smoke tests prove
container startup/configuration. Neither proves IAM, network routing, cloud logging or billing.
A private endpoint must identify the real instance, access method, port, release and dated response;
a planned endpoint is not a deployed endpoint. Live delivery remains pending until you do it.
