# Failure modes — learner owned
Lesson 8: for each case give last durable fact, client observation, safe code/log, retry or fail,
cleanup/reconciliation and one test or explicit test limitation.
- Invalid upload before persistence.
- Disk creation failure.
- Blob stored, metadata insert fails.
- Process dies between blob write and metadata insert.
- Metadata commits, scheduling is lost.
- Worker cannot read stored blob.
- Worker dies while running or after result write but before completion.
- Metadata database unavailable while recording failure.
- Duplicate delivery and completed-job repeat.
- Retry budget exhausted; non-transient error.

Own five-state arrows (plain-text fallback for the Mermaid diagram):
Own observations and recovery limits:
