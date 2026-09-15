# Week 07 — Docker

**Resolved source:** TARGET_WEEK=7 → `article#week-7`, source heading **Docker, Compose, Local Production Shape, Logging, Health Checks, and CI Intro**.
Source: `/home/an10/Downloads/ai-backend-roadmap.html`, inspected 2026-09-14; SHA-256 `70466aa6c6ecb8ed7ca94c84882faa54f26147d180c9de17d5bf095fc945579e`.
Workspace: `cloud-devops/week-07/`. The existing cloud-devops topic best fits reproducible local runtime and CI. No same-number workspace or naming exception was found.

[Open the study desk](index.html) → [First lesson](lessons/0001-start.html).

Main deliverables: ingestion API Dockerfile; five-service Compose stack (API, PostgreSQL, Redis, worker, Qdrant placeholder); /health and /ready; safe structured request-ID logs; Ruff/pytest push/PR workflow; documented fresh-clone start; service/network diagram; actual debugging note and test evidence.

The numbered source section is authoritative. Week 6 provides ingestion prerequisites; Week 8 later uses more AI dependencies. Only Week 7 is taught here. Interview algorithm curricula and related drills/logs are excluded.

## Honest starting state
Earlier Week 6 `service.py` and `worker.py` still raise NotImplementedError and progress is unassessed. Their files and learner records remain untouched. This workspace supplies an explicitly minimal raw-text/Postgres/RQ prerequisite fixture, not a completed Week 6 project. Read [bridge notes](projects/local-stack/bridge-notes.md) before adapting it.

Completed teaching examples are in practice; learner functions/configuration are intentionally unfinished. No finished main project is hidden in examples or author tests. No learning is inferred from author checks.

## Start and navigate
Start at `/home/an10/code/notes-repo/cloud-devops/week-07` for Python commands; lessons explicitly enter `projects/local-stack` for Compose. Read [sequence](plan/README.md), [coverage](plan/coverage.md), [file introductions](plan/file-map.html), [assessment](plan/assessment.md), and [verification](VALIDATION.md).

Use Python 3.12 and the supplied requirements.lock. Docker Engine + Compose with daemon access and image-download access are required for live labs. No GPU, cloud account or provider key is needed. Hosted CI is a separate learner action with GitHub account/permissions and applicable billing prerequisites.
