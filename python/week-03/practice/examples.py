"""Completed teaching examples, separate from assessed text processing."""

import json
import logging
from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field, ValidationError


@dataclass
class Badge:
    name: str
    visits: int = 0


class Booking(BaseModel):
    model_config = ConfigDict(extra="forbid")
    seats: int = Field(gt=0)


class StrictBooking(BaseModel):
    seats: int = Field(gt=0, strict=True)


class EventFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps({"level": record.levelname, "event": record.getMessage()})


def demonstrate() -> None:
    print(Badge("Ada", "two"))  # Deliberately shows absent runtime type enforcement.
    print(Booking(seats="2").model_dump())
    try:
        StrictBooking(seats="2")
    except ValidationError:
        print("strict rejected")
    record = logging.LogRecord("demo", logging.WARNING, "", 0, "retry", (), None)
    print(EventFormatter().format(record))


if __name__ == "__main__":
    demonstrate()
