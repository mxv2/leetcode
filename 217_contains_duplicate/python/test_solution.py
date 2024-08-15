from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_twice(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_unique(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_multiple(self):
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_one_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_empty(self):
        self.assertFalse(self.solution.containsDuplicate([]))
