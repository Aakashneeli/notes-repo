# Completion is demonstrated ability

All items are learner demonstrations, not tutor checkboxes. Record evidence in
weekly-logs/week-03.md and link it from progress.md.

- Implement normalize, split_text and summarize from contracts with examples closed.
  Predict normal, whitespace-only, Unicode and punctuation results before testing.
- Explain all public typed signatures, including optional versus default arguments.
- Show a dataclass accepting a wrong type and a strict Pydantic field rejecting it.
  Explain conversion, defaults, forbidden extras, required output fields and serialization.
- Trace command-scoped env strings through load_settings to a Config; demonstrate bad
  config, missing config and an exact-size boundary without silently defaulting errors.
- Show one success JSON record on stdout and one safe structured event on stderr.
  Explain logger threshold, handler, formatter, propagation, and the allowlist's limits.
- Demonstrate pure core tests, injected-reader workflow tests, real tmp_path tests and
  CLI subprocess tests. Explain why each isolates a different failure boundary.
- Reproduce and fix a meaningful bug, add a new regression test, and explain the failure.
- Pass the required project tests and Ruff checks; explain every scaffold, import,
  fixture and wrapper. Add tests for your own variations rather than only supplied cases.
- Predict the two async traces and a sequential-await variation; explain why synchronous
  local file processing is sufficient here and why blocking inside async still blocks.
- Fill a real repo architecture note with entrypoints/modules/tests/config evidence.
- Save your actual editable draw.io/Excalidraw module diagram; distinguish imports from
  data flow. A blank template or tutor diagram does not satisfy this requirement.
- Complete project README setup, outputs, failures, design rationale and size limitation;
  demonstrate a reviewed local commit and reproduction from declared dependencies.
- After a delay, explain and vary the program without a copied implementation.

## Roadmap explain-back — answer in your weekly log

1. Why did you split the code into these modules? Cite one benefit and one cost.
2. Which functions are pure and which cause side effects? Trace each effect's caller.
3. Where is configuration loaded, and why there? Show how a test supplies different settings.
4. What would become hard to test if you moved code into the wrong layer? Demonstrate with
   one proposed bad move, without damaging your working version.

Do not mark complete if a required artifact or explanation is missing. Local checks do
not prove production memory limits, live integration, deployment or learning durability.
