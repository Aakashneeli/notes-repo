"""Local mock wiring. Implement rag.py first. Run from weekly root."""
from pathlib import Path
import json
import uvicorn
from rag import Store, create_app


def fixture_embed(text):
    # Synthetic keyword axes: mechanical test only, no semantic understanding.
    lowered = text.lower()
    return [1.0 + lowered.count("return"), 1.0 + lowered.count("ship"),
            1.0 + lowered.count("support")]


def fixture_llm(messages):
    # Deliberate abstention, never pretends to answer from evidence.
    return json.dumps({"answer": "Insufficient evidence.", "citations": []})


if __name__ == "__main__":
    Path("runtime").mkdir(exist_ok=True)
    store = Store("runtime/project-db", 3)
    try:
        uvicorn.run(create_app(store, fixture_embed, fixture_llm), host="127.0.0.1", port=8008)
    finally:
        store.close()
