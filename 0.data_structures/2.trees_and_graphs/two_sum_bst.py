# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3908/
from typing import Optional


def from_list(list_):
    # 2 * i + 1, 2 * i + 2
    for idx in range(len(list_)):
        if list_[idx] is None:
            list_.insert(2 * idx + 1, None)
            list_.insert(2 * idx + 2, None)

    def build(ls, i=0):
        if i >= len(ls) or ls[i] is None:
            return

        return TreeNode(
            ls[i], left=build(ls, i * 2 + 1), right=build(ls, i * 2 + 2)
        )

    tree = build(list_)
    return tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        d = {}
        while queue:
            ele = queue.pop(0)
            if not ele:
                continue
            if ele.val in d.values():
                return True

            d[ele.val] = k - ele.val
            queue.append(ele.left)
            queue.append(ele.right)
        return False

    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        q = [root]
        while q:
            root = q.pop(0)
            if k - root.val in s:
                return True
            s.add(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return False


if __name__ == "__main__":
    print(Solution().findTarget(from_list([5, 3, 6, 2, 4, None, 7]), 9))
