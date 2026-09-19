# Week 8 resources

## Knowledge

Verified against official pages on 2026-09-17; live provider/model availability must be rechecked before use.

- [groq](https://console.groq.com/docs/openai) — Provider compatibility and base URL; check before choosing a client endpoint.
- [structured](https://console.groq.com/docs/structured-outputs) — Schema-mode capabilities and model support; distinguish shape guarantees from truth.
- [chat](https://console.groq.com/docs/text-chat) — Messages and chat response structure; use for the raw request trace.
- [router](https://openrouter.ai/docs/api/reference/overview) — Alternative provider HTTP contract; do not assume identical model features.
- [stream](https://openrouter.ai/docs/api/reference/streaming) — Streaming transport and deltas; awareness, not a required streaming server implementation.
- [qdrant](https://github.com/qdrant/qdrant-client) — Python local mode and query_points usage; inspect for persistence and client lifetime.
- [filter](https://qdrant.tech/documentation/concepts/filtering/) — Payload filtering clauses; use for the trusted-tenant query.
- [chroma](https://docs.trychroma.com/docs/overview/getting-started) — Collection setup and operations; conceptual store comparison.
- [pg](https://github.com/pgvector/pgvector) — Postgres vector extension, distances and indexes; conceptual alternative to separate storage.
- [pinecone](https://docs.pinecone.io/guides/index-data/data-modeling) — Managed record/metadata model; evaluate operational and ownership boundaries.
- [model](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — Example embedding encoder dimensions, limits and use; read before any download.
- [cards](https://huggingface.co/docs/hub/model-cards) — Model provenance, license and limitations; informs the learner's model decision.
- [similarity](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) — Sentence embeddings and cosine similarity; intuition, not calibrated confidence.
- [pydantic](https://docs.pydantic.dev/latest/concepts/models/) — Model validation and serialization; local structured-output gate.
- [fastapi](https://fastapi.tiangolo.com/tutorial/testing/) — TestClient and isolated HTTP checks; use for route contracts.
- [fastembed](https://qdrant.github.io/fastembed/Getting%20Started/) — TextEmbedding generator and model downloads; optional real-encoder probe.
- [recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) — Evidence-coverage metrics; distinguish source coverage from the lab's hit@k.
- [faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) — Supported-claim evaluation; separate valid citation IDs from factual support.

## Wisdom (Communities)

- [Qdrant project discussions](https://github.com/qdrant/qdrant-client/discussions) — Optional place to compare a minimal, redacted retrieval reproduction with practitioners; check project contribution guidance before posting.
- [Groq developer community](https://community.groq.com/) — Optional provider-specific clarification. Joining or sending messages is a learner action; none was done.

## Limits
Local deterministic checks cannot establish semantic quality, live-provider compatibility or deployment readiness. No additional framework is required for evaluation.
