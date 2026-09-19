import logging

from app import app
from fastapi.testclient import TestClient


def test_routes(monkeypatch, caplog):
    monkeypatch.setenv("API_KEY", "test-only")
    monkeypatch.setenv("RELEASE", "test-release")
    monkeypatch.delenv("FAIL_MODE", raising=False)
    caplog.set_level(logging.INFO, logger="uvicorn.error")
    with TestClient(app) as client:
        assert client.get("/health").json() == {"alive": True, "release": "test-release"}
        assert client.get("/ready").status_code == 200
        assert client.get("/message").status_code == 401
        response = client.get("/message", headers={"X-API-Key": "test-only"})
        assert response.status_code == 200
        assert len(response.headers["X-Request-ID"]) == 32
        assert "test-only" not in caplog.text
        monkeypatch.setenv("FAIL_MODE", "dependency")
        assert client.get("/health").status_code == 200
        assert client.get("/ready").status_code == 503
        assert client.get("/message", headers={"X-API-Key": "test-only"}).status_code == 500


def test_missing_config(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    with TestClient(app) as client:
        assert client.get("/ready").status_code == 503
        assert client.get("/message").status_code == 503
