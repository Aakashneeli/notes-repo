# Exact source coverage — Week 6

TARGET_WEEK=6 → /home/an10/Downloads/ai-backend-roadmap.html#week-6 → **Backend Architecture, Auth, Security Basics, File Ingestion, Redis, and Jobs**
(label Backend) → **backend/week-06/**. No naming exception or mismatched existing syllabus.
Source rationale: ingestion precedes RAG because files, metadata, background processing,
retries, jobs, storage, authentication and failure handling must be understood first.
Main deliverables: ingestion backend, security checklist, job-state diagram/failure notes,
Postman collection; lab notes for local-to-S3 and BackgroundTasks-to-RQ migration.

| In-scope source requirement | Lessons | Practice / artifact | Demonstrated ability required |
|---|---|---|---|
| Practical Python LLD: routers, schemas, services, repositories, integrations | 3, 7, 11 | Package contracts + design.md | Trace one request; implement boundaries; explain a storage substitution |
| API-key dependency, secrets, .env.example, safe logging | 4, 11, 12 | safe_event; auth and log tests; security-checklist.md | 401 missing/wrong keys; no secrets/content in events; fail closed config |
| CORS, validation, rate-limit awareness, parameterized SQL | 5, 7, 12 | CORS contract; query fixture; security checklist | Explain browser preflight vs auth; demonstrate bound malicious-looking input; justify limiter location |
| Size/type checks, safe names, local vs S3 | 5, 6, 12 | Upload and storage tests; storage-migration.md | Exact limit succeeds, overflow fails; private keys; partial-write explanation |
| BackgroundTasks and limitations | 9, 11 | Toy lifecycle; learner worker and API | 202/poll workflow; explain process death and TestClient timing |
| Redis/RQ queues, worker, retries, status, idempotency | 8–10 | State/retry practice; rq-migration.md; optional rq scripts | Classify transient failure; trace producer/Redis/worker; duplicate job no-op |
| pending, running, completed, failed, retrying | 8, 9 | job-state.mmd + failure-modes.md | Draw all five states and allowed arrows; base path and migration path distinguished |
| Lab: upload, validate, store metadata, create ingestion job | 5–7, 11 | projects/ingestion code and contract tests | Independent end-to-end local implementation |
| Lab: local files first, S3 replacement note | 6 | LocalStorage; storage-migration.md | Safe disk effects + concrete adapter/credentials/failure note; no cloud action |
| Lab: API key and negative tests | 4, 11–12 | Contract + Postman missing/invalid auth | Reject before side effects |
| Lab: extract text/metadata and update status | 8–9, 11 | worker.py; completion/missing blob/repeat tests | Correct character/word counts, failed path, no duplicate effect |
| Lab: RQ if time; otherwise BackgroundTasks + RQ migration note | 9–10 | Chosen required path: BackgroundTasks + rq-migration.md | Explicit dispatch gap/recovery/idempotency design; optional live RQ evidence only if run |
| Deliverable: document ingestion repo or branch | 3–12 | Project in existing notes Git repo | Scoped reviewed code and runnable instructions; no nested repo needed |
| Deliverable: security checklist | 4–7, 12 | security-checklist.md | Evidence for auth/validation/secrets/file safety/logging |
| Deliverable: job-state diagram and failure notes | 8–10 | job-state.mmd; failure-modes.md | Own diagram plus handling/recovery limits for each crash point |
| Deliverable: Postman upload/auth failure/invalid file/status | 12 | postman collection and environment | Manual outcomes, saved job ID; learner adds edge case |
| Explain: long ingestion should not block HTTP | 9, 13 | assessment + weekly log | Explain latency/timeouts and 202 not success |
| Explain: worker crashes halfway | 8–10, 13 | failure notes + assessment | Name durable state, duplicate risk and reconciliation need |
| Explain: unsafe uploads | 5–6, 13 | security checklist + assessment | Explain spoofed metadata, traversal, resource exhaustion and content handling |
| Explain: where rate limiting belongs and why | 10, 12–13 | security checklist + assessment | Protect scarce resources, coordinate workers, define failure policy |
| Resources: FastAPI, Redis, OWASP-style guidance | All relevant lessons | RESOURCES.md and lesson citations | Use official docs to answer a focused question in reading log |

## Explicit boundaries
The complete source DSA block (including its Python drills and retry sets) is excluded as requested.
Ordinary collections for job data remain. No detailed Week 7 deployment or Week 8 RAG material.
RQ concepts remain required; live Redis/RQ is optional per the exact source. BackgroundTasks plus
a substantive learner RQ migration note is the chosen required implementation path.
SQLite is a disclosed minimal prerequisite fixture because Week 5 learner persistence is unfinished.
This source does not require implementing PostgreSQL again or extending Task CRUD in Week 6.
Text extraction is narrowly UTF-8 .txt; document parser breadth is not required by the source.

Coverage is authored, not learned. All assessed implementations, diagram decisions, migration notes
and evidence remain learner work. Live services and visual checks are separately reported in VALIDATION.md.
