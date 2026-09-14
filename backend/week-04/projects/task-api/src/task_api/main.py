"""Supplied composition shell; learner completes wiring in lessons 8–10."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Return a fresh app with independent memory for each call.

    TODO: create TaskService and attach it to app.state.service; include router;
    register consistent error handlers; wire the authentication dependency.
    Keep /health public. No global task dictionary shared across apps.
    """
    app = FastAPI(title="Week 4 Task API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
