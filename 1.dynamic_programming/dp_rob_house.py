# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        row = [0] * len(nums)
        for i in range(len(nums)):
            row[i] = max(nums[i] + row[i - 2], row[i - 1])
        return row[-1]


if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))
