"""Learner-owned database access. Accept a request-scoped Session.
Never commit here: the HTTP unit of work commits task + event together.
Return plain dicts while session is open. Raise Missing or Conflict as appropriate.
"""
class Missing(Exception):
    pass

class Conflict(Exception):
    pass

class TaskRepository:
    def __init__(self, session):
        self.session = session

    def create(self, title, done):
        raise NotImplementedError("Insert task and created event; flush for ID")

    def page(self, done, offset, limit):
        raise NotImplementedError("Filter, count before page, order by id")

    def get(self, task_id):
        raise NotImplementedError("Fetch or raise Missing")

    def update(self, task_id, changes):
        raise NotImplementedError("Apply only supplied fields; append updated event")

    def delete(self, task_id):
        raise NotImplementedError("Delete or raise Missing; explain event deletion policy")
