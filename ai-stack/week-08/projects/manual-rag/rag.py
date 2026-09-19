"""Learner implementation. Read contract.md and lessons; no completed pipeline supplied."""


def chunk_document(document, size=40, overlap=8):
    """Return chunks per contract; stable IDs, provenance, no duplicate tail."""
    raise NotImplementedError("Lab 1: fixed word windows, metadata, validation")


class Store:
    def __init__(self, path, dimension):
        """Open/create persistent local Qdrant collection 'chunks'; validate dimension."""
        raise NotImplementedError("Lab 2: use supplied vectors; no implicit embedding downloads")

    def put(self, chunks, vectors):
        """Upsert idempotently; validate lengths/dimensions before any writes."""
        raise NotImplementedError("Lab 2")

    def search(self, vector, tenant, limit=3):
        """Return payload dictionaries plus score, filtered before top-k."""
        raise NotImplementedError("Lab 2: tenant must be included in query_filter")

    def close(self):
        raise NotImplementedError("Release client before reopening same local path")


def answer_question(question, hits, llm):
    """Call llm(messages), validate JSON and citations, at most two attempts; see contract."""
    raise NotImplementedError("Lab 3: empty hits abstain without calling model")


def create_app(store, embed, llm, tenant="red"):
    """Return FastAPI app implementing contract; injected functions make tests offline."""
    raise NotImplementedError("Lab 3: POST /ingest, /search, /ask")
