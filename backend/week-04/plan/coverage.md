# Week 4 coverage map

Source: `/home/an10/Downloads/ai-backend-roadmap.html` article **week-4**, label **FastAPI**, title **HTTP, REST, FastAPI, API Design, Postman, and API Tests**.
Workspace: **backend/week-04/**, no naming exception. See [source mapping](../roadmap/source-week-04.md). Main deliverables: in-memory API, complete API tests, Postman export, API README, lifecycle note/diagram.

| In-scope source requirement | Lessons | Practice or artifact | Demonstrated ability evidence (pending) |
| --- | --- | --- | --- |
| Purpose/rationale: first networked service after professional Python | 1–2 | bridge and greeting app | baseline trace; setup output |
| HTTP methods/status/headers/query/path/JSON | 3–4, 8 | greeting curl variants; Task contract | annotated request and observed statuses |
| REST resource names and create/read/update schemas | 4–5 | schemas.py; strict/partial input checks | own schema decisions; invalid create/patch checks |
| Pagination and filtering | 7 | page_done; list/query contract checks | filter-before-page trace, empty/false/boundary cases |
| Routes, routers and dependencies | 4, 9–10 | routes.py, dependencies.py, main.py | all protected route checks and module explanation |
| Startup/shutdown awareness | 10 | greeting lifespan and context-managed TestClient | predict startup/exit flags; explain memory lifetime |
| 400 vs 401 vs 403 vs 404 vs 409 vs 422 vs 500 | 8–9 | error handlers and negative-case tests | status rationale, envelope and no-leak checks |
| OpenAPI/Swagger, curl | 2–4, 12 | running greeting/project, /openapi.json and /docs | manual response and schema observations |
| Postman collections and environments | 12 | starter collection/environment, learner additions/export | final export plus re-import/run evidence |
| TestClient or HTTPX API tests | 11 | fixture, parametrized contract and learner regression | passing complete suite, before/after regression |
| Lab 1: in-memory Task/Notes create/list/get/update/delete | 5–6, 10–11 | Task API learner modules and contract tests | independent CRUD behavior and restart explanation |
| Lab 2: pagination/filtering/consistent errors | 7–8 | list and error modules/checks | page/error traces and rejected-mutation evidence |
| Lab 3: API-key dependency | 9 | APIKeyHeader, role checks and OpenAPI | missing/wrong key every endpoint, read-only denial |
| Lab 4: Postman happy/invalid/missing-auth/missing-resource | 12 | ordered starter; learner export | observed positive/negative runs, not static JSON |
| Lab 5: every endpoint and negative case tested | 11 | test_contract.py + test_learner.py | assertions, state preservation, real regression |
| Deliverable: FastAPI repo with router/schema/service separation | 6, 10, 14 | package inside existing notes repo | reviewed modules, local Git evidence |
| Deliverable: exported Postman collection | 12, 14 | learner creates postman/task-api.postman_collection.json | re-imported learner export |
| Deliverable: API README with curl/status behavior | 12, 14 | project README contract + learner sections | observed examples and documented failures |
| Deliverable: lifecycle note and sequence diagram | 13–14 | reading note and sequence starter | learner request-lifecycle.md and request-sequence.mmd |
| Resource: FastAPI first steps/parameters/dependencies/testing | 2–5, 9–11 | annotated RESOURCES.md and per-lesson citations | applied primary reading and code note |
| Resource: Postman Learning Center | 12 | annotated collection/environment/script docs | chosen environment, modified scripts and export |
| Resource: HTTP methods/status reference | 3, 8 | RFC 9110 and reference glossary/status guide | correctly justified method/status choices |
| Explain-back: request arrival through response | 13–14 | lifecycle trace and assessment prompt 1 | own-word success and failure trace |
| Explain-back: where validation happens | 5, 13–14 | models/dependency/response trace; prompt 2 | distinguish request error from output bug |
| Explain-back: why each status | 8, 14 | status table; prompt 3 | resource-specific rationale |
| Explain-back: tests vs Postman | 11–12, 14 | test and manual evidence; prompt 4 | in-process vs listener/client limits |

## Exclusions and boundaries

DSA, NeetCode, algorithm interview exercises, complexity drills and associated logs are excluded. Ordinary task dictionaries/lists and practical filtering remain. Broad backend-topic lists do not add file ingestion, jobs, databases, cloud or advanced auth to numbered Week 4. No earlier or future workspace was rewritten.

The source allows Task/Notes; this workspace chooses Tasks. Strict booleans, duplicate-title policy, IDs, exact errors and a dummy read-only key are explicit teaching contracts. A fresh Week 4 project is appropriate: no extension is requested by this week.

## Coverage vs completion

Teaching/scaffolding covers all in-scope rows; learner implementations/evidence remain pending. Postman execution/export and the independent API are learner deliverables, not unresolved missing lessons. See [validation limits](../VALIDATION.md). No material is marked learned.

## Depth revision after learner feedback

Lessons 3–12 have additional execution/data-flow traces and diagnostic exercises.
practice/mechanisms.py + practice/test_mechanisms.py support model validation (5),
state/error ownership (6), dependency replacement (9) and assertion/fixture reasoning
(11). These bridge the jump into independent implementation without supplying a Task
API solution. Scope and completion criteria are unchanged; progress remains unassessed.
