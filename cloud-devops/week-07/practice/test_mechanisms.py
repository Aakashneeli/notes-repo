import json
import pytest
from fastapi.testclient import TestClient
from mechanisms import choose_status, demo_app, event_line


@pytest.mark.parametrize("checks, expected", [({}, 503), ({"db": True}, 200),
                         ({"db": True, "queue": False}, 503)])
def test_status(checks, expected):
    assert choose_status(checks) == expected


def test_json():
    assert json.loads(event_line("GET", 503))["status"] == 503


def test_middleware():
    with TestClient(demo_app()) as client:
        response = client.get("/accepting")
    assert response.status_code == 503
    assert response.headers["X-Lesson"] == "traced"
