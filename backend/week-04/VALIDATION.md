# Week 4 author verification

Verified 2026-09-13. These are tutor checks of teaching material, **not learner evidence**.
All learner progress remains unassessed; main project implementations remain unfinished.

## Source and preservation

- Read the exact local roadmap article `week-4`: FastAPI — HTTP, REST, FastAPI, API Design, Postman, and API Tests. Source extraction and SHA-256 are in roadmap/source-week-04.md.
- Read the sequence rationale, numbered neighboring weeks, project ladder and broader outline. Scope comes from numbered Week 4; excluded interview material was omitted.
- Inspected topic directories, shared rules, existing lessons/assets, disclosed baseline and Week 3 source/progress. No matching Week 4 workspace existed. Reused backend and existing CSS/print components.
- Existing learner implementations, notes, logs and Git history were preserved. Changes are the new backend desk/workspace and one location entry in WORKSPACE-STRUCTURE.md. No commits, external messages, account changes or deployment were performed.

## Environment actually exercised

Python 3.14.7; uv 0.12.10; FastAPI 0.141.1; Pydantic 2.13.5; Starlette 1.6.0;
HTTPX 0.28.1; Uvicorn 0.52.4; pytest 9.1.1; Ruff 0.16.7.
Exact transitive resolutions are in projects/task-api/uv.lock. The manifest declares
Python 3.11–3.14; only the interpreter above was executed. Installed environment is
generated and ignored, approximately 52 MB including the workspace at verification.

Dependency downloads required approved network access. In the restricted author
sandbox, TestClient stalled at context entry; a timed traceback localized that stall.
The same tests passed outside the sandbox. Chromium also required execution outside
the sandbox. No test/code workaround was inserted to disguise those environment limits.

The locked stack emits two dependency deprecation warnings: Starlette's HTTPX
TestClient integration and an AnyIO BlockingPortal alias. They did not fail checks.
A future client/dependency migration should deliberately update the lock and rerun
verification. The temporary oracle's programmatic pytest entry also emitted an
assert-rewrite warning, separate from the supplied learner commands.

## Runtime checks and their precise limits

| Check | Observed result | What it establishes |
| --- | --- | --- |
| Completed bridge script | Both documented dictionary outputs matched | Runnable prerequisite fixture |
| practice/test_examples.py | 2 passed | Validation, greeting routes, bad path/query/body, badge, OpenAPI and lifespan entry/exit |
| Beginner explained answers injected in temporary author process | 3 passed | The revealed merge/field/page answers satisfy exercise checks; learner files were not edited |
| Untouched beginner starter | 3 NotImplementedError failures | Expected unfinished baseline, not infrastructure breakage |
| Full API contract against temporary correct-behavior fixture | 52 passed | Contract is satisfiable; tests accept correct public behavior |
| Temporary wrong page order | 1 targeted failure | Test exposes filter/pagination mistake |
| Temporary removal of explicit false changes | 1 targeted failure | Test exposes lost False update |
| Temporary auth bypass | 10 targeted failures | Missing/wrong auth checks reject bypass on every task operation |
| Untouched project starter | 1 passed, 51 failed | Only health is implemented; task/error/security work remains learner-owned |
| Real localhost greeting server + curl | 7 response checks passed | Documented 200/201/401/404/422 greeting requests work over a listening socket |
| Real localhost project factory smoke | Health 200 and task 404 | Factory command/import works; starter has no task routes |
| Project README curl sequence against temporary author fixture | 201, 200, 200, 200, 422, 401, 404, 204 | Commands, sample file paths and JSON inputs match the intended contract; not proof of learner implementation |
| Installed code-reading command | fastapi/routing.py, get_request_handler at line 375 in this environment | Source lookup works; learner must supply their own reading note |

Temporary author fixtures were outside the learning workspace and were never copied
into the project or hidden in scaffolding. Only the smaller greeting and Python
bridge are supplied completed examples. Local verification servers were stopped.

## Static, navigation and presentation checks

