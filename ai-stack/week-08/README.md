# Week 08 — RAG
Source: /home/an10/Downloads/ai-backend-roadmap.html, exact numbered article #week-8.
Title: Raw LLM APIs, Embeddings, Vector DBs, Manual RAG, and Retrieval Evaluation
Rationale: build ingestion, retrieval and evaluation manually before agent orchestration.
Workspace: ai-stack/week-08/ (existing AI topic; no same-number workspace or naming exception found).
Deliverables: ingest/search/ask API with citations; vector-store comparison; data-flow diagram;
15–25-question retrieval evaluation report; chunking, filtering and mocked-response tests.

Start at [the study desk](index.html), then [Lesson 1](lessons/0001-start.html).
All commands start in this weekly root unless a lesson explicitly says otherwise:
`cd /home/an10/code/notes-repo/ai-stack/week-08`.

Python and Git exposure is the disclosed baseline, not mastery. Week 6 service and Week 7
operations remain unfinished when inspected. A tiny JSON ingestion bridge is supplied.
It does not claim to implement earlier uploads, auth, queues or PostgreSQL.
If you have since completed ingestion, follow Lesson 2's integration seam instead of replacing it.

[Sequence](plan/README.md) · [Coverage](plan/coverage.md) · [File map](plan/file-map.html) ·
[Assessment](plan/assessment.md) · [Verification](VALIDATION.md).
Instructor examples are in practice/examples.py; learner work is in practice/exercises.py
and projects/manual-rag/rag.py. Full project checks intentionally fail until implemented.
No provider calls, model downloads, publishing or cloud resources are needed for author checks.
Semantic embedding and live generation have explicit learner-run paths and separate evidence.
