# Week 1: Foundation

Goal: manage files, environment and Git deliberately, and write three small Python utilities you can explain. DSA is excluded. The complete material is ready now; learning it is a sequence of practice sessions, not a requirement to finish everything today.

## Seven flexible sessions

| Session | Lessons | Practice and evidence | Suggested time |
|---|---|---|---|
| 1 — start today | 01–03: learning routine, paths, inspection | First script run, command/path traces, locate JSON via two paths, find error lines, write log | 90–120 min |
| 2 | 04–06: environment, permissions, Git | Dummy env var, permission trace, staging lab, branch/merge; conflict/remote drills can be separate sessions | 120–180 min |
| 3 | 07–08: uv, values and strings | Sync project, identify interpreter, compare files, predict types, workshop strings round | 90–120 min |
| 4 | 09–11: collections, functions, paths/JSON/imports | Workshop collections/flow/io rounds, deliberate errors, file → object trace; split this session as needed | 120–180 min |
| 5 | 12–13: file counter and pretty-printer | First read the CLI/test walkthrough; then implement, test, document and merge core functions | 120–180 min |
| 6 | 14: log filter + integration | Write filter, add your own case, run full tests, inspect wrapper flow | 120–180 min |
| 7 — lighter review | 15: ownership review | Fresh clone, debugging note, docs/code reading, explain-back, retry plan | 90–120 min |

These are teaching estimates, not a new fixed daily commitment. Take breaks between lessons and repeat sessions when needed. Read docs for at most 20–30 minutes before doing a small experiment. If a lab takes longer, continue next session without declaring mastery early.

## Feedback loop

Predict first. Execute one step. Compare with expected output. Try the transfer prompt without the worked example. Keep a specific question for your teacher. Quizzes check one idea; automated tests check behavior; explain-back checks your reasoning.

## Where to work

Lessons and reference HTML open from the course [study desk](../index.html). Terminal exercises specify their starting directory. Implement code under `projects/week-01-toolbox/src/week1_toolbox/`; record evidence in `weekly-logs/week-01.md` and `python/mistake-log.md`.

The parent notes repo already contains the broader topic structure. This course provides its own weekly log and project starter within the requested directory. The roadmap's requested DSA directory/logs are intentionally omitted.

## Spaced review

The next day after a lesson: spend five minutes on its retrieve prompt with the page closed. Three days later: mix one old terminal task with a new Python task. On day 7: rebuild one function from its contract. One week after finishing: redo a path, Git and function task cold. Record actual dates in the log; do not invent completion dates.

See [coverage](coverage.md), [assessment](assessment.md), and [progress](progress.md).

## Practice route added for stronger foundations

- After lesson 08: workshop strings round.
- After lesson 09: workshop collections round.
- After lesson 10: workshop flow round.
- After lesson 11: workshop text/files round and the CLI/test walkthrough.
- After lesson 05: the isolated staging lab makes index versus working tree visible.
- After lesson 06: use the controlled conflict lab if resolving a merge still feels mysterious.

Lessons 16 and 17 are newly added Week 1 bridge material, so their filenames follow the original 15. Their place in the study sequence is **before lesson 12**, as shown on the study desk. The navigation follows that sequence.

The expanded material needs more practice time than the initial short pack. Seven sessions are an organizing guide; split them into more sittings when necessary. Do not rush a 12-exercise workbook in one sitting.
