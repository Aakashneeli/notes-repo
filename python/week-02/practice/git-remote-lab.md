# Rehearse clone, push and pull without an account

Prerequisite: lesson 05, with at least one toolbox commit on `main`. Use these commands once, from the course root. The remote is a local bare repository: it holds history without a working tree. No network or GitHub account is needed.

```bash
mkdir -p practice/remote-lab
git init --bare --initial-branch=main practice/remote-lab/origin.git
cd projects/week-02-toolbox
git remote add training ../../practice/remote-lab/origin.git
git push -u training main
cd ../..
git clone practice/remote-lab/origin.git practice/remote-lab/peer
cd practice/remote-lab/peer
```

Edit the peer's README: add one sentence about how to run the tools. Use your own repository-local Git identity if prompted.

```bash
git add README.md
git diff --cached
git commit -m "Clarify toolbox setup instructions"
git push origin main
cd ../../../projects/week-02-toolbox
git fetch training
git log --oneline main..training/main
git pull --ff-only training main
```

Expected: the peer's commit appears in your toolbox. Fetch downloaded it; pull integrated it into the checked-out main branch. `--ff-only` refuses divergent history instead of silently choosing a merge/rebase policy. If refused, inspect `git log --graph --oneline --all` and ask your teacher to help reason about both histories.

If you rerun the lab, existing destinations/remotes are expected errors. Inspect `git remote -v` and reuse the existing clone instead of deleting work. These relative remote URLs are for this local drill and will not make sense if the toolbox is moved elsewhere.

## GitHub PR habit (when you have your own remote)

Create an empty GitHub repository in your account. Copy its URL into a repository-local variable (replace the example with your real URL):

```bash
course_remote_url='https://github.com/YOUR-ACCOUNT/YOUR-REPO.git'
git remote add origin "$course_remote_url"
git push -u origin main
git switch -c docs/review-pr
# Make a small README change, stage, inspect, and commit it.
git push -u origin docs/review-pr
```

GitHub will require your configured authentication. Never paste a token into a tracked file or notes. In GitHub, open a PR with base `main`, compare `docs/review-pr`, and use `templates/pull-request.md` from this course. Read the diff, record validation, then merge the PR when satisfied. Locally switch to main and run `git pull --ff-only origin main`.

Do not create an initial README/license in an otherwise empty remote when following these commands; that would create a separate initial history. If you already did, ask for help integrating the histories instead of force-pushing.

Primary reading: [Pro Git remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) and [GitHub PR guide](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).
