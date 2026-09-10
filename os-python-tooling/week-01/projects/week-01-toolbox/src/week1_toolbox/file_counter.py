"""Count direct regular files, excluding symbolic links."""
import argparse
from pathlib import Path
import sys


def count_files(folder: Path) -> int:
    """Return direct file count including hidden files, excluding symlinks.

    Do not recurse. Raise FileNotFoundError for a missing path and
    NotADirectoryError for a path that exists but is not a directory.
    Lesson 12 contains a hint ladder. Write your own implementation here.
    """
    raise NotImplementedError("Implement count_files in lesson 12")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Directory to inspect")
    args = parser.parse_args()
    try:
        result = count_files(args.folder)
    except OSError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
