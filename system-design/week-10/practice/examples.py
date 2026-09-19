"""Completed small teaching examples, not the architecture-review project solution."""
import asyncio
import json
import time
from typing import Protocol


class Catalog(Protocol):
    def title(self, item_id: str) -> str: ...


class MemoryCatalog:
    def title(self, item_id):
        return {"book-1": "Field guide"}[item_id]


def label(item_id: str, catalog: Catalog) -> str:
    return catalog.title(item_id).upper()


async def timed_demo():
    events = []
    start = time.perf_counter()
    try:
        await asyncio.wait_for(asyncio.sleep(0.03), timeout=0.005)
    except TimeoutError:
        events.append({"event": "catalog.timeout", "elapsed_ms": round(
            (time.perf_counter() - start) * 1000, 2)})
    return events


def retry_read(read, attempts=3):
    for attempt in range(attempts):
        try:
            return read()
        except TimeoutError:
            if attempt == attempts - 1:
                raise
    raise ValueError("attempts must be positive")


def main():
    print(label("book-1", MemoryCatalog()))
    print(json.dumps(asyncio.run(timed_demo())[0], sort_keys=True))
    calls = []
    def read():
        calls.append(1)
        if len(calls) == 1:
            raise TimeoutError("temporary")
        return "available"
    print(retry_read(read), "attempts", len(calls))


if __name__ == "__main__":
    main()
