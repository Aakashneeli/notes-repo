"""Tutor-only verification of small exercises and meaningful wrong implementations.
No main project solution is supplied. Monkeypatches are confined to individual tests.
Run from weekly root: uv run pytest maintenance/test_author_checks.py -q
"""
import pytest
import examples
import test_examples
import test_exercises

def test_beginner_answers_fit_contract(monkeypatch):
    def text(data):
        if not data or b'\x00' in data:
            raise ValueError('invalid_text')
        return data.decode('utf-8')
    monkeypatch.setattr(test_exercises,'safe_event',lambda j,s:{'event':'job_state','job_id':j,'state':s})
    monkeypatch.setattr(test_exercises,'valid_text',text)
    monkeypatch.setattr(test_exercises,'retry_decision',lambda c,n: 'retry' if c=='storage_busy' and n<3 else 'fail')
    test_exercises.test_event()
    test_exercises.test_text()
    for args in [('storage_busy',1,'retry'),('storage_busy',3,'fail'),('invalid_text',1,'fail')]:
        test_exercises.test_retry(*args)

def test_check_rejects_unbounded_read(monkeypatch):
    monkeypatch.setattr(test_examples,'bounded',lambda chunks,limit:b''.join(chunks))
    with pytest.raises(pytest.fail.Exception): test_examples.test_boundaries()

def test_check_rejects_auth_bypass(monkeypatch):
    monkeypatch.setattr(examples,'matches',lambda *args:True)
    with pytest.raises(AssertionError): test_examples.test_auth_and_lifecycle()

def test_check_rejects_permissive_state_graph(monkeypatch):
    monkeypatch.setattr(test_examples,'can_move',lambda *args:True)
    with pytest.raises(AssertionError): test_examples.test_states('completed','running',False)

def test_check_rejects_empty_text(monkeypatch):
    monkeypatch.setattr(test_exercises,'valid_text',lambda data:data.decode('utf-8'))
    with pytest.raises(pytest.fail.Exception): test_exercises.test_text()

def test_check_rejects_unbounded_retry(monkeypatch):
    monkeypatch.setattr(test_exercises,'retry_decision',lambda *args:'retry')
    with pytest.raises(AssertionError): test_exercises.test_retry('storage_busy',3,'fail')
