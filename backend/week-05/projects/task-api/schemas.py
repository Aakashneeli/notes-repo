"""Completed minimal Week 4 validation bridge, not assessed Week 5 persistence."""
from typing import Annotated
from pydantic import BaseModel, ConfigDict, StringConstraints, StrictBool, model_validator

Title = Annotated[str, StringConstraints(strict=True, strip_whitespace=True, min_length=1, max_length=80)]

class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title
    done: StrictBool = False

class TaskPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title | None = None
    done: StrictBool | None = None

    @model_validator(mode="after")
    def reject_explicit_null(self):
        for key in self.model_fields_set:
            if getattr(self, key) is None:
                raise ValueError("explicit null is not allowed")
        return self
