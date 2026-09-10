"""Print formatted JSON without modifying the input file."""
import argparse
import json
from pathlib import Path
import sys


def pretty_json(text: str) -> str:
    """Return valid JSON text with indent=2 and sort_keys=True.

    Accept any valid JSON value. Let JSONDecodeError propagate for invalid
    text. Do not print here. Lesson 13 contains the hint ladder.
    """
    raise NotImplementedError("Implement pretty_json in lesson 13")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="UTF-8 JSON file to read")
    args = parser.parse_args()
    try:
        result = pretty_json(args.path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
