# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        row = [0 for _ in range(len(nums))]
        row[0] = nums[0]
        for i in range(1, len(nums)):
            row[i] = max(nums[i], nums[i] + row[i - 1])

        return max(row)


if __name__ == "__main__":
    ns = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(ns))
