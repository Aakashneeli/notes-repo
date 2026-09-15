import pytest
from exercises import safe_fields, service_address


def test_addresses():
    assert service_address("host") == ("127.0.0.1", 8077)
    assert service_address("worker") == ("api", 8000)
    with pytest.raises(ValueError):
        service_address("unknown")


def test_allowlist():
    original = {"event": "http", "request_id": "abc", "status": 201,
                "body": "private", "password": "secret", "new_secret": "oops"}
    assert safe_fields(original) == {"event": "http", "request_id": "abc", "status": 201}
    assert original["body"] == "private"
    assert safe_fields({}) == {}
