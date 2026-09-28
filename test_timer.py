import sys
import unittest
from pathlib import Path

# Allow the test file to import main.py when tests are discovered from the tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import format_time, validate_time


class TestCountdownTimer(unittest.TestCase):

    def test_format_time(self):
        self.assertEqual(format_time(0), "00:00")
        self.assertEqual(format_time(65), "01:05")
        self.assertEqual(format_time(600), "10:00")

    def test_valid_time(self):
        self.assertEqual(validate_time(2, 30), 150)

    def test_negative_time(self):
        with self.assertRaises(ValueError):
            validate_time(-1, 0)

    def test_invalid_seconds(self):
        with self.assertRaises(ValueError):
            validate_time(1, 60)

    def test_zero_time(self):
        with self.assertRaises(ValueError):
            validate_time(0, 0)


if __name__ == "__main__":
    unittest.main()
