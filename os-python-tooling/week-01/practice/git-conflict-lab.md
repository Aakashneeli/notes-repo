# Git conflict: choose the final meaning

Do this after the ordinary branch/merge exercise. It intentionally creates overlapping edits in a disposable repository. Run one block at a time.

## Start from shared content

From the course root:

```bash
mkdir practice/conflict-lab
cd practice/conflict-lab
git init -b main
git config user.name "Practice Learner"
git config user.email "practice@example.invalid"
printf 'Run from here.\n' > usage.txt
git add usage.txt
git commit -m "Record initial usage note"
```

The dummy author identity is local to this practice repo.

## Make the same line mean different things

```bash
git switch -c docs/location
printf 'Run from the toolbox folder.\n' > usage.txt
git add usage.txt
git commit -m "Specify the toolbox location"
git switch main
printf 'Run from the project root.\n' > usage.txt
git add usage.txt
git commit -m "Specify the project root"
git merge docs/location
```

Expected: merge stops with a content conflict. That nonzero exit status is intentional. Inspect before changing anything:

```bash
git status
cat usage.txt
git log --oneline --graph --all
```

HEAD's side is main's text; the other side is docs/location's text. Both descend from the original note, and both replaced the same line. There is no universally correct string for Git to choose.

## Resolve with a coherent sentence

Open usage.txt in your editor. Replace the entire conflict-marked region with:

```text
Run from projects/week-01-toolbox, the project root.
```

Save the file, then:

```bash
git diff
git add usage.txt
git commit -m "Clarify project root and toolbox location"
git status
git log --oneline --graph --all
```

Expected: a clean working tree and a merge commit connecting both histories. Verify no conflict markers remain. Explain why the chosen sentence carries both intended clarifications.

If you want to abandon the attempt while the merge is still in progress, `git merge --abort` can return you to the pre-merge state. It is not the right command after the merge has already been committed. Start a new practice repository for a clean retry instead of rewriting history you do not understand.

Primary source: [Pro Git branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
