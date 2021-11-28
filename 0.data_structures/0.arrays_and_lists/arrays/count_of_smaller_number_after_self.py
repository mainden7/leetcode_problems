# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def insert(self, ele):








class Solution:

    def countSmaller(self, nums):
        tree = TreeNode(nums[0])
        for i in nums[1:]:
            tree.insert(i)



if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))
