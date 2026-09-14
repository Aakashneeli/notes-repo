import pytest
from exercises import safe_event, valid_text, retry_decision

def test_event():
    assert safe_event('j1','running') == {'event':'job_state','job_id':'j1','state':'running'}

def test_text():
    assert valid_text('café'.encode()) == 'café'
    for data in (b'',b'a\x00b',b'\xff'):
        with pytest.raises(ValueError): valid_text(data)

@pytest.mark.parametrize('code,n,expected',[('storage_busy',1,'retry'),('storage_busy',3,'fail'),('invalid_text',1,'fail')])
def test_retry(code,n,expected): assert retry_decision(code,n) == expected
