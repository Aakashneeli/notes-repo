import json
import logging

import pytest
from examples import Badge, Booking, EventFormatter, StrictBooking
from pydantic import ValidationError


def test_dataclass_is_not_validator():
    assert Badge("Ada", "two").visits == "two"


def test_conversion_and_strictness():
    assert Booking(seats="2").seats == 2
    with pytest.raises(ValidationError):
        StrictBooking(seats="2")
    with pytest.raises(ValidationError):
        Booking(seats=0)
    with pytest.raises(ValidationError):
        Booking(seats=1, secret="not allowed")


def test_log_allowlist():
    record = logging.LogRecord("demo", logging.INFO, "", 0, "ready", (), None)
    record.secret = "hidden"
    assert json.loads(EventFormatter().format(record)) == {"level": "INFO", "event": "ready"}
