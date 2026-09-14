from exercises import apply_changes, page_done, supplied_fields


def test_merge():
    original = {"hot": True, "text": "tea"}
    assert apply_changes(original, {"hot": False}) == {"hot": False, "text": "tea"}
    assert original == {"hot": True, "text": "tea"}
    assert apply_changes(original, {}) == original
    assert apply_changes(original, {}) is not original


def test_fields():
    assert supplied_fields() == {"hot": False}


def test_page():
    rows = [{"id": 4, "done": True}, {"id": 1, "done": False}, {"id": 2, "done": True}]
    assert page_done(rows, True, 1, 1) == {
        "items": [{"id": 4, "done": True}],
        "total": 2,
    }
    assert page_done(rows, False, 0, 2) == {
        "items": [{"id": 1, "done": False}],
        "total": 1,
    }
    assert page_done(rows, True, 99, 1) == {"items": [], "total": 2}
    assert page_done([], True, 0, 1) == {"items": [], "total": 0}
    assert rows[0]["id"] == 4
