"""Black-box requirements; keep these checks and add independent cases."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from app import create_app

WRITE = {"X-API-Key":"local-study-key"}
READ = {"X-API-Key":"local-read-key"}

def new(client, title, done=False):
    r = client.post("/tasks", headers=WRITE, json={"title":title,"done":done})
    assert r.status_code == 201, r.text
    row = r.json()
    assert set(row) == {"id","title","done"} and row["id"] > 0
    return row

def test_crud_restart_filter(engine):
    with TestClient(create_app(engine)) as client:
        a = new(client, "A")
        b = new(client, "B", True)
        c = new(client, "C", True)
        r = client.get("/tasks?done=true&offset=1&limit=1", headers=READ)
        assert r.json() == {"items":[c],"total":2,"offset":1,"limit":1}
        assert client.patch(f"/tasks/{a['id']}", headers=WRITE, json={"done":True}).json()["done"] is True
    # New application, same database: catches in-memory substitutes.
    with TestClient(create_app(engine)) as client:
        assert client.get(f"/tasks/{a['id']}", headers=READ).json()["done"] is True
        assert client.delete(f"/tasks/{b['id']}", headers=WRITE).status_code == 204
        assert client.get(f"/tasks/{b['id']}", headers=READ).status_code == 404

def test_conflict_is_atomic(engine):
    with TestClient(create_app(engine)) as c:
        a = new(c, "A")
        new(c, "B")
        r = c.patch(f"/tasks/{a['id']}", headers=WRITE, json={"title":"B","done":True})
        assert r.status_code == 409
        assert c.get(f"/tasks/{a['id']}", headers=READ).json() == a
        assert new(c, "After failure")["title"] == "After failure"
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT count(*) FROM task_events WHERE task_id=:id"), {"id":a["id"]}) == 1

def test_event_failure_rolls_back_task(engine):
    # Test-only constraint rejects all events; service must not commit task first.
    with engine.begin() as conn:
        conn.exec_driver_sql("ALTER TABLE task_events ADD CONSTRAINT injected_failure CHECK (kind <> 'created')")
    with TestClient(create_app(engine), raise_server_exceptions=False) as c:
        assert c.post("/tasks", headers=WRITE, json={"title":"Must vanish"}).status_code == 500
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT count(*) FROM tasks")) == 0

@pytest.mark.parametrize("statement", [
    "INSERT INTO tasks(title,done) VALUES ('',false)",
    "INSERT INTO tasks(title,done) VALUES ('   ',false)",
    "INSERT INTO tasks(title,done) VALUES (NULL,false)",
    "INSERT INTO tasks(title,done) VALUES ('X',NULL)",
    "INSERT INTO task_events(task_id,kind) VALUES (999999,'created')",
])
def test_database_constraints(engine, statement):
    with pytest.raises(IntegrityError):
        with engine.begin() as conn:
            conn.exec_driver_sql(statement)

def test_unique_constraint_bypassing_api(engine):
    with engine.begin() as conn:
        conn.exec_driver_sql("INSERT INTO tasks(title,done) VALUES ('Unique',false)")
    with pytest.raises(IntegrityError):
        with engine.begin() as conn:
            conn.exec_driver_sql("INSERT INTO tasks(title,done) VALUES ('Unique',true)")

def test_named_title_constraint(engine):
    with engine.connect() as conn:
        names = conn.execute(text("SELECT conname FROM pg_constraint WHERE conrelid='tasks'::regclass")).scalars().all()
        assert "uq_tasks_title" in names

def test_bridge_validation_and_authorization(engine):
    with TestClient(create_app(engine)) as c:
        assert c.get("/tasks").status_code == 401
        assert c.post("/tasks", headers=READ, json={"title":"X"}).status_code == 403
        for body in [{"title":""},{"title":"X","done":"yes"},{"title":"X","extra":1}]:
            assert c.post("/tasks", headers=WRITE, json=body).status_code == 422
        a = new(c,"valid")
        assert c.patch(f"/tasks/{a['id']}", headers=WRITE, json={}).status_code == 400
        assert c.patch(f"/tasks/{a['id']}", headers=WRITE, json={"done":None}).status_code == 422
        assert c.get("/tasks?limit=0", headers=READ).status_code == 422
