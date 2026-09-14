"""Completed PostgreSQL mechanism checks, independent of learner models."""
import os
from pathlib import Path
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def connection():
    raw = os.environ.get("TEST_DATABASE_URL")
    if not raw:
        pytest.fail("Set local TEST_DATABASE_URL; PostgreSQL checks are not skipped")
    u = make_url(raw)
    assert u.host == "127.0.0.1" and u.port == 55435 and u.database == "w5_test"
    e = create_engine(u)
    with e.connect() as c:
        # psycopg can execute this parameter-free multi-statement sample.
        c.exec_driver_sql(Path(__file__).with_name("seed.sql").read_text())
        c.commit()
        yield c
    e.dispose()

def test_seed_and_left_join(connection):
    c = connection
    rows = c.execute(text("SELECT a.name,count(b.id) FROM authors a LEFT JOIN articles b ON b.author_id=a.id GROUP BY a.id,a.name ORDER BY a.id")).all()
    assert rows == [("Asha",2),("Ben",1),("Chen",0)]
    wrong = c.execute(text("SELECT a.name,count(*) FROM authors a LEFT JOIN articles b ON b.author_id=a.id GROUP BY a.id,a.name ORDER BY a.id")).all()
    assert wrong[-1] == ("Chen",1)  # Meaningful mutation exposed.

def test_partial_write_rollback(connection):
    c = connection
    with pytest.raises(IntegrityError):
        with c.begin():
            c.exec_driver_sql("UPDATE articles SET views=11 WHERE id=1")
            c.exec_driver_sql("INSERT INTO articles VALUES (5,999,'bad',false,0)")
    assert c.scalar(text("SELECT views FROM articles WHERE id=1")) == 10
    c.rollback()
    with c.begin():
        c.exec_driver_sql("UPDATE articles SET views=views+1 WHERE id=1")
    assert c.scalar(text("SELECT views FROM articles WHERE id=1")) == 11

def test_parameter_is_data(connection):
    c = connection
    assert c.execute(text("SELECT id FROM articles WHERE title=:title"), {"title":"x' OR true --"}).all() == []

def test_index_plan(connection):
    c = connection
    c.execute(text("CREATE TEMP TABLE measurements AS SELECT g AS id, g % 1000 AS batch FROM generate_series(1,50000) g"))
    c.exec_driver_sql("ANALYZE measurements")
    before = c.exec_driver_sql("EXPLAIN (FORMAT JSON) SELECT * FROM measurements WHERE batch=42").scalar()
    c.exec_driver_sql("CREATE INDEX ON measurements(batch)")
    c.exec_driver_sql("ANALYZE measurements")
    after = c.exec_driver_sql("EXPLAIN (FORMAT JSON) SELECT * FROM measurements WHERE batch=42").scalar()
    assert before[0]["Plan"]["Node Type"] == "Seq Scan"
    assert "Index" in str(after[0]["Plan"])
    assert c.scalar(text("SELECT count(*) FROM measurements WHERE batch=42")) == 50

def test_two_connections_compete(connection):
    from concurrent.futures import ThreadPoolExecutor
    from threading import Barrier
    import uuid
    e = connection.engine
    schema = "w5_demo_" + uuid.uuid4().hex
    with e.begin() as c:
        c.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
        c.exec_driver_sql(f'CREATE TABLE "{schema}".counter (id integer PRIMARY KEY,n integer NOT NULL)')
        c.exec_driver_sql(f'INSERT INTO "{schema}".counter VALUES (1,0)')
        c.exec_driver_sql(f'CREATE TABLE "{schema}".names (name text UNIQUE NOT NULL)')
    try:
        gate = Barrier(2, timeout=5)
        def increment():
            with e.begin() as c:
                c.exec_driver_sql("SET LOCAL lock_timeout='5s'")
                gate.wait()
                c.exec_driver_sql(f'UPDATE "{schema}".counter SET n=n+1 WHERE id=1')
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(increment) for _ in range(2)]
            for future in futures:
                future.result(timeout=10)
        with e.connect() as c:
            assert c.exec_driver_sql(f'SELECT n FROM "{schema}".counter').scalar() == 2
        gate = Barrier(2, timeout=5)
        def compete():
            try:
                with e.begin() as c:
                    c.exec_driver_sql("SET LOCAL lock_timeout='5s'")
                    gate.wait()
                    c.execute(text(f'INSERT INTO "{schema}".names VALUES (:name)'), {"name":"same"})
                return "committed"
            except IntegrityError:
                return "conflict"
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(compete) for _ in range(2)]
            assert sorted(f.result(timeout=10) for f in futures) == ["committed","conflict"]
    finally:
        with e.begin() as c:
            c.exec_driver_sql(f'DROP SCHEMA "{schema}" CASCADE')
