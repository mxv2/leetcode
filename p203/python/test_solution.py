from typing import Any
from unittest import TestCase
from p203.python.solution import Solution, ListNode


class TestSolution(TestCase):
    solution = Solution()

    def test_remove_several_nodes(self):
        head = self.buildList([1, 2, 6, 3, 4, 5, 6])

        result = self.solution.removeElements(head, 6)

        expected = self.buildList([1, 2, 3, 4, 5])
        self.assertListEqual(result, expected, "wrong new list")

    def test_empty(self):
        head = self.buildList([])

        result = self.solution.removeElements(head, 1)

        expected = self.buildList([])
        self.assertListEqual(result, expected, "wrong new list")

    def test_remove_all_nodex(self):
        head = self.buildList([7, 7, 7, 7])

        result = self.solution.removeElements(head, 7)

        expected = self.buildList([])
        self.assertListEqual(result, expected, "wrong new list")

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
