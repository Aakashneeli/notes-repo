"""Supplied configuration bridge; no implicit .env loading."""
from dataclasses import dataclass, field
from pathlib import Path
import os
@dataclass(frozen=True)
class Settings:
    api_key: str = field(repr=False)
    root: Path
    max_bytes: int = 1024
    def __post_init__(self):
        if not self.api_key or not self.api_key.strip():
            raise ValueError("INGEST_API_KEY must be set")
        if self.max_bytes < 1:
            raise ValueError("max_bytes must be positive")
    @classmethod
    def from_env(cls):
        return cls(os.environ.get("INGEST_API_KEY", ""),
                   Path(os.environ.get("INGEST_ROOT", "runtime/dev")))
