"""Supplied raw-text ingestion boundary; no filesystem uploads, RAG or migrations."""
import os
import secrets
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from starlette.concurrency import run_in_threadpool
from . import core


def router(backend=core):
    def authorize(x_api_key: str | None = Header(default=None)):
        expected = os.environ.get("API_KEY", "")
        if not expected:
            raise HTTPException(503, "configuration_missing")
        if x_api_key is None or not secrets.compare_digest(x_api_key.encode(), expected.encode()):
            raise HTTPException(401, "unauthorized")

    routes = APIRouter(dependencies=[Depends(authorize)])

    @routes.post("/documents", status_code=202)
    async def upload(request: Request):
        if request.headers.get("content-type", "").split(";")[0] != "text/plain":
            raise HTTPException(415, "text_only")
        data = bytearray()
        async for piece in request.stream():
            data.extend(piece)
            if len(data) > 4096:
                raise HTTPException(413, "too_large")
        if not data:
            raise HTTPException(422, "empty")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(422, "invalid_utf8") from None
        try:
            job_id = await run_in_threadpool(backend.submit, text,
                getattr(request.state, "request_id", "fixture-without-middleware"))
        except Exception:
            raise HTTPException(503, "ingestion_unavailable") from None
        return {"job_id": job_id}

    @routes.get("/jobs/{job_id}")
    def job(job_id: str):
        try:
            result = backend.status(job_id)
        except Exception:
            raise HTTPException(503, "storage_unavailable") from None
        if result is None:
            raise HTTPException(404, "not_found")
        return result

    return routes
