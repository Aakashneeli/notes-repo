# Foundation resources

Reviewed 2026-09-08. Use the linked section for a small experiment, not cover-to-cover reading.

## Knowledge

- [Python: numbers, strings, lists](https://docs.python.org/3/tutorial/introduction.html)
  Use for: values, strings and list basics.
- [Python: control flow and functions](https://docs.python.org/3/tutorial/controlflow.html)
  Use for: branches, iteration and small functions.
- [Python: collection operations](https://docs.python.org/3/tutorial/datastructures.html)
  Use for: lists, dictionaries, sets and mutation.
- [Python: modules and packages](https://docs.python.org/3/tutorial/modules.html)
  Use for: file paths versus imports and packages.
- [Python: file input and output](https://docs.python.org/3/tutorial/inputoutput.html)
  Use for: UTF-8 text reading and output.
- [Python: errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
  Use for: distinguishing syntax, type, file and parsing failures.
- [Python: pathlib reference](https://docs.python.org/3/library/pathlib.html)
  Use for: direct directory iteration, file checks and symlinks.
- [Python: JSON reference](https://docs.python.org/3/library/json.html)
  Use for: loads/dumps, indentation and parse errors.
- [Python: argparse tutorial and reference](https://docs.python.org/3/library/argparse.html)
  Use for: understanding the supplied command wrappers.
- [uv: working on projects](https://docs.astral.sh/uv/guides/projects/)
  Use for: project creation, lockfiles and environments.
- [uv: dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/)
  Use for: runtime requirements versus development tools.
- [uv: packaging and command entry points](https://docs.astral.sh/uv/concepts/projects/config/)
  Use for: src packaging and console script mappings.
- [Pro Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
  Use for: staging, reviewing diffs and committing.
- [Pro Git: branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
  Use for: feature branches, merges and conflicts.
- [Pro Git: remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
  Use for: clone/fetch/push/pull rehearsal.
- [GitHub: creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)
  Use for: proposing and reviewing a change.
- [ripgrep: maintainer’s guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)
  Use for: content searches and default exclusions.
- [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
  Use for: shell navigation, quoting and environment inheritance. Local bash help cd/export was consulted because web retrieval failed.
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
  Use for: file listing, head/tail and permissions. Installed --help output was consulted because web retrieval failed.
- [GNU Findutils manual](https://www.gnu.org/software/findutils/manual/html_mono/find.html)
  Use for: finding paths by name/type; local find --help consulted.
- [pytest: first tests](https://docs.pytest.org/en/stable/getting-started.html)
  Use for: running supplied assertions and understanding failures.

- [Python interpreter modes](https://docs.python.org/3/tutorial/interpreter.html)
  Use for: where to type shell versus Python commands and how script execution differs from interactive evaluation.
- [Python built-in types](https://docs.python.org/3/library/stdtypes.html)
  Use for: truthiness, short-circuit conditions, string splitting and mutation semantics.
- [Git diff reference](https://git-scm.com/docs/git-diff)
  Use for: exact comparisons among working tree, index and commits.
- [Git restore reference](https://git-scm.com/docs/git-restore)
  Use for: unstaging edits without discarding working-tree content.
- [Git status reference](https://git-scm.com/docs/git-status)
  Use for: interpreting the two short-status columns.
- [uv project command execution](https://docs.astral.sh/uv/concepts/projects/run/)
  Use for: explaining project discovery, environment synchronization and command invocation.
- [Python unittest](https://docs.python.org/3/library/unittest.html)
  Use for: the two dependency-free tests accompanying the complete greeting example. The actual toolbox continues to use pytest.

## Wisdom (Communities)

- [Python Help on Python.org](https://discuss.python.org/c/help/7)
  Use for a focused question with a minimal reproduction after your own attempt. Participation is optional; no posts are made for you.

## Gaps

- Weeks 2–12 sources will be reviewed when those lessons are authored. Their summaries are curriculum planning, not current API guidance.
- GNU web manuals did not load during research; installed author-provided help was the verification source for terminal examples.
