# Week 7 coverage map

TARGET_WEEK=7 → source `article#week-7` → **Docker, Compose, Local Production Shape, Logging, Health Checks, and CI Intro** → `cloud-devops/week-07/`.
Source `/home/an10/Downloads/ai-backend-roadmap.html`; SHA-256 `70466aa6c6ecb8ed7ca94c84882faa54f26147d180c9de17d5bf095fc945579e`. No numbering or directory exception.

Rationale: make the backend reproducible locally before cloud/AI dependencies multiply. Prior Week 6 ingestion is an unmet prerequisite, so a labelled minimal fixture is supplied; it does not assert Week 6 completion. This map tracks prepared teaching coverage, not learner achievement.

| In-scope source requirement | Lessons | Practice/project | Demonstrated-ability evidence |
|---|---|---|---|
| Image/container; build/run; ports, volumes, networks | 3–6 | tiny-image, service_address, Compose | Predict two runs; identify runtime data; change host port |
| FastAPI Dockerfile: base, workdir, dependencies, command | 4 | projects/local-stack/Dockerfile | Build/import check; explain every COPY and runtime argument |
| Compose services, environment, networks, volumes, health checks | 5–7 | compose.yaml; service-contract.md | config gate + live healthy startup + retained job |
| Local API, Postgres, Redis, vector DB and worker | 2, 5–6, 10 | fixture; five learner service definitions; smoke.py | Accepted job completes; vector reachable; diagram matches actual DNS |
| Logs, container shell, port conflicts, startup order | 6, 10 | debugging-note.md; runbook | Actual problem, discriminating probe, fix and regression |
| Structured logs, request IDs, health endpoints | 7–9 | operations.py; observability.py; contract tests | 200/503 distinction; safe correlated success/404/500 events |
| GitHub Actions lint/test on push/PR | 11 | ci/workflow.yml; ci-evidence.md | Local Ruff/pytest pass; meaningful failure; hosted run separately pending |
| Lab 1: Dockerfile for ingestion API | 2, 4 | prerequisite fixture + learner Dockerfile | Explicit bridge limits, built importable app |
| Lab 2: Compose API/Postgres/Redis/worker/vector placeholder | 5–6, 10 | compose.yaml | Five services and actual job completion |
| Lab 3: /health and /ready | 7 | operations.py | Dependency fault does not break liveness; readiness recomputes |
| Lab 4: structured logging + request-ID middleware | 8–9 | observability.py | Header/log ID agreement; sanitized fields and unexpected error |
| Lab 5: GitHub Actions ruff and pytest | 11 | ci/workflow.yml | Runnable completed workflow draft; learner installation only |
| Deliverable: fresh clone starts with one documented command | 12 | runbook.md | Committed fresh-copy trial with unique project and preserved old data |
| Deliverable: architecture diagram with service/network boundaries | 5, 12 | architecture.mmd; decisions.md | Learner arrows/ports/volume lifetimes match actual stack |
| Deliverable: CI workflow file and passing test run | 9, 11–12 | ci/workflow.yml; ci-evidence.md | Learner local pass required; author pass is not learner CI |
| Deliverable: one Docker problem and fix | 10 | debugging-note.md | Real observation or disclosed environment block; no invented story |
| Explain-back: image contents versus runtime | 3–4, 13 | weekly log | Name code, environment, writable layer and named volume |
| Explain-back: API discovery of Postgres/Redis | 5, 13 | architecture + log | Trace caller/network/service DNS/container port |
| Explain-back: health proof and limits | 7, 10, 13 | fault evidence + log | Differentiate process, connectivity, schema, worker and business success |
| Explain-back: local and AWS log destinations | 8, 13 | decisions.md + log | Explain stdout collection versus configured cloud delivery |
| Source resources: Docker, Actions, FastAPI official docs | All | RESOURCES.md; reading-log.md | Purposeful reading linked to one implemented decision |


## Exclusions and limits
The source's entire DSA focus block and related interview drills/logs are excluded by request. Ordinary dict/list operations used for configuration and logging remain. No detailed Week 8+ teaching or cloud provisioning is included. Qdrant is chosen from the allowed Qdrant/Chroma alternative and remains a placeholder.

All in-scope requirements have teaching and a verification route. Learner implementation, live Docker evidence, a committed fresh-copy trial, and hosted CI remain open until actually performed. No hosted passing run is claimed from local checks. The prerequisite fixture's schema bootstrap/raw-text storage/recovery limits are explicit in bridge-notes.md.
