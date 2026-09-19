"""Instructor examples only; intentionally separate from learner checks."""

import importlib.util
from decimal import Decimal
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "worked_examples", Path(__file__).resolve().parents[1] / "practice/examples.py"
)
examples = importlib.util.module_from_spec(spec)
spec.loader.exec_module(examples)


def test_cost_example():
    assert examples.estimate(
        Decimal("100"), Decimal(".01"), Decimal("1"), Decimal(".005"), Decimal(".5"), Decimal("2")
    ) == Decimal("5")
    assert examples.estimate(
        Decimal("0"), Decimal(".01"), Decimal("1"), Decimal(".005"), Decimal(".5"), Decimal("2")
    ) == Decimal("3.5")


def test_release_observation():
    assert examples.choose_probe(200, "old", "new") == "wrong release"
    assert examples.choose_probe(503, "new", "new") == "investigate"
    assert examples.choose_probe(200, "new", "new") == "candidate"
