"""Supplied composition root. No global app: Uvicorn --factory creates one."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import Settings
from .repository import Repository
from .storage import LocalStorage
from .routes import build_router

def create_app(settings=None):
    settings = settings or Settings.from_env()
    repo = Repository(settings.root / "metadata.sqlite3")
    storage = LocalStorage(settings.root / "blobs")
    app = FastAPI(title="Week 6 local ingestion lab")
    app.add_middleware(CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_methods=["GET", "POST"], allow_headers=["X-API-Key", "Content-Type"])
    app.include_router(build_router(settings, repo, storage))
    return app
