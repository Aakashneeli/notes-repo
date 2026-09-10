# Git staging: see three versions of one file

Use a disposable repository under this course. Run one command at a time. If the directory already exists, reuse it only after inspecting it, or choose a new name; do not erase an earlier attempt.

## Create the initial snapshot

From the course root:

```bash
mkdir practice/staging-lab
cd practice/staging-lab
git init -b main
git config user.name "Practice Learner"
git config user.email "practice@example.invalid"
printf 'one\n' > notes.txt
git add notes.txt
git commit -m "Record the initial note"
```

The example identity applies only to this throwaway repository. Use your real chosen author identity in your actual project.

## Make the three versions diverge

```bash
printf 'two\n' > notes.txt
git add notes.txt
printf 'three\n' > notes.txt
git status --short
git diff
git diff --cached
git show HEAD:notes.txt
git show :notes.txt
cat notes.txt
```

Predict before comparing:

- `HEAD:notes.txt` reads the committed version: one.
- `:notes.txt` reads the staged version: two.
- `cat` reads the working tree: three.
- `git diff` shows two becoming three; `git diff --cached` shows one becoming two.
- `git status --short` shows `MM notes.txt`: both staged and unstaged changes exist.

## Commit only what was staged

```bash
git commit -m "Change the recorded note to two"
git show HEAD:notes.txt
cat notes.txt
git status --short
```

The commit contains two. The working file still contains three. Status now shows only the unstaged modification (a space in the first column, M in the second).

## Unstage without discarding

```bash
git add notes.txt
git restore --staged notes.txt
cat notes.txt
git diff --cached
git diff
```

The working file remains three. The staged diff is empty; the unstaged diff still shows two → three. This is the distinction between removing a change from the next commit and discarding the edit itself.

Explain-back: Which comparison answers “what will the next commit change”? Which command removes a file's staged changes without deleting your work?

Next: return to lesson 05. See [git diff](https://git-scm.com/docs/git-diff) and [git restore](https://git-scm.com/docs/git-restore).
