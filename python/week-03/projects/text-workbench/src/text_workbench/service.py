"""Learner implementation: one file-processing workflow."""

from collections.abc import Callable
from pathlib import Path

from text_workbench.models import Config, Record


def read_utf8(path: Path) -> str:
    """Supplied I/O adapter; explicit encoding, errors propagate to caller."""
    return path.read_text(encoding="utf-8")


def process_file(path: Path, config: Config, reader: Callable[[Path], str] = read_utf8) -> Record:
    """Read once, reject raw text longer than max_chars, summarize, validate output.

    On success log INFO event processed with only characters/words via logger
    text_workbench.service. Never log source text or path. Allow I/O errors through.
    """
    raise NotImplementedError("Implement orchestration after lesson 8")
