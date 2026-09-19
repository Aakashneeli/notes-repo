import pytest
from practice import exercises as e

@pytest.mark.parametrize('text,want',[('OUTAGE',True),('billing',False),('',False)])
def test_state_patch(text,want):
    state={'text':text,'queue':'old'}
    assert e.state_patch(state)=={'urgent':want}
    assert state=={'text':text,'queue':'old'}

@pytest.mark.parametrize('urgent,want',[(True,'fast'),(False,'normal')])
def test_next_queue(urgent,want):
    assert e.next_queue({'urgent':urgent})==want

def test_allowed_lookup():
    assert e.allowed_lookup({'ticket_id':'T-01'})=='T-01'
    for raw in ({'ticket_id':'../secret'},{'ticket_id':1},{'ticket_id':'T-01','team':'red'},{}):
        with pytest.raises(ValueError): e.allowed_lookup(raw)

def test_slowest():
    spans=[{'name':'retrieve','start_ms':0,'end_ms':20},
           {'name':'answer','start_ms':20,'end_ms':120}]
    assert e.slowest(spans)=='answer'
    assert e.slowest(list(reversed(spans)))=='answer'
