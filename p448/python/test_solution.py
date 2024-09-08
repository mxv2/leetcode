from unittest import TestCase
from p448.python.solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_missing_in_middle(self):
        result = self.solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        self.assertEqual(result, [5, 6], "wrong numbers")

    def test_missing_last(self):
        result = self.solution.findDisappearedNumbers([1, 1])
        self.assertEqual(result, [2], "wrong numbers")

    def test_missing_first(self):
        result = self.solution.findDisappearedNumbers([3, 2, 2])
        self.assertEqual(result, [1], "wrong numbers")

    def test_missing_on_the_tails(self):
        result = self.solution.findDisappearedNumbers([3, 2, 2, 2])
        self.assertEqual(result, [1, 4], "wrong numbers")

    def test_one_element(self):
        result = self.solution.findDisappearedNumbers([1])
        self.assertEqual(result, [], "wrong numbers")

    def test_empty(self):
        result = self.solution.findDisappearedNumbers([])
        self.assertEqual(result, [], "wrong numbers")
