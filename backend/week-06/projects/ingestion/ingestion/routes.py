"""Learner HTTP adapter; expose POST /documents and GET /jobs/{job_id}.
Use APIRouter; auth on both; response_model; multipart field named file.
Persist before tasks.add_task(run_job, job_id, repo, storage). Return 202.
Map UploadProblem to HTTPException and missing jobs to 404.
"""
def build_router(settings, repo, storage):
    raise NotImplementedError("Build the two protected routes")
