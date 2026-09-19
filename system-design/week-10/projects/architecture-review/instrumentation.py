"""Assessed learner file. No project implementation is supplied."""
def build_event(request_id, model, elapsed_ms, status, hits, usage, rates):
    """Return only contract.md's allowlisted fields. Rates are fictional USD/million."""
    raise NotImplementedError("Lesson 8: structured AI event")


async def observe(operation, emit, request_id, model, rates):
    """Await operation once; emit one event on success/failure; preserve result/error."""
    raise NotImplementedError("Lesson 8: instrument the seam")
