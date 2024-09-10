from typing import Any
from unittest import TestCase
from p242.python.solution import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_anagram(self):
        result = self.solution.isAnagram("anagram", "nagaram")

        self.assertTrue(result, "it's anagram")

    def test_not_anagram(self):
        result = self.solution.isAnagram("rat", "car")

        self.assertFalse(result, "it's not anagram")
