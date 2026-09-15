# Learner project: production-shaped local ingestion lab

This is a Week 7 project around a supplied prerequisite fixture. Main implementation remains yours. Read [bridge notes](bridge-notes.md) before claiming it extends a completed earlier backend.

## Supplied infrastructure
fixture/ contains a bounded raw-text API, Postgres repository, RQ callable, bootstrap and dependency probes. app.py composes these with learner operations/logging hooks. tests/test_contract.py defines expected behavior; smoke.py exercises real services with data/hello.txt. requirements.lock is two directories above; Compose build context is ../.. . No embeddings or AI calls occur.

## Your work
1. Dockerfile: Python 3.12, /app, dependency installation from the lock, runtime source, exec-form Uvicorn factory command. See L4.
2. compose.yaml: implement [service contract](service-contract.md), runtime environment, networks, named volumes and readiness ordering. See L5–6.
3. operations.py: required postgres/redis True → 200; any missing/false → 503. Body `{"ready": bool, "checks": {"postgres": bool, "redis": bool}}`. /health always responds 200 `{"alive": true}` without probes; /ready invokes probes on each request and sanitizes exceptions.
4. observability.py: accept safe client ID or generate UUID hex; store in request.state and X-Request-ID. One JSON log event per response, including 404 and sanitized unexpected 500. Fields exactly event, request_id, method, status, duration_ms. No confidential content.
5. ci/workflow.yml: Ubuntu, Python 3.12, read-only contents, checkout/setup/install/lint/test, push/PR triggers and correct working directory. Draft stays inactive until learner deliberately installs it.
6. tests/test_learner.py, decisions.md, architecture.mmd, debugging-note.md, runbook.md and ci-evidence.md: your independent evidence and decisions.

## Expected unfinished failures
operations.py, observability.py and practice/exercises.py raise NotImplementedError. Dockerfile is comments only; Compose/workflow have empty mappings. Full tests and configuration gate must fail until you implement them. Author checks run separately; do not weaken the assessed checks.

## End-to-end contract
With the completed stack, public GET /health is 200 and /ready is 200 when Postgres/Redis probes succeed. POST /documents requires X-API-Key plus Content-Type text/plain, takes raw UTF-8 bytes, returns 202 + job_id. Empty/invalid UTF-8 → 422; over 4096 bytes → 413; wrong type → 415; missing/invalid key → 401. GET /jobs/{id} uses the same key; unknown → 404. A running worker changes the sample job to completed with characters=17. Data survives container replacement through the Postgres volume. Queue connectivity alone does not prove consumption.

Run Python commands at Week 7 root; run Compose commands in this directory with `--env-file .env.example`. Real credentials are not needed. The one-command startup is an assessed target in runbook.md, not a promise that an unfinished starter runs.
