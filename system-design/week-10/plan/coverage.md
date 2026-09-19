# Source coverage — Week 10
Authority: /home/an10/Downloads/ai-backend-roadmap.html, numbered article #week-10.
Exact title: **System Design, LLD/HLD, Observability, Performance, Reliability, and Security Review**.
Workspace: **system-design/week-10/**. Existing best-fit topic; no mismatch or naming exception.
Main deliverables: five diagram views + written architecture; four ADRs; safe AI/request logs + checklist; cache/rate-limit design; measured performance note; backend/AI security review.
Validation of numbering/title performed before authoring on 2026-09-19.

| Source requirement | Lessons | Practice/artifact | Demonstrated ability evidence |
|---|---|---|---|
| Rationale: reason about API/DB/jobs/vector/RAG/agent/Docker together | 1–4 | architecture.md; prior-project inspection | Trace one path and label actual/fixture/proposed. |
| LLD: modules, service/repository boundaries, DI, useful interfaces/protocols | 2 | examples.py; exercises.label; reading-log | Inject a fake, predict calls, vary an interface and explain its limit. |
| HLD: clients, API, workers, DB, Redis, vector DB, object storage, provider, observability | 3–4 | Five-page draw.io packet; architecture.md | Explain component ownership and arrow data/protocol, including absent/proposed components. |
| Reliability: timeouts, retries, circuit-breaker awareness | 5 | retryable exercise; reliability.md | Bound attempts/deadlines, classify errors, explain open/probe recovery. |
| Idempotency, queue retries, dead jobs | 6 | Crash-point table; reliability.md; runbook.md | Reason across write/ack crashes and concurrent claims; controlled replay. |
| Observability: structured logs, request IDs, latency, error rate | 7–8 | events.jsonl; error_rate; instrumentation.py + seven tests | Correlate concurrent calls; preserve outcomes; emit safe success/error events. |
| CloudWatch mapping and LangSmith traces | 7–8 | observability.md; sources | Distinguish logs/metrics/trace children, stream/group/retention and privacy; conceptual only. |
| Performance: indexes, pagination, caching, embedding batching, async I/O/blocking | 9–10 | cache-key check; design note; performance.md; fixture experiment | Predict version/isolation misses; explain index tradeoff and stable cursor; measure blocking and discuss batching bounds. |
| Security: injection, poisoning, leakage, unsafe tools, dependency risks; backend review | 11 | Six threat cases + one learner variation; security-review.md | Name deterministic boundary controls, actual test or pending status, residual risk. |
| Technical writing: ADRs, runbooks, architecture notes, PR descriptions | 3–4,6,12 | Four adrs/ files; architecture.md; runbook.md; pr-description.md | Defend alternatives, rehearse an incident, explain before/after and validation. |
| Lab 1: draw.io/Excalidraw context, container, sequence, data-flow, deployment diagrams | 3–4 | diagrams/architecture.drawio (draw.io route) | Save/reopen five consistent labelled views; no finished design supplied. |
| Lab 2: four ADR-style notes: vector DB, queue, model provider, deployment | 12 | adrs/0001..0004 | Write own constraint-based choices, costs, alternatives and revisit triggers. |
| Lab 3: add request-ID and AI logs: model, latency, token/cost estimate, retrieval hits | 7–8 | instrumentation.py; run_observed.py; observability.md | Local implementation tests plus distinct actual-backend integration gate. |
| Lab 4: caching/rate-limit awareness with Redis or documented design | 9 | cache-rate-limit.md | Document keys, TTL, races, invalidation, identity/quota, outage and test table. |
| Lab 5: one simple latency/load experiment and bottleneck note | 10 | experiment.py; performance.md | Three configurations repeated, failures counted, competing hypothesis and independent variation. |
| Deliverable: architecture packet with written explanation | 3–4,12 | Five diagrams; architecture.md; four ADRs | Reader can follow success/failure/data/deployment and explain assumptions. |
| Deliverable: observability checklist and log examples | 7–8 | observability.md | Actual local success/failure events with safe fields, missing usage and correlation. |
| Deliverable: bottlenecks, quick wins, what not to optimize yet | 10 | performance.md | Measurements justify one improvement and one deferral; fixture limitations explicit. |
| Deliverable: backend and AI security review | 11 | security-review.md | Control/test/residual-risk reasoning for all supplied cases and a variation. |
| Explain-back: vector DB slow/unavailable | 5,13 | Assessment prompt 1 / weekly log | Trace timeout/retry/failure/telemetry rather than invent empty retrieval. |
| Explain-back: retry versus not retry | 5–6,13 | Assessment prompt 2 | Handle transient, permanent and uncertain-side-effect cases. |
| Explain-back: trust boundaries | 4,11,13 | Assessment prompt 3 / diagram | Locate identity, uploaded/retrieved data, tools and exports. |
| Explain-back: first production latency-spike inspection | 7,10,12–13 | Assessment prompt 4 / runbook | Scope metrics then correlate a slow request; distinguish wait, dependency and blocking. |
| Source resources: Software Design book; DDIA selected reliability/storage; AWS/CloudWatch | 2,5–7,12 | RESOURCES.md; focused reading log | Official author/docs sources, optional legal book reading; no mandatory purchase. |
| Continuous habits: tests, reading, debugging, Git, notes and explain-back | 2,8,12–13 | Tests; codebase-reading; weekly logs; exact-file local commit | Preserve failed attempt, repair, assistance and later independent variation. |

## Exclusions and gates
All DSA, NeetCode, interview algorithm work, complexity drills and associated logs are excluded. Normal lists/dictionaries support backend examples. Unrelated historical learner files are preserved.
Detailed future-week material and cloud provisioning are excluded. CloudWatch is a mapping, Redis takes the source's documented-design option, and draw.io satisfies the allowed diagram tool choice.
All in-scope source requirements have teaching and evidence paths. No learner achievement is claimed. Main project implementations, diagrams/decisions, measured learner evidence and actual backend integration remain learner work. Earlier Week 8/9 stubs mean actual integration is currently pending; a fixture is not silently counted as that deliverable.
