import pytest
from pydantic import BaseModel, ValidationError

from text_workbench.models import Config, Record
from text_workbench.settings import load_settings


def test_models_are_validation_boundaries():
    assert issubclass(Config, BaseModel)
    assert issubclass(Record, BaseModel)
    assert Config().max_chars == 1_000_000
    assert Config().log_level == "INFO"
    assert Record(characters=0, words=0).model_dump() == {"characters": 0, "words": 0}


@pytest.mark.parametrize(
    "data",
    [
        {"max_chars": 0},
        {"max_chars": -1},
        {"max_chars": "12"},
        {"max_chars": True},
        {"log_level": "LOUD"},
        {"typo": 1},
    ],
)
def test_invalid_config(data):
    with pytest.raises(ValidationError):
        Config(**data)


@pytest.mark.parametrize(
    "data",
    [
        {"characters": -1, "words": 2},
        {"characters": 1, "words": "2"},
        {"characters": 1},
        {"characters": 1, "words": 2, "text": "private"},
    ],
)
def test_invalid_record(data):
    with pytest.raises(ValidationError):
        Record(**data)


def test_settings():
    assert load_settings({}).max_chars == 1_000_000
    cfg = load_settings({"TEXT_MAX_CHARS": "12", "TEXT_LOG_LEVEL": "DEBUG", "OTHER": "x"})
    assert (cfg.max_chars, cfg.log_level) == (12, "DEBUG")


@pytest.mark.parametrize(
    "env",
    [
        {"TEXT_MAX_CHARS": "bad"},
        {"TEXT_MAX_CHARS": ""},
        {"TEXT_MAX_CHARS": "0"},
        {"TEXT_LOG_LEVEL": "info"},
    ],
)
def test_bad_settings(env):
    with pytest.raises((ValueError, ValidationError)):
        load_settings(env)
