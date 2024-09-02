from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_missing_in_middle(self):
        result = self.solution.missingNumber([3, 0, 1])
        self.assertEqual(result, 2, "wrong missing number")

    def test_missing_last(self):
        result = self.solution.missingNumber([0, 1])
        self.assertEqual(result, 2, "wrong missing number")

    def test_missing_near_end(self):
        result = self.solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        self.assertEqual(result, 8, "wrong missing number")

    def test_missing_first(self):
        result = self.solution.missingNumber([1, 5, 3, 2, 4])
        self.assertEqual(result, 0, "wrong missing number")

    def test_one_element(self):
        result = self.solution.missingNumber([0])
        self.assertEqual(result, 1  , "wrong missing number")

    def test_empty(self):
        result = self.solution.missingNumber([])
        self.assertEqual(result, 0, "wrong missing number")
