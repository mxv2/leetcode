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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        cur = prev.next
        while cur:
            if prev.val != cur.val:
                prev.next = cur
                prev = cur

            cur = cur.next

        prev.next = None

        return head
