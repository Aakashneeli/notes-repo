"""Learner work. Keep examples.py unchanged; implement one function at a time."""
def state_patch(state):
    """Return only {'urgent': bool}; 'outage' anywhere, case-insensitive; don't mutate input."""
    raise NotImplementedError("Lesson 2")


def next_queue(state):
    """Return 'fast' for urgent=True, otherwise 'normal'."""
    raise NotImplementedError("Lesson 3")


def allowed_lookup(raw):
    """Return validated T-XX ticket ID; reject extras, wrong types and bad syntax with ValueError."""
    raise NotImplementedError("Lesson 4")


def slowest(spans):
    """Return name with greatest end_ms-start_ms; unique maximum, nonempty flat spans."""
    raise NotImplementedError("Lesson 7; do not add parent and child times")
