"""Minimal prerequisite fixture: validated extracted text, no upload/queue/backend claims."""
import json
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field


class Document(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    doc_id: str = Field(min_length=1)
    tenant: str = Field(min_length=1)
    title: str = Field(min_length=1)
    text: str = Field(min_length=1)
    version: int = Field(ge=1)


def load_documents():
    path = Path(__file__).parent / "data" / "documents.json"
    return [Document.model_validate(row).model_dump() for row in json.loads(path.read_text())]
