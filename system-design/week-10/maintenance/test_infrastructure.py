"""Tutor checks for completed examples/fixtures; contains no project implementation."""
import asyncio
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


examples = module('examples', 'practice/examples.py')
# Contract module inserts its project directory, which also resolves fixture imports.
contract = module('contract', 'projects/architecture-review/tests/test_contract.py')
fixture = module('fixture_local', 'projects/architecture-review/fixture.py')
experiment = module('experiment', 'projects/architecture-review/experiment.py')


class Infrastructure(unittest.TestCase):
    def test_boundary_example_and_failure(self):
        self.assertEqual(examples.label('book-1', examples.MemoryCatalog()), 'FIELD GUIDE')
        with self.assertRaises(KeyError):
            examples.label('absent', examples.MemoryCatalog())

    def test_retry_stops_and_does_not_swallow_wrong_error(self):
        calls = []
        def read():
            calls.append(1)
            raise TimeoutError('synthetic')
        with self.assertRaises(TimeoutError):
            examples.retry_read(read)
        self.assertEqual(len(calls), 3)
        calls.clear()
        def invalid():
            calls.append(1)
            raise ValueError('invalid')
        with self.assertRaises(ValueError):
            examples.retry_read(invalid)
        self.assertEqual(len(calls), 1)

    def test_timeout_example(self):
        events = asyncio.run(examples.timed_demo())
        self.assertEqual(events[0]['event'], 'catalog.timeout')
        self.assertGreaterEqual(events[0]['elapsed_ms'], 0)

    def test_fixture_success_and_fault(self):
        self.assertEqual(asyncio.run(fixture.query())['hits'], 2)
        with self.assertRaises(TimeoutError):
            asyncio.run(fixture.query(fail=True))

    def test_measurement_counts_errors_and_samples(self):
        for mode in ('cooperative', 'blocking'):
            result = asyncio.run(experiment.measure(mode, 4, 20))
            self.assertEqual(result['error_rate'], .1)
            self.assertEqual(len(result['rows']), 20)
            self.assertLessEqual(result['p50_ms'], result['p95_ms'])
            self.assertGreater(result['requests_per_second'], 0)
            self.assertTrue(all(r['latency_ms'] >= r['service_ms'] >= 0
                                for r in result['rows']))

    def test_beginner_answers_printed_in_lessons(self):
        # These are explained beginner answers, not the assessed logging project.
        def retryable(status, safe):
            return status in (429, 503) and safe
        def key(tenant, version, query):
            return json.dumps([tenant, version, query])
        def error_rate(statuses):
            if not statuses:
                return 0.0
            return sum(status >= 500 for status in statuses) / len(statuses)
        self.assertTrue(retryable(503, True))
        self.assertFalse(retryable(503, False))
        self.assertFalse(retryable(401, True))
        self.assertNotEqual(key('a:b', 'c', 'q'), key('a', 'b:c', 'q'))
        self.assertEqual(error_rate([200, 500, 503, 400]), .5)
        self.assertEqual(error_rate([]), 0)

    def test_event_checker_accepts_sample_and_rejects_mutants(self):
        event = json.loads((ROOT / 'projects/architecture-review/data/events.jsonl')
                           .read_text().splitlines()[0])
        contract.assert_event(self, event)
        for patch in ({'prompt': 'SECRET'}, {'status': 'anything'},
                      {'latency_ms': -1}, {'latency_ms': float('nan')},
                      {'retrieval_hits': -1}, {'request_id': ''}):
            with self.subTest(patch=patch), self.assertRaises(AssertionError):
                contract.assert_event(self, {**event, **patch})

    def test_json_fixtures(self):
        data = ROOT / 'projects/architecture-review/data'
        events = [json.loads(line) for line in (data / 'events.jsonl').read_text().splitlines()]
        self.assertEqual(sum(e['status'] == 'error' for e in events), 1)
        self.assertEqual(len(events), 3)
        cases = json.loads((data / 'threat-cases.json').read_text())
        self.assertEqual(len({c['id'] for c in cases}), 6)


if __name__ == '__main__':
    unittest.main()
