import logging
from pathlib import Path

import pytest

from text_workbench.models import Config
from text_workbench.service import process_file


def test_injected_reader(caplog):
    calls = []

    def fake(path):
        calls.append(path)
        return " PRIVATE text "

    with caplog.at_level(logging.INFO, logger="text_workbench.service"):
        record = process_file(Path("not-on-disk"), Config(), reader=fake)
    assert calls == [Path("not-on-disk")]
    assert record.model_dump() == {"characters": 12, "words": 2}
    events = [r for r in caplog.records if r.getMessage() == "processed"]
    assert len(events) == 1
    assert (events[0].characters, events[0].words) == (12, 2)
    assert "PRIVATE" not in caplog.text
    assert "not-on-disk" not in caplog.text


def test_real_file_and_empty(tmp_path):
    path = tmp_path / "input.txt"
    path.write_text("Hello\nworld", encoding="utf-8")
    assert process_file(path, Config()).words == 2
    path.write_text("", encoding="utf-8")
    assert process_file(path, Config()).characters == 0


def test_large_and_limit(tmp_path):
    path = tmp_path / "large.txt"
    path.write_text("a " * 100_000, encoding="utf-8")
    result = process_file(path, Config())
    assert result.words == 100_000
    assert result.characters == 199_999
    with pytest.raises(ValueError):
        process_file(path, Config(max_chars=199_999))
    assert process_file(path, Config(max_chars=200_000)).words == 100_000


def test_raw_limit_not_normalized_length():
    with pytest.raises(ValueError):
        process_file(Path("unused"), Config(max_chars=1), reader=lambda _: "a  ")


def test_file_errors(tmp_path):
    with pytest.raises(FileNotFoundError):
        process_file(tmp_path / "missing", Config())
    bad = tmp_path / "bad.txt"
    bad.write_bytes(b"\xff")
    with pytest.raises(UnicodeDecodeError):
        process_file(bad, Config())
