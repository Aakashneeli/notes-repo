"""Learner implementation: JSON logging, allowlisted fields only."""

import logging


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        """JSON object: level and event; optional characters and words only.

        Use record.getMessage() for event, record.levelname for level.
        Do not dump record.__dict__, arguments, traceback, source text, or paths.
        """
        raise NotImplementedError("Implement formatter after lesson 7")


def configure_logging(level: str) -> None:
    """Configure text_workbench logger with one stderr StreamHandler.

    Set logger level; use JsonFormatter; set propagate=False; repeated calls must
    not duplicate handlers. Called by CLI at startup, never while importing.
    """
    raise NotImplementedError("Implement logging setup after lesson 7")
