"""Learner-owned ORM schema. See README and lessons 7, 9.
Define Task and TaskEvent on Base, with named constraints and relationships.
Do not call create_all here: migrations own the persistent schema.
"""
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# TODO: Task and TaskEvent; no assessed model implementation supplied.
