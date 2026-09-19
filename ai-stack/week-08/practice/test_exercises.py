import pytest
from practice.exercises import text_from_deltas, safe_overlap, allowed_hits

def test_deltas():
    events = [{"choices": []}, {"choices": [{"delta": {"role": "assistant"}}]},
              {"choices": [{"delta": {"content": "Thirty "}}]},
              {"choices": [{"delta": {"content": None}}]},
              {"choices": [{"delta": {"content": "days."}}]}]
    assert text_from_deltas(events) == "Thirty days."
    assert text_from_deltas([]) == ""

@pytest.mark.parametrize("size,overlap,want", [(4,1,True),(4,0,True),(4,4,False),
    (0,0,False),(4,-1,False),(True,0,False),(4,1.5,False)])
def test_overlap(size, overlap, want):
    assert safe_overlap(size, overlap) is want

def test_filter():
    rows = [{"tenant":"red","id":"a"},{"tenant":"blue","id":"b"},{"id":"c"}]
    assert allowed_hits(rows, "red") == [rows[0]]
    assert allowed_hits(rows, "green") == []
