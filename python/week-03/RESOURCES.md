# Week 3 Resources

## Knowledge

- [Python modules](https://docs.python.org/3/tutorial/modules.html)
  Imports, packages and module execution; use in lesson 2 when an import fails.

- [Python typing](https://docs.python.org/3/library/typing.html)
  Unions, optional values, collections and Callable; lesson 4 contract reading.

- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)
  Generated constructors and limitations; compare Badge with runtime validation in lesson 5.

- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)
  Model construction, errors and serialization; lesson 5. The lock pins v2.

- [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
  Why strict counts reject strings/bools; inspect after the model experiment.

- [Python environment](https://docs.python.org/3/library/os.html#os.environ)
  String-valued environment mapping; lesson 6 explicit settings boundary.

- [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)
  Levels, handlers and application configuration; lesson 7.

- [Python logging reference](https://docs.python.org/3/library/logging.html)
  LogRecord, Formatter, extra fields and propagation; debug structured logging.

- [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)
  Coroutines, scheduling, gather and blocking; lesson 9 local experiment.

- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
  Explicit UTF-8 reading and file errors; service adapter in lessons 8/10.

- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
  Dependency injection in tests and fixture lifecycle; lessons 3/10.

- [pytest parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)
  Multiple input/output rows; test_core.py in lesson 3.

- [pytest logging](https://docs.pytest.org/en/stable/how-to/logging.html)
  caplog records versus rendered output; service checks in lesson 8.

- [uv project layout](https://docs.astral.sh/uv/concepts/projects/layout/)
  Manifest, lock and environment responsibilities; lesson 2.

- [uv project commands](https://docs.astral.sh/uv/guides/projects/)
  sync/run workflow; setup and reproducibility in lessons 2/12.

- [Ruff configuration](https://docs.astral.sh/ruff/configuration/)
  Lint rules, formatter and pyproject settings; lessons 2/10.

- [PyPA sampleproject](https://github.com/pypa/sampleproject)
  Actual small repository for lesson 11. Pinned offline snapshot and provenance are supplied.

- [A Philosophy of Software Design — original author](https://web.stanford.edu/~ouster/cgi-bin/book.php)
  Roadmap book anchor: if you already have access, read chapters on modules and information hiding. Optional paid book; the local lesson teaches the necessary design reasoning without requiring purchase.

- [draw.io editor documentation](https://www.drawio.com/docs/manual/storage-location-select/)
  Save an editable diagram on your device; lesson 11. A local desktop editor avoids uploads.

## Wisdom (Communities)

- [Python Discourse — Python Help](https://discuss.python.org/c/help/7)
  Optional peer feedback on a minimal reproducible Python question after a local attempt.
  Share only code/data you intend to make public; participation is a learner action,
  never sent by the tutor. No community preference has been asserted.

## Gaps and limits

Official APIs were checked on 2026-09-10 and exercised with the locked local versions.
The optional book's full chapters were not accessed; no chapter-specific claims or
excerpts are supplied. The module examples are local teaching choices. This workspace
contains no live-service or deployment requirement.
