"""Learner-owned Python behavior. Do not import FastAPI here.

Choose method signatures and internal storage. Suggested operations:
create, list, get, update, delete. Each instance starts empty, IDs increase
from 1 without reuse. Raise domain errors for missing IDs and duplicate titles.
Titles are unique after trimming, case-sensitive. Exclude self on update.
Filter done before pagination, sort by ascending id, retain filtered total.
Use a lock around compound mutations if routes can run concurrently, or document
and enforce a serial local-only design. Multi-process persistence is out of scope.
"""


class TaskService:
    def __init__(self) -> None:
        raise NotImplementedError("Design the in-memory service in lesson 6")
