"""Learner L7: see README contract. Keep dependencies injectable for tests."""

def readiness(checks):
    """Return (HTTP status int, public dict). Require postgres and redis, both True.
    Missing required keys fail closed. Ignore extra keys (vector is a placeholder).
    Body is {'ready': bool, 'checks': {'postgres': bool, 'redis': bool}}.
    """
    raise NotImplementedError("Implement a pure readiness policy")


def install_health(app, check_dependencies):
    """Register GET /health and /ready. /health must never call dependencies.
    /ready uses the supplied callable; exception => both checks False and 503.
    Use sync route def for synchronous network probes; no startup probe caching.
    """
    raise NotImplementedError("Add two routes with distinct meanings")
