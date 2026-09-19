# Source coverage — Week 08
Source /home/an10/Downloads/ai-backend-roadmap.html, numbered article #week-8.
Exact title: Raw LLM APIs, Embeddings, Vector DBs, Manual RAG, and Retrieval Evaluation
Path: ai-stack/week-08/. No mismatch/naming exception found.
Main deliverables: manual RAG API; store comparison; data-flow diagram; retrieval evaluation;
chunking, filter and mocked-response tests.
Scope authority is the numbered week, not the roadmap's compressed sequence strip.
Week 7 supplies operational context; Week 9 explains why manual retrieval comes first.
No detailed lessons for those weeks were authored.

| In-scope requirement | Lessons | Practice/project | Demonstrated-ability evidence |
|---|---|---|---|
| Raw APIs: Groq/OpenRouter-compatible clients, messages, roles, streaming awareness | 3 | practice/provider_probe.py; text_from_deltas | Envelope trace, assembled deltas, disclosed live-probe status |
| Structured output: JSON schema/Pydantic, invalid-output retry | 4, 9 | parse_answer; answer_question tests | Reject wrong type/ID, two-attempt bound, explained support limit |
| Embeddings: vectors, cosine, dimensions, model choice | 6, 8 | cosine; semantic_probe; Store | Predicted scores, real-encoder run and model decision |
| Chunking: fixed-size, semantic-ish, overlap, metadata, deduplication | 5, 7 | chunk_document; boundary comparison | Edge tests, sentence/window comparison, stable IDs/version decision |
| Vector DBs: pgvector, Chroma, Qdrant, managed tradeoffs | 7, 12 | Store; store-comparison.md | Local persistence/filter checks; four comparison axes |
| RAG flow: retrieve, rerank awareness, prompt, cited answer | 2, 9, 10 | answer_question; create_app; data-flow.md | Concrete request trace, hand-rerank, selected IDs and citations |
| Evaluation: golden questions, expected sources, retrieval misses, hallucinations | 11 | golden-seeds → learner golden.json; evaluation-report | 15–25 curated cases, labels, unsupported claims, controlled change |
| Lab 1: extend ingestion to chunks and metadata | 2, 5 | bridge or completed existing seam; chunk_document | Bridge decision, metadata/chunk tests; no claim earlier work complete |
| Lab 2: generate embeddings and store in local DB | 6–8 | Store + semantic embedding adapter | Real-encoder vectors persisted/retrieved, config recorded |
| Lab 3: /ask with context and citations | 9–10 | answer_question; create_app | Mock contracts plus separate semantic/live evidence |
| Lab 4: compare two stores, conceptual permitted | 12 | store-comparison.md | Qdrant/pgvector conceptual comparison, tested versus inferred |
| Lab 5: 15–25 evaluation questions, classify failures | 11 | golden.json + evaluation-report.md | Learner validates seeds and rewrites/adds >=5 |
| Deliverable: ingest/search/ask manual RAG API | 5–10 | rag.py | Independent code, tests and local requests |
| Deliverable: vector DB comparison | 12 | store-comparison.md | Setup/filtering/persistence/deployment fit |
| Deliverable: RAG diagram and retrieval report | 2, 11, 13 | data-flow.md; evaluation-report.md | Concrete IDs, boundaries, results and limitations |
| Deliverable: chunking/filter/mock LLM tests | 5, 7, 9–10 | tests/test_contract.py + learner variations | Passing behavior checks and independently added failure |
| Explain: document/chunk/embedding storage | 2, 5–8, 13 | diagram/review | Fields and lifetimes explained |
| Explain: context selection | 9, 13 | diagram/review | Filter, ranking, budget and selected IDs |
| Explain: retrieval versus generation failure | 11, 13 | evaluation/review | Retrieval-only and oracle-context diagnosis |
| Explain: sensitive data in prompts/logs | 3, 9–10, 13 | decisions/review | Ownership boundary and safe error/log trace |
| Resources: Qdrant, Chroma, HF, Groq/OpenRouter | 3, 6–8, 12–13 | RESOURCES; reading-log | Annotated source reading tied to implementation |

## Exclusions and evidence limits
The source DSA focus, NeetCode, graph drills, interview exercises and associated logs are excluded.
Ordinary dictionaries/lists/sets remain where needed by API, metadata and evaluation tasks.
Real-model download/provider calls are learner actions, with offline checks clearly distinguished.
The 20 supplied seeds are examples, not claimed learner-created questions or completed evaluation.
Reranking and streaming are awareness topics, not extra production implementation requirements.
No syllabus gaps identified in teaching coverage; learner project/evaluation remain intentionally unfinished.
