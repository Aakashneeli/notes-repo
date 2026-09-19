# Learner project: bounded RAG workflow

Start in ai-stack/week-09. Read contract.md in Lesson 3; implement workflow.py through Lessons 3–6. bridge.py is an exact-keyword prerequisite fixture because Week 8 is unfinished. It is not semantic retrieval, a production provider or your project solution.

```sh
.venv/bin/python -m pytest projects/agent-rag/tests -q
.venv/bin/python projects/agent-rag/run_local.py
```

Initially both expose NotImplementedError. The supplied server binds only 127.0.0.1:8009. Unit/API tests need no server. Live tracing and inference are separate learner actions introduced in Lessons 8 and 10.

Keep the evidence notes here, with generated runs in ignored runtime/. Do not overwrite earlier evidence. Read the contract for what the fixture proves and the real integration gate.
