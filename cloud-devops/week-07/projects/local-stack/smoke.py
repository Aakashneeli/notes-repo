"""Learner L9: live check. Mutates only the local lab by adding one sample job."""
import os
import time
from pathlib import Path
import httpx

base = os.environ.get("LAB_URL", "http://127.0.0.1:8077")
key = os.environ.get("API_KEY", "week7-practice-key")
with httpx.Client(base_url=base, timeout=15) as client:
    assert client.get("/health").json() == {"alive": True}
    assert client.get("/ready").status_code == 200
    assert client.post("/documents", content="hello").status_code == 401
    data = Path(__file__).with_name("data").joinpath("hello.txt").read_bytes()
    response = client.post("/documents", content=data, headers={"X-API-Key": key,
        "Content-Type": "text/plain", "X-Request-ID": "smoke-7"})
    assert response.status_code == 202, response.text
    assert response.headers["X-Request-ID"] == "smoke-7"
    job_id = response.json()["job_id"]
    for attempt in range(30):
        result = client.get(f"/jobs/{job_id}", headers={"X-API-Key": key})
        assert result.status_code == 200, result.text
        if result.json()["state"] == "completed":
            break
        time.sleep(1)
    else:
        raise AssertionError("worker did not complete within 30 seconds")
    assert result.json()["characters"] == len(data.decode("utf-8"))
    print({"live_smoke": "passed", "job_id": job_id, "characters": result.json()["characters"]})
