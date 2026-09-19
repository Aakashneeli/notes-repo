import pytest
from exercises import failing_requests, monthly_total, rule_allows


def test_total():
    assert monthly_total(100, 0.01, 1, 0.005, 0.5, 2) == 5
    assert monthly_total(0, 0.01, 1, 0.005, 0.5, 2) == 3.5
    with pytest.raises(ValueError):
        monthly_total(100, -0.01, 1, 0.005, 0.5, 2)


def test_rules():
    rules = [{"port": 22, "source": "198.51.100.8/32"}]
    assert rule_allows(rules, 22, "198.51.100.8/32")
    assert not rule_allows(rules, 8000, "198.51.100.8/32")
    assert not rule_allows(rules, 22, "203.0.113.4/32")
    assert rule_allows([{"port": 22, "source": "0.0.0.0/0"}], 22, "203.0.113.4/32")
    assert not rule_allows([], 22, "198.51.100.8/32")


def test_events():
    assert failing_requests([]) == []
    assert failing_requests(
        [
            {"request_id": "a", "status": 499},
            {"request_id": "b", "status": 500},
            {"request_id": "c", "status": 503},
        ]
    ) == ["b", "c"]
