# Definition for a binary tree node.

from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, list_, root=None):
        for idx in range(len(list_)):
            if list_[idx] is None:
                list_.insert(2 * idx + 1, None)
                list_.insert(2 * idx + 2, None)

        def build(ls, i=0):
            if i >= len(ls) or ls[i] is None:
                return

            return cls(
                ls[i], left=build(ls, i * 2 + 1), right=build(ls, i * 2 + 2)
            )

        tree = build(list_)
        return tree

    def __repr__(self, level: int = 0):
        str_ = "   " * level
        str_ += f"Tree: {self.val}\n"
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)

        for ch in children:
            str_ += ch.__repr__(level + 1)
        return str_


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(tree, min_=float("inf"), max_=float("-inf")):
            if not tree:
                return True

            if tree.val <= max_ or tree.val >= min_:
                return False

            return traverse(
                tree.left, min_=min(min_, tree.val), max_=max_
            ) and traverse(tree.right, min_=min_, max_=max(tree.val, max_))

        return traverse(root)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.counter = {}
        self.max_ = 0

        def traverse(tree):
            if not tree:
                return

            self.counter[tree.val] = self.counter.get(tree.val, 0) + 1
            if self.counter[tree.val] > self.max_:
                self.res = [tree.val]
                self.max_ = self.counter[tree.val]
            elif self.counter[tree.val] == self.max_:
                self.res.append(tree.val)

            traverse(tree.left)
            traverse(tree.right)

        traverse(root)
        return self.res


if __name__ == "__main__":
    print(Solution().findMode(TreeNode.from_list([1, 0, 1, 0, 0, 1, 1, 0])))
