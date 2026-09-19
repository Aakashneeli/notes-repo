# Independent completion
For each claim, link code, a run/result, an explanation and a variation. Do not tick from reading.
- Implement chunking from the contract and predict overlap/empty/final-boundary results.
- Re-ingest without duplicates; preserve metadata and demonstrate tenant isolation before top-k.
- Generate real embeddings, document the model/configuration and reopen a real local vector store.
- Independently implement ingest/search/ask; validate generated JSON and IDs, abstain, bound repairs.
- Test malformed output, unknown citations, timeout, empty context, stale versions and private tenants.
- Explain what local mocks prove, then separately document real retrieval and live generation
  (or clearly name credentials/network/budget limitations; do not label a mock end-to-end RAG).
- Curate 15–25 golden questions, include expected sources/unknowns, classify every failure,
  inspect unsupported claims, run one controlled fix and check held-out variations.
- Finish comparison (setup/filtering/persistence/deployment fit), data-flow diagram and failure note.
- Answer the four source explain-backs without copying and vary one implementation after a delay.
Completion is evidence-based. A blocked real-model or provider step remains pending, not waived.
