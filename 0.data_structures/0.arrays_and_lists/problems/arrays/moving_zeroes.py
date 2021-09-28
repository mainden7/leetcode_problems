# https://leetcode.com/problems/move-zeroes/submissions/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)):
            idx = len(nums) - idx - 1
            if not nums[idx]:
                nums.append(nums.pop(idx))
