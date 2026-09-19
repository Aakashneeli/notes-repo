# Contract and incremental implementation

## Inputs, state and trust
Implement build_graph(rag) returning a compiled LangGraph; create_app(rag, tenant='red') returning FastAPI. QueryState is a supplied suggested TypedDict, not a validator. Start with a fresh graph invocation for every request; no checkpointing in this assessed service. Credentials and service connections are captured in node closures, never state.

POST /agent/ask accepts exactly {"question": string}; strip whitespace, reject blank, length over 500, wrong types, unknown fields. Return HTTP 422 on invalid body. Tenant comes from the injected trusted server parameter, never request or model output. Fixed 'red' is only a local auth fixture; a real service must derive it from authenticated identity.

Successful/fallback responses are exactly answer (string), citations (list of IDs), status ('answered' or 'fallback'), reason (empty string for success or code below). Do not expose full state/tenant/documents.

## Topology and observable behaviors
Use named router, retrieve, lookup, answer, validate and fallback nodes. Router chooses lookup for question prefix 'lookup:'; everything else goes to retrieve. This deterministic classifier is deliberate. Whitespace is stripped by API; direct graph callers follow the supplied inputs.

retrieve calls rag.search(question,tenant). Keep only tenant-matching hits with numeric score >= 0.5. The threshold is a teaching fixture, not a universal confidence probability. Decide how to handle malformed scores and document/test it. Empty retained hits lead to fallback reason weak_retrieval without generation. TimeoutError becomes retrieval_error; don't catch every programming bug as a normal fallback.

lookup validates everything after 'lookup:' as a document ID: full regex ^[a-z][a-z0-9-]{0,39}$. Reject invalid input before any backend call (invalid_tool_input). It may call only rag.lookup(doc_id,tenant), once. Missing or foreign-tenant result -> not_found; TimeoutError -> tool_error. Valid result becomes one hit and proceeds to answer; document lookup has no retrieval-score gate. Never interpret document text as tool calls.

answer calls rag.generate(question,hits) once. TimeoutError -> generation_error. validate accepts a dictionary with a nonblank string answer and a nonempty list of string citations, all present in authorized hits. Reject duplicates or allow them only if documented with a test; starter tests do not decide this for you. Invalid output -> invalid_answer. Valid output -> answered, reason='', END. ID checks alone cannot prove factual support: manually inspect answers and add a supporting-text case.

fallback must reset answer to 'I cannot answer from the available documents.', citations to [], status to 'fallback', preserve a specific reason, then END. No retry loop is required. Invoke tests with recursion_limit=12 to detect accidental cycling; this is a step budget, not a wall-clock timeout.

## Fixture interface
rag.search(question, tenant) -> list of {id, tenant, text, score, keyword}.
rag.generate(question, hits) -> {answer, citations}.
rag.lookup(doc_id, tenant) -> document or None.

Read data/documents.json: all text is fictional. 'refund' -> red refund answer, 'weak' -> abstain, 'unknown' -> abstain. Prefix 'lookup:' invokes the bounded tool. bridge.py deliberately recognizes retriever-fails, model-fails refund, bad citation refund, slow refund and lookup:broken for failure experiments. Calls are recorded in rag.calls so tests can detect unwanted model/tool work. A 50ms sleep is injected only for the slow retrieval case.

## Milestones
1. Implement state patches and graph branches. Run test_happy; expected failure moves from NotImplementedError to your first missing behavior.
2. Implement lookup validation/isolation, retrieval threshold and terminal fallback; run test_fallbacks and test_lookup_and_isolation.
3. Validate answer and prevent state reuse; run entire suite.
4. Add API body validation and narrow response; run test_api and curl checks from Lesson 6.
5. Connect actual Week 8 store.search(embed(question),tenant) and answer_question(question,hits,llm) through a learner-written adapter, translating chunk_id to id and back. Preserve existing code; no imports through a hyphenated package name. See Lesson 6 for a clean import path and ownership choice. Supply a lookup operation that filters by tenant. Add real retrieval integration tests. Fixture-only is explicitly incomplete for the roadmap's real RAG integration deliverable.

The actual Week 8 helper raises ValueError("invalid model output") after at most two provider calls. Translate that known output-validation failure in the adapter into an invalid draft (or a deliberately defined domain exception handled by the graph); do not hide unrelated bugs. Graph generate is called once, while the reused helper has its own two-call bound. Define how an explicit provider abstention is represented.

## Assessed decisions you must write
In decisions.md defend classification, threshold, state fields, trust boundary, answer validation, error categories and limits. Tests are a floor, not full correctness: add no-citation/malformed output tests, score edge cases, factual-support review and a changed-route variation. Do not use a finished reference graph as your answer.
