# Independent completion gate

Close worked answers. A green instructor test is not proof of learning.

- Implement workflow.py yourself. Run all project tests, then add tests for no citations, out-of-range score, non-string answer, and a new tool argument failure. Explain why each fails before repair.
- Draw state after every node for refund, weak retrieval and a tool timeout. Predict which backend methods are never called.
- Explain source prompt 1: What is stored in LangGraph state at each step? Include tenant origin, transient hits, answer draft and terminal status; distinguish checkpoints from traces.
- Explain source prompt 2: Why is this an agent workflow instead of a normal function pipeline? Say precisely that our predefined router is a workflow; a graph alone does not confer autonomous agency. Explain what model-directed tool selection would change.
- Explain source prompt 3: How do LangSmith traces differ from backend logs? Use a real success, failure, slow and tool-error run. Include at least ten inspected run IDs overall, not merely twelve script invocations.
- Explain source prompt 4: When choose hosted APIs, Ollama/llama.cpp or vLLM? Defend with measured local limitations, load, quality, cost, hardware and privacy constraints.
- Integrate the actual RAG search/generation behind the contract once Week 8 is ready. Prove persistence/real retrieval separately; fixtures do not satisfy that gate.
- Run one real small local model or embedding model. Record revision, license, load versus warm latency, CPU/RAM, outputs and task-level quality.
- Find and repair one bug; preserve before/after failing case and regression test in debugging-note.md.
- Change the lookup prefix or retrieval threshold and add a case which changes route. Explain the tradeoff without reading the original implementation.
- Read one framework function/test path and record where an assumption was confirmed or rejected.

Record readiness as independent / with hints / blocked, never by time spent. If accounts/hardware block a lab, retain partial completion and exact next action; do not quietly replace it with a mock.
