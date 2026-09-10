# Week 3 author verification

Verified 2026-09-10. This records material/infrastructure checks, **not learner mastery**.
Source: `/home/an10/Downloads/ai-backend-roadmap.html`, exact numbered article `week-3`:
Pro Python — Professional Python Structure, Pydantic, Logging, and Practical LLD.
Workspace: `python/week-03/`; no Week 3 naming exception.

## Environment and dependencies

- Python 3.14.7 and uv 0.12.10 on Linux; project declares Python >=3.12.
- Locked Pydantic 2.13.5, pytest 9.1.1, Ruff 0.16.6; Hatchling build backend.
- `uv sync --locked` installed the project and development tools. A subsequent
  `UV_CACHE_DIR=/tmp/week03-uv-cache uv sync --locked --offline` succeeded.
- The initial restricted-network attempts could not resolve hosts. Authorized network
  retries fetched public dependencies and PyPA source successfully; no remaining setup blocker.
- Installed import resolves to this project's `src/text_workbench/__init__.py`.
  `uv run text-workbench --help` succeeds without invoking unfinished functions.
- `uv build --offline --out-dir /tmp/week03-build` produced a source distribution and wheel.
  The wheel contains text_workbench modules and excludes the environment. Build success
  proves packaging, not implementation correctness. No artifact was published.

## Executable examples and checks

From `projects/text-workbench/`:

```bash
uv run pytest ../../practice/test_examples.py -q
uv run python ../../practice/examples.py
uv run python ../../practice/async_demo.py
uv run python ../../practice/async_demo.py --blocking
uv run ruff check . ../../practice ../../maintenance
uv run ruff format --check . ../../practice ../../maintenance
```

- Three completed-example tests passed; dataclass, Pydantic conversion/strictness and
  allowlisted event output match lesson observations.
- Async outputs matched the two documented orders; no timing or network-performance
  claim is inferred. The lesson 7 standalone logging command produced only level/event.
- Ruff lint and format checks passed for all 18 authored Python files in the listed
  paths. Run from the stated project directory so its configuration is selected.
  The unmodified upstream snapshot is deliberately not reformatted to our style.
- Four disclosed beginner answers were tested in a temporary directory: four passed.
  The delivered beginner functions remain unfinished, each raising NotImplementedError.

## Project contract validation without completing learner work

- All 30 project tests collected and ran on the delivered starter. All 30 failed as
  expected: NotImplementedError, placeholder-model assertions or CLI assertions caused
  by unfinished settings. There were no test-collection/import infrastructure failures.
- A separate temporary implementation outside the repository passed all 30 tests,
  including real local file reads, invalid UTF-8/missing paths, invalid models/settings,
  empty files, 200,000-character input, exact size limit, logs and CLI subprocesses.
  It is not included in the learning workspace or linked as an answer.
- Six deliberate faults were each rejected by a relevant test: counting raw characters;
  rejecting exact-limit input; omitting the raw size limit; serializing private log extras;
  duplicate handlers; allowing invalid string output counts through coercion.
- The temporary correct command produced normal 17/3, empty 0/0, Unicode 7/2 output records
  and separate matching structured stderr events. These are contract checks, not a claim
  that the delivered unfinished CLI is already functional.

## Scope, navigation and provenance

- 12 numbered lessons, two references, a study desk, and a full file-to-lesson map supplied.
- `python maintenance/verify_workspace.py` from the weekly root passed: all 74 supplied
  files mapped; authored local Markdown/HTML links and HTML fragments resolved; Python
  source parsed; HTML language/viewport/title/navigation checks passed; examples reran.
- All absolute lesson `cd` starting directories exist. Project-relative check paths were
  exercised. Conditional learner-created scratch/diagram files are recognized by the
  verifier and need not exist before their lessons.
- The map explains first use/actions; lessons introduce records, fixtures, scaffolds,
  dependencies and generated categories. Main source functions and assessed notes/diagram
  are unfinished; no progress checkbox or mastery record was filled.
- PyPA sampleproject commit `621e4974ca25ce531773def586ba3ed8e736b3fc`: all 12 snapshot files
  byte-match the pinned checkout; MIT license retained. Local unittest discovery passed
  its one test. Upstream release/CI files were read, not executed. Our links into the
  snapshot are checked; inherited upstream documentation links are left unmodified.
- The draw.io template parses as XML. It is intentionally blank and does not satisfy the
  learner's diagram deliverable. Opening/saving it in the learner's diagram app is pending.
- Earlier weekly content, learner entries and Git history were preserved. Only topic
  navigation and WORKSPACE-STRUCTURE.md were updated outside the new weekly directory.
  No commits, pushes, deployments, external messages or account changes were made.

## Visual checks

- Isolated headless Chromium checked all 16 weekly HTML pages at 1280px and 390px:
  32 page/viewport checks passed with no document-level horizontal overflow, one h1,
  loaded local CSS and navigation. The file map uses an intentional horizontal scroll
  region on narrow screens, with a keyboard focus target and scroll instruction.
- Desktop study desk, mobile model lesson and mobile file map screenshots were visually
  reviewed. A missing closing brace in the reused stylesheet was fixed in Week 3 only.
- Lesson 5 rendered to a tagged three-page A4 PDF; all three pages were visually inspected
  and text/code were readable. Print answer expansion and restoration passed, including
  repeated beforeprint handling. PDF/screenshots are temporary QA artifacts, not deliverables.
- Not performed: every page at every viewport, every lesson's printed pagination,
  screen-reader testing, alternate browser engines, or opening the diagram in draw.io.

## Limits and learner actions

Local tests prove only their assertions. Fake readers do not prove service connections;
no live service/deployment is required or verified. The size check happens after a whole
file read, so it is not a memory-safety boundary. The tested large input is bounded local
data, not a production load test. Only the available Python version was executed.

Official Python, Pydantic, pytest, uv, Ruff and draw.io documentation supported the lessons;
see RESOURCES.md. The optional design book's full chapters were not accessed and no
chapter-specific summary is claimed. First installation still needs internet/cache.

The learner must implement the project, finish the reading note/diagram/README decisions,
record real debugging evidence, review their own Git changes and demonstrate delayed
retrieval and variation. Preparation and author checks do not establish those abilities.
