"""Learner-facing operational contract; intentionally red until implementation."""
import json
import re
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from operations import install_health, readiness
from observability import install_logging, request_id


@pytest.mark.parametrize("checks,ok", [({"postgres": True, "redis": True}, True),
    ({"postgres": True, "redis": False}, False), ({"postgres": False, "redis": True}, False),
    ({}, False), ({"postgres": True}, False),
    ({"postgres": True, "redis": True, "vector": False}, True)])
def test_readiness(checks, ok):
    status, body = readiness(checks)
    assert status == (200 if ok else 503)
    assert body == {"ready": ok, "checks": {k: checks.get(k, False) is True
                                          for k in ("postgres", "redis")}}


def test_routes_recheck_without_coupling_health():
    app = FastAPI()
    calls = []
    def checks():
        calls.append(1)
        return {"postgres": True, "redis": len(calls) == 1}
    install_health(app, checks)
    with TestClient(app) as client:
        assert client.get("/health").json() == {"alive": True}
        assert calls == []
        assert client.get("/ready").status_code == 200
        assert client.get("/ready").status_code == 503
        assert client.get("/health").status_code == 200
    assert len(calls) == 2


def test_probe_exception():
    app = FastAPI()
    def broken():
        raise OSError("postgres://private:secret@db")
    install_health(app, broken)
    with TestClient(app) as client:
        response = client.get("/ready")
    assert response.status_code == 503
    assert "secret" not in response.text


def test_id_validation():
    assert request_id("a-B_09") == "a-B_09"
    assert request_id("a" * 64) == "a" * 64
    for bad in (None, "", "x" * 65, "bad id", "line\nbreak", "é", "a/b"):
        assert re.fullmatch(r"[a-f0-9]{32}", request_id(bad))
    assert request_id(None) != request_id(None)


@pytest.mark.parametrize("path,status", [("/ok?token=private", 200), ("/missing", 404),
                                        ("/boom", 500)])
def test_logs(caplog, path, status):
    app = FastAPI()
    @app.get("/ok")
    def ok():
        return {"ok": True}
    @app.get("/boom")
    def boom():
        raise ValueError("private exception")
    install_logging(app)
    with caplog.at_level("INFO", logger="week7.http"):
        with TestClient(app, raise_server_exceptions=False) as client:
            response = client.get(path, headers={"X-Request-ID": "demo-7", "X-API-Key": "private"})
    assert response.status_code == status
    assert response.headers["X-Request-ID"] == "demo-7"
    events = [json.loads(r.message) for r in caplog.records if r.name == "week7.http"]
    assert len(events) == 1
    event = events[0]
    assert set(event) == {"event", "request_id", "method", "status", "duration_ms"}
    assert event["event"] == "http_request"
    assert event["request_id"] == "demo-7"
    assert event["status"] == status and event["method"] == "GET"
    assert event["duration_ms"] >= 0
    assert "private" not in json.dumps(event)
    if status == 500:
        assert response.json() == {"detail": "internal_error"}
