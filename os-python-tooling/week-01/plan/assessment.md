# Week 1 finish line

Status: not assessed. Prepared materials and instructor validation do not count as your completion.

## Demonstrate without copying

1. From the course root, read the sample JSON with both an absolute and a relative path. Explain why `cd` changes only the latter's interpretation.
2. Find error lines with line numbers. Show only the last error. Explain the pipe.
3. Pass a dummy environment variable to Python; remove it; explain inheritance. Decode `-rw-------`.
4. Show three feature branches' commits/merge history. For each commit say what changed and why. Explain staged versus unstaged changes.
5. Demonstrate clone/push/pull in the local remote lab. Write a review using the PR template. A real public PR is not required.
6. Explain what happens when you run `uv run python src/week1_toolbox/file_counter.py data/count`.
7. Locate declared requirements, resolved versions and installed packages. Explain dependency groups and the console-script mapping.
8. Distinguish file path, module import path and package, with examples from the toolbox.
9. Run all tests, then add at least one meaningful case of your own. Explain one failing test you fixed.
10. Rebuild one core function from its contract with your previous code hidden. Change one requirement and explain which behavior/test must change.
11. Follow your README from a fresh clone. Run all three tools and invalid-input examples.
12. Write one docs/code-reading note, one genuine debugging note and your terminal cheat sheet in your own words.

## Evidence bundle to show your teacher

- Your three functions and a terminal transcript of `uv run pytest -q`.
- `git log --oneline --graph --all` and one explained diff.
- Weekly log, mistake note, reading note and fresh-clone results.
- A 3–5 minute explanation: command → environment → interpreter → function → output/error.

## How we choose the next session

- **Independent:** correct behavior and explanation without hints, plus a successful variation. Proceed while spacing review.
- **With hints:** behavior works but you needed prompts or cannot explain a line. Repeat that lesson with one smaller task.
- **Blocked:** cannot locate the failure or predict basic behavior. Bring the exact command/code/output; work on one prerequisite together.

Passing supplied tests alone is insufficient. No timed algorithm or DSA assessment is included.

## Foundation readiness check

Before judging the main projects, inspect these prerequisites: can you distinguish shell commands from Python statements; trace assignment versus mutation; choose a collection for an actual operation; follow a loop without skipping iterations; return a value to a caller; separate missing files from invalid JSON; and explain staged versus working-tree content?

Use the workshop to repair a specific gap. A copied workshop answer does not count until you reconstruct it from the contract with the disclosure closed. The completed greeting command is a worked example, not one of your project deliverables.
