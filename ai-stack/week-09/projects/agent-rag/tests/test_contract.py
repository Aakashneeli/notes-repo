import pytest
from fastapi.testclient import TestClient
from bridge import FixtureRag
from workflow import build_graph, create_app


def run(question, tenant='red'):
    rag=FixtureRag()
    graph=build_graph(rag)
    assert hasattr(graph, 'get_graph'), 'Use a real compiled LangGraph'
    assert {'router','retrieve','lookup','answer','validate','fallback'} <= set(graph.get_graph().nodes)
    result=graph.invoke({'question':question,'tenant':tenant}, {'recursion_limit':12})
    return result,rag


def test_happy():
    out,rag=run('refund')
    assert out['status']=='answered'
    assert out['citations']==['refund-red']
    assert '30 days' in out['answer']
    assert [c[0] for c in rag.calls]==['search','generate']

@pytest.mark.parametrize('q,reason',[
    ('unknown','weak_retrieval'),('weak','weak_retrieval'),
    ('retriever-fails','retrieval_error'),('model-fails refund','generation_error'),
    ('bad citation refund','invalid_answer'),('lookup:missing','not_found'),
    ('lookup:broken','tool_error'),('lookup:../secret','invalid_tool_input'),
    ('lookup:refund-blue','not_found')])
def test_fallbacks(q,reason):
    out,rag=run(q)
    assert out['status']=='fallback' and out['reason']==reason
    assert out['answer']=='I cannot answer from the available documents.'
    assert out['citations']==[]
    if q in ('unknown','weak','lookup:../secret'):
        assert not any(c[0]=='generate' for c in rag.calls)
    if q=='lookup:../secret': assert rag.calls==[]


def test_lookup_and_isolation():
    out,rag=run('lookup:refund-red')
    assert out['status']=='answered' and out['citations']==['refund-red']
    assert [c[0] for c in rag.calls]==['lookup','generate']
    out,_=run('refund','blue')
    assert out['citations']==['refund-blue']


def test_injection_cannot_dispatch_tools():
    out,rag=run('injection')
    assert out['status']=='answered'
    assert [c[0] for c in rag.calls]==['search','generate']
    # A copied malicious sentence is still a quality problem; this only proves no dispatch.


def test_request_state_does_not_leak():
    graph=build_graph(FixtureRag())
    graph.invoke({'question':'refund','tenant':'red'})
    out=graph.invoke({'question':'unknown','tenant':'red'})
    assert out['citations']==[] and out['status']=='fallback'


def test_api():
    with TestClient(create_app(FixtureRag())) as client:
        response=client.post('/agent/ask',json={'question':'refund'})
        assert response.status_code==200
        body=response.json()
        assert set(body)=={'answer','citations','status','reason'}
        assert body['citations']==['refund-red']
        for payload in ({'question':''},{'question':'   '},{'question':'x'*501},
                        {'question':'refund','tenant':'blue'},{'question':7},{}):
            assert client.post('/agent/ask',json=payload).status_code==422
        assert client.post('/agent/ask',json={'question':'weak'}).json()['status']=='fallback'
