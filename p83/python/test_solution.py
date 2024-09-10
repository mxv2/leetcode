from typing import Any
from unittest import TestCase
from p83.python.solution import Solution, ListNode


class TestSolution(TestCase):
    solution = Solution()

    def test_one_duplicate(self):
        head = self.buildList([1, 1, 2])

        result = self.solution.deleteDuplicates(head)

        expected = self.buildList([1, 2])
        self.assertListEqual(result, expected, "wrong list")

    def test_several_duplicates(self):
        head = self.buildList([1, 1, 2, 3, 3])

        result = self.solution.deleteDuplicates(head)

        expected = self.buildList([1, 2, 3])
        self.assertListEqual(result, expected, "wrong list")

    def test_reverse_empty(self):
        head = self.buildList([])

        result = self.solution.deleteDuplicates(head)

        expected = self.buildList([])
        self.assertListEqual(result, expected, "wrong list")

    def buildList(self, nums):
        head = None
        current = None

        for i, n in enumerate(nums):
            node = ListNode(n)

            if head == None:
                head = node

            if current != None:
                current.next = node

            current = node

        return head

    def assertListEqual(
        self, list1: ListNode, list2: ListNode, msg: Any = None
    ) -> None:
        self.assertEqual(list1, list2, "heads not equal")

        pos = 0
        while list1 and list2:
            self.assertEqual(list1, list2, f"nodes not equal on position {pos}")

            list1 = list1.next
            list2 = list2.next
            pos += 1

        self.assertEqual(list1, None, "list1 has more nodes")
        self.assertEqual(list2, None, "list2 has more nodes")
