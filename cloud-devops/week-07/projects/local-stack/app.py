"""Supplied composition root: learner implements operations and observability hooks."""
from fastapi import FastAPI
from fixture.api import router
from fixture.probes import dependency_checks
from operations import install_health
from observability import install_logging


def create_app():
    app = FastAPI(title="Week 7 local ingestion fixture")
    app.include_router(router())
    install_health(app, dependency_checks)
    install_logging(app)
    return app
