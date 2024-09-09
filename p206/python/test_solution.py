from typing import Any
from unittest import TestCase
from p206.python.solution import Solution, ListNode


class TestSolution(TestCase):
    solution = Solution()

    def test_reverse_several_nodes(self):
        head = self.buildList([1, 2, 3, 4, 5])

        result = self.solution.reverseList(head)

        expected = self.buildList([5, 4, 3, 2, 1])
        self.assertListEqual(result, expected, "wrong reversed list")

    def test_reverse_2_nodes(self):
        head = self.buildList([1, 2])

        result = self.solution.reverseList(head)

        expected = self.buildList([2, 1])
        self.assertListEqual(result, expected, "wrong reversed list")

    def test_reverse_empty(self):
        head = self.buildList([])

        result = self.solution.reverseList(head)

        expected = self.buildList([])
        self.assertListEqual(result, expected, "wrong reversed list")

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
