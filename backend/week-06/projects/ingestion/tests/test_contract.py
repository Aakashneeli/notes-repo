"""Behavior contracts for unfinished learner project. No skips or xfail masking TODOs."""
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from ingestion.app import create_app
from ingestion.config import Settings
from ingestion.repository import Repository
from ingestion.storage import LocalStorage
from ingestion.worker import run_job

@pytest.fixture
def setup(tmp_path):
    settings=Settings('test-only', tmp_path, max_bytes=32)
    with TestClient(create_app(settings)) as client:
        yield client, settings

HEADERS={'X-API-Key':'test-only'}
def upload(client, data=b'Hello world', name='note.txt', kind='text/plain', headers=HEADERS):
    return client.post('/documents', headers=headers, files={'file':(name,data,kind)})

@pytest.mark.parametrize('headers',[{}, {'X-API-Key':'incorrect'}])
def test_reject_key(setup,headers):
    client, settings=setup
    assert upload(client,headers=headers).status_code == 401
    assert client.get('/jobs/unknown',headers=headers).status_code == 401
    assert not list((settings.root/'blobs').glob('*'))

@pytest.mark.parametrize('data,name,kind,status',[
    (b'', 'a.txt','text/plain',400),
    (b'x'*33,'a.txt','text/plain',413),
    (b'abc','../a.txt','text/plain',400),
    (b'abc',r'..\a.txt','text/plain',400),
    (b'abc','a.html','text/plain',415),
    (b'abc','a.txt','application/pdf',415),
    (b'\xff','a.txt','text/plain',415),
    (b'a\x00b','a.txt','text/plain',415)])
def test_invalid_upload(setup,data,name,kind,status):
    client,settings=setup
    assert upload(client,data,name,kind).status_code == status
    assert not list((settings.root/'blobs').glob('*'))

def test_complete_repeat_and_restart(setup):
    client,settings=setup
    response=upload(client)
    assert response.status_code == 202
    accepted=response.json()
    assert accepted['state'] == 'pending'
    jid=accepted['job_id']
    status=client.get('/jobs/'+jid,headers=HEADERS)
    assert status.status_code == 200
    expected={'job_id':jid,'state':'completed','attempts':1,'characters':11,'words':2,'error_code':None}
    assert status.json() == expected
    repo=Repository(settings.root/'metadata.sqlite3')
    row=repo.get(jid)
    key=row['storage_key']
    assert key.endswith('.txt') and len(key)==36
    int(key[:-4],16)
    assert row['original_name']=='note.txt' and row['size']==11
    assert (settings.root/'blobs'/key).read_bytes()==b'Hello world'
    run_job(jid,repo,LocalStorage(settings.root/'blobs'))
    assert repo.get(jid)['attempts']==1
    with TestClient(create_app(settings)) as fresh:
        assert fresh.get('/jobs/'+jid,headers=HEADERS).json() == expected

def test_exact_limit(setup):
    assert upload(setup[0],b'x'*32).status_code == 202

def test_unknown(setup):
    assert setup[0].get('/jobs/unknown',headers=HEADERS).status_code == 404

def test_missing_blob(tmp_path):
    repo=Repository(tmp_path/'db.sqlite3')
    key='a'*32+'.txt'
    repo.create('lost',key,'note.txt',3)
    run_job('lost',repo,LocalStorage(tmp_path/'blobs'))
    row=repo.get('lost')
    assert row['state']=='failed' and row['error_code']=='storage_missing'
    assert row['attempts']==1

def test_safe_storage(tmp_path):
    storage=LocalStorage(tmp_path/'blobs')
    for key in ('../escape.txt','/tmp/escape.txt',r'..\escape.txt','user.txt'):
        for action in (lambda:storage.put(key,b'x'),lambda:storage.read(key),lambda:storage.delete(key)):
            with pytest.raises(ValueError): action()
    key='a'*32+'.txt'
    storage.put(key,b'first')
    with pytest.raises(FileExistsError): storage.put(key,b'second')
    assert storage.read(key)==b'first'
    storage.delete(key)
    storage.delete(key)

def test_cors(setup):
    client,_=setup
    def preflight(origin):
        return client.options('/documents',headers={'Origin':origin,'Access-Control-Request-Method':'POST','Access-Control-Request-Headers':'X-API-Key'})
    assert preflight('http://localhost:3000').headers['access-control-allow-origin']=='http://localhost:3000'
    assert 'access-control-allow-origin' not in preflight('https://untrusted.invalid').headers

def test_no_secret_logs(setup,caplog):
    client,_=setup
    with caplog.at_level('INFO',logger='ingestion'):
        response=upload(client,b'private document words')
    assert response.status_code==202
    records=[r for r in caplog.records if r.name.startswith('ingestion')]
    assert records, 'Emit safe state events through logging.getLogger(__name__)'
    assert 'test-only' not in caplog.text
    assert 'private document words' not in caplog.text

def test_compensation(tmp_path):
    from ingestion.service import accept
    class BrokenRepo:
        def create(self,*args,**kwargs): raise RuntimeError('simulated metadata failure')
    storage=LocalStorage(tmp_path/'blobs')
    with pytest.raises(RuntimeError, match="simulated metadata failure"): accept(b'abc','a.txt',BrokenRepo(),storage)
    assert not list((tmp_path/'blobs').glob('*'))
