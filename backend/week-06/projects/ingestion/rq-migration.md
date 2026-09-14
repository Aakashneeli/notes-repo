# BackgroundTasks → RQ — required learner deliverable
Complete even if the optional live queue lab is skipped. Lesson 10.
Why the current API-process task can be lost:
Producer / dedicated Redis / worker boundaries and connection configuration:
Importable worker entry and serialized job_id (no live objects/secrets):
How the worker constructs adapters and reaches stored bytes:
Commit-before-enqueue gap and reconciliation/outbox concept:
Five domain states mapped to queue observations, including retrying:
Transient vs permanent error; total attempt budget; interval/scheduler:
How exceptions reach RQ and how domain failure remains visible:
Idempotent result effects, atomic claim, stale-running recovery/lease decision:
Redis persistence/eviction, restricted access, serializer trust:
Safe logs and job-description redaction:
Local optional evidence or explicitly unperformed:
What mocks cannot prove:
