"""Behavior contracts, not a solution: run with uv run pytest -q."""
from pathlib import Path
import pytest
from week1_toolbox.file_counter import count_files


def test_counts_only_direct_files_including_hidden(tmp_path):
    (tmp_path / "a.txt").write_text("hello", encoding="utf-8")
    (tmp_path / ".hidden").write_text("hidden", encoding="utf-8")
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "deep.txt").write_text("deep", encoding="utf-8")
    assert count_files(tmp_path) == 2


def test_empty_directory(tmp_path):
    assert count_files(tmp_path) == 0


def test_missing_path(tmp_path):
    with pytest.raises(FileNotFoundError):
        count_files(tmp_path / "missing")


def test_file_is_not_directory(tmp_path):
    file = tmp_path / "file.txt"
    file.touch()
    with pytest.raises(NotADirectoryError):
        count_files(file)


def test_symlinks_are_excluded(tmp_path):
    target = tmp_path / "real.txt"
    target.touch()
    (tmp_path / "link.txt").symlink_to(target)
    (tmp_path / "broken.txt").symlink_to(tmp_path / "absent")
    assert count_files(tmp_path) == 1


def test_returns_integer(tmp_path):
    assert type(count_files(Path(tmp_path))) is int
