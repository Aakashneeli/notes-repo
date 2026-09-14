"""Learner-owned domain exceptions and HTTP handler registration.

Define domain errors here or in a pure domain module; service must not know HTTP.
All HTTP errors: {"error": {"code": str, "message": str}}.
Handle Starlette HTTPException (including unmatched routes), FastAPI request
validation errors and unexpected Exception. Retain exception headers for 401/405.
Do not expose request inputs, validation internals, tracebacks or keys to clients.
Internal errors return generic 500; server-side logging may retain a traceback.
"""
# TODO: implement error types and handler installer in lesson 8.
