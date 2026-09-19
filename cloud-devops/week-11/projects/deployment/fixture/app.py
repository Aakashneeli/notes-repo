"""Minimal completed prerequisite fixture: no DB, uploads, RAG, or real user data."""

import hmac
import json
import logging
import os
import time
import uuid

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse

logger = logging.getLogger("uvicorn.error")
app = FastAPI()


@app.middleware("http")
async def safe_event(request, call_next):
    request_id = uuid.uuid4().hex
    started = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        response = JSONResponse({"detail": "internal error"}, status_code=500)
    event = {
        "event": "request",
        "request_id": request_id,
        "release": os.getenv("RELEASE", "dev"),
        "status": response.status_code,
        "duration_ms": round((time.perf_counter() - started) * 1000, 2),
    }
    logger.info(json.dumps(event))
    response.headers["X-Request-ID"] = request_id
    return response


@app.get("/health")
def health():
    return {"alive": True, "release": os.getenv("RELEASE", "dev")}


@app.get("/ready")
def ready():
    configured = bool(os.getenv("API_KEY")) and os.getenv("FAIL_MODE") != "dependency"
    return JSONResponse({"ready": configured}, status_code=200 if configured else 503)


@app.get("/message")
def message(x_api_key: str = Header(default="")):
    secret = os.getenv("API_KEY", "")
    if not secret:
        raise HTTPException(503, "not configured")
    if not hmac.compare_digest(x_api_key.encode(), secret.encode()):
        raise HTTPException(401, "unauthorized")
    if os.getenv("FAIL_MODE") == "dependency":
        raise RuntimeError("simulated downstream failure")
    return {"message": "deployment rehearsal", "release": os.getenv("RELEASE", "dev")}
