# Completion means observable ownership
Read in Lesson 13; learner completes with evidence, tutor reviews reasoning.

1. Implement: complete practice/exercises.py and project instrumentation.py without copying a project solution. Explain every import, callback, field and exception path.
2. Test: all four exercise tests and seven project tests pass. Add a meaningful negative test, such as leakage through error/answer content or a concurrent correlation bug.
3. Debug: deliberately reproduce one bug, predict the failing test, repair it, preserve output in the mistake log.
4. Diagram: five editable pages (context, container, sequence, data flow, deployment), saved/reopened; consistent names, labelled arrows and trust boundaries. Actual/fixture/proposed status explicit.
5. Decide: four ADRs with context, constraints, two alternatives, decision, consequences and measurable revisit trigger. Do not use fabricated experience.
6. Observe: correlate local success/failure logs; explain metrics versus traces, known-zero versus unknown cost and CloudWatch mapping.
7. Design: cache/rate-limit policy handles tenant isolation, versions, invalidation, expiry atomicity, burst limits and outage behavior.
8. Measure: repeat three configurations, retain denominators/errors, interpret burst queueing, identify a bottleneck and name a deferred optimization.
9. Secure: each sample threat plus one new scenario has an asset/boundary/control, attempted test or honest pending status, residual risk and owner.
10. Operate/write: rehearse the runbook on a fictional incident; write a concrete PR note; inspect a local Git diff and commit only intended paths.
11. Explain: answer the four source prompts (vector unavailable, retry choices, trust boundaries, first latency-spike inspection) from memory with a diagram and actual evidence.
12. Vary later: change a failure, corpus/tenant or operating constraint after a delay, predict the consequence, verify and revise.

Separate gates:
- Fixture completion proves local mechanisms only.
- Applying instrumentation/diagrams to a working actual backend requires its entrypoint/revision and happy/error/concurrent evidence. Unfinished Week 8/9 prerequisites keep this pending.
- No live cloud service is required by Week 10's conceptual CloudWatch review or documented Redis option. Do not claim a mock is a live integration.

Useful scoring per item: 0 no attempt; 1 copied/with full help; 2 independently explain and run; 3 independently debug and vary. Completion requires at least 2 everywhere relevant and 3 on implementation/failure variation. This is guidance, not an automatic grade.
