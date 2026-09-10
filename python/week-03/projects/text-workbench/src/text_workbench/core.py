"""Learner implementation: deterministic text rules, with no I/O or logging."""


def normalize(text: str) -> str:
    """Collapse whitespace runs to one space and lowercase; retain punctuation."""
    raise NotImplementedError("Implement normalize after lesson 3")


def split_text(text: str) -> list[str]:
    """Split normalized text on single spaces; empty normalized text gives []."""
    raise NotImplementedError("Implement split_text after lesson 3")


def summarize(text: str) -> dict[str, int]:
    """Return normalized character count and token count as characters/words."""
    raise NotImplementedError("Implement summarize after lesson 3")
