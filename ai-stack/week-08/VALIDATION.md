# Author verification — 2026-09-17

## Source and preservation
Resolved exact numbered article #week-8 in /home/an10/Downloads/ai-backend-roadmap.html:
Raw LLM APIs, Embeddings, Vector DBs, Manual RAG, and Retrieval Evaluation.
Read agreement, sequencing, adjacent weeks, project ladder and existing workspace records.
Used ai-stack/week-08; no existing same-number workspace or mismatch found.
Added topic navigation and one organization entry. Existing Week 1 learner edits and untracked
hello.py were left intact. No commit, publishing, account changes or external messages.

## Executed checks
- CPython 3.14.7/Linux with the exact 30-package core set in requirements.lock, installed
  into /tmp/week08-author-venv. Core installation required network access outside the sandbox.
- `python -m pytest maintenance -q`: **19 passed**, including actual embedded Qdrant
  close/reopen persistence and filtering; structured output; chunk/vector/evaluation examples;
  fixture/20 seed validation; dry provider request; a small FastAPI TestClient echo boundary.
- Three deliberately wrong variants distinguished: raw dot product instead of cosine,
  duplicate final chunk tail, and an unknown-inclusive evaluation denominator.
- All six `python -m practice.examples NAME` commands executed with their documented outputs.
  Provider dry run sent no HTTP request. Bridge command executed from projects/manual-rag
  and produced `6 returns red`, verifying the explicit directory transition.
- `python -m pytest projects/manual-rag/tests practice/test_exercises.py --collect-only -q`:
  **35 checks collected**. Full run: **35 expected NotImplementedError failures** at learner
  stubs, not skipped/xfail-masked tests. The main implementation was not supplied or overwritten.
- `python maintenance/verify.py`: **59 supplied files** checked for complete first-lesson map,
  local HTML/Markdown/CSS links and HTML anchors, Python/JSON syntax, basic HTML metadata.
- `git diff --check`: passed. Command starting paths were reviewed against the actual tree;
  project HTTP smoke commands remain conditional on learner implementation.

## Browser and teaching review
Headless Chromium loaded all 17 weekly HTML pages at 1280px and 390px widths: shared styles
loaded and no document-level horizontal overflow. Code/table regions intentionally scroll.
Visually inspected Lesson 7 screenshots at desktop/mobile widths and in print media.
Print helper expanded every answer disclosure on the inspected page. Full paginated printing,
screen-reader operation and every browser engine were not tested. No claim of a full accessibility audit.
Temporary screenshots were verification artifacts, not course files.
Opening Lesson 1 with xdg-open was attempted but the desktop browser hit the sandbox's
socket restriction; use the study-desk/lesson links directly. Headless visual checks above
ran successfully with the necessary permissions.

Reviewed teaching sufficiency separately in plan/teaching-review.md: traces, failure cases,
guided checks/hints, independent variations, targeted bridges and delayed retrieval.
Coverage is recorded in plan/coverage.md; neither review establishes learner mastery.

## Environment notes and limits
The socket-restricted sandbox stalled FastAPI TestClient and blocked Chromium startup. Both
checks passed outside that sandbox; the stalled test was interrupted. The installed Starlette
emits HTTPX/BlockingPortal deprecation warnings; tested behavior passed, warnings remain disclosed.
Pinned packages reflect the verified Python 3.14 environment; other platforms/interpreters untested.

Not executed: optional FastEmbed install/model-weight download/semantic_probe, live provider
calls, the learner's full RAG server/curl workflow, real ingestion integration, Qdrant server or
other store deployments, hosted services, and actual 15–25-case learner evaluation. Optional
FastEmbed is version-bounded but not locked or runtime-verified. Its API was checked against
official documentation. No GPU, provider key or paid resource was used.

Project contracts were collected and inspected; a complete passing learner RAG implementation
was deliberately not authored. Full project correctness must be demonstrated by learner code.
The known-vector store check proves mechanics, not semantic quality or production readiness.
Provider/real-model actions have explicit prerequisites and separate evidence slots.
No progress item was marked learned. Existing learner evidence remains unchanged.
