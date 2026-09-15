"""Completed small examples, intentionally separate from project implementations."""
import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse


def choose_status(checks):
    """Empty checks must not accidentally claim readiness."""
    return 200 if checks and all(checks.values()) else 503


def event_line(method, status):
    return json.dumps({"event": "example", "method": method, "status": status})


def demo_app():
    app = FastAPI()

    @app.middleware("http")
    async def marker(request, call_next):
        response = await call_next(request)
        response.headers["X-Lesson"] = "traced"
        return response

    @app.get("/alive")
    def alive():
        return {"alive": True}

    @app.get("/accepting")
    def accepting():
        return JSONResponse({"accepting": False}, status_code=503)

    return app


if __name__ == "__main__":
    print(choose_status({"db": True, "queue": False}))
    print(event_line("GET", 503))
