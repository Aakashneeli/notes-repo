# Exact source-to-workspace coverage
TARGET_WEEK=5 → article #week-5 (Data) → **PostgreSQL, SQL, SQLAlchemy/SQLModel, Alembic, and Data Modeling** → backend/week-05/.
Source /home/an10/Downloads/ai-backend-roadmap.html, inspected 2026-09-14.
No same-number collision. Backend reused for the Week 4 API persistence extension.
Source rationale: disciplined storage precedes retrieval/AI work. Actual prerequisites are unassessed;
Week 4 remains unfinished and the minimal bridge is explicitly supplied. SQLAlchemy chosen from
the source's SQLAlchemy/SQLModel alternatives. No Redis/vector syllabus inferred from summary strip.

| In-scope source requirement | Teaching / practice | Independent evidence |
|---|---|---|
| SELECT, ordering, limits | L3; queries Q01–10 | Predicted/observed rows in sql-notes |
| INSERT, UPDATE, DELETE | L4; Q17–20 | Targeted writes and affected-row explanation |
| Joins, grouping | L5; Q11–16; beginner counts | Preserve Chen's zero and vary filter location |
| PK, FK, constraints, nullable fields | L4/L7; seed failures | Models/migrations; direct-SQL negative tests; diagram |
| Transactions; danger of partial writes | L6/L8/L10 | Task+event atomicity; injected failure; concurrency log |
| Index benefits/costs; basic query plans | L12; index-lab.sql | Project filter index, measured plans and tradeoff |
| SQLAlchemy/SQLModel models, sessions, repository access | L7–8; label mechanism | Learner models.py and repository.py |
| Alembic create/apply/inspect/rollback awareness | L9; completed label migrations | Learner initial/follow-up revisions; migration-notes |
| Database integration tests and test-data setup | L11; conftest.py | PostgreSQL suite, new regression/concurrency tests |
| Replace Week 4 memory with PostgreSQL | L1/L10; explicit minimal HTTP bridge | Durable create/restart/get and all CRUD |
| Add models, migrations, queries, transaction boundaries | L7–11 | Implemented project and endpoint-to-SQL explanation |
| Index fields used in filters/search and explain why | L12 | Chosen index and migration; no universal speed claim |
| Integration tests against a test database | L11; random isolated test schemas | TEST_DATABASE_URL run evidence |
| ER/data model diagram in draw.io or Excalidraw | L13; schema-design.md | Editable named-tool diagram + export checked against DB |
| FastAPI + Postgres repo with migrations/tests | L9–11 | Completed local project; main code intentionally unfinished |
| Schema diagram and migration notes | L9/L13 | Linked editable/exported diagram and notes |
| At least 20 queries written by learner | L3–5; sql-lab.md Q01–Q20 | queries.sql + sql-notes; supplied examples never count |
| README explaining local database run | L2/L10/L14 | Confirmed setup/start/stop/reuse instructions and versions |
| Why these tables/relationships? | L4/L7/L13 | Source explain-back in weekly log |
| What if two writes happen at once? | L6/L11 | Two-session observation + unique-title race test |
| What query does this endpoint execute? | L8/L10/L13 | Actual SQL and call trace |
| What breaks without index or constraint? | L4/L12/L14 | Correctness vs performance explanation with evidence |
| Source PostgreSQL docs; ORM docs; Alembic docs | RESOURCES.md; per-lesson citations | Question-led reading note |
| Continuous writing, debugging, codebase reading, Git/AI discipline | L1/L11/L13/L14 | Reading/mistake/retrieval records; scoped local Git review |

## Exclusions and limits
The source's entire DSA focus block (trees, recursion, DFS/BFS, recursive problem traces),
NeetCode, interview algorithms, complexity drills and related logs are excluded.
Ordinary Python collections remain when useful. Detailed future lessons and cloud work are excluded.
Coverage is material availability, not demonstrated completion. There are no unresolved teaching-scope gaps;
unfinished learner work, optional personal tool access and author verification limits are in VALIDATION.md.
