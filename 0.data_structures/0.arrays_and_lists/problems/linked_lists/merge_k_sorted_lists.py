# https://leetcode.com/problems/merge-k-sorted-lists
from typing import List
from typing import Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    @classmethod
    def from_list(cls, list_: List[int]) -> "ListNode":
        prev = None
        head = None
        while list_:
            node = ListNode(list_.pop(0))
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
        return head


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if len(lists) < 2:
            return lists[0] if lists else lists

        def merge(a, b):
            if a.val > b.val:
                a, b = b, a
            head = a
            while a and b:
                if a.next:
                    if a.next.val > b.val:
                        a.next, b = b, a.next
                else:
                    a.next = b
                    break
                a = a.next
            return head

        queue = [lists.pop(0), lists.pop(0)]
        while len(queue) >= 2:
            l1 = queue.pop(0)
            l2 = queue.pop(0)
            if l1 and l2:
                res = merge(l1, l2)
                queue.append(res)
            else:
                queue.append(l1 if l1 else l2)
            if lists:
                queue.append(lists.pop(0))
        return queue[0] if queue else None

    def mergeKLists2(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        queue = []
        # fake node
        head = point = ListNode(0)
        for list_ in lists:
            if list_:
                heapq.heappush(queue, list_)
        while queue:
            node = heapq.heappop(queue)
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(queue, node)
        return head.next


if __name__ == "__main__":
    print(
        Solution().mergeKLists2(
            [
                ListNode.from_list([1, 4, 5]),
                ListNode.from_list([1, 3, 4]),
                ListNode.from_list([2, 6]),
            ]
        )
    )
