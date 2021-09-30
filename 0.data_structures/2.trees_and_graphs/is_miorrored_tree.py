from typing import Optional


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        levels = dict()
        def traverse(tree, level=0):
            levels.setdefault(level, []).append(tree.val)
            if tree.left:
                traverse(tree.left, level + 1)
            else:
                levels.setdefault(level + 1, []).append(None)
            if tree.right:
                traverse(tree.right, level + 1)
            else:
                levels.setdefault(level + 1, []).append(None)

        for lvl, vals in levels.items():
            if lvl == 0:
                continue
            n = len(vals) // 2
            if len(vals) % 2 != 0 or vals[:n] != vals[n:][::-1]:
                return False
        return True


if __name__ == "__main__":
    print(
        Solution().isSymmetric(TreeNode.from_list([1, 2, 2, None, 3, None, 3]))
    )
