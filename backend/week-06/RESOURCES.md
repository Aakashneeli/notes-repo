# Week 6 resources

## Knowledge

Verified against official documentation on 2026-09-14. Local lockfile records actual versions.
The original roadmap is a user-provided scope source, not API documentation.

- [FastAPI application structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
  Router composition and dependencies; lessons 1 and 3.
- [FastAPI security tools](https://fastapi.tiangolo.com/reference/security/)
  APIKeyHeader and explicit missing-key behavior; lesson 4.
- [FastAPI uploads](https://fastapi.tiangolo.com/tutorial/request-files/)
  Multipart, UploadFile and async reading; lessons 5 and 11.
- [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  Post-response work and process limitations; lesson 9.
- [Starlette background lifecycle](https://starlette.dev/background/)
  Sequential execution and error propagation; lesson 13 code reading.
- [FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/)
  Origins, headers and preflight configuration; lesson 12.
- [OWASP file upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
  Layered file controls and limits of extension/MIME validation; lesson 5.
- [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
  Secret lifecycle, exposure and rotation; lesson 4.
- [OWASP SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
  Bound values and allowlisted identifiers; lesson 7.
- [OWASP REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
  Access control, errors and rate-limit awareness; lesson 12.
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
  Parameter binding and transaction/connection context behavior; fixture in lesson 7.
- [Redis data structures](https://redis.io/docs/latest/develop/data-types/)
  Strings, lists, hashes and use cases; lesson 10.
- [RQ queues](https://python-rq.org/docs/)
  Importable jobs, queue creation and results; lesson 10.
- [RQ failures and retries](https://python-rq.org/docs/exceptions/)
  Retry counts/intervals, failure handling; lessons 8 and 10.
- [RQ workers](https://python-rq.org/docs/workers/)
  Worker CLI, process boundaries, trusted Redis and serializer concerns; lesson 10.
- [S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html)
  Bucket/key/object model for the design-only storage note; lesson 6.
- [Postman multipart parameters](https://learning.postman.com/docs/use/send-requests/create-requests/parameters/)
  Form-data file selection and generated request bodies; lesson 12.
- [uv locking and sync](https://docs.astral.sh/uv/concepts/projects/sync/)
  Locked environment setup and optional extras; lesson 2.

## Wisdom (Communities)
- [FastAPI discussions](https://github.com/fastapi/fastapi/discussions)
  Optional venue for focused framework questions. Bring a minimal reproduction, versions and
  sanitized observations after your own attempt. Reading is enough; no joining or posting is required.

## Limits
The local policy is intentionally small and does not certify production upload safety.
Live S3, worker crash recovery and multi-user authorization are not inferred from local tests.
