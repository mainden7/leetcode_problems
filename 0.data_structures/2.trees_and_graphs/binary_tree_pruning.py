import typing


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def prune_tree(self, root: TreeNode) -> typing.Union[None, TreeNode]:
        if not root:
            return None

        root.left = self.prune_tree(root.left)
        root.right = self.prune_tree(root.right)

        if not root.right and not root.left and not root.val:
            return None
        return root
