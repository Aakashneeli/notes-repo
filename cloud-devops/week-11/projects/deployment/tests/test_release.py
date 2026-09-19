import pytest
from release import can_promote


@pytest.mark.parametrize(
    "status,ready,observed,expected,result",
    [
        (200, True, "a", "a", True),
        (500, True, "a", "a", False),
        (200, False, "a", "a", False),
        (200, True, "old", "new", False),
        (200, True, "", "", False),
        (200, 1, "a", "a", False),
        (503, False, "a", "a", False),
    ],
)
def test_promotion(status, ready, observed, expected, result):
    assert can_promote(status, ready, observed, expected) is result
