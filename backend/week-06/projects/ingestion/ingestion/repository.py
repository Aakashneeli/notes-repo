"""Completed minimal SQLite prerequisite fixture, NOT earlier-week mastery.
One connection per operation; values bound as parameters; short transactions.
Does not implement orchestration, leases, retry policy, or production migrations.
"""
from contextlib import closing
import sqlite3
class Repository:
    def __init__(self, path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with closing(self.connect()) as db, db:
            db.execute("""CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY, storage_key TEXT NOT NULL UNIQUE,
                original_name TEXT NOT NULL, size INTEGER NOT NULL CHECK(size > 0),
                state TEXT NOT NULL CHECK(state IN
                    ('pending','running','completed','failed','retrying')),
                attempts INTEGER NOT NULL DEFAULT 0, characters INTEGER,
                words INTEGER, error_code TEXT)""")
    def connect(self):
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        return db
    def create(self, job_id, storage_key, original_name, size):
        with closing(self.connect()) as db, db:
            db.execute("INSERT INTO jobs(id,storage_key,original_name,size,state) VALUES (?,?,?,?,?)",
                       (job_id, storage_key, original_name, size, "pending"))
        return self.get(job_id)
    def get(self, job_id):
        with closing(self.connect()) as db:
            row = db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        return dict(row) if row is not None else None
    def transition(self, job_id, expected, target, *, characters=None, words=None, error_code=None):
        # Compare-and-set: only one caller can change a row from expected to target.
        # Learner's service/worker must enforce the allowed transition graph.
        with closing(self.connect()) as db, db:
            cur = db.execute("""UPDATE jobs SET state=?, characters=?, words=?, error_code=?,
                attempts=attempts + ? WHERE id=? AND state=?""",
                (target, characters, words, error_code, int(target == 'running'), job_id, expected))
            return cur.rowcount == 1
