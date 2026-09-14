"""Learner orchestration. Domain code must not import FastAPI."""
def accept(data, original_name, repo, storage):
    raise NotImplementedError("Generate UUID; store bytes then metadata; compensate on DB failure; return job_id")
def get_status(job_id, repo):
    raise NotImplementedError("Return public JobView-shaped dict, or None")
