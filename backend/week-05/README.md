# Week 05 — PostgreSQL, SQL, SQLAlchemy/SQLModel, Alembic, and Data Modeling

TARGET_WEEK=5 → source article #week-5, label Data → backend/week-05/.
Source: /home/an10/Downloads/ai-backend-roadmap.html, inspected 2026-09-14.
The numbered article is authoritative; the earlier summary strip groups topics differently.
No same-number workspace exists. Backend is reused because the primary lab extends its
Week 4 FastAPI service. No directories for unrequested weeks are created.

Open [the study desk](index.html), then [lesson 1](lessons/0001-start.html).
Deliverables: PostgreSQL-backed Task API, models/CRUD/transaction boundaries, migrations,
integration tests, justified filter indexes, draw.io/Excalidraw ER diagram, migration notes,
20 learner-written SQL queries, confirmed local database run instructions.
SQLAlchemy 2.0 is the selected source-supported ORM; no need to also learn SQLModel.

Week 4 remains unfinished; this workspace supplies a minimal HTTP bridge and keeps main
persistence decisions and implementations as starters. Existing work and progress are preserved.
Read [mission](MISSION.md), [sequence](plan/README.md), [coverage](plan/coverage.md),
[file-to-lesson map](plan/file-map.html), [assessment](plan/assessment.md) and
[verification](VALIDATION.md). The map accounts for every supplied file.

Commands in lessons name their starting directory. Most use:
`cd /home/an10/code/notes-repo/backend/week-05`.
`uv sync --locked` prepares dependencies; lesson 2 introduces the isolated local PostgreSQL lab.
Beginner examples: `uv run pytest practice/test_examples.py -q`.
Unfinished drills: `uv run pytest practice/test_exercises.py -q`.
Real database checks: `uv run pytest practice/test_postgres.py -q`.
Main project checks: `uv run pytest projects/task-api/tests -q`.
Read their different meanings before interpreting results.

No learner mastery is inferred. Excluded: DSA, NeetCode, interview algorithms, complexity
drills and related logs. Redis, vector databases, ingestion, deployment and later topics
are outside numbered Week 5 and receive no detailed lessons here.
