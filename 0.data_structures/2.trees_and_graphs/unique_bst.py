# Definition for a binary tree node.
from math import factorial
from typing import List
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
    def generateTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n) ** 2 // (n + 1)

    def generateTrees2(self, n: int) -> List[Optional[TreeNode]]:
        if n < 1:
            return []
        cache = {}

        def generate(first, last):
            if first > last:
                return [None]
            if (first, last) in cache:
                return cache[first, last]
            trees = []
            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += (node,)
            cache[first, last] = trees
            return trees

        return generate(1, n)


if __name__ == "__main__":
    # print(TreeNode(1, left=TreeNode(0), right=TreeNode(3, left=TreeNode(2))))
    for tr in Solution().generateTrees2(3):
        print(tr)
