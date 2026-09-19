"""Learner implementation. Read contract.md. Do not replace bridge.py with the solution."""
from typing import TypedDict

class QueryState(TypedDict, total=False):
    question: str
    tenant: str
    route: str
    hits: list[dict]
    answer: str
    citations: list[str]
    status: str
    reason: str


def build_graph(rag):
    """Return compiled LangGraph with router/retrieve/lookup/answer/validate/fallback nodes.
    rag supplies search(question,tenant), generate(question,hits), lookup(doc_id,tenant).
    See contract for decisions and required observable behavior.
    """
    raise NotImplementedError('Lessons 3–5: learner graph')


def create_app(rag, tenant='red'):
    """Return FastAPI app with POST /agent/ask. Trusted tenant is server-injected, never body-controlled."""
    raise NotImplementedError('Lesson 6: integrate graph into RAG service')
