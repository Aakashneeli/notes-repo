# Mission: Own safe document ingestion

## Why
Build toward independently designing, debugging and explaining Python-first AI backends.
This week turns a file upload into protected, stored, observable background work so later
AI features have trustworthy inputs and explicit failure behavior.

## Success looks like
- Independently implement the protected local upload and job-status contract.
- Reject unsafe inputs, preserve metadata, test failed extraction and repeated execution.
- Explain architecture, process lifetime, retries, idempotence and limiter placement.
- Produce security evidence, a job-state diagram, manual QA and migration notes.

## Constraints
- Python/basic Git exposure; no demonstrated mastery of the earlier backend starters.
- Flexible pace, short traces, progressive hints, recall and independent variations.
- All workspace changes local; no external provisioning, publishing or real secrets.
- Main implementation and assessment decisions belong to the learner.

## Out of scope
- Interview algorithm curricula and related exercises or logs.
- Production deployment, S3 provisioning, RAG implementation and rich-file extraction.
