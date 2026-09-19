"""Completed teaching example: approval of a fictional support ticket, not the RAG project."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel, ConfigDict, Field
from langsmith import traceable

class Ticket(TypedDict, total=False):
    text: str
    urgent: bool
    queue: str


def classify(state):
    return {"urgent": "outage" in state["text"].lower()}


def choose(state):
    return "fast" if state["urgent"] else "normal"


def ticket_graph(memory=False):
    builder = StateGraph(Ticket)
    builder.add_node("classify", classify)
    builder.add_node("fast", lambda state: {"queue": "on-call"})
    builder.add_node("normal", lambda state: {"queue": "helpdesk"})
    builder.add_edge(START, "classify")
    builder.add_conditional_edges("classify", choose, {"fast": "fast", "normal": "normal"})
    builder.add_edge("fast", END)
    builder.add_edge("normal", END)
    return builder.compile(checkpointer=InMemorySaver() if memory else None)


class TicketArgs(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    ticket_id: str = Field(pattern=r"^T-[0-9]{2}$")


@traceable(run_type="tool", name="ticket_lookup")
def lookup_ticket(raw, trusted_team="blue"):
    args = TicketArgs.model_validate(raw)
    rows = {"T-01": {"team": "blue", "status": "open"}}
    row = rows.get(args.ticket_id)
    if row is None or row["team"] != trusted_team:
        return {"status": "not_found"}
    return {"status": row["status"]}


def main():
    print(ticket_graph().invoke({"text": "Database outage"}))
    print(lookup_ticket({"ticket_id": "T-01"}))

if __name__ == "__main__":
    main()
