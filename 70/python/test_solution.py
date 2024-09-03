from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_1_stairs(self):
        result = self.solution.climbStairs(1)
        self.assertEqual(result, 1, "wrong variants")

    def test_2_stairs(self):
        result = self.solution.climbStairs(2)
        self.assertEqual(result, 2, "wrong variants")

    def test_4_stairs(self):
        result = self.solution.climbStairs(4)
        self.assertEqual(result, 5, "wrong variants")

    def test_5_stairs(self):
        result = self.solution.climbStairs(5)
        self.assertEqual(result, 8, "wrong variants")

