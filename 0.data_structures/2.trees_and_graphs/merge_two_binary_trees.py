# https://leetcode.com/problems/merge-two-binary-trees/
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

    @classmethod
    def from_list(cls, list_):
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


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if any([not root1, not root2]):
            return root1 or root2

        def dfs(tree1, tree2):
            if not tree1 and not tree2:
                return

            val = (tree1.val if tree1 else 0) + (tree2.val if tree2 else 0)
            root = TreeNode(val=val)

            root.left = dfs(
                tree1.left if tree1 else None, tree2.left if tree2 else None
            )
            root.right = dfs(
                tree1.right if tree1 else None, tree2.right if tree2 else None
            )
            return root

        return dfs(root1, root2)

    def connect(self, root: "TreeNode") -> Optional["TreeNode"]:
        if not root:
            return None

        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


if __name__ == "__main__":
    # print(
    #     Solution().mergeTrees(
    #         root1=TreeNode.from_list([1, 3, 2, 5]),
    #         root2=TreeNode.from_list([2, 1, 3, None, 4, None, 7]),
    #     )
    # )
    # print(
    #     Solution().mergeTrees(
    #         root1=TreeNode.from_list([1]),
    #         root2=None,
    #     )
    # )
    print(Solution().connect(TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])))
