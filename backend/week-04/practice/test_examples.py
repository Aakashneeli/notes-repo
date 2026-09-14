import pytest
from bridge import Label, rename
from fastapi.testclient import TestClient
from hello_api import app
from pydantic import ValidationError


def test_bridge():
    assert Label(text="  tea  ").model_dump() == {"text": "tea"}
    with pytest.raises(ValidationError):
        Label(text=" ")
    assert rename({"hot": True}, {"hot": False}) == {"hot": False}


def test_greeting_lifecycle():
    with TestClient(app) as c:
        assert app.state.ready is True
        assert c.get("/greetings/2?loud=true").json() == {"message": "HELLO 2"}
        r = c.get("/greetings/nope")
        assert r.status_code == 422
        assert r.json()["error"]["code"] == "validation_error"
        assert c.get("/greetings/0").status_code == 422
        assert c.get("/greetings/2?loud=maybe").status_code == 422
        r = c.post(
            "/greetings", json={"name": " Ada "}, headers={"X-Badge": "practice"}
        )
        assert r.status_code == 201 and r.json() == {"message": "Hello Ada"}
        assert c.post("/greetings", json={"name": "Ada"}).status_code == 401
        assert (
            c.post(
                "/greetings", json={"name": " "}, headers={"X-Badge": "practice"}
            ).status_code
            == 422
        )
        assert c.get("/openapi.json").json()["paths"]["/greetings"]["post"]
    assert app.state.ready is False
