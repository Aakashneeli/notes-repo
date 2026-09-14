"""Unfinished beginner variations, introduced in lessons 3, 5, 8."""
def safe_event(job_id, state):
    """Return exactly {'event':'job_state','job_id':job_id,'state':state}."""
    raise NotImplementedError

def valid_text(data):
    """Return decoded UTF-8 text; raise ValueError for empty, NUL or invalid UTF-8."""
    raise NotImplementedError

def retry_decision(error_code, attempts, max_attempts=3):
    """Return retry only for storage_busy and attempts < max_attempts; else fail."""
    raise NotImplementedError
