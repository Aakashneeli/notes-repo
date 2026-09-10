"""Learner implementation: replace placeholder classes with Pydantic models.

Config: max_chars positive strict int, default 1_000_000; log_level restricted
uppercase DEBUG/INFO/WARNING/ERROR/CRITICAL, default INFO; forbid extra fields.
Record: characters and words nonnegative strict ints; forbid extra fields.
"""


class Config:
    def __init__(self, **data: object) -> None:
        raise NotImplementedError("Build Config with Pydantic after lesson 5")


class Record:
    def __init__(self, **data: object) -> None:
        raise NotImplementedError("Build Record with Pydantic after lesson 5")
