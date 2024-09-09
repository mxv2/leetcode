from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other: object) -> bool:
        if other == None:
            return False

        return self.val == other.val

    def __str__(self) -> str:
        return f"({self.val})"

    def __repr__(self) -> str:
        return f"({self.val})"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        next = head.next
        head.next = None

        newHead = self.reverseList(next)
        next.next = head

        return newHead
