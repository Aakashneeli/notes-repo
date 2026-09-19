"""Learner: health gates for promotion. Pure decision function; no Docker/AWS side effects."""


def can_promote(status, ready, observed_release, expected_release):
    """True iff status==200, ready is True, and both release strings match and are nonempty."""
    raise NotImplementedError("Lesson 11: prevent false-positive promotion")
