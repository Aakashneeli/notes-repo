# Week 03 — Pro Python

**Source title:** Professional Python Structure, Pydantic, Logging, and Practical LLD.
**Source:** `/home/an10/Downloads/ai-backend-roadmap.html`, numbered article `week-3`.
**Workspace:** `/home/an10/code/notes-repo/python/week-03/`.

Start at [the study desk](index.html), then [lesson 1](lessons/0001-start-and-baseline.html).
Main deliverables: your src-layout text-processing package with typed signatures,
Pydantic config/output validation, settings, structured logging, pytest, Ruff,
.env.example and README; a codebase-reading note; an editable draw.io/Excalidraw module
diagram; evidence that you can debug, explain and vary the work.

Week 3 is an existing exact numbered section, not a reused Foundation syllabus.
The existing [Week 2 Foundation desk](../week-02/index.html) follows a historical
numbering exception and is preserved. No Week 3 conflict exists. This new text package
is not an extension of a missing earlier app. The small bridges in lessons 1 and 3 are
based on the disclosed baseline, not presumed mastery of Week 2.

## Start and navigate

```bash
cd /home/an10/code/notes-repo/python/week-03
```

Open index.html in your browser. Markdown/code links are intended for reading in an
editor; browsers may display or download them. Lessons introduce files when needed;
[the file map](plan/file-map.html) records first-use lessons and actions for every
supplied file. Start commands from the directory stated in each lesson.

- `lessons/`: short teaching units with worked traces, practice and feedback.
- `reference/`, `assets/`: quick retrieval and shared accessible screen/print components.
- `plan/`: sequence, scope coverage, file map, assessment and learner progress.
- `practice/`: clearly separated completed examples and unfinished small exercises.
- `projects/text-workbench/`: assessed package; implementation intentionally unfinished.
- `templates/`, `weekly-logs/`, `python/`: reusable prompts and learner evidence/mistakes.
- `codebase-reading/`: pinned real upstream snapshot and your architecture note.
- `roadmap/`: exact source mapping and brief context only.
- `maintenance/`, `VALIDATION.md`: author checks, never learner mastery.

## Tools and boundaries

Python >=3.12, uv, pytest, Pydantic v2 and Ruff; a normal CPU and terminal are enough.
Initial dependency installation requires internet and local disk. No paid service,
credentials, GPU, backend server or cloud account is needed. For the diagram use a
local draw.io editor or explicitly choose diagrams.net device storage. The editable
project diagram remains a learner deliverable; the supplied template is blank.

Package setup (lesson 2):

```bash
cd projects/text-workbench
UV_CACHE_DIR=/tmp/week03-uv-cache uv sync --locked
uv run text-workbench --help
```

`UV_CACHE_DIR` changes only where uv caches downloads for that command; a normal later
uv command may use the default cache. It does not move the project environment.
Installed packages and caches are generated, ignored files, not lesson content.

All substantive project work stays in this notes repository; its project subdirectory
is independently packaged. This adapts the roadmap's separate-repo convention to the
user's repository-only constraint. No publication or nested Git history is created.
All excluded interview/DSA material and logs remain excluded. Full future-week teaching
is out of scope. [Coverage](plan/coverage.md) explains every scope decision.

[Validation](VALIDATION.md) distinguishes passing teaching examples from intentional
unfinished-starter failures. No work is marked learned automatically.