- Standard-library maintenance verifier passed: 62 supplied files, Python syntax,
  JSON parsing, local HTML/Markdown links and anchors, responsive/language metadata,
  and exact file-map coverage under `--strict`.
- Every supplied learning item has a first-use lesson and intended action. Command
  starting paths and the project/weekly-root transitions were checked against files;
  future learner exports/notes are described as outputs, not broken links.
- All 11 Postman post-response script bodies and shared print JavaScript passed
  JavaScript syntax compilation. Collection structure, ordered cases and environment
  placeholders were inspected. **Postman itself was not run or imported.** No full
  Postman JSON Schema validator or collection runtime was used.
- Ruff lint passed for project source/tests, practice and maintenance. Ruff format
  check passed for all 14 supplied project/practice Python files. git diff --check
  passed. No learner implementation was substituted to make starter checks green.
- Chromium screenshots inspected: desktop study desk at 1280×1000 and schema lesson
  at 390×844. Text/navigation were readable with no visible clipping in those views.
- Chromium print output for the pagination lesson rendered and all three pages were
  inspected with Poppler. Code stayed readable, answers expanded, no clipped text.
  This was print QA, not a separate PDF deliverable. Shared CSS supports mobile/print;
  not every lesson/viewport/browser combination was visually inspected.

## Re-run from the weekly root

```bash
cd /home/an10/code/notes-repo/backend/week-04
python maintenance/verify_workspace.py
UV_CACHE_DIR=/tmp/week4-uv-cache uv run --locked --project projects/task-api pytest practice/test_examples.py -q
UV_CACHE_DIR=/tmp/week4-uv-cache uv run --locked --project projects/task-api ruff check projects/task-api/src projects/task-api/tests practice maintenance
```

Use `python maintenance/verify_workspace.py --strict` for an author audit of every
new supplied file. Normal mode tolerates new learner outputs and reports them for
linking from the project README. The verifier never executes or grades learner code.

## Still pending, explicitly

- Learner implementation, own regression/variation tests, documentation, diagram,
  explain-back, independent delayed recall and real progress evidence.
- Actual Postman installation/import, resolved environment behavior, manual execution,
  learner additions, export and re-import; instructions and starters are provided.
- Live Swagger UI rendering against the learner API. Greeting OpenAPI JSON was checked;
  CDN asset availability is not guaranteed offline.
- Other Python versions, production concurrency, durability, TLS, external services and
  deployment. No local mock/in-process check is claimed to prove those.
- Broad visual/accessibility audit or physical printing. Representative rendering and
  static navigation checks were performed, not an exhaustive device audit.

## Depth revision after learner feedback — 2026-09-13

The initial 476–725-word lessons covered the source requirements but several lacked
sufficient worked mechanisms before assessed implementation. Expanded lessons 3–12
with parsing/validation traces, signature interpretation, model construction, state
ownership, pagination traces, error diagnosis, dependency replacement, factory/lifespan
reasoning, assertion/fixture walkthroughs and Postman response-script reasoning.
The denser lessons now contain roughly 950–1,100 words and explicit pause points;
length alone is not treated as proof of teaching quality.

Added completed practice/mechanisms.py and its focused tests, separately from the
learner's Task API. No project implementation, learner exercise or progress entry
was changed. Updated first-use map, sequence, coverage, sources and tutor preferences.

Verification of this revision:
- 10 new mechanism cases plus 2 existing instructor cases: **12 passed**.
- Additional parsing/validation probes: malformed JSON -> 422; numeric name -> 422;
  valid name -> 201, through the completed greeting app's TestClient.
- **64 supplied files and 375 local links/anchors** passed strict workspace verification.
- Ruff lint, new-file formatting and git diff --check passed.
- Updated schema lesson's normal entry rendered and was inspected at 390×844.
  Headless captures navigated directly to the new fragment returned blank images;
  those captures were not accepted as visual verification of the expanded section.
  Fragment targets passed static anchor checks. Expanded section interiors and
  revised print pagination were not visually re-audited in this revision.
- Existing dependency deprecation warnings and sandbox TestClient limitation remain
  as described above. No new learner mastery or Postman execution is claimed.
