"""Supplied focused checks; lessons 5/6/9 introduce each group before lesson 11's trace."""

import pytest
from fastapi.testclient import TestClient
from mechanisms import (
    Counter,
    DialInput,
    LimitReached,
    create_dependency_app,
    get_prefix,
)
from pydantic import ValidationError


def test_dial_normal():
    assert DialInput(label="  desk  ", level=0).model_dump() == {
        "label": "desk",
        "level": 0,
    }


@pytest.mark.parametrize(
    "data,field",
    [
        ({"label": "desk", "level": "2"}, "level"),
        ({"label": "desk", "level": True}, "level"),
        ({"label": "desk", "level": 6}, "level"),
        ({"label": " ", "level": 2}, "label"),
        ({"label": "desk", "level": 2, "colour": "red"}, "colour"),
    ],
)
def test_dial_rejects(data, field):
    with pytest.raises(ValidationError) as failure:
        DialInput(**data)
    assert failure.value.errors()[0]["loc"] == (field,)


def test_counter_state():
    counter = Counter()
    assert counter.advance() == 1
    assert counter.advance() == 2
    with pytest.raises(LimitReached):
        counter.advance()
    assert counter.snapshot() == {"value": 2}


def test_counter_snapshot_is_not_shared():
    counter = Counter()
    view = counter.snapshot()
    view["value"] = 99
    assert counter.snapshot() == {"value": 0}


def test_counter_instances_are_independent():
    first, second = Counter(), Counter()
    first.advance()
    assert second.snapshot() == {"value": 0}


def test_dependency_and_override():
    app = create_dependency_app()
    with TestClient(app) as client:
        assert client.get("/message").json() == {"message": "Hello, learner"}
        app.dependency_overrides[get_prefix] = lambda: "Welcome"
        try:
            assert client.get("/message").json() == {"message": "Welcome, learner"}
        finally:
            app.dependency_overrides.clear()
        assert client.get("/message").json() == {"message": "Hello, learner"}
