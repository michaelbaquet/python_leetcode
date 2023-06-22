from unittest import TestCase

from python_leetcode.containsduplicates217 import contains_duplicate


class TestContainsDuplicate(TestCase):
    def test_contains_duplicate_true(self):
        input_true = [1, 2, 3, 4, 5, 1]
        self.assertTrue(contains_duplicate(input_true))

    def test_contains_duplicate_false(self):
        input_true = [1, 2, 3, 4, 5, 6]
        self.assertFalse(contains_duplicate(input_true))