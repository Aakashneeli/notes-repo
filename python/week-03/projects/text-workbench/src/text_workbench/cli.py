"""Supplied command adapter; core decisions and implementation stay with learner."""

import argparse
import os
import sys
from pathlib import Path

from pydantic import ValidationError

from text_workbench.logging_setup import configure_logging
from text_workbench.service import process_file
from text_workbench.settings import load_settings


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize UTF-8 text metadata")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        config = load_settings(os.environ)
        configure_logging(config.log_level)
        record = process_file(args.path, config)
    except (OSError, ValueError, ValidationError):
        # Stable message avoids echoing input/configuration values to stderr.
        print("Cannot process input: check file, encoding, size and settings.", file=sys.stderr)
        return 2
    print(record.model_dump_json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
