# Completion means independent ability

For each requirement, attach implementation/test evidence, your explanation and help used.
Use the main project's contract tests plus your own cases; do not modify checks to accept bugs.
1. Implement upload and status independently, then explain a real sample from request to durable result.
2. Test both auth failures, unsupported/empty/oversize/unsafe inputs, exact limit and UTF-8 counting.
3. Debug a missing blob and metadata-write failure without leaking contents or damaging existing files.
4. Repeat a completed job; prove unchanged results/attempt count. Add a concurrent-claim test.
5. Explain parameter binding, CORS vs auth, process-local scheduling and production limiter placement.
6. Produce your own five-state diagram, failure/security notes, S3 and RQ migration decisions.
7. Complete Postman cases and graceful restart retrieval; label live RQ separately if attempted.
8. Vary one policy without copying, add a regression, read a real framework code path, review a Git diff.

## Exact source explain-backs — answer before opening notes
- Why should long-running ingestion not block the HTTP request?
- What happens if the worker crashes halfway through a job?
- What makes an upload unsafe?
- Where would you add rate limiting and why?

## Tutor rubric, revealed after an attempt
A sufficient first answer distinguishes acceptance from completion and explains timeout/resource costs.
A sufficient crash answer locates persisted state, lost in-process work, duplicate effects and recovery limits.
A sufficient upload answer covers untrusted names/types, content policy, resource limits and storage boundaries.
A sufficient rate-limit answer names the protected resource, caller identity, ingress/per-key boundary,
shared coordination and behavior when the limiter fails.
Do not award mastery for repeating those phrases: ask for a changed scenario and a test prediction.

## Delayed evidence
Two days later: reproduce the state graph and crash trace without notes.
About a week later: change the upload limit and add an independent failing-then-passing boundary test.
Record gaps honestly in weekly-logs/week-06.md, then revisit only the relevant lesson.
