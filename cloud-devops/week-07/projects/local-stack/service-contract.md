# Five-service contract — read with Lessons 5 and 6

These are requirements and tool facts, not a completed Compose solution. All service names below are intentional DNS names. Compose file location: projects/local-stack/compose.yaml; all build paths are relative to that file.

| Service | Process/image | Runtime connection/config | Network / persistence |
|---|---|---|---|
| api | build context ../..; dockerfile projects/local-stack/Dockerfile; image week7-api:local | DATABASE_URL=postgresql://lab:week7-local-only@postgres:5432/ingestion; REDIS_URL=redis://redis:6379/0; QDRANT_URL=http://vector:6333; API_KEY from env example | app + data; only published port 127.0.0.1:${API_PORT:-8077}:8000 |
| postgres | postgres:16-alpine | POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB from .env.example | data; pgdata:/var/lib/postgresql/data |
| redis | redis:7-alpine; command redis-server --appendonly yes | No public credentials/port; disposable isolated lab | data; redisdata:/data |
| worker | same build/image as api; rq worker --url redis://redis:6379/0 ingestion | DATABASE_URL and REDIS_URL; importable fixture package; no API key needed | data; no host port |
| vector | qdrant/qdrant:v1.13.6 (illustrative pinned release, not latest) | QDRANT__TELEMETRY_DISABLED=true; no collections or model provider | data; vectordata:/qdrant/storage; no host port |

`app` is a normal Compose bridge network; `data` has internal: true. Declare the three named volumes at top level. Service-to-service calls use container ports and DNS names, never the published API port. Default credentials are public local lab values; map each into the container explicitly. If passwords contain URL-reserved characters, encode them for DATABASE_URL or use an appropriate connection configuration; the supplied simple values avoid that bridge complication.

API command: execute `python -m fixture.bootstrap` successfully, then `exec uvicorn app:create_app --factory --host 0.0.0.0 --port 8000 --no-access-log`. To sequence these in Compose, use an explicit shell, e.g. a command list beginning sh, -c and one command string. The && means start the server only on bootstrap success. exec replaces the shell so the server receives stop signals.

Postgres health: pg_isready using the container's POSTGRES_USER/POSTGRES_DB, interval 5s, timeout 3s, retries 10, start_period 10s. Redis health: redis-cli ping with the same cadence. API depends on both with condition service_healthy.

API health: use `python -c` with `urllib.request.urlopen('http://127.0.0.1:8000/ready', timeout=9)`; unhandled HTTP/network error produces nonzero exit. Health timeout 10s, interval 10s, retries 10, start_period 15s. The probes inside /ready have finite waits; the outer timeout also bounds the request. Worker depends on healthy API, Redis and Postgres, so schema bootstrap precedes consumption. The fixture has one worker; no autoscaling design is required.

Vector is a separately probed placeholder; do not assume curl exists in its image. L10 calls its /readyz from the API's supplied Python adapter. API /ready intentionally does not depend on vector; running vector and worker containers are not business-success proof. Record resolved image digests after actual pulls. Major/variant tags for Python/Postgres/Redis may update; a future rebuild can differ despite Python package pins. Digest pinning is an optional reproducibility improvement after a verified pull.

Fresh copy needs no absolute host source mounts. Named-volume contents are runtime data, not committed source. Avoid container_name and fixed IPs; they make independent project names collide. Do not use delete-volume cleanup or broad system prune in this lab.
