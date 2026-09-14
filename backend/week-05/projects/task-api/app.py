"""Supplied minimal HTTP bridge. Database models/queries/migrations are learner work.
Preserves core Task CRUD, title validation, filtering and dummy API-key roles.
It is not proof that Week 4's full error/OpenAPI/QA curriculum was completed.
"""
from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Depends, HTTPException, Query, Response
from fastapi.security import APIKeyHeader
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from db import make_engine
from repository import TaskRepository, Missing, Conflict
from schemas import TaskCreate, TaskPatch

def create_app(engine=None):
    owned = engine is None
    engine = engine if engine is not None else make_engine()

    @asynccontextmanager
    async def lifespan(app):
        yield
        if owned:
            engine.dispose()

    app = FastAPI(title="Week 5 persistence bridge", lifespan=lifespan)
    key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

    def reader(key=Depends(key_header)):
        if key == os.getenv("TASK_API_KEY", "local-study-key"):
            return "write"
        if key == os.getenv("TASK_READ_KEY", "local-read-key"):
            return "read"
        raise HTTPException(401, "Invalid API key", headers={"WWW-Authenticate":"APIKey"})

    def writer(role=Depends(reader)):
        if role != "write":
            raise HTTPException(403, "Read-only key")

    def repo():
        with Session(engine) as session:
            yield TaskRepository(session)

    def transact(repository, operation):
        try:
            # Commit happens before the successful response is returned.
            with repository.session.begin():
                result = operation()
            return result
        except Missing as exc:
            raise HTTPException(404, "Task not found") from exc
        except Conflict as exc:
            raise HTTPException(409, "Title conflict") from exc
        except IntegrityError as exc:
            # Only the expected unique-title constraint is an HTTP conflict.
            cause = exc.orig
            name = getattr(getattr(cause, "diag", None), "constraint_name", None)
            if name == "uq_tasks_title":
                raise HTTPException(409, "Title conflict") from exc
            raise

    @app.get("/health")
    def health():
        return {"status":"ok"}

    @app.post("/tasks", status_code=201, dependencies=[Depends(writer)])
    def create(body: TaskCreate, r=Depends(repo)):
        return transact(r, lambda: r.create(body.title, body.done))

    @app.get("/tasks", dependencies=[Depends(reader)])
    def page(done: bool | None = None, offset: int = Query(0, ge=0),
             limit: int = Query(20, ge=1, le=100), r=Depends(repo)):
        return transact(r, lambda: r.page(done, offset, limit))

    @app.get("/tasks/{task_id}", dependencies=[Depends(reader)])
    def get(task_id: int, r=Depends(repo)):
        if task_id < 1:
            raise HTTPException(422, "Positive ID required")
        return transact(r, lambda: r.get(task_id))

    @app.patch("/tasks/{task_id}", dependencies=[Depends(writer)])
    def update(task_id: int, body: TaskPatch, r=Depends(repo)):
        if task_id < 1:
            raise HTTPException(422, "Positive ID required")
        changes = body.model_dump(exclude_unset=True)
        if not changes:
            raise HTTPException(400, "Empty update")
        return transact(r, lambda: r.update(task_id, changes))

    @app.delete("/tasks/{task_id}", status_code=204, dependencies=[Depends(writer)])
    def delete(task_id: int, r=Depends(repo)):
        if task_id < 1:
            raise HTTPException(422, "Positive ID required")
        transact(r, lambda: r.delete(task_id))
        return Response(status_code=204)

    return app
