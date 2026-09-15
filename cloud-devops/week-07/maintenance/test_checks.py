"""Test checker rules with tiny synthetic fragments; no solved main project."""
from check_project import compose_errors, dockerfile_errors, workflow_errors


def test_empty_configs_rejected():
    assert compose_errors({})
    assert workflow_errors({})
    assert dockerfile_errors("# starter")


def test_hidden_service_port_detected():
    errors = compose_errors({"services": {"redis": {"ports": ["6379:6379"]}}})
    assert "redis: internal service must not publish a host port" in errors


def test_safe_service_port_not_falsely_rejected():
    errors = compose_errors({"services": {"redis": {"networks": ["data"]}}})
    assert not any("internal service must not publish" in value for value in errors)


def test_wrong_build_path_detected():
    errors = compose_errors({"services": {"api": {"build": {"context": "."}}}})
    assert any("api: expected shared" in value for value in errors)


def test_python_yaml_on_key():
    errors = workflow_errors({True: ["push", "pull_request"], "permissions": {"contents": "read"}})
    assert not any("triggers" in value for value in errors)
    assert not any("permission" in value for value in errors)
    assert "workflow: add a lint/test job" in errors


def test_docker_instruction_recognition():
    text = 'FROM python:3.12-slim\nWORKDIR /sample\nCOPY sample.py .\nRUN python --version\nCMD ["python", "sample.py"]'
    assert dockerfile_errors(text) == []
    assert dockerfile_errors(text + '\nCOPY .env /sample/.env')
