import json
import logging
import os
import subprocess
import sys
from pathlib import Path

from text_workbench.logging_setup import JsonFormatter, configure_logging

ROOT = Path(__file__).resolve().parents[1]


def test_formatter_allowlist():
    record = logging.LogRecord("demo", logging.INFO, "", 0, "processed", (), None)
    record.characters = 3
    record.words = 1
    record.secret = "DO-NOT-LOG"
    value = json.loads(JsonFormatter().format(record))
    assert value == {"level": "INFO", "event": "processed", "characters": 3, "words": 1}


def test_configure_twice(capsys):
    logger = logging.getLogger("text_workbench")
    old_handlers, old_level, old_propagate = logger.handlers[:], logger.level, logger.propagate
    try:
        configure_logging("INFO")
        configure_logging("INFO")
        logger.debug("hidden")
        logger.info("ready")
        lines = capsys.readouterr().err.splitlines()
        assert len(lines) == 1
        assert json.loads(lines[0]) == {"level": "INFO", "event": "ready"}
    finally:
        logger.handlers = old_handlers
        logger.setLevel(old_level)
        logger.propagate = old_propagate


def run_cli(path, **overrides):
    env = {k: v for k, v in os.environ.items() if not k.startswith("TEXT_")}
    env.update(overrides)
    return subprocess.run(
        [sys.executable, "-m", "text_workbench.cli", str(path)],
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )


def test_cli_success():
    result = run_cli(ROOT / "data/normal.txt")
    assert result.returncode == 0
    assert json.loads(result.stdout) == {"characters": 17, "words": 3}
    assert json.loads(result.stderr) == {
        "level": "INFO",
        "event": "processed",
        "characters": 17,
        "words": 3,
    }


def test_cli_negative(tmp_path):
    for path, env in [
        (tmp_path / "PRIVATE-missing", {}),
        (ROOT / "data/normal.txt", {"TEXT_MAX_CHARS": "bad"}),
        (ROOT / "data/normal.txt", {"TEXT_MAX_CHARS": "1"}),
    ]:
        result = run_cli(path, **env)
        assert result.returncode == 2
        assert result.stdout == ""
        assert result.stderr == "Cannot process input: check file, encoding, size and settings.\n"
