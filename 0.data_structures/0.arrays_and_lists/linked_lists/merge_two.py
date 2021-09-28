# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1
        if l1.next:
            if l1.next.val > l2.val:
                l1.next, l2 = l2, l1.next
        else:
            l1.next = l2
            return l1

        if l1.next and l2:
            self.merge_two_lists(l1.next, l2)
        return l1
