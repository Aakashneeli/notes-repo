# Workspace relocation verification — 2026-09-10

The Week 1 workspace moved from `os-python-tooling/` to `os-python-tooling/week-01/`. Its planning files moved from `weeks/week-01/` to `plan/`, matching the Week 2 layout. Topic-level README and HTML entry pages now link to each weekly study desk. See [shared organization rules](../../WORKSPACE-STRUCTURE.md).

All 68 original material files were checked after the move. Learner Python source, progress and logs remain byte-for-byte unchanged. Teaching links and terminal starting paths were updated; NOTES received an appended relocation record. Historical evidence retains its original wording. An existing unterminated shell quote in lesson 04 was repaired.

Verification:

- 21 HTML pages, 254 local HTML links and anchors, and Markdown links: no broken links.
- 35 recognizable shell blocks: syntax checks pass. Supplied Python files compile.
- The project environment was rebuilt offline from the unchanged manifest and lockfile. Python imports resolve to the new source directory.
- All three installed CLI help commands work; the three corresponding subprocess tests pass. Main implementations remain learner exercises.
- Week 2 still passes its independent link/syntax checks: 32 HTML pages, 459 local HTML links and 44 shell blocks.

The old generated environment is recoverable at `.validation/venv-before-relocation/`. It is retained only as a backup; use the rebuilt `.venv` in the new project directory. No learning progress or mastery was inferred from these checks. No new visual browser review was performed for this structural migration.

To recheck links and syntax, run `python maintenance/verify_workspace.py` from this weekly root. Earlier content-validation results remain in NOTES as history.
