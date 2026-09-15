"""Author checks for supplied bridge only; no live services or Week 7 solutions."""
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fixture.api import router
from fixture import probes


class MemoryBackend:
    def __init__(self):
        self.jobs = {}
    def submit(self, text, request_id):
        self.jobs["sample"] = {"state": "pending", "characters": None}
        return "sample"
    def status(self, job_id):
        return self.jobs.get(job_id)


def test_fixture_boundary(monkeypatch):
    monkeypatch.setenv("API_KEY", "local")
    app = FastAPI()
    app.include_router(router(MemoryBackend()))
    with TestClient(app) as client:
        assert client.post("/documents", content="hello").status_code == 401
        headers = {"X-API-Key": "local", "Content-Type": "text/plain"}
        assert client.post("/documents", content="", headers=headers).status_code == 422
        assert client.post("/documents", content=b"\xff", headers=headers).status_code == 422
        assert client.post("/documents", content="x" * 4097, headers=headers).status_code == 413
        response = client.post("/documents", content="hello", headers=headers)
        assert response.status_code == 202 and response.json()["job_id"] == "sample"
        assert client.get("/jobs/sample", headers=headers).json()["state"] == "pending"
        assert client.get("/jobs/absent", headers=headers).status_code == 404


def test_probes_fail_closed(monkeypatch):
    def broken():
        raise OSError("secret")
    monkeypatch.setattr(probes, "connection", broken)
    monkeypatch.setattr(probes, "queue_connection", broken)
    assert probes.dependency_checks() == {"postgres": False, "redis": False}
