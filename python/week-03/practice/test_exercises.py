import pytest
from exercises import describe, label, lengths, read_limit


def test_label():
    assert label(None) == "(untitled)"
    assert label("  hi ") == "hi"
    assert label("") == ""


def test_lengths():
    assert lengths(["hi", "", "猫"]) == [2, 0, 1]
    assert lengths([]) == []


def test_limit():
    assert read_limit({}) == 5
    assert read_limit({"LIMIT": "8"}) == 8
    for value in ["0", "-1", "bad", ""]:
        with pytest.raises(ValueError):
            read_limit({"LIMIT": value})


def test_describe():
    calls = []

    def fake():
        calls.append(True)
        return "abc"

    assert describe(fake) == "3 chars"
    assert len(calls) == 1
