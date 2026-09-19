"""Learner-owned small exercises. Lessons 2, 5, 7, 9 introduce these."""
def retryable(status, safe_to_repeat):
    """True only for 429/503 AND safe_to_repeat; no retries of 400/401/403."""
    raise NotImplementedError("Lesson 5")


def cache_key(tenant, corpus_version, query):
    """Return unambiguous JSON encoding of [tenant, corpus_version, query]."""
    raise NotImplementedError("Lesson 9")


def error_rate(statuses):
    """Fraction of statuses >=500; empty input returns 0.0."""
    raise NotImplementedError("Lesson 7")


def label(item_id, catalog):
    """Ask injected catalog.title(item_id), then uppercase the returned title."""
    raise NotImplementedError("Lesson 2")
