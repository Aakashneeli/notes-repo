# Author verification — 2026-09-18

This records preparation checks, not learner mastery. The assessed learner functions remain unfinished and progress remains unassessed.

## Source and preservation

- Read the roadmap's numbered `#week-9` article and surrounding sequence/prerequisites. Exact title and scope are recorded in README.md and plan/coverage.md.
- Inspected topic organization, shared CSS, Week 8 code/progress and the existing baseline learning record. No prior learner implementation or evidence was replaced.
- Added ai-stack/week-09 and links in the existing AI stack topic README/index and WORKSPACE-STRUCTURE.md. The pre-existing Week 8 organization entry, Week 1 notes and untracked learner work were preserved. No Git history changes, commits, publishing or account actions were performed.
- Read official documentation for graph state/edges/persistence, LangSmith tracing/privacy/evaluation, HF model cards/tokenizers/pipelines, Ollama, llama.cpp and vLLM. Current core APIs were also checked against installed packages. The vLLM latest server page returned a redirect-only response; its explicitly versioned server reference is identified in RESOURCES.md.

## Runnable checks performed

Python 3.12.14; core lock includes LangGraph 1.2.11, langchain-core 1.6.3, LangSmith 0.12.6, FastAPI 0.141.1 and pytest 9.1.1.

From ai-stack/week-09:

```sh
LANGSMITH_TRACING=false .venv/bin/python -m practice.examples
LANGSMITH_TRACING=false .venv/bin/python -m pytest maintenance -q
.venv/bin/python maintenance/verify.py
```

- Completed ticket example returned urgent=True / on-call and lookup status=open as taught.
- Four shipped instructor/fixture tests passed, covering branches, update streaming, checkpoint thread isolation, runtime tool validation and fixture boundaries.
- Executed the lesson's update-stream and checkpoint snippets; observed classify/normal patches, on-call for saved thread and empty state for another thread. Confirmed the real-adapter relative path resolves to the existing Week 8 project.
- All 21 learner test cases were run unchanged against the shipped starters: all fail with the intended NotImplementedError. This is expected unfinished work, not an infrastructure defect.
- Separately, a temporary author-only in-memory reference passed all 21 beginner/project tests, including named graph nodes and in-process HTTP validation. Learner files were never overwritten; no finished assessed graph is shipped. The scratch reference was removed after verification.
- Mutation checks caught incorrectly promoted weak scores and a beginner classification mistake. An unauthorized fixture lookup was still rejected by defensive graph validation. This is a useful sample, not exhaustive mutation coverage.
- The offline trace runner produced 12 valid JSONL records with tracing disabled against that temporary reference. Checked explicit live-client flush API availability; live delivery was not exercised.
- Syntax parsing, supplied JSON, HTML/Markdown/CSS local link targets, HTML anchors, language/viewport declarations and file-map coverage passed. Navigation checks include the shared CSS import and earlier-week bridge links. Supplied lesson commands use the weekly root; the two-terminal curl workflow explicitly restores that path.

The restricted execution sandbox blocked Chromium startup and an in-process HTTP event loop. These author checks were rerun outside that restriction using temporary profiles and fictional local data. The API checks passed. A dependency deprecation warning about AnyIO's BlockingPortal alias remains; it did not fail the tests. Temporary oracle invocation also caused benign pytest plugin rewrite warnings.

## Real CPU inference performed

[Raw author measurements](maintenance/author-inference.json) are tutor verification, not learner evidence. The supplied practice/local_model.py ran without modification against:

- Model: HuggingFaceTB/SmolLM2-135M-Instruct, revision `12fd25f77366fa6b3b4b768ec3050bf629380bac`.
- Transformers 4.57.6, PyTorch 2.14.0+cpu, Python 3.12.14, two inference threads. No GPU or hosted model API.
- Six generations: three prompts, repeated twice. Initial download/load took about 33.36s. Generation wall times ranged about 0.89–2.74s; Linux process peak RSS was 1,185,948 KiB. These are one machine/process observations, not a production benchmark.
- Simple fact extraction returned “Refunds take 30 days.” The JSON request returned a truncated Python code block; the unanswerable-context prompt invented a policy. These are observed quality failures, not runner failures.
- The model's default temperature setting emitted a nonsampling warning; deterministic decoding ignored that setting. The processor-name field was empty on this platform; the lesson asks the learner to record lscpu output separately.

Packages and model cache for this author probe live in temporary verification storage, not in learner code. The ignored core .venv uses a Python runtime under /tmp; if temporary storage is cleared, recreate it using Lesson 1's uv commands. The learner's separate inference environment is not preinstalled by the teaching setup.

## Layout and teaching review

- Chromium loaded all 16 HTML pages at 1440px and 390px widths; none had document-level horizontal overflow. Shared local typography/styles loaded. Wide file/serving tables scroll inside their own labelled regions.
- Visually inspected desktop/mobile study-desk screenshots, a mobile tool lesson and a print-style failure lesson. Print CSS hides navigation and reveals disclosure answers. Checked keyboard focus on the skip link and disclosure controls. Actual paginated printing, screen-reader testing and non-Chromium engines were not performed.
- Reviewed teaching sufficiency independently of coverage and code checks in [plan/teaching-review.md](plan/teaching-review.md): prerequisite probe, mechanism trace, relevant failure, guided exercise, feedback and independent variation precede larger tasks. No main project solution or fabricated learning record was supplied.

## Remaining learner actions / verification limits

- Implement the assessed graph/API and beginner exercises; add the independent edge-case tests and explanations.
- Connect a completed real Week 8 RAG service. Week 8 remains a starter, so fixture tests cannot prove real embeddings, persistence, provider behavior or integration with that service.
- Configure a LangSmith project personally and inspect at least ten real runs. No credentials, project creation, trace upload, hosted-model comparison or live account action was performed here. The live SDK path is taught but not end-to-end verified.
- Repeat a local model experiment as learner evidence and defend hardware/quality conclusions. Ollama and llama.cpp alternative commands were documentation-checked but not executed; vLLM is intentionally a concept lab, not a GPU deployment.
- Uvicorn/curl instructions depend on the learner's completed app. In-process API behavior was checked against the temporary reference; no running learner server or real-backend endpoint was claimed.
