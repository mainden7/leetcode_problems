# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self, level: int = 0):
        str_ = "   " * level
        str_ += f"Tree: {self.val}\n"
        chls = []
        if self.left:
            chls.append(self.left)
        if self.right:
            chls.append(self.right)
        for ch in chls:
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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestorIterative(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root


if __name__ == "__main__":
    print(
        Solution().lowestCommonAncestor(
            root=TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            p=TreeNode(4),
            q=TreeNode(11),
        )
    )
