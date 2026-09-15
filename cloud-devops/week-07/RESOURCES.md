# Week 7 Resources

## Knowledge

Sources inspected 2026-09-14. Official documentation grounds mechanisms; local tests validate our examples. Version tags may move; record resolved digests after live pulls.

- [Docker image model](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/) — Image content versus a running instance; Lesson 3.
- [Dockerfile instructions](https://docs.docker.com/build/concepts/dockerfile/) — Build recipe and runtime command; Lesson 4.
- [Build context and ignore rules](https://docs.docker.com/build/concepts/context/) — Explain which host files COPY can read; Lessons 4/12.
- [Compose networking](https://docs.docker.com/compose/how-tos/networking/) — Service DNS, ports and network boundaries; Lesson 5.
- [Compose interpolation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/) — Host variable substitution versus container environment; Lesson 5.
- [Compose service reference](https://docs.docker.com/reference/compose-file/services/) — Exact service, healthcheck and command syntax; Lessons 5/6.
- [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/) — service_healthy gates and their limits; Lesson 6.
- [Docker volumes](https://docs.docker.com/engine/storage/volumes/) — Named-volume lifetime and mount targets; Lessons 6/10.
- [Postgres official image](https://hub.docker.com/_/postgres) — Initialization variables and version-sensitive data paths; use the selected 16-alpine path.
- [Compose up CLI](https://docs.docker.com/reference/cli/docker/compose/up/) — --build, --wait, --wait-timeout; live lab and fresh checkout.
- [FastAPI container deployment](https://fastapi.tiangolo.com/deployment/docker/) — Serving process and container startup concepts; Lessons 1/4.
- [FastAPI middleware](https://fastapi.tiangolo.com/tutorial/middleware/) — Before/downstream/after control flow; Lesson 9 and reading task.
- [FastAPI additional status codes](https://fastapi.tiangolo.com/advanced/additional-status-codes/) — A JSONResponse can set the actual HTTP status; Lesson 7.
- [Python logging](https://docs.python.org/3/library/logging.html) — Logger, handler, formatter and propagation; Lesson 8.
- [Psycopg basic use](https://www.psycopg.org/psycopg3/docs/basic/usage.html) — Understand supplied transaction and parameterized-query bridge.
- [RQ jobs](https://python-rq.org/docs/) — Queued callable and job ID semantics; prerequisite bridge.
- [RQ workers](https://python-rq.org/docs/workers/) — Worker command, shared import paths and queue selection.
- [Qdrant readiness API](https://api.qdrant.tech/master/api-reference/service/readyz) — HTTP placeholder probe; does not demonstrate retrieval.
- [Qdrant official Helm release history](https://github.com/qdrant/qdrant-helm/blob/main/CHANGELOG.md) — Confirms the illustrative v1.13.6 release exists; not a recommendation to deploy an old version publicly.
- [Ruff tutorial](https://docs.astral.sh/ruff/tutorial/) — Lint command and error workflow; Lesson 11.
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — Substitute dependency boundaries for offline feedback.
- [GitHub Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) — Current Python setup and check workflow; Lesson 11.
- [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — Triggers, permissions, jobs and default working directories.

- [ECS stdout/stderr delivery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) — explains the configured CloudWatch destination in the source explain-back; no deployment exercise.

## Wisdom (Communities)

- [Docker Community Forums](https://forums.docker.com/) — learner-initiated troubleshooting with a minimal reproduction and versions, after local probes.
- [FastAPI discussions](https://github.com/fastapi/fastapi/discussions) — compare a middleware explanation or small test with maintainers/practitioners.

No joining or posting is required or authorized here. Community advice needs reproduction and source checking.

## Practical gaps
Qdrant website installation/monitoring pages redirected without readable content in the browser tool; the official API and official release history support the narrow placeholder. Live image pulls and runtime compatibility need a working daemon and learner checks; hosted Actions requires a real learner run.
