"""Black-box contract checks. Read assertions; keep supplied checks unchanged.
Add your own regression/variation checks in test_learner.py. See lesson 11.
"""

import pytest
from fastapi.testclient import TestClient

from task_api.main import create_app

WRITE = {"X-API-Key": "local-study-key"}
READ = {"X-API-Key": "local-read-key"}


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("TASK_API_KEY", WRITE["X-API-Key"])
    monkeypatch.setenv("TASK_READ_KEY", READ["X-API-Key"])
    with TestClient(create_app(), raise_server_exceptions=False) as c:
        yield c


def error(response, status, code):
    assert response.status_code == status, response.text
    assert response.headers["content-type"].startswith("application/json")
    body = response.json()
    assert set(body) == {"error"}
    assert set(body["error"]) == {"code", "message"}
    assert body["error"]["code"] == code
    assert isinstance(body["error"]["message"], str) and body["error"]["message"]
    for forbidden in ("Traceback", "local-study-key", "local-read-key"):
        assert forbidden not in response.text


def create(client, title="Read HTTP", **extra):
    r = client.post("/tasks", headers=WRITE, json={"title": title, **extra})
    assert r.status_code == 201, r.text
    return r.json()


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_crud_and_id_policy(client):
    a = create(client, "  Read HTTP  ")
    assert a == {"id": 1, "title": "Read HTTP", "done": False}
    assert client.get("/tasks/1", headers=READ).json() == a
    r = client.patch("/tasks/1", headers=WRITE, json={"done": True})
    assert r.status_code == 200
    assert r.json() == {**a, "done": True}
    r = client.patch("/tasks/1", headers=WRITE, json={"title": "Write tests"})
    assert r.status_code == 200
    assert r.json() == {"id": 1, "title": "Write tests", "done": True}
    r = client.delete("/tasks/1", headers=WRITE)
    assert r.status_code == 204 and r.content == b""
    error(client.get("/tasks/1", headers=READ), 404, "not_found")
    error(client.delete("/tasks/1", headers=WRITE), 404, "not_found")
    assert create(client, "Next")["id"] == 2


def test_list_filter_before_slice(client):
    create(client, "A", done=False)
    create(client, "B", done=True)
    create(client, "C", done=True)
    r = client.get("/tasks?done=true&offset=1&limit=1", headers=READ)
    assert r.status_code == 200
    assert r.json() == {
        "items": [{"id": 3, "title": "C", "done": True}],
        "total": 2,
        "offset": 1,
        "limit": 1,
    }
    body = client.get("/tasks", headers=READ).json()
    assert [t["id"] for t in body["items"]] == [1, 2, 3]
    assert (body["total"], body["offset"], body["limit"]) == (3, 0, 20)
    r = client.get("/tasks?done=false", headers=READ)
    assert [t["id"] for t in r.json()["items"]] == [1]
    r = client.get("/tasks?offset=99", headers=READ)
    assert r.json() == {"items": [], "total": 3, "offset": 99, "limit": 20}


def test_empty_list(client):
    r = client.get("/tasks", headers=READ)
    assert r.status_code == 200
    assert r.json() == {"items": [], "total": 0, "offset": 0, "limit": 20}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"title": ""},
        {"title": " "},
        {"title": "x" * 81},
        {"title": 3},
        {"title": None},
        {"title": "ok", "done": "yes"},
        {"title": "ok", "done": 1},
        {"title": "ok", "done": None},
        {"title": "ok", "id": 77},
    ],
)
def test_invalid_create(client, payload):
    error(client.post("/tasks", headers=WRITE, json=payload), 422, "validation_error")
    assert client.get("/tasks", headers=READ).json()["total"] == 0


@pytest.mark.parametrize(
    "payload",
    [
        {"title": None},
        {"done": None},
        {"title": " "},
        {"title": "x" * 81},
        {"title": 7},
        {"done": "true"},
        {"done": 0},
        {"extra": "x"},
    ],
)
def test_invalid_patch_is_atomic(client, payload):
    a = create(client)
    error(client.patch("/tasks/1", headers=WRITE, json=payload), 422, "validation_error")
    assert client.get("/tasks/1", headers=READ).json() == a


