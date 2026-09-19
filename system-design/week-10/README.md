# Week 10 — System Design, LLD/HLD, Observability, Performance, Reliability, and Security Review

Source authority: /home/an10/Downloads/ai-backend-roadmap.html, numbered article #week-10 (validated 2026-09-19).
Workspace: system-design/week-10/. Existing system-design topic fits the main objective; no same-number workspace or naming exception exists.

[Open the study desk](index.html), then [Lesson 1](lessons/0001-start.html).
Main deliverables: five draw.io diagrams and architecture explanation; four ADRs (vector DB, queue, model provider, deployment); request/AI log implementation and observability checklist; documented cache/rate-limit design; measured latency/load note; backend and AI security review.

## Why here, why now
The numbered roadmap places design after API/data/jobs/Docker/RAG/agents and before deployment. This workspace covers Week 10 only. The short six-part roadmap summary is not used to select a syllabus.
Prior Week 8/9 implementations remain unfinished. Their content and progress are untouched. A minimal in-process fixture supports local practice; actual backend integration remains a separate evidence gate.

## Start
From the repository root:
```sh
cd system-design/week-10
python --version
python practice/examples.py
```
Python >=3.11, standard library only. No pip install, secret, GPU or paid service is needed.
For the required diagrams use draw.io Desktop if available, or its web editor with Device storage and local saves. No account, publication or infrastructure provisioning is part of preparation.

## Organization
- lessons/: primary self-contained teaching; reference/: compact recall aids.
- practice/: completed teaching examples and unfinished beginner exercises.
- projects/architecture-review/: assessed implementation, diagrams, design decisions and evidence.
- plan/: sequence, coverage, assessment, learner progress and [file-to-lesson map](plan/file-map.md).
- templates/, weekly-logs/, codebase-reading/: reuseable prompts and learner-owned evidence.
- assets/: local course style importing the established repository component.
- maintenance/, VALIDATION.md: author checks, not learner completion.

[Mission](MISSION.md) · [Resources](RESOURCES.md) · [Assistance](AI-USAGE.md) · [Coverage](plan/coverage.md).
No learning-records directory is created until learner evidence justifies a record. DSA/interview exercises, complexity drills and related logs are excluded; existing unrelated history is preserved.
