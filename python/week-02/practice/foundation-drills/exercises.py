"""Small Week 2 exercises. Work on one group at a time.

Run: python practice/foundation-drills/check.py strings
Contracts, hints and explanations are in lessons/0016-foundation-workshop.html.
"""
import json
from pathlib import Path


def tidy_name(raw):
    """Remove surrounding whitespace and lowercase a filename. Return the new string; do not print."""
    raise NotImplementedError("Complete tidy_name: strings group")


def make_label(name, count):
    """Return the exact text name: count files. count is an integer; no singular/plural special case is required."""
    raise NotImplementedError("Complete make_label: strings group")


def add_filename(files, name):
    """Return a new list with name appended. Leave the input list unchanged."""
    raise NotImplementedError("Complete add_filename: collections group")


def read_level(record):
    """Return the value under the level key; if the key is absent, return INFO. An explicitly present empty value remains empty."""
    raise NotImplementedError("Complete read_level: collections group")


def known_levels(levels):
    """Return a set of distinct level strings. Preserve spelling and case; no normalization is requested."""
    raise NotImplementedError("Complete known_levels: collections group")


def can_process(name, enabled):
    """Return True only when enabled is a boolean True and name ends with .txt. Inputs are a string and a bool; suffix matching is case-sensitive."""
    raise NotImplementedError("Complete can_process: flow group")


def describe_count(count):
    """For a nonnegative integer, return empty for 0, one file for 1, and many files for larger values."""
    raise NotImplementedError("Complete describe_count: flow group")


def total_bytes(sizes):
    """Return the sum of a list of nonnegative integer byte sizes. An empty list gives zero. Use an explicit loop for this drill so you can trace the running value."""
    raise NotImplementedError("Complete total_bytes: flow group")


def keep_nonblank(lines):
    """Return original nonblank lines in order. A line is blank if strip() produces an empty string. Do not remove spacing from retained lines or mutate the input."""
    raise NotImplementedError("Complete keep_nonblank: flow group")


def first_token(line):
    """Return the first whitespace-delimited token. Return an empty string for an empty/whitespace-only line. Preserve token case."""
    raise NotImplementedError("Complete first_token: io group")


def read_utf8(path):
    """Accept a pathlib.Path. Return the file text decoded as UTF-8, with newlines retained as read_text returns them. Let missing-file errors propagate."""
    raise NotImplementedError("Complete read_utf8: io group")


def parse_json(text):
    """Return the Python value parsed from JSON text. Support any valid JSON value. Let JSONDecodeError propagate for invalid text."""
    raise NotImplementedError("Complete parse_json: io group")
