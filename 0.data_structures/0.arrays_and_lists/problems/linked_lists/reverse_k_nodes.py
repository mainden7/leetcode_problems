# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    @classmethod
    def from_list(cls, list_):
        head = node = ListNode(0)
        while list_:
            node.next = ListNode(list_[0])
            list_ = list_[1:]
            node = node.next
        return head.next


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next


if __name__ == "__main__":
    print(Solution().reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5]), k=2))
