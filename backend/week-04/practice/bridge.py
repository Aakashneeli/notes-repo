"""Completed prerequisite fixture; no prior mastery is assumed."""

from pydantic import BaseModel, ConfigDict, Field


class Label(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    text: str = Field(min_length=1, max_length=12)


def rename(row: dict[str, object], changes: dict[str, object]) -> dict[str, object]:
    return {**row, **changes}


if __name__ == "__main__":
    print(Label(text="  tea  ").model_dump())
    print(rename({"text": "tea", "hot": True}, {"hot": False}))
