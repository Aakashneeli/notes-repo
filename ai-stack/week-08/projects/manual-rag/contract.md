# Manual RAG contract
Start at the weekly root. Implement projects/manual-rag/rag.py. Keep bridge.py and tests unchanged.
This is a synchronous small-corpus lab; it is not a production upload/auth/queue implementation.

## chunk_document(document, size=40, overlap=8)
Document has doc_id, tenant, title, text, version (see bridge.Document).
Require actual integer size > 0 and 0 <= overlap < size (bool is not accepted).
Split by whitespace. Empty/whitespace-only text returns []. Do not emit a duplicate final tail.
Each chunk has chunk_id, doc_id, tenant, title, version, start, end, text.
Offsets are zero-based word indices, end exclusive, in normalized split text (not byte offsets).
Use chunk_id = tenant + ":" + doc_id + ":v" + str(version) + ":" + str(start).
IDs are stable within a document version/chunk policy; changed text must bump version.
The lab only searches one ingested version at a time. Reject or explicitly replace old versions
before live evaluation; do not mix stale policies. Record chosen version-handling in decisions.md.

## Store(path, dimension)
Use QdrantClient(path=path); collection chunks, cosine, declared dimension.
If collection exists, reject dimension mismatch. An exception must not leave a client lock held.
Map string chunk IDs to valid Qdrant UUIDs using uuid5(NAMESPACE_URL, chunk_id).
Keep original chunk_id in payload. put(chunks,vectors) validates equal counts, every vector's
dimension, finite numeric values and nonzero norm, then upserts. Empty batch is a no-op.
The same IDs update existing points. Deduplication is per tenant/document/version/start;
identical text in two tenants must not collapse ownership.
search(vector,tenant,limit=3): validate query similarly and positive integer limit.
Return payload plus score; only matching tenant, ordered by descending similarity. Empty store
returns []. Never query globally then discard other tenants after top-k.
close() releases storage; caller owns lifecycle. This is single-process embedded mode.

## answer_question(question,hits,llm)
llm is an injected callable receiving list[dict] messages and returning a JSON string.
Output exactly {"answer": str, "citations": list[str]}; no extra keys/coercions.
Empty hits => {"answer":"Insufficient evidence.","citations":[]} without invoking llm.
Build system instruction and user question/context separately. Source text is untrusted data.
Use all supplied hits in this unit; API limits retrieval to 3. Mark each with its chunk_id.
Accept only unique citations drawn from supplied hits. A substantive answer needs citations;
the exact abstention above must have none. Reject malformed JSON, wrong types, extra keys,
unknown or repeated IDs, and empty answer. On validation error request one repair (two calls
total). Do not retry arbitrary programming/transport errors here. After two invalid outputs
raise ValueError("invalid model output"). Returned structure is not proof of factual support.

## create_app(store,embed,llm,tenant="red")
tenant is trusted server-side fixture identity, never accepted from client.
Pydantic bodies forbid extra fields. Reject empty/whitespace strings and invalid types (422).
POST /ingest: {doc_id,title,text,version}; version positive integer, text at most 10,000 chars.
Attach trusted tenant; chunk, embed each chunk's text, store. Return 200 {"chunks": count}.
POST /search: {"question":str}; embed once, return 200 {"hits": [...]}, up to 3 scoped chunks.
POST /ask: {"question":str}; retrieve as search then answer_question. Return answer/citations.
ValueError for invalid model output maps to 502 with generic detail; TimeoutError from the
provider maps to 504 with generic detail. Do not expose exception strings or source text.
Health/auth/rate limiting are earlier/later context; bind this fixture only to 127.0.0.1.
Do not treat a caller-supplied tenant header as authentication.

## Integration handoff
With a completed earlier ingestion service, call chunk/embed/store only after extraction succeeds,
using its trusted owner and document version. Mark ingestion complete only after writes succeed;
retry with stable IDs. Preserve existing files. Record partial-write recovery (re-upsert), and
old-version cleanup choice. The supplied bridge instead begins at already-extracted documents.
A live embedding adapter must use the same model/revision/dimension for query and stored text.
A live generation adapter must return content string, not the entire HTTP envelope.
