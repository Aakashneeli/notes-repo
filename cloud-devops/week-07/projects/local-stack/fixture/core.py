"""Supplied tiny ingestion backend. SQL transactions do not include the Redis enqueue.
This bridge stores small text IN Postgres, not a complete Week 6 upload implementation.
"""
import os
from uuid import uuid4
import psycopg
from redis import Redis
from rq import Queue


def connection():
    return psycopg.connect(os.environ["DATABASE_URL"], connect_timeout=2)


def queue_connection():
    return Redis.from_url(os.environ["REDIS_URL"], socket_connect_timeout=2, socket_timeout=2)


def initialize():
    # Lab-only schema bootstrap: not a replacement for Week 5 Alembic migrations.
    with connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS week7_jobs (
            id text PRIMARY KEY, body text NOT NULL, state text NOT NULL,
            characters integer, request_id text NOT NULL)""")


def submit(text, request_id):
    job_id = uuid4().hex
    with connection() as conn:
        conn.execute("INSERT INTO week7_jobs(id,body,state,request_id) VALUES (%s,%s,%s,%s)",
                     (job_id, text, "pending", request_id))
    try:
        Queue("ingestion", connection=queue_connection()).enqueue(
            "fixture.core.extract", job_id, job_id=job_id, job_timeout=30)
    except Exception:
        # Bounded fixture compensation; an ambiguous network failure may still enqueue.
        with connection() as conn:
            conn.execute("UPDATE week7_jobs SET state='failed' WHERE id=%s", (job_id,))
        raise
    return job_id


def extract(job_id):
    # One transaction locks the row until completion. A worker crash rolls it back.
    with connection() as conn:
        row = conn.execute("SELECT body,state FROM week7_jobs WHERE id=%s FOR UPDATE",
                           (job_id,)).fetchone()
        if row is None or row[1] != "pending":
            return
        conn.execute("UPDATE week7_jobs SET state='completed',characters=%s WHERE id=%s",
                     (len(row[0]), job_id))


def status(job_id):
    with connection() as conn:
        row = conn.execute("SELECT state,characters FROM week7_jobs WHERE id=%s",
                           (job_id,)).fetchone()
    return None if row is None else {"job_id": job_id, "state": row[0], "characters": row[1]}
