"""Completed small greeting example; intentionally NOT a CRUD solution."""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Path, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field


class GreetingIn(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    name: str = Field(min_length=1, max_length=20)


class GreetingOut(BaseModel):
    message: str


def require_badge(badge: Annotated[str | None, Header(alias="X-Badge")] = None) -> str:
    if badge != "practice":
        raise HTTPException(
            401, "Badge required", headers={"WWW-Authenticate": "APIKey"}
        )
    return badge


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ready = True
    yield
    app.state.ready = False


app = FastAPI(title="Greeting teaching example", lifespan=lifespan)


@app.exception_handler(RequestValidationError)
async def invalid_request(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": {"code": "validation_error", "message": "Check your input"}},
    )


@app.get("/greetings/{number}", response_model=GreetingOut)
def greeting(
    number: Annotated[int, Path(ge=1)], loud: Annotated[bool, Query()] = False
) -> dict[str, str]:
    message = f"Hello {number}"
    return {"message": message.upper() if loud else message}


@app.post("/greetings", status_code=201, response_model=GreetingOut)
def create_greeting(
    payload: GreetingIn, badge: Annotated[str, Depends(require_badge)]
) -> dict[str, str]:
    return {"message": f"Hello {payload.name}"}