def test_boundary_unicode_and_false(client):
    create(client, "x" * 80)
    a = create(client, "पढ़ना ☕", done=True)
    r = client.patch(f"/tasks/{a['id']}", headers=WRITE, json={"done": False})
    assert r.status_code == 200 and r.json()["done"] is False


def test_empty_patch_and_conflicts(client):
    a = create(client, "A")
    create(client, "B")
    error(client.patch("/tasks/1", headers=WRITE, json={}), 400, "empty_update")
    error(client.post("/tasks", headers=WRITE, json={"title": " A "}), 409, "conflict")
    error(
        client.patch("/tasks/1", headers=WRITE, json={"title": "B", "done": True}), 409, "conflict"
    )
    assert client.get("/tasks/1", headers=READ).json() == a
    assert client.patch("/tasks/1", headers=WRITE, json={"title": "A"}).status_code == 200
    assert create(client, "a")["title"] == "a"


@pytest.mark.parametrize("query", ["offset=-1", "limit=0", "limit=101", "limit=oops", "done=maybe"])
def test_invalid_query(client, query):
    error(client.get("/tasks?" + query, headers=READ), 422, "validation_error")


@pytest.mark.parametrize(
    "method,payload", [("get", None), ("patch", {"done": True}), ("delete", None)]
)
def test_missing_resource(client, method, payload):
    error(client.request(method, "/tasks/999", headers=WRITE, json=payload), 404, "not_found")


@pytest.mark.parametrize("path", ["/tasks/nope", "/tasks/0", "/tasks/-1"])
def test_bad_path(client, path):
    error(client.get(path, headers=READ), 422, "validation_error")


@pytest.mark.parametrize(
    "method,path,payload",
    [
        ("post", "/tasks", {"title": "x"}),
        ("get", "/tasks", None),
        ("get", "/tasks/1", None),
        ("patch", "/tasks/1", {"done": True}),
        ("delete", "/tasks/1", None),
    ],
)
@pytest.mark.parametrize("headers", [{}, {"X-API-Key": "wrong"}])
def test_auth_all_endpoints(client, method, path, payload, headers):
    r = client.request(method, path, json=payload, headers=headers)
    error(r, 401, "unauthorized")
    assert r.headers["www-authenticate"] == "APIKey"


@pytest.mark.parametrize(
    "method,path,payload",
    [
        ("post", "/tasks", {"title": "x"}),
        ("patch", "/tasks/1", {"done": True}),
        ("delete", "/tasks/1", None),
    ],
)
def test_read_only_key(client, method, path, payload):
    error(client.request(method, path, json=payload, headers=READ), 403, "forbidden")


def test_malformed_and_unmatched(client):
    error(
        client.post("/tasks", headers={**WRITE, "Content-Type": "application/json"}, content="{"),
        422,
        "validation_error",
    )
    error(client.get("/absent", headers=READ), 404, "not_found")
    r = client.put("/tasks", headers=WRITE, json={})
    error(r, 405, "method_not_allowed")
    assert "allow" in r.headers


def test_unexpected_error_is_generic(client):
    # A test-only route, never add it to the real API.
    @client.app.get("/_test_crash")
    def fail():
        raise RuntimeError("private stack detail")

    r = client.get("/_test_crash")
    error(r, 500, "internal_error")
    assert "private stack detail" not in r.text


def test_openapi(client):
    r = client.get("/openapi.json")
    assert r.status_code == 200
    spec = r.json()
    for path, methods in {
        "/tasks": ["get", "post"],
        "/tasks/{task_id}": ["get", "patch", "delete"],
    }.items():
        for method in methods:
            operation = spec["paths"][path][method]
            assert operation.get("security"), "Declare the API key in OpenAPI too"
    assert spec["components"]["securitySchemes"]


def test_independent_apps(monkeypatch):
    monkeypatch.setenv("TASK_API_KEY", WRITE["X-API-Key"])
    monkeypatch.setenv("TASK_READ_KEY", READ["X-API-Key"])
    with TestClient(create_app()) as first:
        create(first)
    with TestClient(create_app()) as second:
        assert second.get("/tasks", headers=READ).json()["total"] == 0
