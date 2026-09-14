"""Beginner exercises; fill one function at a time in lessons 1, 5 and 7."""


def apply_changes(row: dict, changes: dict) -> dict:
    """Return a NEW merged dictionary; retain explicit False and leave row unchanged."""
    raise NotImplementedError("Lesson 1")


def supplied_fields() -> dict:
    """Define a tiny Pydantic model with hot default True; construct with hot=False.
    Return model_dump(exclude_unset=True). This is not the main project schema.
    """
    raise NotImplementedError("Lesson 5")


def page_done(rows: list[dict], done: bool, offset: int, limit: int) -> dict:
    """Filter by done, sort ascending id, then page; return items and filtered total.
    Inputs are already valid. Do not mutate rows.
    """
    raise NotImplementedError("Lesson 7")
