"""Completed disposable label demo; schema is intentionally unrelated to tasks."""
import os
from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url

url = make_url(os.environ["DEMO_DATABASE_URL"])
if url.host != "127.0.0.1" or url.port != 55435 or url.database != "w5_demo":
    raise ValueError("Demo requires isolated local w5_demo")
engine = create_engine(url)
with engine.connect() as connection:
    context.configure(connection=connection)
    with context.begin_transaction():
        context.run_migrations()
engine.dispose()
