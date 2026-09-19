import pytest
from practice.examples import ticket_graph, lookup_ticket
from pydantic import ValidationError

def test_branches():
    graph=ticket_graph()
    assert graph.invoke({'text':'OUTAGE'})['queue']=='on-call'
    assert graph.invoke({'text':'billing'})['queue']=='helpdesk'
    updates=list(graph.stream({'text':'outage'},stream_mode='updates'))
    assert [next(iter(row)) for row in updates]==['classify','fast']

def test_memory():
    graph=ticket_graph(memory=True)
    cfg={'configurable':{'thread_id':'blue-1'}}
    graph.invoke({'text':'outage'},cfg)
    assert graph.get_state(cfg).values['queue']=='on-call'
    assert graph.get_state({'configurable':{'thread_id':'blue-2'}}).values=={}

def test_tool():
    assert lookup_ticket({'ticket_id':'T-01'})=={'status':'open'}
    assert lookup_ticket({'ticket_id':'T-01'},'red')=={'status':'not_found'}
    assert lookup_ticket({'ticket_id':'T-99'})=={'status':'not_found'}
    with pytest.raises(ValidationError): lookup_ticket({'ticket_id':'../secret'})
    with pytest.raises(ValidationError): lookup_ticket({'ticket_id':'T-01','team':'red'})
