# Learner project: manual RAG
Read contract.md after Lesson 2, then implement rag.py incrementally through Lessons 5–10.
bridge.py and data/documents.json provide extracted fictional documents because earlier ingestion
is unfinished. run_local.py injects deterministic fixtures, not semantic embeddings or an LLM.
Start all commands at ai-stack/week-08:
```sh
.venv/bin/python -m pytest projects/manual-rag/tests -q
.venv/bin/python projects/manual-rag/run_local.py
```
Initially tests fail with NotImplementedError and run_local.py cannot start. This is expected.
Once implemented, use the curl steps in Lesson 10, then close the server before reopening its
runtime/project-db local store. No Docker, GPU or API key required for this offline stage.
For real semantics use Lesson 8's embedding adapter; for live answers use Lesson 3's provider
contract and Lesson 4 validation. Record these separately in evaluation-report.md.
Do not call mock evidence live integration. Runtime/cache folders are generated and ignored.
