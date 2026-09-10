import argparse
import sys


def greeting(name: str) -> str:
    if not name.strip():
        raise ValueError("name must not be blank")
    return f"Hello, {name.strip()}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Greet one person")
    parser.add_argument("name")
    args = parser.parse_args()
    try:
        message = greeting(args.name)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
