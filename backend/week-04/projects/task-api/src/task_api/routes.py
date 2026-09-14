"""Learner-owned HTTP adapter. Add decorated operations to this router.

Use prefix /tasks. Inject the service and authenticated role. Convert domain
errors to HTTP at the boundary. Create 201, list/get/update 200, delete 204.
Use response models and typed path/query parameters. See project README.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])
