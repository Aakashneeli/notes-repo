"""End-to-end checks: real commands, real fixture inputs, exit/output behavior."""
from pathlib import Path
import subprocess
import sys
import json
import pytest

ROOT = Path(__file__).resolve().parents[1]


def run(module, *args):
    return subprocess.run([sys.executable, "-m", f"week2_toolbox.{module}", *args],
                          cwd=ROOT, capture_output=True, text=True, timeout=10)


@pytest.mark.parametrize("module", ["file_counter", "json_pretty", "log_filter"])
def test_help_without_implementation(module):
    result = run(module, "--help")
    assert result.returncode == 0
    assert "usage:" in result.stdout


def test_counter_command():
    result = run("file_counter", "data/count")
    assert result.returncode == 0
    assert result.stdout == "3\n"
    assert result.stderr == ""


def test_pretty_command_keeps_source():
    path = ROOT / "data/example.json"
    before = path.read_bytes()
    result = run("json_pretty", str(path))
    assert result.returncode == 0
    assert json.loads(result.stdout) == json.loads(before)
    assert path.read_bytes() == before


def test_log_command():
    result = run("log_filter", "data/app.log", "ERROR")
    assert result.returncode == 0
    assert result.stdout == "ERROR upload failed\nERROR storage unavailable\n"


@pytest.mark.parametrize("module,args", [
    ("file_counter", ["data/does-not-exist"]),
    ("json_pretty", ["data/invalid.json"]),
    ("json_pretty", ["data/does-not-exist"]),
    ("log_filter", ["data/does-not-exist", "ERROR"]),
    ("log_filter", ["data/app.log", "DEBUG"]),
])
def test_input_failure(module, args):
    result = run(module, *args)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "error:" in result.stderr


@pytest.mark.parametrize("module", ["file_counter", "json_pretty", "log_filter"])
def test_missing_arguments(module):
    result = run(module)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "usage:" in result.stderr


@pytest.mark.parametrize("module,args", [("json_pretty", []), ("log_filter", ["ERROR"])])
def test_invalid_utf8_is_a_read_failure(module, args, tmp_path):
    source = tmp_path / "invalid-utf8.txt"
    source.write_bytes(b"\xff")
    result = run(module, str(source), *args)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "error:" in result.stderr
