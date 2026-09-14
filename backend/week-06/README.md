# Week 06 — Backend Architecture, Auth, Security Basics, File Ingestion, Redis, and Jobs

TARGET_WEEK=6 → numbered source article #week-6, label Backend → backend/week-06/.
Source: /home/an10/Downloads/ai-backend-roadmap.html, inspected 2026-09-14.
The exact numbered article controls scope; roadmap summary groupings do not renumber it.
No existing Week 6 workspace or numbering mismatch was found. Backend is the existing topic
that fits the main objective: protected document ingestion with background processing.

Start at [the study desk](index.html), then [lesson 1](lessons/0001-start.html).
Deliverables: learner-owned document ingestion backend; security checklist; job-state diagram
and failure-mode notes; Postman upload/auth-failure/invalid-file/status collection; local-to-S3
storage note and required RQ migration note for the chosen BackgroundTasks implementation.
Redis/RQ concepts are required; the live Redis/RQ implementation is optional in the source.

Week 5 precedes ingestion; Week 7 packages the backend; Week 8 builds RAG on ingested data.
Earlier projects and progress are preserved. Their persistence implementation is unfinished.
A small completed SQLite repository is explicitly supplied as a prerequisite fixture, not
as a completed PostgreSQL project. Main validation, storage, auth, routes, service, schemas
and worker remain learner-owned starters. Plain UTF-8 .txt is the local upload policy; no
paid service, account changes, publishing, real credentials or document parser is required.

[Mission](MISSION.md) · [Sequence](plan/README.md) · [Coverage](plan/coverage.md) ·
[File-to-lesson map](plan/file-map.html) · [Assessment](plan/assessment.md) ·
[Progress](plan/progress.md) · [Verification](VALIDATION.md).

Commands start at `/home/an10/code/notes-repo/backend/week-06` unless a lesson says otherwise.
`uv sync --locked` creates the environment. `uv run pytest practice/test_examples.py -q`
checks completed examples. `uv run pytest practice/test_exercises.py -q` and
`uv run pytest projects/ingestion/tests -q` intentionally fail until you implement the tasks.
Read the lesson before interpreting failures. The project does not ship a hidden completed app.

Excluded throughout this request: DSA, NeetCode, interview algorithms, complexity drills and
associated logs. No detailed future-week lessons or speculative future directory choices.
No learner mastery inferred from author verification.
