from pathlib import Path
import sqlite3
import pytest
from fastapi.testclient import TestClient
from examples import matches, bounded, can_move, demo_app
from ingestion.config import Settings
from ingestion.repository import Repository

def test_boundaries():
    assert bounded([b"ab", b"cd"], 4) == b"abcd"
    assert bounded([], 4) == b""
    with pytest.raises(ValueError, match="too_large"):
        bounded([b"ab", b"cde"], 4)

def test_auth_and_lifecycle():
    events=[]
    with TestClient(demo_app(events)) as client:
        for headers in ({}, {"X-API-Key":"wrong"}):
            assert client.post("/receipts",headers=headers).status_code == 401
        assert events == []
        result=client.post("/receipts",headers={"X-API-Key":"demo-only"})
        assert result.status_code == 202
        assert result.json() == {"accepted":True}
        assert events == ["handler", "after-response"]

def test_settings():
    with pytest.raises(ValueError): Settings("", Path("unused"))
    assert "private-value" not in repr(Settings("private-value",Path("unused")))

def test_claim_persistence_and_parameters(tmp_path):
    path=tmp_path/'db.sqlite3'; r=Repository(path)
    evil="x'); DROP TABLE jobs;--"
    r.create('a','a.txt',evil,4)
    assert Repository(path).get('a')['original_name'] == evil
    assert r.get("' OR 1=1 --") is None
    assert r.transition('a','pending','running')
    assert not r.transition('a','pending','running')
    assert r.get('a')['attempts'] == 1
    with pytest.raises(sqlite3.IntegrityError): r.create('a','b.txt','b.txt',4)
    assert r.get('a')['storage_key'] == 'a.txt'

@pytest.mark.parametrize('old,new,expected', [('pending','running',True),('running','retrying',True),('completed','running',False),('failed','completed',False)])
def test_states(old,new,expected): assert can_move(old,new) is expected

def test_keys():
    assert matches('a','a')
    assert not matches(None,'a')
    assert not matches('','')
    assert not matches('b','a')


def test_multipart_mechanism():
    from examples import preview_app
    with TestClient(preview_app()) as client:
        result=client.post('/preview',files={'file':('a.txt',b'abcd','text/plain')})
        assert result.status_code == 200
        assert result.json() == {'name':'a.txt','bytes':4}
        assert client.post('/preview',files={'file':('a.txt',b'abcde','text/plain')}).status_code == 413
        assert client.post('/preview').status_code == 422


def test_response_schema_example():
    from typing import Literal
    from pydantic import BaseModel, ValidationError
    class Receipt(BaseModel):
        state: Literal['accepted']
    assert Receipt(state='accepted').model_dump() == {'state':'accepted'}
    with pytest.raises(ValidationError): Receipt(state='finished')


def test_supplied_sample_counts():
    data=(Path(__file__).resolve().parents[1]/'projects/ingestion/data/hello.txt').read_bytes()
    assert len(data)==34
    text=data.decode('utf-8')
    assert len(text)==34 and len(text.split())==5
