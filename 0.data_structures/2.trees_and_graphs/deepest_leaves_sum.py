# https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = {}

        def traverse(tree, lvl=0):
            levels.setdefault(lvl, []).append(tree.val)
            if tree.left:
                traverse(tree.left, lvl + 1)
            if tree.right:
                traverse(tree.right, lvl + 1)

        traverse(root, 0)
        return sum(levels[max(levels.keys())])


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


if __name__ == "__main__":
    ans = Solution().deepestLeavesSum(
        from_list([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
    )
    print(ans)
