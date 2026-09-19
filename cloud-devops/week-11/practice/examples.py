"""Completed small examples; not a deployment implementation. Python standard library only."""

import json
from decimal import Decimal
from pathlib import Path


def estimate(hours, hourly, disk, ipv4_hourly, logs, reserve):
    """All amounts are USD; hypothetical input rates, never a current price quote."""
    return hours * (hourly + ipv4_hourly) + disk + logs + reserve


def choose_probe(status, release, expected):
    if status != 200:
        return "investigate"
    if release != expected:
        return "wrong release"
    return "candidate"


def main():
    total = estimate(
        Decimal("100"), Decimal("0.01"), Decimal("1"), Decimal("0.005"), Decimal("0.5"), Decimal("2")
    )
    print(f"illustrative total: ${total:.2f}")
    print(choose_probe(200, "old", "new"))
    events = [
        json.loads(line) for line in (Path(__file__).parent / "data/events.jsonl").read_text().splitlines()
    ]
    for event in events:
        if event["status"] >= 500:
            print(event["request_id"], event["release"], event["error_code"])


if __name__ == "__main__":
    main()
