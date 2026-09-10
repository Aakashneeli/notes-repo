# Roadmap → Week 1 material

Source: `/home/an10/Downloads/ai-backend-roadmap.html`, Foundation section. Read on 2026-09-08. All non-DSA Week 1 requirements are mapped below. Practical file/JSON handling and minimal test reading are introduced only as needed for the three required scripts; deeper Python belongs to the next week.

| Roadmap requirement | Material | Proof |
|---|---|---|
| Learning system, notes and AI discipline | Lesson 01, MISSION.md, AI-USAGE.md, weekly log | Prediction/attempt/explanation and AI-use note |
| pwd, ls, cd; absolute/relative paths | Lesson 02 | Same file via two paths |
| cat, less, head, tail, rg, find | Lesson 03 | Find error lines and filenames |
| Files/folders, permissions, env vars | Lessons 02, 04 | Dummy setting and permission explanation |
| Git init, status, add, commit | Lesson 05 | Inspect actual staged diff and commit |
| Branch, merge, readable messages | Lesson 06 and each script lab | One branch and merge per command |
| Clone, push, pull and PR habit | Lesson 06, practice/git-remote-lab.md, PR template | Local remote round trip; PR-style review; optional real GitHub PR |
| uv, pyproject.toml, groups, scripts | Lesson 07, supplied packaged starter | Interpreter location, sync, command help |
| Variables, types, strings | Lesson 08 | Predict and modify values |
| Lists, dicts, sets | Lesson 09 | Explain representation and mutation |
| Loops, conditionals, functions | Lesson 10 | Write label_count and assertions |
| Files, imports, packages needed by tools | Lesson 11 | Path → text → object explain-back |
| File counter | Lesson 12, starter, data, tests | Own implementation + passing cases |
| JSON pretty-printer | Lesson 13, starter, data, tests | Preserve JSON meaning and input |
| Simple log filter | Lesson 14, starter, data, tests | Exact first-token matching |
| Docs-reading habit | Every lesson, RESOURCES.md, reading template | Official source → small experiment |
| Week log and own-word terminal sheet | weekly-logs/week-01.md, python/terminal-in-my-words.md | User-authored explanations |
| Explain-back prompts and repeatability | Lesson 15, assessment | Fresh clone and verbal explanation |

## Depth added after the first review

Every core lesson now includes a worked explanation, concrete trace or comparison, and misconception/transfer feedback. New support stays within the non-DSA Week 1 requirements:

| Earlier gap | New support |
|---|---|
| Where/how to type and run code | Lesson 01: shell versus REPL versus editor; save/run/modify cycle |
| Commands felt like unexplained recipes | Lessons 02–04: path tree, argument/quote breakdown, pipe/output trace, permission and process models |
| Git snapshots and conflicts were too abstract | Lessons 05–06 plus isolated staging and conflict labs |
| uv configuration looked like boilerplate | Lesson 07: command flow and configuration-table walkthrough |
| Python definitions jumped to projects | Lessons 08–11 traces plus workshop's 12 small exercises and 30 checks |
| Supplied wrappers/tests were unexplained | Lesson 17: complete greeting CLI, two worked tests and a toolbox mapping |
| Learner could get stuck without feedback | Two hints and an explained answer per workshop function; six debugging exercises |
| Project contracts needed interpretation | Lessons 12–14: decision tables, output boundaries and failure diagnosis |
| “Explain it” was underspecified | Lesson 15: example explanation, variation prompts and evidence format |
