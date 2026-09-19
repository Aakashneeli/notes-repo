"""Completed teaching fragments, never a complete RAG service. Run from weekly root."""
import json
import math
import sys
from tempfile import TemporaryDirectory

from pydantic import BaseModel, ConfigDict, ValidationError
from qdrant_client import QdrantClient, models


class Answer(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    answer: str
    citations: list[str]


def parse_answer(raw, allowed):
    result = Answer.model_validate_json(raw)
    if not set(result.citations) <= set(allowed):
        raise ValueError("citation outside supplied context")
    return result


def cosine(a, b):
    if len(a) != len(b) or not a:
        raise ValueError("dimensions differ or empty")
    denominator = math.sqrt(sum(x*x for x in a) * sum(x*x for x in b))
    if denominator == 0:
        raise ValueError("zero vector")
    return sum(x*y for x, y in zip(a, b)) / denominator


def windows(text, size=4, overlap=1):
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("require size > overlap >= 0")
    words = text.split()
    out = []
    start = 0
    while start < len(words):
        stop = min(start + size, len(words))
        out.append({"start": start, "end": stop, "text": " ".join(words[start:stop])})
        if stop == len(words):
            break
        start = stop - overlap
    return out


def client_demo():
    # Generated database lives only in a temporary directory; no learner data touched.
    with TemporaryDirectory(prefix="week08-example-") as path:
        client = QdrantClient(path=path)
        client.create_collection("demo", vectors_config=models.VectorParams(
            size=3, distance=models.Distance.COSINE))
        client.upsert("demo", points=[
            models.PointStruct(id=1, vector=[1., 0., 0.],
                payload={"tenant": "red", "chunk_id": "red:1", "text": "Return in 30 days."}),
            models.PointStruct(id=2, vector=[1., 0., 0.],
                payload={"tenant": "blue", "chunk_id": "blue:1", "text": "Return in 90 days."}),
        ])
        client.close()
        client = QdrantClient(path=path)
        hits = client.query_points("demo", query=[1., 0., 0.],
            query_filter=models.Filter(must=[models.FieldCondition(
                key="tenant", match=models.MatchValue(value="red"))]),
            limit=2, with_payload=True).points
        result = [h.payload["chunk_id"] for h in hits]
        client.close()
        return result


def hit_rate(rows):
    # Only answerable rows belong in this denominator.
    eligible = [r for r in rows if r["expected"]]
    if not eligible:
        return None
    return sum(bool(set(r["expected"]) & set(r["retrieved"])) for r in eligible) / len(eligible)


def run(name):
    if name == "messages":
        messages = [{"role": "system", "content": "Answer using supplied evidence."},
                    {"role": "user", "content": "When can I return a book?"}]
        print(json.dumps(messages, indent=2))
    elif name == "validation":
        for raw in ['{"answer":"30 days","citations":["c1"]}',
                    '{"answer":"30 days","citations":"c1"}',
                    '{"answer":"90 days","citations":["secret"]}']:
            try:
                print(parse_answer(raw, ["c1"]).model_dump())
            except (ValidationError, ValueError):
                print("rejected")
    elif name == "chunking":
        print(windows("one two three four five six seven"))
    elif name == "vectors":
        print(round(cosine([1, 0], [1, 1]), 3))
        print(round(cosine([1, 0], [0, 1]), 3))
    elif name == "store":
        print(client_demo())
    elif name == "evaluation":
        print(hit_rate([{"expected": ["a"], "retrieved": ["a"]},
                        {"expected": ["b"], "retrieved": ["a"]},
                        {"expected": [], "retrieved": []}]))
    else:
        raise ValueError("choose messages, validation, chunking, vectors, store, evaluation")


if __name__ == "__main__":
    run(sys.argv[1])
