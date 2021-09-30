# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3871/
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Tree {self.val} -> {self.children if self.children else ''}"


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        lvl = {
            0: [root.val],
        }

        def traverse(level, children):
            if not children:
                return
            lvl.setdefault(level, []).extend([c.val for c in children])
            for ch in children:
                traverse(level + 1, ch.children)

        traverse(1, root.children)
        return list(lvl.values())


if __name__ == "__main__":
    tree14 = Node(14)
    tree13 = Node(13)
    tree12 = Node(12)
    tree11 = Node(11)
    tree10 = Node(10)
    tree9 = Node(9)
    tree8 = Node(8)
    tree7 = Node(7)
    tree6 = Node(6)
    tree5 = Node(5)
    tree4 = Node(4)
    tree3 = Node(3)
    tree2 = Node(2)
    tree1 = Node(1)

    tree11.children = [tree14]
    tree7.children = [tree11]
    tree8.children = [tree12]
    tree9.children = [tree13]
    tree5.children = [tree9, tree10]
    tree3.children = [tree7, tree6]
    tree4.children = [tree8]
    tree1.children = [tree2, tree3, tree4, tree5]

    print(Solution().levelOrder(tree1))
