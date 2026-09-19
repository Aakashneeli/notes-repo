# Author verification — 2026-09-19

## Source and preservation

- Validated TARGET_WEEK=11 against article#week-11, its exact title, rationale,
  seven subtopics, six labs, four deliverables and four explain-back prompts.
  Mapping/hash are in README and coverage. Algorithm-interview material is excluded.
- Inspected repository organization, shared assets, baseline learning record, Week 7
  unfinished Dockerfile/Compose and Week 10 unassessed progress. No mastery inferred.
- Added cloud-devops/week-11 and its topic links/organization entry. Existing Week 10
  content and the user's pre-existing WORKSPACE-STRUCTURE changes were preserved.
  No Git commit, push, publication, message, account change or cloud provisioning occurred.

## Runnable checks actually performed

- Python 3.12.14: resolved and installed 23 pinned packages from requirements.lock.
  Author environment now uses ignored generated/python rather than a temporary interpreter.
- `python -m pytest maintenance/test_examples.py projects/deployment/fixture -q`:
  **4 passed**. Fixture tests cover normal, absent/wrong key, missing configuration,
  dependency failure, readiness, release, request ID and absence of the dummy secret in logs.
  TestClient required execution outside sandbox thread/socket restrictions; its initial
  sandbox invocation stalled. No AWS or network service was involved in those unit tests.
- `python practice/examples.py`: matched the four documented output lines, including
  illustrative $5.00, wrong release and the two failing request IDs.
- Temporary isolated answer audit: all three revealed beginner answers passed their
  tests. Mutations omitting IPv4 costs, ignoring port matching and excluding status 500
  were rejected. An always-promote main-project mutation was rejected. Learner files
  remained unchanged; no completed main gate was installed.
- `python -m pytest practice/test_exercises.py projects/deployment/tests -q`:
  **10 expected NotImplementedError failures** (3 exercises, 7 promotion cases).
  These are unfinished learner work, not infrastructure defects.
- Learner Dockerfile: expected `file with no instructions` build failure confirmed.
  Workflow YAML is an intentionally inactive empty-jobs starter, not working hosted CI.
- Separate temporary author image built with the pinned lock and fixture on
  python:3.12-slim. Three disposable containers verified normal/missing-key/dependency
  states over real localhost HTTP: health, readiness, authorized/unauthorized responses,
  release, request ID, safe logs and UID/GID 65534. The good release remained ready
  during candidate failure. Stop/rename/restart preserved its configuration.
  This validates supplied fixture/runtime behavior, not the learner Dockerfile or AWS.
- All three disposable author containers were removed. Automatic approval review initially
  rejected removal of image `week11-author-fixture:20260919` because its usage limit was
  reached. After the stated retry time passed, the same cleanup was approved and succeeded.
  The temporary author image is removed; ordinary downloaded base layers/build cache may
  remain. No AWS resources were created.
- Ruff passes for practice, project and maintenance Python. Python AST parsing passes.
  `git diff --check` passes. Shell starting directories, file references and transitions
  were reviewed against actual paths; live placeholders remain explicitly marked.

## Navigation and presentation

- `python maintenance/verify.py`: **60 supplied files mapped; 318 local links/anchors
  checked**, including the imported shared stylesheet and previous-week bridges.
  Generated interpreter/environment/caches are excluded as tooling categories.
- Chromium 152: all 15 HTML pages checked at 1280px and 390px viewport widths;
  shared styles loaded, one h1 per page, no page-level horizontal overflow or JS errors.
- Visually inspected desktop/mobile study desks and page 1 of the A4 deployment lesson
  PDF. Print rendering generated four pages; disclosure display was checked in print mode.
  These checks preceded the final added image-user bridge and optional rollback command
  disclosure; their HTML links/syntax were checked afterward, but no exhaustive visual
  review of every printed page, screen reader or browser engine was performed.
- Primary AWS, Docker, FastAPI and GitHub documentation opened and reviewed; pricing
  is intentionally an input the learner must verify by region/account/date, not a quote.
- Attempted to open lesson 1 with xdg-open. The desktop browser failed under sandbox
  socket restrictions; open the study-desk/lesson links manually. This does not affect
  the earlier successful headless Chromium layout checks.

## Teaching sufficiency review (separate from tests)

Reviewed every lesson for a defined outcome, mechanism explanation, worked trace,
failure diagnosis, guided action/feedback, independent variation and evidence destination.
Added a base-image/non-root/output-buffering bridge before Dockerfile implementation and
an explicit optional host switch/recovery pattern before independent runbook work.
Small exercise answers use progressive disclosures; main project decisions and release
gate remain unfinished. File introductions identify read/edit/run/record ownership.
Progress, session, mistake and reading records remain unassessed/empty of invented evidence.

## Limits and next verification

- AWS CLI is not installed here; account IAM, SSH host access, EC2 deployment, ECR push,
  S3/RDS integration, CloudWatch delivery, budget notifications, shutdown and billing
  were **not executed**. Official command documentation was checked, not live behavior.
- No hosted GitHub Actions run; no actual private endpoint exists from this session.
- The fixture has no upload requirement. The learner must explicitly decide whether S3
  is not applicable or implement/test it in the chosen real ingestion app.
- The fixed dependency set emits upstream Starlette warnings about HTTPX TestClient and
  AnyIO BlockingPortal deprecations. Tests pass; future dependency refresh should revisit
  those APIs rather than suppressing warnings or assuming eternal compatibility.
- Main Dockerfile, CI workflow, release gate, operating decisions and real cloud evidence
  are intentionally learner-owned. Author validation does not satisfy their assessment.
