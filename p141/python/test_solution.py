from unittest import TestCase
from p141.python.solution import Solution, ListNode


class TestSolution(TestCase):
    solution = Solution()

    def test_no_cycle_1(self):
        head = self.buildList([1], -1)

        result = self.solution.hasCycle(head)
        self.assertEqual(result, False, "wrong answer")

    def test_no_cycle_2(self):
        head = self.buildList([1, 2], -1)

        result = self.solution.hasCycle(head)
        self.assertEqual(result, False, "wrong answer")

    def test_cycle_2(self):
        head = self.buildList([1, 2], 0)

        result = self.solution.hasCycle(head)
        self.assertEqual(result, True, "wrong answer")

    def test_cycle_4(self):
        head = self.buildList([3, 2, 0, -4], 1)

        result = self.solution.hasCycle(head)
        self.assertEqual(result, True, "wrong answer")

    def buildList(self, nums, pos):
        head = None
        current = None
        cycleNode = None
        for i, n in enumerate(nums):
            node = ListNode(n)

            if pos == i:
                cycleNode = node

            if head == None:
                head = node

            if current != None:
                current.next = node

            current = node

        if cycleNode != None:
            current.next = cycleNode
            
        return head
