# https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, l1: ListNode, l2: ListNode, m: int = 0
    ) -> ListNode:
        if not l1.next and not l2.next:
            x = l1.val + l2.val + m
            if x >= 10:
                x -= 10
                return ListNode(val=x, next=ListNode(val=1))
            else:
                return ListNode(val=x)

        if not l1.next:
            l1.next = ListNode(val=0)
        if not l2.next:
            l2.next = ListNode(val=0)
        x = l1.val + l2.val + m
        m = 0
        if x >= 10:
            x -= 10
            m = 1
        l1.val = x
        l1.next = self.add_two_numbers(l1.next, l2.next, m)
        return l1
