from unittest import TestCase
from p136.python.solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_single_last(self):
        result = self.solution.singleNumber([2, 2, 1])
        self.assertEqual(result, 1, "wrong number")

    def test_single_first(self):
        result = self.solution.singleNumber([4, 1, 2, 1, 2])
        self.assertEqual(result, 4, "wrong number")

    def test_single(self):
        result = self.solution.singleNumber([1])
        self.assertEqual(result, 1, "wrong number")

    def test_single_negative(self):
        result = self.solution.singleNumber([2, 2, -1])
        self.assertEqual(result, -1, "wrong number")

    def test_single_several_negatives(self):
        result = self.solution.singleNumber([-4, 2, 2, -1, -4])
        self.assertEqual(result, -1, "wrong number")

    def test_single_min(self):
        result = self.solution.singleNumber([-4, 2, 2, -30000, -4])
        self.assertEqual(result, -30000, "wrong number")

    def test_single_max(self):
        result = self.solution.singleNumber([-4, 2, 2, 30000, -4])
        self.assertEqual(result, 30000, "wrong number")
