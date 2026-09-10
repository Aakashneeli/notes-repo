"""Beginner practice only; progressive answers are in lessons 3, 4, 5, 6, 8."""

from collections.abc import Callable, Mapping


def label(value: str | None) -> str:
    """None -> '(untitled)'; other strings stripped, including empty strings."""
    raise NotImplementedError


def lengths(lines: list[str]) -> list[int]:
    """Return length of each string, in the same order."""
    raise NotImplementedError


def read_limit(env: Mapping[str, str]) -> int:
    """Use LIMIT or default '5'; int conversion, then reject values <= 0."""
    raise NotImplementedError


def describe(load: Callable[[], str]) -> str:
    """Call load once and return '<length> chars', without reading files here."""
    raise NotImplementedError
