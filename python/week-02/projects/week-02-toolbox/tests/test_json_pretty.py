import json
import pytest
from week2_toolbox.json_pretty import pretty_json


def test_indents_and_sorts_object():
    assert pretty_json('{"z": 1, "a": 2}') == '{\n  "a": 2,\n  "z": 1\n}'


@pytest.mark.parametrize("text", ['[]', '{}', '[1, true, null]', '42', '"hello"'])
def test_preserves_json_meaning(text):
    assert json.loads(pretty_json(text)) == json.loads(text)


def test_nested_object_and_unicode():
    text = '{"z": {"b": "नमस्ते", "a": [1, 2]}}'
    assert json.loads(pretty_json(text)) == json.loads(text)


@pytest.mark.parametrize("text", ['', '{"x":}', '{"x": 1,}', "{'x': 1}"])
def test_invalid_json(text):
    with pytest.raises(json.JSONDecodeError):
        pretty_json(text)
