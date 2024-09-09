from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other: object) -> bool:
        if other == None:
            return False

        return self.val == other.val


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = None
        current = None

        while head:
            if val != head.val:
                if newHead == None:
                    newHead = head
                else:
                    current.next = head

                current = head

            head = head.next

        if current:
            current.next = None

        return newHead
