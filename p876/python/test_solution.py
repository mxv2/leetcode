from unittest import TestCase
from p876.python.solution import Solution, ListNode


class TestSolution(TestCase):
    solution = Solution()

    def test_empty(self):
        head = self.buildList([])

        result = self.solution.middleNode(head)
        self.assertEqual(result, None, "wrong middle node")

    def test_1_node(self):
        head = self.buildList([1])

        result = self.solution.middleNode(head)
        self.assertEqual(result, ListNode(1), "wrong middle node")

    def test_2_nodes(self):
        head = self.buildList([1, 2])

        result = self.solution.middleNode(head)
        self.assertEqual(result, ListNode(2), "wrong middle node")

    def test_odd_length(self):
        head = self.buildList([1, 2, 3, 4, 5])

        result = self.solution.middleNode(head)
        self.assertEqual(result, ListNode(3), "wrong middle node")

    def test_even_length(self):
        head = self.buildList([1, 2, 3, 4, 5, 6])

        result = self.solution.middleNode(head)
        self.assertEqual(result, ListNode(4), "wrong middle node")

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
