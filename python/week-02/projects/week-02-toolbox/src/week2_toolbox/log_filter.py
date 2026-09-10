"""Print lines whose first token is the requested log level."""
import argparse
from pathlib import Path
import sys


def filter_lines(lines: list[str], level: str) -> list[str]:
    """Select exact, case-sensitive first-token matches; retain original lines.

    Accepted levels: INFO, WARNING, ERROR. Raise ValueError otherwise.
    Ignore blanks, keep order and newlines, and do not mutate the input.
    Lesson 14 contains the hint ladder.
    """
    raise NotImplementedError("Implement filter_lines in lesson 14")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="UTF-8 log file")
    parser.add_argument("level", choices=["INFO", "WARNING", "ERROR"])
    args = parser.parse_args()
    try:
        lines = args.path.read_text(encoding="utf-8").splitlines(keepends=True)
        result = filter_lines(lines, args.level)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    sys.stdout.writelines(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
