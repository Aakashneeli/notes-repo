import importlib.util
from pathlib import Path
import pytest
P=Path(__file__).resolve().parents[1]/'projects/agent-rag'
spec=importlib.util.spec_from_file_location('fixture_bridge',P/'bridge.py')
bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)

def test_fixture_boundaries():
    rag=bridge.FixtureRag()
    assert [h['id'] for h in rag.search('refund','red')]==['refund-red']
    assert rag.lookup('refund-blue','red') is None
    assert rag.search('weak','red')[0]['score']<0.5
    with pytest.raises(TimeoutError): rag.lookup('broken','red')
    assert rag.generate('bad citation refund',rag.search('refund','red'))['citations']==['foreign']
