"""Minimal prerequisite fixture: no HTTP, auth, database, semantic RAG or model calls."""
import asyncio
import time


async def query(*, mode="cooperative", fail=False):
    if mode == "blocking":
        time.sleep(0.02)  # Deliberate event-loop blocking fault.
    else:
        await asyncio.sleep(0.02)  # Simulated vector-store I/O.
    if fail:
        raise TimeoutError("synthetic vector timeout")
    await asyncio.sleep(0.01)  # Simulated model I/O.
    return {"hits": 2, "usage": {"input_tokens": 100, "output_tokens": 20},
            "answer": "Fictional answer; no real retrieval or model."}
