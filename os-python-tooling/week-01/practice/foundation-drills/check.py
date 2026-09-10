"""Check one small exercise group using only Python's standard library."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile


def same(actual, expected):
    if type(actual) is not type(expected) or actual != expected:
        raise AssertionError(f"expected {expected!r}, got {actual!r}")


def cases(ex):
    checks = []

    def case(group, label, run):
        checks.append((group, label, run))

    case("strings", "tidy_name: spaces and case", lambda: same(ex.tidy_name("  REPORT.TXT  "), "report.txt"))
    case("strings", "tidy_name: empty input", lambda: same(ex.tidy_name("   "), ""))
    case("strings", "make_label: exact format", lambda: same(ex.make_label("uploads", 3), "uploads: 3 files"))
    case("strings", "make_label: zero", lambda: same(ex.make_label("new", 0), "new: 0 files"))

    def independent_list():
        original = ["a.txt"]
        result = ex.add_filename(original, "b.txt")
        same(result, ["a.txt", "b.txt"])
        same(original, ["a.txt"])
        if result is original:
            raise AssertionError("result must be a different list")

    case("collections", "add_filename: new list, preserved input", independent_list)
    case("collections", "add_filename: empty", lambda: same(ex.add_filename([], "x"), ["x"]))
    case("collections", "read_level: present", lambda: same(ex.read_level({"level": "ERROR"}), "ERROR"))
    case("collections", "read_level: missing", lambda: same(ex.read_level({}), "INFO"))
    case("collections", "read_level: explicitly empty", lambda: same(ex.read_level({"level": ""}), ""))
    case("collections", "known_levels: duplicate and case", lambda: same(ex.known_levels(["INFO", "INFO", "info"]), {"INFO", "info"}))
    case("collections", "known_levels: empty set", lambda: same(ex.known_levels([]), set()))
    for name, enabled, expected in [("a.txt", True, True), ("a.txt", False, False), ("a.TXT", True, False), ("a.log", True, False)]:
        case("flow", f"can_process: {name}, {enabled}", lambda n=name, e=enabled, x=expected: same(ex.can_process(n, e), x))
    for count, expected in [(0, "empty"), (1, "one file"), (4, "many files")]:
        case("flow", f"describe_count: {count}", lambda n=count, x=expected: same(ex.describe_count(n), x))
    case("flow", "total_bytes: all iterations", lambda: same(ex.total_bytes([12, 8, 5]), 25))
    case("flow", "total_bytes: empty", lambda: same(ex.total_bytes([]), 0))

    def unchanged_lines():
        lines = [" ", "  note\n", "\n", "last"]
        original = lines.copy()
        same(ex.keep_nonblank(lines), ["  note\n", "last"])
        same(lines, original)

    case("flow", "keep_nonblank: order, spacing, no mutation", unchanged_lines)
    case("flow", "keep_nonblank: empty", lambda: same(ex.keep_nonblank([]), []))
    for line, expected in [("  ERROR disk full\n", "ERROR"), ("\t ", ""), ("INFO", "INFO")]:
        case("io", f"first_token: {line!r}", lambda s=line, x=expected: same(ex.first_token(s), x))

    def read_text():
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "message.txt"
            path.write_text("नमस्ते\nsecond line", encoding="utf-8")
            same(ex.read_utf8(path), "नमस्ते\nsecond line")

    def missing_text():
        with tempfile.TemporaryDirectory() as folder:
            try:
                ex.read_utf8(Path(folder) / "missing.txt")
            except FileNotFoundError:
                return
            raise AssertionError("missing input should raise FileNotFoundError")

    case("io", "read_utf8: Unicode and newline", read_text)
    case("io", "read_utf8: missing input", missing_text)
    def parsed_array():
        result = ex.parse_json("[true, null, 2]")
        same(result, [True, None, 2])
        same(result[0], True)
        same(result[1], None)
        same(result[2], 2)

    case("io", "parse_json: array and value types", parsed_array)
    case("io", "parse_json: scalar", lambda: same(ex.parse_json("42"), 42))

    def invalid_json():
        try:
            ex.parse_json('{"x":}')
        except json.JSONDecodeError:
            return
        raise AssertionError("invalid text should raise JSONDecodeError")

    case("io", "parse_json: invalid syntax", invalid_json)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("group", choices=["strings", "collections", "flow", "io", "all"])
    parser.add_argument("--file", type=Path, default=Path(__file__).with_name("exercises.py"),
                        help="Alternate Python exercise file, useful for a fresh retry")
    args = parser.parse_args()
    try:
        spec = importlib.util.spec_from_file_location("learner_exercises", args.file)
        if spec is None or spec.loader is None:
            raise ValueError("Choose a Python .py exercise file")
        ex = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ex)
    except (OSError, SyntaxError, ImportError, ValueError) as error:
        print(f"Could not load your exercise file: {error}", file=sys.stderr)
        print("Check the path and Python syntax first.", file=sys.stderr)
        return 2
    checks = [(g, label, run) for g, label, run in cases(ex) if args.group in (g, "all")]
    passed = 0
    for group, label, run in checks:
        try:
            run()
        except NotImplementedError as error:
            print(f"TODO  {label}: {error}")
        except Exception as error:
            print(f"FIX   {label}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"PASS  {label}")
    print(f"\n{passed}/{len(checks)} checks passed. Explain one result before moving on.")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
