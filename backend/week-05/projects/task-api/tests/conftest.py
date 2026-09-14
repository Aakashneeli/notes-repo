"""Supplied real-Postgres isolation. Creates/drops only a new random schema."""
import os
from pathlib import Path
import uuid
import pytest
from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url

@pytest.fixture
def engine(monkeypatch):
    raw = os.environ.get("TEST_DATABASE_URL")
    if not raw:
        pytest.fail("Set TEST_DATABASE_URL to the local w5_test database; not a mock test")
    url = make_url(raw)
    if (url.get_backend_name() != "postgresql" or url.host != "127.0.0.1"
            or url.port != 55435 or url.database != "w5_test"):
        pytest.fail("Refusing database outside 127.0.0.1:55435/w5_test")
    if url.query:
        pytest.fail("Test base URL must not supply connection options")
    schema = "w5_" + uuid.uuid4().hex
    admin = create_engine(url)
    isolated = None
    try:
        with admin.begin() as conn:
            conn.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
        test_url = url.update_query_dict({"options": f"-csearch_path={schema}"})
        monkeypatch.setenv("DATABASE_URL", test_url.render_as_string(hide_password=False))
        config = Config(str(Path(__file__).resolve().parents[1] / "alembic.ini"))
        if not ScriptDirectory.from_config(config).get_heads():
            pytest.fail("EXPECTED STARTER: write your first migration in lesson 9")
        command.upgrade(config, "head")
        isolated = create_engine(test_url)
        yield isolated
    finally:
        if isolated is not None:
            isolated.dispose()
        with admin.begin() as conn:
            conn.exec_driver_sql(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE')
        admin.dispose()
