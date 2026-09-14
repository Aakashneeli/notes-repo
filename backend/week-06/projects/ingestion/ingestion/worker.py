"""Learner: small sync extraction function callable after HTTP response.
Claim pending->running, read persisted bytes, compute characters/words, complete.
Duplicate completed/running calls no-op. Missing blob => failed/storage_missing.
Catch anticipated decode/storage failures; safe code only, no raw contents in logs.
No automatic recovery from abandoned running jobs in the base path.
"""
def run_job(job_id, repo, storage):
    raise NotImplementedError("Implement claim, extraction, terminal state and sanitized event logs")
