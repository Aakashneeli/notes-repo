# Local storage → S3 — design-only learner note
Lesson 6. No account creation or deployment is part of this task.
Current adapter contract (put/read/delete) and local root assumptions:
Mapping of server storage key to bucket/object key:
Private access and worker credentials; no keys in code:
Cost categories and prerequisites before any future live trial:
Consistency across object write and metadata commit; orphan cleanup:
Failure classification, retries and idempotency behavior:
How worker on another machine reads the same bytes:
Test double plan and what it cannot prove about S3:
