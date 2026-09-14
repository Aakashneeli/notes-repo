"""Completed mechanism examples for lessons 5, 6 and 9; not a Task API solution.

Read the named section when its lesson introduces it. No task routes, CRUD,
project authentication or assessed project schemas are implemented here.
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict, Field


class DialInput(BaseModel):
    """A strict, bounded input example, introduced in lesson 5."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    label: str = Field(min_length=1, max_length=12)
    level: int = Field(strict=True, ge=0, le=5)


class LimitReached(Exception):
    """A domain failure; deliberately has no HTTP status."""


class Counter:
    """Tiny stateful service for lesson 6; call serially in this demonstration."""

    def __init__(self, maximum: int = 2) -> None:
        self._value = 0
        self._maximum = maximum

    def advance(self) -> int:
        candidate = self._value + 1
        if candidate > self._maximum:
            raise LimitReached("Counter is full")
        self._value = candidate
        return self._value

    def snapshot(self) -> dict[str, int]:
        return {"value": self._value}


def get_prefix() -> str:
    """A replaceable input supplier for lesson 9; not authentication."""
    return "Hello"


def create_dependency_app() -> FastAPI:
    """A minimal dependency example, separate from the assessed project."""
    app = FastAPI()

    @app.get("/message")
    def message(prefix: Annotated[str, Depends(get_prefix)]) -> dict[str, str]:
        return {"message": f"{prefix}, learner"}

    return app
