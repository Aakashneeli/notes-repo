"""Learner L8: request correlation and one JSON event per handled response/error."""

def request_id(candidate):
    """Accept ASCII [A-Za-z0-9_-] of length 1..64, otherwise generate uuid4().hex."""
    raise NotImplementedError("Validate client input; generate a safe replacement")


def install_logging(app):
    """Register middleware: set request.state.request_id before call_next;
    return X-Request-ID and emit one JSON object through logger 'week7.http'.
    Fields: event='http_request', request_id, method, status, duration_ms >= 0.
    No URL/query/body/headers/secrets or raw exception messages.
    Unexpected exception: return sanitized JSON {'detail':'internal_error'} with 500,
    correlated header and event. Configure StreamHandler(stdout) once per logger.
    """
    raise NotImplementedError("Implement safe correlated structured logs")
