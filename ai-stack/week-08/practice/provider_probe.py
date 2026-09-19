"""Explicit learner-run, potentially billable call. No automatic calls during tests."""
import argparse
import json
import os
import httpx

def request_body(model):
    return {"model": model, "stream": False, "messages": [
        {"role": "system", "content": "Reply with one short sentence."},
        {"role": "user", "content": "Say hello to a backend learner."}]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    body = request_body(os.environ.get("LLM_MODEL", "SELECT-A-CURRENT-MODEL"))
    if not args.live:
        print(json.dumps(body, indent=2))
        return
    provider = os.environ.get("LLM_PROVIDER", "groq")
    urls = {"groq": "https://api.groq.com/openai/v1/chat/completions",
            "openrouter": "https://openrouter.ai/api/v1/chat/completions"}
    if provider not in urls or body["model"] == "SELECT-A-CURRENT-MODEL":
        raise SystemExit("Select groq/openrouter and a currently available LLM_MODEL")
    key = os.environ.get("LLM_API_KEY")
    if not key:
        raise SystemExit("Set LLM_API_KEY without saving it in Git")
    try:
        with httpx.Client(timeout=20) as client:
            response = client.post(urls[provider], json=body,
                headers={"Authorization": "Bearer " + key})
            response.raise_for_status()
            result = response.json()
            print(result["choices"][0]["message"]["content"])
    except httpx.HTTPStatusError as exc:
        raise SystemExit(f"Provider HTTP {exc.response.status_code}; body withheld") from None
    except (httpx.RequestError, KeyError, IndexError, ValueError):
        raise SystemExit("Transport/response failure; inspect safely without logging secrets") from None

if __name__ == "__main__":
    main()
