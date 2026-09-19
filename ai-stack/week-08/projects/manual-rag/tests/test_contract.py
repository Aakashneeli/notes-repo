import json
import pytest
from fastapi.testclient import TestClient
from rag import chunk_document, Store, answer_question, create_app

DOC = dict(doc_id="policy",tenant="red",title="Policy",version=1,text="one two three four five six seven")
def test_chunk_trace():
    chunks = chunk_document(DOC, 4, 1)
    assert [c["text"] for c in chunks] == ["one two three four", "four five six seven"]
    assert [(c["start"],c["end"]) for c in chunks] == [(0,4),(3,7)]
    assert [c["chunk_id"] for c in chunks] == ["red:policy:v1:0","red:policy:v1:3"]
    for c in chunks:
        for key in ["doc_id","tenant","title","version"]:
            assert c[key] == DOC[key]
    assert chunk_document(DOC,4,1) == chunks

@pytest.mark.parametrize("size,overlap", [(0,0),(4,4),(4,-1),(True,0),(4,1.5)])
def test_chunk_invalid(size, overlap):
    with pytest.raises(ValueError):
        chunk_document(DOC,size,overlap)

def test_chunk_edges():
    assert chunk_document(dict(DOC,text="   ")) == []
    assert [c["text"] for c in chunk_document(dict(DOC,text="one two"),4,0)] == ["one two"]
    assert len(chunk_document(dict(DOC,text="one two three four"),4,1)) == 1

def payload(tenant, name):
    return dict(chunk_id=name,tenant=tenant,doc_id=name,title=name,version=1,start=0,end=1,text="evidence")

def test_store_persistence_filter_and_upsert(tmp_path):
    path = str(tmp_path/"db")
    store = Store(path,3)
    try:
        rows = [payload("red","r"),payload("blue","b")]
        store.put(rows, [[0.8,0.2,0.],[1.,0.,0.]])
        store.put([dict(rows[0],text="updated")], [[0.8,0.2,0.]])
        hits = store.search([1.,0.,0.],"red",1)
        assert len(hits) == 1 and hits[0]["chunk_id"] == "r"
        assert hits[0]["text"] == "updated"
        assert isinstance(hits[0]["score"],float)
        assert store.search([1.,0.,0.],"green") == []
    finally:
        store.close()
    store = Store(path,3)
    try:
        assert len(store.search([1.,0.,0.],"red",10)) == 1
    finally:
        store.close()

@pytest.mark.parametrize("vectors", [[], [[1.,0.]], [[0.,0.,0.]], [[float("nan"),0.,1.]]])
def test_store_rejects_bad_batch(tmp_path,vectors):
    store = Store(str(tmp_path/"db"),3)
    try:
        with pytest.raises(ValueError):
            store.put([payload("red","r")],vectors)
        assert store.search([1.,0.,0.],"red") == []
    finally:
        store.close()

def test_collection_dimension(tmp_path):
    path = str(tmp_path/"db")
    store = Store(path,3)
    store.close()
    with pytest.raises(ValueError):
        Store(path,4)

HITS = [payload("red","c1")]
def test_empty_context_never_calls_model():
    def forbidden(messages):
        raise AssertionError("provider called on empty context")
    assert answer_question("unknown",[],forbidden) == {"answer":"Insufficient evidence.","citations":[]}

def test_answer_repairs_and_builds_context():
    calls = []
    def llm(messages):
        calls.append(messages)
        return '{"answer":"supported","citations":' + ('"c1"}' if len(calls)==1 else '["c1"]}')
    assert answer_question("question",HITS,llm)["citations"] == ["c1"]
    assert len(calls) == 2
    encoded = json.dumps(calls[0])
    assert "question" in encoded and "c1" in encoded and "evidence" in encoded
    assert calls[0][0]["role"] == "system"

@pytest.mark.parametrize("raw", ["not-json",'{"answer":7,"citations":["c1"]}',
    '{"answer":"yes","citations":["secret"]}','{"answer":"yes","citations":[]}',
    '{"answer":"yes","citations":["c1","c1"]}',
    '{"answer":"","citations":["c1"]}','{"answer":"yes","citations":["c1"],"extra":1}'])
def test_bad_output_is_bounded(raw):
    calls=[]
    def llm(messages):
        calls.append(messages)
        return raw
    with pytest.raises(ValueError,match="invalid model output"):
        answer_question("question",HITS,llm)
    assert len(calls)==2

def test_no_retry_transport():
    def llm(messages):
        raise TimeoutError("SECRET")
    with pytest.raises(TimeoutError):
        answer_question("question",HITS,llm)

def test_api_flow_and_trusted_tenant(tmp_path):
    store=Store(str(tmp_path/"db"),3)
    def embed(text):
        return [1.,0.,0.]
    def llm(messages):
        return '{"answer":"Insufficient evidence.","citations":[]}'
    try:
        with TestClient(create_app(store,embed,llm)) as client:
            body = {k:v for k,v in DOC.items() if k!="tenant"}
            assert client.post("/ingest",json=body).json()=={"chunks":1}
            assert client.post("/ingest",json=dict(body,tenant="blue")).status_code==422
            hits=client.post("/search",json={"question":"policy"}).json()["hits"]
            assert hits and all(h["tenant"]=="red" for h in hits)
            result=client.post("/ask",json={"question":"policy"})
            assert result.status_code==200 and result.json()["citations"]==[]
            for question in ["", "   ", 3]:
                assert client.post("/ask",json={"question":question}).status_code==422
    finally:
        store.close()

@pytest.mark.parametrize("error,code", [(ValueError("invalid model output"),502),(TimeoutError("SECRET"),504)])
def test_api_sanitizes_provider_failures(tmp_path,error,code):
    store=Store(str(tmp_path/"db"),3)
    store.put(HITS,[[1.,0.,0.]])
    def llm(messages):
        raise error
    try:
        with TestClient(create_app(store,lambda text:[1.,0.,0.],llm)) as client:
            response=client.post("/ask",json={"question":"policy"})
            assert response.status_code==code
            assert "SECRET" not in response.text
    finally:
        store.close()
