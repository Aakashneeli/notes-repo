"""Small, complete worked tests using only the standard library."""
import unittest
from greet import greeting


class GreetingTests(unittest.TestCase):
    def test_trims_name(self):
        self.assertEqual(greeting("  Asha  "), "Hello, Asha")

    def test_blank_name_is_invalid(self):
        with self.assertRaises(ValueError):
            greeting("   ")


if __name__ == "__main__":
    unittest.main()
