# Architecture review packet — learner project
The roadmap asks you to reason about your AI backend, add observability, document caching/rate limits and measure one bottleneck. This is a review/instrumentation project, not a new full RAG implementation.

Read contract.md in Lesson 3, fixture.py in Lesson 1, instrumentation.py/tests in Lesson 8 and experiment.py in Lesson 10.
- Completed infrastructure: fixture.py, experiment.py, run_observed.py, tests/test_contract.py and data/.
- Learner work: instrumentation.py, diagrams/architecture.drawio, all project Markdown records and four adrs/.
- Generated output: console JSON or optional ignored runtime/ at weekly root. Do not treat samples as learner measurements.

Actual earlier work (inspect; preserve):
- [Week 8 RAG](../../../../ai-stack/week-08/projects/manual-rag/README.md) and [rag.py](../../../../ai-stack/week-08/projects/manual-rag/rag.py).
- [Week 9 agent](../../../../ai-stack/week-09/projects/agent-rag/README.md) and [workflow.py](../../../../ai-stack/week-09/projects/agent-rag/workflow.py).
- [Week 7 local stack](../../../../cloud-devops/week-07/projects/local-stack/README.md).

Current baseline: RAG/agent starters unfinished. Fixture omits HTTP/auth, real storage, vectors, queue, provider and cloud exports. It is a minimal request-shaped async call for local instrumentation and scheduling practice. Do not claim it is an integrated AI backend.

All commands start in system-design/week-10:
```sh
python -m unittest discover -s projects/architecture-review/tests -v
python projects/architecture-review/run_observed.py
python projects/architecture-review/experiment.py --mode cooperative --concurrency 4 --count 20
```
First two initially expose unfinished instrumentation. The experiment runs immediately without completing the assessed implementation.
