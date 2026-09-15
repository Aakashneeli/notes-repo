"""Structural learner gate. No network, Docker daemon or project execution.
This cannot prove runtime connectivity, safe middleware or business correctness.
"""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]


def compose_errors(config):
    errors = []
    services = config.get("services", {}) or {}
    required = {"api", "postgres", "redis", "worker", "vector"}
    if set(services) != required:
        errors.append("Define exactly api, postgres, redis, worker, vector")
    for name, service in services.items():
        if not isinstance(service, dict):
            errors.append(f"{name}: service must be a mapping")
            continue
        if name != "api" and service.get("ports"):
            errors.append(f"{name}: internal service must not publish a host port")
        if service.get("container_name"):
            errors.append(f"{name}: omit fixed container_name for isolated project trials")
        networks = service.get("networks", [])
        expected = {"app", "data"} if name == "api" else {"data"}
        if set(networks) != expected:
            errors.append(f"{name}: expected networks {sorted(expected)}")
    api = services.get("api", {})
    for name in ("api", "worker"):
        build = services.get(name, {}).get("build", {})
        if not isinstance(build, dict) or build.get("context") != "../.." or build.get(
            "dockerfile") != "projects/local-stack/Dockerfile":
            errors.append(f"{name}: expected shared Week 7 build context/Dockerfile")
    if not api.get("ports") or not all(str(p).startswith("127.0.0.1:") for p in api["ports"]):
        errors.append("api: publish only on host loopback with short port syntax")
    for name in ("api", "postgres", "redis"):
        if not services.get(name, {}).get("healthcheck", {}).get("test"):
            errors.append(f"{name}: missing healthcheck test")
    for target in ("postgres", "redis"):
        if api.get("depends_on", {}).get(target, {}).get("condition") != "service_healthy":
            errors.append(f"api: wait for healthy {target}")
    if services.get("worker", {}).get("depends_on", {}).get("api", {}).get(
        "condition") != "service_healthy":
        errors.append("worker: wait for healthy api after bootstrap")
    if not config.get("networks", {}).get("data", {}).get("internal"):
        errors.append("data network must be internal")
    for name, mount in {"postgres": "pgdata:/var/lib/postgresql/data",
                        "redis": "redisdata:/data", "vector": "vectordata:/qdrant/storage"}.items():
        if mount not in services.get(name, {}).get("volumes", []):
            errors.append(f"{name}: missing named-volume mount {mount}")
    if set(config.get("volumes", {})) != {"pgdata", "redisdata", "vectordata"}:
        errors.append("Declare all three named volumes")
    return errors


def workflow_errors(config):
    errors = []
    # YAML 1.1 interprets unquoted `on` as True; GitHub uses the workflow key as text.
    triggers = config.get("on", config.get(True, []))
    if not {"push", "pull_request"}.issubset(set(triggers or [])):
        errors.append("workflow: require push and pull_request triggers")
    if config.get("permissions", {}).get("contents") != "read":
        errors.append("workflow: set contents permission to read")
    jobs = config.get("jobs", {}) or {}
    if not jobs:
        errors.append("workflow: add a lint/test job")
    for name, job in jobs.items():
        if job.get("runs-on") != "ubuntu-latest":
            errors.append(f"{name}: use Ubuntu runner for this lab")
        if job.get("defaults", {}).get("run", {}).get("working-directory") != "cloud-devops/week-07":
            errors.append(f"{name}: expected Week 7 default working directory")
        steps = job.get("steps", [])
        uses = [step.get("uses", "") for step in steps]
        if not any(value.startswith("actions/checkout@") for value in uses):
            errors.append(f"{name}: missing checkout action")
        if not any(step.get("uses", "").startswith("actions/setup-python@") and
                   str(step.get("with", {}).get("python-version")) == "3.12" for step in steps):
            errors.append(f"{name}: missing Python 3.12 setup")
        commands = "\n".join(step.get("run", "") for step in steps)
        for required in ("pip install -r requirements.lock", "python -m ruff check .", "python -m pytest -q"):
            if required not in commands:
                errors.append(f"{name}: missing {required}")
        if any(step.get("continue-on-error") for step in steps) or "|| true" in commands:
            errors.append(f"{name}: checks must fail the job on failure")
    return errors


def dockerfile_errors(text):
    instructions = [line.strip() for line in text.splitlines()
                    if line.strip() and not line.lstrip().startswith("#")]
    errors = []
    for prefix in ("FROM ", "WORKDIR ", "COPY ", "RUN ", "CMD ["):
        if not any(line.startswith(prefix) for line in instructions):
            errors.append(f"Dockerfile: missing {prefix.strip()}")
    if any(".env" in line for line in instructions):
        errors.append("Dockerfile: do not bake .env into image")
    return errors


def main():
    project = ROOT / "projects/local-stack"
    try:
        compose = yaml.safe_load((project / "compose.yaml").read_text()) or {}
        workflow = yaml.safe_load((project / "ci/workflow.yml").read_text()) or {}
        errors = (dockerfile_errors((project / "Dockerfile").read_text())
                  + compose_errors(compose) + workflow_errors(workflow))
    except (yaml.YAMLError, AttributeError, TypeError) as exc:
        print(f"Configuration shape error: {type(exc).__name__}; inspect YAML mappings/lists")
        return 1
    for error in errors:
        print("TODO:", error)
    if errors:
        print(f"{len(errors)} unfinished/invalid configuration requirements; expected on untouched starters")
        return 1
    print("Structural gate passed. Still run Compose config, live smoke, pytest and manual review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
