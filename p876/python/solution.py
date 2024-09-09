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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
