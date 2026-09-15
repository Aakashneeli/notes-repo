"""Supplied I/O adapters. False means the narrow probe failed; no secret error text."""
import os
import httpx
from .core import connection, queue_connection


def dependency_checks():
    checks = {}
    try:
        with connection() as conn:
            checks["postgres"] = conn.execute("SELECT 1").fetchone() == (1,)
    except Exception:
        checks["postgres"] = False
    try:
        checks["redis"] = bool(queue_connection().ping())
    except Exception:
        checks["redis"] = False
    return checks


def vector_check():
    # Placeholder is reachable; no collections, embeddings or retrieval are exercised.
    try:
        response = httpx.get(os.environ["QDRANT_URL"] + "/readyz", timeout=2)
        return response.status_code == 200
    except Exception:
        return False
