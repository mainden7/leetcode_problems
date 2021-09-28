from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = ""
        node = self
        while node:
            s += f"{node.val}->"
            node = node.next
        return s


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if head.next is None:
            return
        node = head
        col = []
        while True:
            col.append(node)
            if node.next is None:
                if n == len(col):
                    return col[1]
                if n == 1:
                    next_ = None
                else:
                    next_ = col[-n + 1]
                col[-(n + 1)].next = next_
                break
            node = node.next
        return head
