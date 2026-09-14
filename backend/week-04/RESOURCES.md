# Week 4 resources

## Knowledge

Authority: local roadmap article week-4; see [mapping](roadmap/source-week-04.md). Official pages checked 2026-09-13; actual package versions are locked in the project.

- [Http](https://www.rfc-editor.org/rfc/rfc9110.html) — HTTP method semantics, successful and failure status meanings; use with lessons 3, 8.
- [First](https://fastapi.tiangolo.com/tutorial/first-steps/) — FastAPI app/decorator model, OpenAPI and interactive documentation; use with lessons 2, 12.
- [Path](https://fastapi.tiangolo.com/tutorial/path-params/) — Typed path input and route ordering; use with lessons 4.
- [Query](https://fastapi.tiangolo.com/tutorial/query-params/) — Defaults, text conversion, optional query parameters; use with lessons 4, 7.
- [Body](https://fastapi.tiangolo.com/tutorial/body/) — Pydantic models as structured request bodies; use with lessons 3.
- [Updates](https://fastapi.tiangolo.com/tutorial/body-updates/) — Partial updates and exclude_unset behavior; use with lessons 5.
- [Models](https://docs.pydantic.dev/latest/concepts/models/) — Pydantic construction, configuration and model serialization; use with lessons 1, 5.
- [Response](https://fastapi.tiangolo.com/tutorial/response-model/) — Output validation/filtering and public schemas; use with lessons 5, 13.
- [Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) — HTTP exceptions, headers and exception handler registration; use with lessons 8.
- [Deps](https://fastapi.tiangolo.com/tutorial/dependencies/) — Callable dependencies and request-time injection; use with lessons 9, 13.
- [Security](https://fastapi.tiangolo.com/reference/security/) — APIKeyHeader extraction, auto_error and OpenAPI security; use with lessons 9.
- [Routers](https://fastapi.tiangolo.com/tutorial/bigger-applications/) — APIRouter registration and module composition; use with lessons 4, 6, 10, 13.
- [Life](https://fastapi.tiangolo.com/advanced/events/) — Lifespan setup/cleanup and context manager semantics; use with lessons 10.
- [Test](https://fastapi.tiangolo.com/tutorial/testing/) — TestClient requests, assertions and error tests; use with lessons 8, 11, 14.
- [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — pytest fixture isolation, yield teardown and parametrization; use with lessons 11.
- [Uv](https://docs.astral.sh/uv/guides/projects/) — Project discovery, environment synchronization and lockfile workflow; use with lessons 2.
- [Curl](https://curl.se/docs/manpage.html) — Request options, headers, JSON bytes and response inspection; use with lessons 3, 12.
- [Postman](https://learning.postman.com/docs/getting-started/importing-and-exporting/exporting-data/) — Export collections for reproducible local manual QA; use with lessons 12.
- [Env](https://learning.postman.com/docs/use/send-requests/variables/managing-environments/) — Postman environment selection and variable scope; use with lessons 12.
- [Scripts](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/) — Post-response scripts, pm.test and response assertions; use with lessons 12.
- [Git](https://git-scm.com/docs/git-add) — Selective staging and inspecting changes before committing; use with lessons 14.

- [Uvicorn settings](https://uvicorn.dev/settings/) — Module/object imports, --app-dir, --factory, loopback host and port; use with lessons 2 and 10.

- [Pydantic validation errors](https://docs.pydantic.dev/latest/errors/errors/) — Interpret field locations, messages and error types in lesson 5.
- [Dependency overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) — Replace a supplier deliberately in lesson 9; understand what the test no longer exercises.
- [Python classes](https://docs.python.org/3/tutorial/classes.html) — Instance attributes, methods and ownership for the counter trace in lesson 6.
- [pytest assertions](https://docs.pytest.org/en/stable/how-to/assert.html) — Read failures and expected exceptions in lesson 11.

## Wisdom (Communities)

- [FastAPI discussions](https://github.com/fastapi/fastapi/discussions) — Optional maintainer/community examples and focused debugging discussions. Read first; posting is a learner action and never required. No community preference has been asserted.

## Limits

Postman desktop execution and your final exported collection require learner action. Local tests do not verify remote services. No paid book is needed for the numbered week.
