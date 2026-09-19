"""Author checks only; no learner implementation or complete RAG solution."""
import importlib.util
import json
from pathlib import Path

import pytest
from pydantic import ValidationError
from practice.examples import cosine, windows, parse_answer, client_demo, hit_rate
from practice.provider_probe import request_body

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bridge", ROOT/"projects/manual-rag/bridge.py")
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)

def test_vectors_and_meaningful_mutation():
    assert cosine([1,0],[1,1]) == pytest.approx(2**-0.5)
    assert cosine([2,0],[1,0]) == 1
    assert cosine([1,0],[0,1]) == 0
    # A common bug returns raw dot product: this distinguishing case rejects it.
    broken = lambda a,b: sum(x*y for x,y in zip(a,b))
    assert broken([2,0],[1,0]) != cosine([2,0],[1,0])

@pytest.mark.parametrize("a,b", [([0,0],[1,0]),([1],[1,0]),([],[])])
def test_bad_vectors(a,b):
    with pytest.raises(ValueError):
        cosine(a,b)

def test_window_trace_and_tail_mutation():
    rows=windows("one two three four five six seven")
    assert [r["text"] for r in rows]==["one two three four","four five six seven"]
    assert [(r["start"],r["end"]) for r in rows]==[(0,4),(3,7)]
    assert windows("")==[]
    assert len(windows("one two three four"))==1
    words="one two three four five six seven".split()
    broken=[" ".join(words[i:i+4]) for i in range(0,len(words),3)]
    assert broken != [r["text"] for r in rows]  # Duplicate final tail is exposed.

@pytest.mark.parametrize("size,overlap",[(0,0),(4,4),(4,-1)])
def test_bad_windows(size,overlap):
    with pytest.raises(ValueError):
        windows("one",size,overlap)

def test_structured_happy():
    assert parse_answer('{"answer":"yes","citations":["c1"]}',["c1"]).answer=="yes"

@pytest.mark.parametrize("raw",['oops','{"answer":3,"citations":[]}',
    '{"answer":"yes","citations":"c1"}','{"answer":"yes","citations":["private"]}',
    '{"answer":"yes","citations":[],"extra":true}'])
def test_structured_bad(raw):
    with pytest.raises((ValidationError,ValueError)):
        parse_answer(raw,["c1"])

def test_local_store_real_persistence_filter():
    assert client_demo()==["red:1"]

def test_hit_denominator():
    rows=[{"expected":["a"],"retrieved":["a"]},{"expected":["b"],"retrieved":[]},
          {"expected":[],"retrieved":[]}]
    assert hit_rate(rows)==0.5
    assert hit_rate([rows[-1]]) is None
    assert 1/len(rows) != hit_rate(rows)  # Incorrect unknown-inclusive denominator.

def test_fixture_and_golden_seeds():
    docs=bridge.load_documents()
    assert len(docs)==6
    keys={(d["tenant"],d["doc_id"]) for d in docs}
    rows=json.loads((ROOT/"projects/manual-rag/data/golden-seeds.json").read_text())
    assert 15 <= len(rows) <= 25
    assert len({r["id"] for r in rows})==len(rows)
    for row in rows:
        assert row["question"] and row["expected_answer"]
        assert all((row["tenant"],doc_id) in keys for doc_id in row["expected_docs"])

def test_dry_request_is_safe_shape():
    body=request_body("test-model")
    assert body["stream"] is False
    assert [m["role"] for m in body["messages"]]==["system","user"]
    assert "api_key" not in body

def test_http_testclient_infrastructure():
    # Verifies the installed route/body/testing boundary without implementing RAG.
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from pydantic import BaseModel
    class EchoBody(BaseModel):
        text: str
    app=FastAPI()
    @app.post("/echo")
    def echo(body: EchoBody):
        return {"text":body.text}
    with TestClient(app) as client:
        assert client.post("/echo",json={"text":"hello"}).json()=={"text":"hello"}
        assert client.post("/echo",json={"text":3}).status_code==422
