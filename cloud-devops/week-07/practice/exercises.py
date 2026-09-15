"""Learner exercises: L5 and L8. Do not replace this with project code."""

def service_address(location):
    """Return ('127.0.0.1', 8077) for host; ('api', 8000) for worker.
    Raise ValueError for any other location.
    """
    raise NotImplementedError("Map the caller's network location")


def safe_fields(event):
    """Return a NEW dict containing only event, request_id, status keys that exist.
    Never mutate event. Ignore all other keys, including headers and body.
    """
    raise NotImplementedError("Use an allowlist, not a list of known secrets")
