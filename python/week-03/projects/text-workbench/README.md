# Text Workbench — learner project

Week 03 Pro Python. This is an independently packaged local project inside the notes repo.
No external repository, account or publication is required. Main functions are deliberately
unfinished; CLI and file adapter are supplied infrastructure.

## Setup and checks

Start: `/home/an10/code/notes-repo/python/week-03/projects/text-workbench`.

```bash
UV_CACHE_DIR=/tmp/week03-uv-cache uv sync --locked
uv run text-workbench --help
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
```

Python >=3.12; internet on initial dependency installation; no service or credentials.
Pydantic v2 is runtime; pytest/Ruff are development tools; Hatchling builds/installs src.
uv.lock pins a tested resolution. Do not hand-edit it. .env.example documents values;
.env is not loaded automatically. Use command-scoped settings as below.

## Contracts — implementation belongs to you

| Module | Contract |
|---|---|
| core.normalize(text: str) -> str | Collapse whitespace runs to one ASCII space; strip ends; lowercase; keep punctuation. |
| core.split_text(text: str) -> list[str] | Normalize, then whitespace tokens in order; empty/whitespace-only -> []. |
| core.summarize(text: str) -> dict[str, int] | Exactly characters=len(normalized text), words=number of tokens. Counts are code points, not UTF-8 bytes. |
| models.Config | Pydantic BaseModel; max_chars strict positive int default 1_000_000; log_level Literal DEBUG/INFO/WARNING/ERROR/CRITICAL default INFO; extra fields forbidden. |
| models.Record | Pydantic BaseModel; required strict nonnegative integers characters and words; extras forbidden. |
| settings.load_settings(env: Mapping[str,str]) -> Config | Select TEXT_MAX_CHARS/TEXT_LOG_LEVEL. Missing keys use defaults; convert max chars using int; invalid values raise ValueError/ValidationError. Ignore unrelated environment keys. No global reads. |
| service.process_file(path, config, reader=read_utf8) -> Record | Call reader exactly once; raw length > max_chars raises ValueError, equality allowed; use core metadata and validate Record; emit one INFO processed event through text_workbench.service with extra characters/words only. Return Record. Errors propagate. |
| logging_setup.JsonFormatter | JSON level/event always, optional characters/words only; use fixed safe event messages. No raw text, path, secret or arbitrary extras. |
| logging_setup.configure_logging(level) -> None | One stderr handler on text_workbench logger using JsonFormatter; logger level set, propagate=False; repeated setup does not duplicate output. |
| cli.main() -> int | Supplied wrapper; success JSON stdout, safe expected-error stderr and exit 2, argparse path, startup env/config/logging. |

Core accepts strings by contract; annotations are not runtime validation. The CLI adapter
ensures file decoding yields strings. The service's default reader reads entire UTF-8
files before the limit check. This bounds permitted processing, not peak read memory.
No streaming or hostile-upload protection is claimed. The large test creates 200,000
characters in tmp_path, tests 100,000 tokens, exact boundary and over-limit behavior.

## Example commands and expected behavior (after your implementation)

```bash
uv run text-workbench data/normal.txt
uv run text-workbench data/empty.txt
uv run text-workbench data/unicode.txt
TEXT_LOG_LEVEL=ERROR uv run text-workbench data/normal.txt
TEXT_MAX_CHARS=1 uv run text-workbench data/normal.txt
```

| Case | stdout JSON | stderr / exit |
|---|---|---|
| normal.txt | {"characters":17,"words":3} | one processed INFO JSON event / 0 |
| empty.txt | {"characters":0,"words":0} | one processed INFO JSON event / 0 |
| unicode.txt | {"characters":7,"words":2} | one processed INFO JSON event / 0 |
| ERROR threshold | same normal record | no INFO log / 0 |
| invalid config, too-large input, missing file, non-UTF-8 | empty | `Cannot process input: check file, encoding, size and settings.` / 2 |

JSON key order and spaces are not semantically significant. Expected success log fields:
level=INFO, event=processed, characters/words matching the output. No file path/text.
A plain unimplemented starter raises NotImplementedError; that is not an operational
error handled by the CLI. Data files are immutable fixtures; generated large/bad data
is isolated by tests. tests/ checks behavior and uses fixtures/subprocesses explained in
lessons 3, 5, 8 and 10. New regression tests are learner-owned additions.

## Finish these learner sections

- Why these module boundaries (include one alternative and tradeoff):
- Pure functions and side effects, including actual call flow:
- Config loading and logging privacy decisions:
- Failure reproduced, regression check and result:
- Test limitations and whole-file memory limitation in your own words:
- Editable module diagram: save `module-diagram.drawio` from the template in lesson 11:
- Actual setup/CLI output evidence, commands and commit IDs:
- Delayed variation and changed tests:

[Return to lesson 10](../../lessons/0010-integration-and-debugging.html).
