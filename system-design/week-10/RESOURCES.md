# Week 10 Resources

## Knowledge
Official documentation checked 2026-09-19. Lessons supply the required teaching; these deepen or verify a mechanism.
- [C4 model, by Simon Brown](https://c4model.com/diagrams): context/container/deployment vocabulary; use while checking diagram zoom and consistent names.
- [draw.io local file saving](https://www.drawio.com/docs/getting-started/save-diagram-files/): editable .drawio/XML and local storage; use to open, save and reopen the five-page packet.
- [Python Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol): structural interfaces; use to verify that type hints do not validate runtime inputs.
- [Python tasks/timeouts](https://docs.python.org/3/library/asyncio-task.html): await, wait_for and cancellation; use when tracing the timeout example.
- [Python async development](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code): event-loop blocking; use to interpret the experiment.
- [Python logging](https://docs.python.org/3/library/logging.html): handlers and event recording; use for transferring JSON events to a real application logger.
- [Python unittest](https://docs.python.org/3/library/unittest.html): assertions and isolated async tests; use to read the supplied checks.
- [AWS bounded retries](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_mitigate_interaction_failure_limit_retries.html): retry caps, backoff and duplicate-side-effect risk; use in reliability policies.
- [AWS: making retries safe](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/): idempotency rationale; use when reviewing queue crash windows.
- [CloudWatch Logs concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html): events, streams, groups, retention and filters; use for a conceptual mapping, no cloud setup.
- [LangSmith observability concepts](https://docs.langchain.com/langsmith/observability-concepts): runs and traces; use to distinguish nested AI work from backend logs.
- [Redis cache-aside](https://redis.io/docs/latest/develop/use-cases/cache-aside/): cache misses, TTL and invalidation; use for the design route.
- [Redis INCR and rate-limit patterns](https://redis.io/docs/latest/commands/incr/): atomicity and expiry pitfalls; use for the quota test table.
- [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html) and [LIMIT/OFFSET](https://www.postgresql.org/docs/current/queries-limit.html): storage/write costs and stable ordering; use to evaluate a proposed query improvement.
- [OWASP API security](https://api-security.owasp.org/editions/2023/en/0x11-t10/): authorization, resource consumption and configuration threats; use for ordinary backend review.
- [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [GenAI risks](https://genai.owasp.org/llm-top-10/): injection, poisoning, disclosure and excessive agency; use to challenge controls at data/tool boundaries.
- [ADR community documentation](https://adr.github.io/): decision context and consequences; use when revising vague tool preferences.
- [A Philosophy of Software Design — John Ousterhout](https://web.stanford.edu/~ouster/cgi-bin/book.php): roadmap-named optional reading on modules and information hiding. Author page verified; full book not accessed. Use a legal owned/library copy for selected module chapters; no purchase required.
- [Designing Data-Intensive Applications — author site](https://dataintensive.net/): roadmap-named optional reliability/storage reading; editions vary, so choose sections by topic. Author page verified; full book not accessed. Use a legal owned/library copy and relate one claim to your failure trace.

## Wisdom (Communities)
- [LangChain community forum](https://forum.langchain.com/): optional practitioner discussion of AI workflow/tracing failures. Learner may ask one sanitized, reproducible question when local evidence is insufficient; no joining or posting is performed here.
No community preference has been assumed.

## Gaps and limits
Source links support teaching, not evidence that your system works. Current live pricing, account setup and deployed integrations were not tested. The diagram editor UI may vary by version; editable XML and Device save are the relevant verified concepts. No need to read whole books before building.
