# Source mapping: Week 04 — FastAPI

Authority: `/home/an10/Downloads/ai-backend-roadmap.html`, article `#week-4`.
Source title: **HTTP, REST, FastAPI, API Design, Postman, and API Tests**.
Workspace: `backend/week-04/`. Existing backend topic fits the primary objective; no matching workspace or naming exception existed.
Source SHA-256: `70466aa6c6ecb8ed7ca94c84882faa54f26147d180c9de17d5bf095fc945579e`.
Recorded 2026-09-13. This extraction retains the numbered week's in-scope wording; the excluded track is omitted.


 04 FastAPI 
 
 HTTP, REST, FastAPI, API Design, Postman, and API Tests 
 Build your first real backend service and learn how APIs behave from client to server. 
 Why this comes now: you have enough Python structure to understand the framework. This week turns Python into a networked service with validation, docs, tests, and manual QA. 
 
 
 Subtopics to learn 
 
 HTTP methods, status codes, headers, query params, path params, JSON bodies. 
 REST resource naming, request/response schemas, pagination and filtering basics. 
 FastAPI routes, routers, dependencies, startup/shutdown awareness. 
 Pydantic schemas for create/read/update responses. 
 Error handling: 400 vs 401 vs 403 vs 404 vs 409 vs 422 vs 500. 
 OpenAPI/Swagger docs, curl, Postman collections and environments. 
 API tests with TestClient or HTTPX. 
 
 
 
 Hands-on labs 
 
 Build an in-memory Task/Notes API with create, list, get, update, delete. 
 Add pagination, filtering, and consistent error response shape. 
 Add API-key dependency even if it uses an in-memory key initially. 
 Create Postman collection for happy path, invalid payloads, missing auth, and missing resources. 
 Write API tests for every endpoint and negative case. 
 
 
 
 Deliverables 
 
 FastAPI repo with clean router/schema/service separation. 
 Postman collection exported into the repo. 
 API README with curl examples and status code behavior. 
 Request lifecycle note and sequence diagram. 
 
 
 
 Explain-back prompts 
 
 What happens from the moment a request hits a route until a response is returned? 
 Where does validation happen? 
 Why does this endpoint return this status code? 
 How do your tests differ from your Postman checks? 
 
 
 
 
 Resources 
 
 FastAPI docs: first steps, path/query/body parameters, dependencies, testing. 
 Postman Learning Center: collections and environments. 
 HTTP reference notes: methods and status codes. 
 
 
 
 
 

## Sequence context
Weeks 1–3 establish tooling, Python behavior and professional structure. Week 4 creates the network boundary and an in-memory service. Week 5 replaces that storage with persistence. Later stages add ingestion, containers, AI workflows, design and deployment. Their broader topic lists do not expand this week's syllabus.

No prior project extension is required here. The existing Week 3 package remains a starter and its evidence is unassessed; this week therefore includes small Python/Pydantic bridges. Historical Week 2 Foundation material does not establish completion of the source's Python Core week.
