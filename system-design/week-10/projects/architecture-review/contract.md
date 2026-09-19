# Project contract
Read in Lesson 3; use implementation details in Lesson 8. The learner makes the design decisions.

## Required packet
- Five pages in diagrams/architecture.drawio: Context, Containers, Sequence, Data flow, Deployment.
- architecture.md explains each page, actual/fixture/proposed inventory and evidence.
- Four ADRs: vector DB, queue, model provider, deployment.
- reliability.md, observability.md, cache-rate-limit.md, performance.md, security-review.md, runbook.md, pr-description.md.
- Implement instrumentation.py; retain meaningful tests. No finished project solution is supplied.

## build_event(request_id, model, elapsed_ms, status, hits, usage, rates)
Return exactly:
event="ai.request", request_id, model, latency_ms, status, retrieval_hits,
input_tokens, output_tokens, estimated_cost_usd.
Copy supplied safe metadata into these fields; no prompt, answer, arbitrary usage keys or exception messages.
Preconditions: nonempty server-generated safe request ID; nonempty configured model name; finite nonnegative elapsed milliseconds; status ok/error; nonnegative integer hits. Rates have nonnegative finite input/output USD per million; supplied counts, when present, are nonnegative integers. Input validation beyond these trusted preconditions is an optional extension, not hidden required behavior.
If usage is None or either token count is absent, both token fields and cost are None. If both counts exist, preserve them, including zero.
Cost = (input_tokens*rates["input"] + output_tokens*rates["output"])/1_000_000.
The sample rates are fictional, not current provider pricing.

## async observe(operation, emit, request_id, model, rates)
operation is a zero-argument async callable; call/await it exactly once.
Success result is a dict with hits and usage; it may contain sensitive answer text.
Measure elapsed time with a monotonic/performance clock. Emit exactly one build_event with status ok, returned hits/usage; return the identical result object.
On an ordinary Exception, emit one error event with hits=0, usage=None, then re-raise the identical exception. No exception content in events. No retry. Never return success on failure.
Request IDs are passed explicitly per call; no shared mutable ID.
Cancellation (BaseException) may propagate without an application event; resource cleanup must not suppress it.
Scope assumption: emit is synchronous, reliable and does not block significantly. Discuss emitter failure/backpressure in observability.md; the starter contract does not solve production telemetry transport.

## Data and edge cases
Use fictional data/events.jsonl for reading; threat-cases.json for tabletop testing.
Tests cover known cost, unknown/partial usage, zero cost, extra sensitive fields, result identity, exception identity, exact call/event count and concurrent correlation.
Add your own regression for a discovered failure. Initial NotImplementedError failures are intentional, not test skips or passing evidence.

## Integration gate
Record the actual earlier backend path/revision and entrypoint; keep its code/progress intact.
When it runs, apply equivalent event construction at a real request/AI call seam; correlate request ID through jobs/traces where applicable.
Verify happy request, dependency timeout, concurrent IDs and no sensitive payload export.
Until then label all implementation evidence fixture-only and real integration pending.

## Local experiment
Three configurations, count 20: cooperative/c1, cooperative/c4, blocking/c4; at least three repetitions each, then one independent variation.
Retain errors, p50/p95, throughput and environment. Explain measured burst queueing versus service time.
No real external latency, throughput guarantee or deployment verification is implied.
