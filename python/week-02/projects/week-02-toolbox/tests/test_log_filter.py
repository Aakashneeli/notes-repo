import pytest
from week2_toolbox.log_filter import filter_lines


def test_matches_level_not_message_and_preserves_order():
    lines = ["ERROR first\n", "INFO previous ERROR recovered\n",
             "ERROR second\n", "ERRORISH wrong\n", "error lowercase\n"]
    original = lines.copy()
    assert filter_lines(lines, "ERROR") == ["ERROR first\n", "ERROR second\n"]
    assert lines == original


def test_empty_and_blank_lines():
    assert filter_lines([], "INFO") == []
    assert filter_lines(["\n", "   ", "\t\n"], "ERROR") == []


def test_preserves_whitespace_and_final_line():
    assert filter_lines(["  ERROR spaced\n", "ERROR final"], "ERROR") == [
        "  ERROR spaced\n", "ERROR final"]


@pytest.mark.parametrize("level", ["DEBUG", "error", "", " ERROR "])
def test_rejects_unsupported_requested_level(level):
    with pytest.raises(ValueError):
        filter_lines([], level)


def test_other_levels_and_no_matches():
    assert filter_lines(["WARNING retry\n"], "WARNING") == ["WARNING retry\n"]
    assert filter_lines(["INFO ready\n"], "ERROR") == []
