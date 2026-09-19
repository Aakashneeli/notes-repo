# Folder/file-to-lesson map
Paths are relative to system-design/week-10. Every supplied learning file is listed; generated runtime captures, caches and optional exports are categories introduced in Lessons 1 and 10. Nothing generated certifies learning.
Folders: lessons = primary reading; reference = retrieval aids; practice = examples/exercises; projects = learner packet plus supplied infrastructure; plan = scope/sequence/evidence; templates = copyable prompts; weekly-logs/codebase-reading = learner notes; assets = shared presentation; maintenance = tutor verification.

| File | First lesson | Action and purpose |
|---|---|---|
| [README.md](../README.md) | [1](../lessons/0001-start.html#materials) | Read. Source mapping, starting commands and course organization. |
| [MISSION.md](../MISSION.md) | [1](../lessons/0001-start.html#materials) | Read. The independent-backend goal grounding each lesson. |
| [RESOURCES.md](../RESOURCES.md) | [1](../lessons/0001-start.html#materials) | Consult. Annotated primary sources; use a focused question, not a reading quota. |
| [NOTES.md](../NOTES.md) | [1](../lessons/0001-start.html#materials) | Leave tutor-maintained. Baseline and preferences; ask the tutor to amend when evidence changes. |
| [AI-USAGE.md](../AI-USAGE.md) | [1](../lessons/0001-start.html#materials) | Read and follow. Assistance boundaries and evidence honesty. |
| [.gitignore](../.gitignore) | [1](../lessons/0001-start.html#materials) | Read; normally leave. Excludes generated caches/environments, runtime captures and secrets. |
| [plan/README.md](../plan/README.md) | [1](../lessons/0001-start.html#materials) | Read. Flexible sequence and retrieval schedule. |
| [plan/coverage.md](../plan/coverage.md) | [1](../lessons/0001-start.html#materials) | Read; tutor maintains. Exact source-to-material mapping; not a mastery claim. |
| [plan/progress.md](../plan/progress.md) | [1](../lessons/0001-start.html#materials) | Update with evidence. Learner-owned checklist; never infer learning from author tests. |
| [plan/assessment.md](../plan/assessment.md) | [13](../lessons/0013-review.html#materials) | Read and demonstrate. Independent completion criteria and integration gates. |
| [plan/file-map.md](../plan/file-map.md) | [1](../lessons/0001-start.html#materials) | Consult; tutor maintains. First lesson, role and action for every supplied learning item. |
| [assets/course.css](../assets/course.css) | [1](../lessons/0001-start.html#materials) | Leave supplied infrastructure. Local shared stylesheet imports the established course asset; optional appearance work only. |
| [practice/examples.py](../practice/examples.py) | [2](../lessons/0002-boundaries.html#materials) | Read and run; leave unchanged. Completed catalog/timeout/retry examples; separate from main project. |
| [practice/exercises.py](../practice/exercises.py) | [2](../lessons/0002-boundaries.html#materials) | Edit incrementally. Learner boundary/retry/error-rate/cache exercises in Lessons 2,5,7,9. |
| [practice/test_exercises.py](../practice/test_exercises.py) | [2](../lessons/0002-boundaries.html#materials) | Read and run; preserve assertions. Four beginner checks; -k selects the current exercise. |
| [weekly-logs/week-10.md](../weekly-logs/week-10.md) | [1](../lessons/0001-start.html#materials) | Append. Predictions, observations, help used and spaced recall evidence. |
| [weekly-logs/mistakes.md](../weekly-logs/mistakes.md) | [13](../lessons/0013-review.html#materials) | Append. Actual failures, diagnosis and regression checks. |
| [codebase-reading/reading-log.md](../codebase-reading/reading-log.md) | [2](../lessons/0002-boundaries.html#materials) | Append. One focused docs/code question with path/revision and evidence. |
| [templates/review.md](../templates/review.md) | [13](../lessons/0013-review.html#materials) | Read/copy headings; leave template. Reusable delayed-retrieval record for the weekly log. |
| [templates/adr.md](../templates/adr.md) | [12](../lessons/0012-decisions.html#materials) | Read; leave template. Explains headings already present in four learner ADR files. |
| [projects/architecture-review/README.md](../projects/architecture-review/README.md) | [3](../lessons/0003-system-views.html#materials) | Read. Project entry, prior-work links and fixture limitations. |
| [projects/architecture-review/contract.md](../projects/architecture-review/contract.md) | [3](../lessons/0003-system-views.html#materials) | Read; use again in Lesson 8. Required deliverables and precise implementation behavior. |
| [projects/architecture-review/fixture.py](../projects/architecture-review/fixture.py) | [1](../lessons/0001-start.html#materials) | Read; leave infrastructure. Minimal async prerequisite; deliberate blocking/timeout modes. |
| [projects/architecture-review/instrumentation.py](../projects/architecture-review/instrumentation.py) | [8](../lessons/0008-instrumentation.html#materials) | Implement. Assessed event builder and async wrapper; intentionally unfinished. |
| [projects/architecture-review/run_observed.py](../projects/architecture-review/run_observed.py) | [8](../lessons/0008-instrumentation.html#materials) | Read and run. Infrastructure invokes success/error with generated IDs and emits JSON. |
| [projects/architecture-review/experiment.py](../projects/architecture-review/experiment.py) | [10](../lessons/0010-performance.html#materials) | Read and run. Bounded in-process burst harness, metrics and raw observations. |
| [projects/architecture-review/tests/test_contract.py](../projects/architecture-review/tests/test_contract.py) | [8](../lessons/0008-instrumentation.html#materials) | Read/run; preserve and extend. Contract assertions for output, failures, leakage and concurrency. |
| [projects/architecture-review/data/events.jsonl](../projects/architecture-review/data/events.jsonl) | [7](../lessons/0007-signals.html#materials) | Read; leave sample unchanged. Three fictional success/error events, not real measurements. |
| [projects/architecture-review/data/threat-cases.json](../projects/architecture-review/data/threat-cases.json) | [11](../lessons/0011-security.html#materials) | Read; leave sample unchanged. Fictional threats to classify and test safely. |
| [projects/architecture-review/diagrams/architecture.drawio](../projects/architecture-review/diagrams/architecture.drawio) | [3](../lessons/0003-system-views.html#materials) | Edit and reopen. Five unfinished diagram pages; Lessons 3–4 complete the lab. |
| [projects/architecture-review/architecture.md](../projects/architecture-review/architecture.md) | [3](../lessons/0003-system-views.html#materials) | Fill. Architecture explanations, inventory and actual integration status. |
| [projects/architecture-review/reliability.md](../projects/architecture-review/reliability.md) | [5](../lessons/0005-retries.html#materials) | Fill. Retry/timeout/queue/dead-job design with traces. |
| [projects/architecture-review/observability.md](../projects/architecture-review/observability.md) | [7](../lessons/0007-signals.html#materials) | Fill. Checklist, mapping and your sanitized local event evidence. |
| [projects/architecture-review/cache-rate-limit.md](../projects/architecture-review/cache-rate-limit.md) | [9](../lessons/0009-cache.html#materials) | Fill. Documented Redis design route, explicit test table and outage decisions. |
| [projects/architecture-review/performance.md](../projects/architecture-review/performance.md) | [10](../lessons/0010-performance.html#materials) | Fill. Actual learner measurements and evidence-backed bottleneck analysis. |
| [projects/architecture-review/security-review.md](../projects/architecture-review/security-review.md) | [11](../lessons/0011-security.html#materials) | Fill. Backend/AI review with controls, evidence, residual risks and owners. |
| [projects/architecture-review/runbook.md](../projects/architecture-review/runbook.md) | [6](../lessons/0006-jobs.html#materials) | Begin; finish in Lesson 12. Dead-job and latency response procedures with tabletop rehearsal. |
| [projects/architecture-review/pr-description.md](../projects/architecture-review/pr-description.md) | [12](../lessons/0012-decisions.html#materials) | Fill. Local reviewer-facing explanation; no PR is posted. |
| [projects/architecture-review/adrs/0001-vector-db.md](../projects/architecture-review/adrs/0001-vector-db.md) | [12](../lessons/0012-decisions.html#materials) | Fill. Learner vector-db decision with alternatives, constraints and revisit trigger. |
| [projects/architecture-review/adrs/0002-queue.md](../projects/architecture-review/adrs/0002-queue.md) | [12](../lessons/0012-decisions.html#materials) | Fill. Learner queue decision with alternatives, constraints and revisit trigger. |
| [projects/architecture-review/adrs/0003-model-provider.md](../projects/architecture-review/adrs/0003-model-provider.md) | [12](../lessons/0012-decisions.html#materials) | Fill. Learner model-provider decision with alternatives, constraints and revisit trigger. |
| [projects/architecture-review/adrs/0004-deployment.md](../projects/architecture-review/adrs/0004-deployment.md) | [12](../lessons/0012-decisions.html#materials) | Fill. Learner deployment decision with alternatives, constraints and revisit trigger. |
| [reference/glossary.html](../reference/glossary.html) | [1](../lessons/0001-start.html#materials) | Consult. Shared vocabulary; explains unfamiliar terms at point of use. |
| [reference/review-card.html](../reference/review-card.html) | [13](../lessons/0013-review.html#materials) | Read after recall. Compact failure/security/performance recall aid. |
| [maintenance/validate.py](../maintenance/validate.py) | [13](../lessons/0013-review.html#materials) | Run; tutor maintains. Static navigation/map/diagram/syntax and instructor checks; not assessment. |
| [maintenance/test_infrastructure.py](../maintenance/test_infrastructure.py) | [13](../lessons/0013-review.html#materials) | Read/run; tutor maintains. Completed examples/harness tests plus event-check sensitivity; no project solution. |
| [maintenance/browser-check.cjs](../maintenance/browser-check.cjs) | [13](../lessons/0013-review.html#materials) | Optional author run. Headless Chromium layout check; requires externally available Playwright. |
| [maintenance/author-results.md](../maintenance/author-results.md) | [13](../lessons/0013-review.html#materials) | Read; tutor-maintained. Author experiment observations, deliberately separate from learner records. |
| [VALIDATION.md](../VALIDATION.md) | [13](../lessons/0013-review.html#materials) | Read; tutor-maintained. Precisely what was tested and remaining limits. |
| [index.html](../index.html) | [1](../lessons/0001-start.html#materials) | Open/navigate. Study desk links every lesson and working material via the file map. |
| [lessons/0001-start.html](../lessons/0001-start.html) | [1](../lessons/0001-start.html) | Read, predict, practice, then record evidence. Trace one request and separate existing evidence from assumptions. |
| [lessons/0002-boundaries.html](../lessons/0002-boundaries.html) | [2](../lessons/0002-boundaries.html) | Read, predict, practice, then record evidence. Inject a small interface and explain who owns policy versus storage. |
| [lessons/0003-system-views.html](../lessons/0003-system-views.html) | [3](../lessons/0003-system-views.html) | Read, predict, practice, then record evidence. Create context and container views without claiming unbuilt components exist. |
| [lessons/0004-request-views.html](../lessons/0004-request-views.html) | [4](../lessons/0004-request-views.html) | Read, predict, practice, then record evidence. Finish sequence, data-flow and deployment views that answer different questions. |
| [lessons/0005-retries.html](../lessons/0005-retries.html) | [5](../lessons/0005-retries.html) | Read, predict, practice, then record evidence. Choose retries using deadlines, repeatability and observable failure. |
| [lessons/0006-jobs.html](../lessons/0006-jobs.html) | [6](../lessons/0006-jobs.html) | Read, predict, practice, then record evidence. Describe a retry-safe job transition and a controlled replay. |
| [lessons/0007-signals.html](../lessons/0007-signals.html) | [7](../lessons/0007-signals.html) | Read, predict, practice, then record evidence. Use a request ID to turn a symptom into a testable hypothesis. |
| [lessons/0008-instrumentation.html](../lessons/0008-instrumentation.html) | [8](../lessons/0008-instrumentation.html) | Read, predict, practice, then record evidence. Implement request-correlated AI logs and test both outcomes. |
| [lessons/0009-cache.html](../lessons/0009-cache.html) | [9](../lessons/0009-cache.html) | Read, predict, practice, then record evidence. Specify tenant-safe keys, staleness and atomic quotas. |
| [lessons/0010-performance.html](../lessons/0010-performance.html) | [10](../lessons/0010-performance.html) | Read, predict, practice, then record evidence. Run a controlled latency experiment and separate waiting from work. |
| [lessons/0011-security.html](../lessons/0011-security.html) | [11](../lessons/0011-security.html) | Read, predict, practice, then record evidence. Turn backend and AI threats into controls with falsifiable checks. |
| [lessons/0012-decisions.html](../lessons/0012-decisions.html) | [12](../lessons/0012-decisions.html) | Read, predict, practice, then record evidence. Produce four reasoned ADRs, an actionable runbook and a reviewable change description. |
| [lessons/0013-review.html](../lessons/0013-review.html) | [13](../lessons/0013-review.html) | Read, predict, practice, then record evidence. Complete an independent implementation, debugging and explain-back review. |

Navigation: every lesson links back to the desk and forward/back through the sequence. The topic README/index and repository organization link this week. Shared style is imported from backend/week-04/assets/course.css; do not edit the earlier course asset for a Week 10-only change.
