# Week 09 — Agents

Source: `/home/an10/Downloads/ai-backend-roadmap.html`, numbered article `#week-9`.
Exact source title: **LangGraph, LangSmith, Tool Use, Hugging Face, Ollama, llama.cpp, and vLLM Concepts**.
Workspace: `ai-stack/week-09/`. Topic chosen because the main objective is stateful AI orchestration after manual RAG. No numbering exception or existing conflicting workspace was found.

[Open the study desk](index.html). Start with [Lesson 1](lessons/0001-start.html).

Required outcomes: LangGraph RAG service + one bounded lookup tool; LangSmith inspection of at least 10 runs including success/failure/slow/tool-error; local inference notes (model, CPU/RAM, latency, quality); vLLM production concept note; failure list and tool safety checklist; four source explain-backs.

Week 8's `projects/manual-rag/rag.py` still raises NotImplementedError, and its progress is unassessed. We preserve it. This week's exact-keyword fixture permits learning orchestration without pretending a semantic RAG backend already exists. Lesson 6 describes the real-backend adapter and its separate evidence gate.

All terminal steps start at this weekly root unless an explicit `cd` says otherwise. Lesson 1 explains installation. Core checks need Python 3.12 and the locked packages; no API key, GPU or model weights. LangSmith and model-download actions belong to the learner.

- `lessons/`: read in sequence, pause at each exercise; `reference/`: glossary and troubleshooting.
- `practice/`: completed ticket example, learner exercises, synthetic trace and real-model probe.
- `projects/agent-rag/`: learner implementation, contract, fixture, tests and evidence notes.
- `plan/`: sequence, coverage, file-to-lesson map, assessment, progress and teaching audit.
- `weekly-logs/`, `templates/`, `codebase-reading/`: learner evidence, not author completion ticks.
- `assets/`: shared local CSS; `maintenance/` and `VALIDATION.md`: tutor verification.

See [file usage map](plan/file-map.html) for every supplied file's first lesson/action. Generated environments/caches are not learning materials. No learning record is created just because materials exist. DSA/interview exercises and associated logs are excluded.
