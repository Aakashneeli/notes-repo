# Source coverage — Week 09

Authority: `/home/an10/Downloads/ai-backend-roadmap.html`, numbered article `#week-9`, **LangGraph, LangSmith, Tool Use, Hugging Face, Ollama, llama.cpp, and vLLM Concepts**.
Workspace: `ai-stack/week-09/`; topic AI stack; no naming exception. Main deliverables: graph-integrated RAG + one tool, ten-run LangSmith notes, real local inference measurements, vLLM concept note, failure/safety evidence and four explain-backs.

| Source requirement | Lessons | Practice/artifact | Ability evidence |
|---|---|---|---|
| Purpose/rationale: stateful workflows after understood manual RAG | 1, 3, 6 | Baseline trace; bridge inspection; real-adapter decision | Explain what fixture omits and connect actual retrieval before marking integration complete. |
| State, nodes, edges, conditional edges, tools, compilation | 2–5 | Ticket example + four beginner exercises + graph tests | Predict patches, write graph, vary a branch. |
| Router, retrieval, answer, fallback and validation nodes | 3, 5–6 | workflow.py; contract happy/weak/invalid-answer cases | Draw state at each node; no generation on empty retained hits. |
| Tool allowlist, input validation and unsafe-use awareness | 4 | lookup + calls assertions + safety-checklist.md | Reject traversal-like IDs, cross-tenant access and invented actions before dispatch. |
| LangSmith project setup, traces, run inspection, latency, prompt/model comparison | 7–8 | trace runner, trace-notes.md, paired comparison | At least ten inspected live runs; success/failure/slow/tool-error; controlled comparison or explicit missing live experiment. |
| LangChain awareness and ecosystem examples | 1, 7, 12 | requirements.lock; installed compile source; reading-log.md | Explain langchain-core versus full LangChain and one traced dependency call. |
| Hugging Face Hub cards, licenses, downloads, tokenizers, pipelines | 9–10 | Card/revision review + local_model.py | Explain input-to-token-to-output flow, license evidence and actual measured output. |
| Ollama / llama.cpp CPU models, quantization, GGUF and limits | 10–11 | Alternative runtime commands and local-inference.md | Distinguish format from quantization; hardware/quality limits; one runtime need be executed. |
| vLLM batching, high-throughput serving, compatible API and GPU relevance | 11 | serving-choice.md | Explain when production load justifies it and why API shape is insufficient. |
| Lab 1 / deliverable: integrate LangGraph around RAG API | 3–6 | Learner graph/API tests + adapter integration instructions | Fixture local gate plus separately evidenced real RAG integration. |
| Lab 2: add one lookup/search/job tool | 4–6 | Document lookup node | Bounded read-only action, schema and authorization checks. |
| Lab 3 / deliverable: trace at least ten LangSmith runs | 7–8 | 12 fictional runner cases and trace row template | Count inspected private run IDs; all four required categories. |
| Lab 4 / deliverable: one real local model or embedding model; hardware note | 9–10 | CPU model runner, three prompts twice, local-inference.md | Record model/revision, RAM/CPU, cold/warm latency, quality; no fabricated results. |
| Lab 5: vLLM production concept note | 11 | serving-choice.md | A workload, decision trigger, rejected alternative and measurement that could reverse choice. |
| Deliverable: agent failure-mode list and tool safety checklist | 4–5, 12 | failure-modes.md; safety-checklist.md; debugging-note.md | Concrete mechanisms and linked negative-case evidence. |
| Explain-back: state at each step | 2–6, 12 | Assessment prompt 1 / learner log | Trace success, weak retrieval and failed tool without reading code. |
| Explain-back: agent workflow versus normal pipeline | 3, 12 | Assessment prompt 2 | Correct the premise: this bounded predefined workflow is not autonomous merely because it is a graph. |
| Explain-back: traces versus backend logs | 7–8, 12 | Assessment prompt 3 | Use a real run and explain error handling and nested latency. |
| Explain-back: hosted APIs, Ollama/llama.cpp or vLLM | 10–12 | Assessment prompt 4 | Defend with hardware, quality, privacy, cost and workload evidence. |
| Source resources: LangGraph including persistence, LangSmith tracing/eval, HF/Ollama/llama.cpp/vLLM | All; persistence 5 | RESOURCES.md and lesson primary-source links | Read one mechanism with a concrete question; checkpoint awareness without extending project scope. |
| Continuous habits in roadmap: tests, code/doc reading, Git, debugging and explain-back | 6, 12 | Tests, local Git checkpoint, reading-log.md, review template | One meaningful local commit, real repair/regression, own-word explanation. |


## Exclusions and honest gates
DSA, NeetCode, algorithm interview work, dynamic programming, interval/greedy exercises, complexity drills and related logs are excluded. Ordinary state dictionaries/lists/sets are retained for backend work. No prior excluded logs are created or altered.

No scope gap is silently replaced by a mock. Materials cover all in-scope requirements. Learner implementation, real Week 8 integration, live LangSmith runs and local hardware experiment are pending evidence. The roadmap source has not been changed. Future weeks are mentioned only to explain sequencing; no detailed future lessons are created.
