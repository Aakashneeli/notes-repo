"""Learner-owned schemas: implement from README and lesson 5.

TaskCreate: title (trimmed, 1..80 chars), done (strict bool, default False).
TaskRead: id (positive int), title, done. No extra response keys.
TaskUpdate: optional-by-omission title/done; explicitly supplied null is invalid.
TaskPage: items (list[TaskRead]), total (filtered count), offset, limit.
Forbid extra request fields. Reject non-string titles, unknown fields, null,
whitespace-only/oversize titles and non-boolean done. Validate before mutation.
"""
# TODO: define the four Pydantic models. There are no assessed answers here.
