"""Supplied connection infrastructure. No schema creation or data reset."""
import os
from sqlalchemy import create_engine

def make_engine(url=None):
    return create_engine(url or os.environ["DATABASE_URL"], pool_pre_ping=True)
