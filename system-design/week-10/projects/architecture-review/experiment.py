"""Supplied measurement harness. Run from week-10; does not write evidence files."""
import argparse
import asyncio
import json
import math
import platform
import time
from fixture import query


async def measure(mode, concurrency, count):
    gate = asyncio.Semaphore(concurrency)
    rows = []
    async def one(i):
        # All requests enter the burst together, before any task blocks the loop.
        submitted = start
        async with gate:
            started = time.perf_counter()
            status = "ok"
            try:
                await query(mode=mode, fail=(i % 10 == 9))
            except TimeoutError:
                status = "error"
            done = time.perf_counter()
            rows.append({"status": status,
                         "latency_ms": (done - submitted) * 1000,
                         "service_ms": (done - started) * 1000})
    start = time.perf_counter()
    await asyncio.gather(*(one(i) for i in range(count)))
    wall = time.perf_counter() - start
    ordered = sorted(r["latency_ms"] for r in rows)
    return {"mode": mode, "concurrency": concurrency, "count": count,
            "python": platform.python_version(), "platform": platform.platform(),
            "p50_ms": round(ordered[math.ceil(count * .5) - 1], 2),
            "p95_ms": round(ordered[math.ceil(count * .95) - 1], 2),
            "max_service_ms": round(max(r["service_ms"] for r in rows), 2),
            "requests_per_second": round(count / wall, 2),
            "error_rate": sum(r["status"] == "error" for r in rows) / count,
            "rows": rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["blocking", "cooperative"], required=True)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 20 or not 1 <= args.count <= 200:
        parser.error("concurrency 1..20; count 1..200")
    print(json.dumps(asyncio.run(measure(args.mode, args.concurrency, args.count)),
                     indent=2))


if __name__ == "__main__":
    main()
