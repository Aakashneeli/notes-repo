"""Learner contract: failures are expected until instrumentation.py is implemented."""
import asyncio
import json
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import instrumentation as subject

FIELDS = {"event", "request_id", "model", "latency_ms", "status", "retrieval_hits",
          "input_tokens", "output_tokens", "estimated_cost_usd"}
RATES = {"input": 2.0, "output": 6.0}


def assert_event(case, event):
    case.assertEqual(set(event), FIELDS)
    case.assertEqual(event["event"], "ai.request")
    case.assertIsInstance(event["request_id"], str)
    case.assertTrue(event["request_id"])
    case.assertIsInstance(event["model"], str)
    case.assertIn(event["status"], ("ok", "error"))
    case.assertTrue(math.isfinite(event["latency_ms"]))
    case.assertGreaterEqual(event["latency_ms"], 0)
    case.assertIsInstance(event["retrieval_hits"], int)
    case.assertGreaterEqual(event["retrieval_hits"], 0)
    json.dumps(event, allow_nan=False)


class EventTests(unittest.TestCase):
    def test_success_allowlist_and_cost(self):
        e = subject.build_event("r1", "fixture", 12.5, "ok", 2,
                                {"input_tokens": 100, "output_tokens": 20,
                                 "prompt": "SECRET"}, RATES)
        assert_event(self, e)
        self.assertEqual(e["request_id"], "r1")
        self.assertEqual(e["model"], "fixture")
        self.assertEqual(e["latency_ms"], 12.5)
        self.assertEqual(e["status"], "ok")
        self.assertEqual(e["retrieval_hits"], 2)
        self.assertEqual(e["input_tokens"], 100)
        self.assertEqual(e["output_tokens"], 20)
        self.assertAlmostEqual(e["estimated_cost_usd"], .00032)
        self.assertNotIn("SECRET", json.dumps(e))
        other = subject.build_event("different", "other-model", 3, "ok", 7,
                                    {"input_tokens": 250, "output_tokens": 50},
                                    {"input": 4.0, "output": 8.0})
        self.assertEqual(other["retrieval_hits"], 7)
        self.assertEqual(other["request_id"], "different")
        self.assertEqual(other["model"], "other-model")
        self.assertAlmostEqual(other["estimated_cost_usd"], .0014)

    def test_unknown_usage(self):
        e = subject.build_event("r2", "fixture", 0, "error", 0, None, RATES)
        assert_event(self, e)
        for field in ("input_tokens", "output_tokens", "estimated_cost_usd"):
            self.assertIsNone(e[field])

    def test_zero_is_known_usage(self):
        e = subject.build_event("r3", "fixture", 1, "ok", 0,
                                {"input_tokens": 0, "output_tokens": 0}, RATES)
        self.assertEqual(e["estimated_cost_usd"], 0)

    def test_missing_or_partial_usage_is_unknown(self):
        for usage in ({}, {"input_tokens": 10}):
            e = subject.build_event("r4", "fixture", 1, "ok", 0, usage, RATES)
            for field in ("input_tokens", "output_tokens", "estimated_cost_usd"):
                self.assertIsNone(e[field])


class ObserveTests(unittest.IsolatedAsyncioTestCase):
    async def test_success_once_and_preserve_result(self):
        calls, events = [], []
        result = {"hits": 2, "usage": {"input_tokens": 100, "output_tokens": 20},
                  "answer": "PRIVATE"}
        async def operation():
            calls.append(1)
            await asyncio.sleep(.01)
            return result
        got = await subject.observe(operation, events.append, "r5", "fixture", RATES)
        self.assertIs(got, result)
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(events), 1)
        assert_event(self, events[0])
        self.assertEqual(events[0]["status"], "ok")
        self.assertEqual(events[0]["retrieval_hits"], 2)
        self.assertEqual(events[0]["request_id"], "r5")
        self.assertEqual(events[0]["model"], "fixture")
        self.assertAlmostEqual(events[0]["estimated_cost_usd"], .00032)
        # Catch seconds reported as milliseconds or a hardcoded zero duration.
        self.assertGreaterEqual(events[0]["latency_ms"], 5)
        self.assertNotIn("PRIVATE", json.dumps(events))

    async def test_error_preserved_and_event_emitted(self):
        events = []
        error = TimeoutError("PRIVATE")
        async def operation():
            raise error
        with self.assertRaises(TimeoutError) as caught:
            await subject.observe(operation, events.append, "r6", "fixture", RATES)
        self.assertIs(caught.exception, error)
        self.assertEqual(len(events), 1)
        assert_event(self, events[0])
        self.assertEqual(events[0]["status"], "error")
        self.assertIsNone(events[0]["estimated_cost_usd"])
        self.assertNotIn("PRIVATE", json.dumps(events))

    async def test_request_ids_do_not_cross(self):
        events = []
        async def operation():
            await asyncio.sleep(.001)
            return {"hits": 0, "usage": None}
        await asyncio.gather(*(subject.observe(operation, events.append, rid,
                              "fixture", RATES) for rid in ("red", "blue")))
        self.assertEqual({e["request_id"] for e in events}, {"red", "blue"})
        self.assertEqual(len(events), 2)


if __name__ == "__main__":
    unittest.main()
