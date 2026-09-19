# Week 9 Resources

## Knowledge

- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
  State updates, edges and compilation; use during Lessons 2–3.

- [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
  Predefined workflow versus model-directed control; use for accurate explain-back.

- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
  Thread checkpoints and stores; Lesson 5 awareness only.

- [Tools](https://docs.langchain.com/oss/python/langchain/tools)
  Schemas and tool interfaces; compare with our directly called Python function.

- [Tracing quickstart](https://docs.langchain.com/langsmith/observability-quickstart)
  Project/environment setup and run inspection; Lesson 8.

- [Custom instrumentation](https://docs.langchain.com/langsmith/annotate-code)
  traceable decorator and nested operations; Lesson 7.

- [Trace privacy](https://docs.langchain.com/langsmith/mask-inputs-outputs)
  Hide or transform trace content; use before live telemetry.

- [Evaluation](https://docs.langchain.com/langsmith/evaluate-llm-application)
  Distinguish a recorded trace from a quality judgment; paired comparisons.

- [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards)
  Intended use, limitations and license evidence before download.

- [SmolLM2 model card](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct)
  Specific small CPU experiment candidate; verify revision and license.

- [Transformers pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines)
  Preprocessing/model/postprocessing and CPU device selection.

- [Tokenization](https://huggingface.co/docs/transformers/tokenizer_summary)
  Why model tokens differ from words and why the matching tokenizer matters.

- [Ollama quickstart](https://docs.ollama.com/quickstart)
  Local runtime and HTTP API; alternative experiment path.

- [Ollama generation API](https://docs.ollama.com/api/generate)
  Nonstreamed response and nanosecond timing metrics.

- [llama.cpp](https://github.com/ggml-org/llama.cpp)
  GGUF, CPU inference and CLI/server examples; awareness and comparison.

- [vLLM documentation](https://docs.vllm.ai/en/stable/)
  Supported hardware and serving concepts; no GPU install required.

- [vLLM server reference](https://docs.vllm.ai/en/v0.21.0/serving/openai_compatible_server/)
  Versioned API reference: compatible HTTP shape is not identical behavior.

- [vLLM engine explanation](https://vllm.ai/blog/2025-09-05-anatomy-of-vllm)
  Continuous batching and KV cache; Lesson 11 concept note.

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
  API tests with an in-process client; Lesson 6.

- [Python typing](https://docs.python.org/3/library/typing.html#typing.TypedDict)
  TypedDict is a typing contract, not runtime input validation.

Checked against official sources on 2026-09-18. Executable core versions are pinned in requirements.lock; future docs may show newer APIs. The live latest vLLM server URL redirected without usable content, so a clearly versioned server reference is supplied.

## Wisdom (Communities)

- [LangChain forum](https://forum.langchain.com/): optional place to discuss a minimal reproducible graph failure after removing private data. Participation is a learner choice; nothing is sent by this workspace.
- [Hugging Face discussions](https://discuss.huggingface.co/): optional hardware/model compatibility discussion; compare answers against the model's official card and your measured results.

## Limits

No fixed hosted-service price or free allowance is promised. Check current account limits before the live tracing lab. Model downloads use bandwidth/disk and CPU inference uses local resources. Neither a synthetic trace nor a mocked backend fulfills the corresponding real integration gate.
