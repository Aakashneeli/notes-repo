# Learning workspace organization

Use existing topic directories and place each requested week at `<topic>/week-XX/`.
Inspect existing content before creating or moving anything. The explicit user-selected topic takes priority; never duplicate a week across topics. Choose future-week locations only when that week is requested.

Current locations:
- `os-python-tooling/week-01/`: existing Week 1 material, relocated with progress preserved.
- `python/week-02/`: the requested Week 2 Foundation workspace.
- `python/week-03/`: source Week 3 — Pro Python (Professional Python Structure, Pydantic, Logging, and Practical LLD).

Each topic may have a short README and HTML index linking its weeks. Each weekly root uses:

```text
index.html                     study desk
README.md                      entry instructions and workspace map
MISSION.md / RESOURCES.md       purpose and annotated primary sources
NOTES.md / AI-USAGE.md          teaching context and assistance rules
VALIDATION.md                   author verification, when performed
assets/                        shared lesson components
lessons/                       numbered, self-contained HTML lessons
reference/                     printable glossary and references
plan/                          README, coverage, assessment, progress
practice/                      beginner exercises and completed examples
projects/                      project starters, samples and checks
templates/                     reusable blank records
weekly-logs/                   session and spaced-retrieval evidence
python/                        Python/tooling mistakes and own-word notes
codebase-reading/              docs and code-reading evidence
learning-records/              only when a justified record exists
roadmap/                       optional brief roadmap context
maintenance/                   verification helpers, when useful
```

Consistency means the same location and naming for the same purpose. Do not manufacture empty records, unused directories or duplicate course content merely to make every week contain identical files.

Lessons must teach how and when to use the workspace, across every topic and future requested week. Introduce each supplied folder and file at its first relevant use: explain its purpose and whether the learner should read, edit, run, fill in, or leave it unchanged. A README or file listing alone is insufficient.

Each hands-on step should specify its starting directory, relative file path, navigation command when needed, intended action, check or expected result, evidence destination, and next step. Connect practice, projects, sample data, tests, configuration, references, templates and learning logs to the lessons that use them. Explain when learning records are justified and who updates them.

Link a compact folder/file-to-lesson map from the study desk, showing the first relevant lesson or section and intended action. Distinguish completed examples, unfinished learner files, supplied infrastructure, generated files and tutor-maintained records. Explain environments and caches as categories rather than documenting every installed dependency file. Verify links and starting paths after moves; introduce navigation progressively.

On migration, preserve learner implementations, logs, progress, Git history and data. Update teaching links, starting directories, package/environment references and planning links. Keep historical evidence intact. Do not reset exercises, infer mastery, delete existing work, or rerun a lab on top of an earlier attempt. Recreate generated environments when relocation breaks absolute paths, using declared dependencies.

Week number and syllabus title must be checked against the source roadmap. If they differ, state the mismatch and follow the user's explicitly selected syllabus; do not silently mix weeks. Detailed lessons are created only for the requested week. Excluded interview practice and associated logs stay excluded across all weeks.
