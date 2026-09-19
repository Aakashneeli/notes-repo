import json
import unittest
import exercises


class Exercises(unittest.TestCase):
    def test_boundary(self):
        class Fake:
            def title(self, item_id):
                assert item_id == "x"
                return "small win"
        self.assertEqual(exercises.label("x", Fake()), "SMALL WIN")

    def test_retry(self):
        for status, safe, expected in [(503, True, True), (429, True, True),
                                       (503, False, False), (400, True, False),
                                       (401, True, False), (403, True, False)]:
            with self.subTest(status=status, safe=safe):
                self.assertEqual(exercises.retryable(status, safe), expected)

    def test_cache(self):
        key = exercises.cache_key("red", "v1", "hi")
        self.assertEqual(json.loads(key), ["red", "v1", "hi"])
        self.assertNotEqual(key, exercises.cache_key("blue", "v1", "hi"))
        self.assertNotEqual(exercises.cache_key("a:b", "c", "q"),
                            exercises.cache_key("a", "b:c", "q"))

    def test_rate(self):
        self.assertEqual(exercises.error_rate([200, 500, 503, 400]), .5)
        self.assertEqual(exercises.error_rate([]), 0)
        self.assertEqual(exercises.error_rate([200]), 0)


if __name__ == "__main__":
    unittest.main()
