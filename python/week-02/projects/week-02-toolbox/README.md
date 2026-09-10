# Week 2 toolbox — learner project

Build three tiny commands yourself. Supplied CLI wrappers and tests are teaching infrastructure. The functions `count_files`, `pretty_json`, and `filter_lines` intentionally raise `NotImplementedError`. That traceback means the exercise is still unfinished.

## Setup

Python >=3.11, uv, and Git are required. They are already installed on the machine this course was created on. From this directory:

```bash
uv sync
uv run file-counter --help
uv run pytest --collect-only -q
```

The first sync may need internet access to install the build backend and pytest. `pyproject.toml` declares dependencies; `uv.lock` records the resolved environment. Commit `uv.lock` after setup. Never commit `.venv` or real `.env` values.

Fresh starter feedback: 41 tests are collected; 30 fail because your three functions are unfinished, while 11 supplied-wrapper checks pass. This is expected, not evidence of a broken installation. Your target after implementation is 41 passing checks plus your own meaningful case and explain-back.

## Build in order

| Lesson | Implement | Focused feedback |
|---|---|---|
| 12 | `src/week2_toolbox/file_counter.py`: `count_files` | `uv run pytest tests/test_file_counter.py -q` |
| 13 | `src/week2_toolbox/json_pretty.py`: `pretty_json` | `uv run pytest tests/test_json_pretty.py -q` |
| 14 | `src/week2_toolbox/log_filter.py`: `filter_lines` | `uv run pytest tests/test_log_filter.py -q` |

Make one feature branch per command. Attempt the function from its docstring first; then consult the lesson's hint ladder. Preserve the declared interfaces so tests can call your code. Do not edit tests merely to make them pass.

## Usage after implementation

```bash
uv run file-counter data/count
# 3 — includes .hidden; excludes nested/deep.txt
uv run json-pretty data/example.json
# JSON with two-space indentation and sorted keys
uv run log-filter data/app.log ERROR
# ERROR upload failed
# ERROR storage unavailable
uv run pytest -q
```

Run from this directory, because the sample data paths are relative to the working directory. `uv run python src/week2_toolbox/file_counter.py data/count` is the script-file alternative. `uv run python -m week2_toolbox.file_counter data/count` uses a module import path. Both call the same main function.

## Behavior and limits

- Counter: direct files only, includes hidden files, excludes symlinks, no recursion. Missing folder is an error; a file passed as a folder is an error.
- Pretty-printer: supports valid JSON values including arrays/scalars; invalid JSON fails. Leaves the input file untouched. Do not redirect output onto the input path.
- Filter: exact first-token level, case-sensitive, supported levels INFO/WARNING/ERROR. Keeps order and original lines; ignores blanks. Reads the whole file into memory.
- Successful commands exit 0. Expected input/read/parse errors exit 2 and use stderr. `NotImplementedError` is deliberately not caught: fix the exercise, not the wrapper.
- JSON and logs use UTF-8. Concurrent filesystem changes, enormous inputs, production logging formats and recursive counting are outside Week 2.

## Understand the provided code

`argparse` reads CLI arguments. `Path` represents a filesystem path. `main()` joins input/output to your function. `try/except` handles expected failures. `print(..., file=sys.stderr)` sends diagnostics separately. `SystemExit(main())` gives the shell the returned exit code. `__name__` lets a module be imported without automatically running the CLI.

In tests, `assert` states expected behavior; `tmp_path` supplies a temporary directory; `pytest.raises` expects a particular exception; `parametrize` repeats a check for multiple inputs. You only need to read and run these now. A later Python course can deepen test authoring.

## Git ownership

Start with lesson 05's local `git init -b main`. Verify the repository root before staging. No commits or branches have been made on your behalf. Add `uv.lock` to a tooling commit after sync. After passing a command's tests, commit the implementation, explain the diff, and merge its branch into main. A separate repo under a notes repo is intentionally independent: record its path/URL in the notes, rather than accidentally staging an embedded repository as ordinary notes.

## Ownership note — fill this in yourself

- What each command does:
- One edge case I added:
- What AI helped explain:
- One line I still cannot explain:
- How I reproduced this from a fresh clone:

## Precise boundaries

JSON behavior follows Python's `json.loads`/`json.dumps` defaults, using `indent=2` and `sort_keys=True`: escaped Unicode is allowed; duplicate object keys keep the last value; non-finite values follow Python's permissive defaults. This exercise is a formatter, not a strict JSON validator. The pure function returns no extra terminal newline; the wrapper's print adds one.

Counter input may itself be a symlink to a directory; symlink entries inside the directory are excluded. Filesystem permission errors should propagate as OSError; platform checks can differ, so the supplied suite does not prove every permissions scenario.

The log function preserves the strings it receives, including whitespace and final newline presence. The CLI reads text with Python's universal newline handling, so CRLF in a file becomes LF before the function sees it. It does not promise byte-for-byte file preservation.

See [scaffolding walkthrough](../../lessons/0025-scaffolding-map.html) for checker internals and test helpers. All supplied files are linked from the desk's file catalogue.
