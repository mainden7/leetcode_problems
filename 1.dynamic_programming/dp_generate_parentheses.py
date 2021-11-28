# https://leetcode.com/problems/generate-parentheses/
from itertools import combinations, permutations
from typing import List


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def make_tree(m, val, sm=None, lvl=0):
    sums = list(range(1, m)) + list(range(m, -1, -1))
    ml = m * 2 - 1
    if sm is None:
        sm = 0
    if sm + val < 0 or sm + val > sums[lvl]:
        return
    if lvl + 1 == ml:
        return Tree(val, left=Tree(val=-1))
    return Tree(
        val=val,
        left=make_tree(m, -1, sm + val, lvl=lvl + 1),
        right=make_tree(m, 1, sm + val, lvl=lvl + 1),
    )


def traverse(root) -> List[str]:
    allPath = []
    if root is None:
        return []
    find_all_paths_recursive(root, [], allPath)
    return allPath


def find_all_paths_recursive(currNode, currPath, allPath):
    if currNode is None:
        return
    currPath.append(currNode.val)
    if currNode.left is None and currNode.right is None:
        allPath.append(currPath[::])
    find_all_paths_recursive(currNode.left, currPath, allPath)
    find_all_paths_recursive(currNode.right, currPath, allPath)
    del currPath[-1]


def swap(item):
    res = []
    for i in item:
        cc = "(" if i == 1 else ")"
        res.append(cc)
    return "".join(res)


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
        # if n == 1:
        #     return ["()"]
        # # sums = list(range(1, n)) + list(range(n, -1, -1))
        #
        # tree = make_tree(n, 1)
        # tree.display()
        # return list(map(swap, traverse(tree)))
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for j in range(1, n + 1):
            for i in range(j):
                for x in dp[i]:
                    for y in dp[j - i - 1]:
                        dp[j] += ["(" + x + ")" + y]
                        print(dp)
        return dp[-1]
    # def generateParenthesis(self, n: int) -> List[str]:
    #     stack = []
    #     res = []
    #
    #     def back(openN, closeN):
    #         print(openN, closeN, stack, res)
    #         if openN == closeN == n:
    #             res.append(''.join(stack))
    #         if openN < n:
    #             stack.append('(')
    #             back(openN + 1, closeN)
    #             stack.pop()
    #         if closeN < openN:
    #             stack.append(')')
    #             back(openN, closeN + 1)
    #             stack.pop()
    #
    #     back(0, 0)
    #     return res


if __name__ == "__main__":
    a = 3
    sol = Solution().generateParenthesis(a)
    print(sol)
    if a == 4:
        exp = [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
        for e in exp:
            if e not in sol:
                print(e)
