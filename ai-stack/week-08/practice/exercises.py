"""Learner-owned drills. Hints/answers are in lessons 3, 5 and 7."""


def text_from_deltas(events):
    """Return concatenated non-null choices[0].delta.content; ignore empty choices."""
    raise NotImplementedError("Read Lesson 3; events are decoded dictionaries, not raw SSE bytes")


def safe_overlap(size, overlap):
    """Return True only for integer size > 0 and integer 0 <= overlap < size; reject bool."""
    raise NotImplementedError("Read Lesson 5")


def allowed_hits(hits, tenant):
    """Return only dictionaries whose tenant equals tenant; preserve original order."""
    raise NotImplementedError("Read Lesson 7")
