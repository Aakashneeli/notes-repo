# Week 11 — Cloud

TARGET_WEEK=11 resolves to article#week-11 in
`/home/an10/Downloads/ai-backend-roadmap.html`, exact title:
**AWS Deployment, CI/CD, Secrets, Cloud Logs, Runbooks, and Cost Control**.
Source inspected 2026-09-19; SHA-256:
`70466aa6c6ecb8ed7ca94c84882faa54f26147d180c9de17d5bf095fc945579e`.

Workspace: `cloud-devops/week-11/`. Existing cloud-devops fits the main objective;
no existing Week 11 or syllabus mismatch was found, so no naming exception applies.
Numbered article is authoritative, not the condensed sequence strip.

Deliverables: deployed API URL or documented private endpoint; deployment diagram/runbook;
CI/CD workflow and secret-management notes; cost-control checklist and rollback plan.
Conditional S3 integration applies only when the selected app stores uploads/artifacts.
All DSA/interview/complexity practice and related logs are excluded.

[Study desk](index.html) → [First lesson](lessons/0001-start.html).
[File introductions](plan/file-map.html) · [Coverage](plan/coverage.md) ·
[Sequence](plan/README.md) · [Assessment](plan/assessment.md) · [Verification](VALIDATION.md).

## Starting evidence
Week 7 Dockerfile/Compose remain unfinished and Week 10 progress is unchecked.
Python/basic Git exposure is self-reported, not independent mastery.
A supplied minimal FastAPI fixture enables deployment practice without pretending the
earlier AI backend is complete. Main Dockerfile, workflow, release gate and assessed
decisions are learner work. Existing implementations and records were not changed.

## Use
Start commands at `/home/an10/code/notes-repo/cloud-devops/week-11`, except explicitly
labelled host/repository commands. Lesson 1 sets up Python 3.12 with uv and requirements.lock.
Local examples need no AWS account/GPU. Docker labs need an accessible daemon and downloads.
AWS/hosted CI require learner accounts, permissions, credentials, pricing checks and action.
This authoring session performs no provisioning, publishing, account changes or messages.

Lessons teach each material at first use. assets/ shares local presentation; practice/
separates examples from exercises; projects/deployment/ is the assessed workspace; plan/
contains sequencing/coverage/progress; weekly-logs/ and codebase-reading/ are learner evidence.
maintenance/ and VALIDATION.md contain tutor checks, not learning claims.
