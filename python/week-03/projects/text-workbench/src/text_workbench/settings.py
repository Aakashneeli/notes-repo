"""Learner implementation: explicit mapping in, validated Config out."""

from collections.abc import Mapping

from text_workbench.models import Config


def load_settings(env: Mapping[str, str]) -> Config:
    """Read TEXT_MAX_CHARS and TEXT_LOG_LEVEL; ignore unrelated env keys.

    Convert max chars with int; invalid strings raise ValueError. Missing keys use
    model defaults. Do not read global os.environ here or load files implicitly.
    """
    raise NotImplementedError("Implement settings after lesson 6")
