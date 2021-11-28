# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        row1 = [float("-inf") for _ in range(len(nums))]
        row2 = [float("-inf") for _ in range(len(nums))]
        row1[0] = nums[0]
        row2[0] = nums[0]
        for idx in range(1, len(nums)):
            row1[idx] = max(
                nums[idx],
                nums[idx] * nums[idx - 1],
                nums[idx] * row1[idx - 1],
                nums[idx] * row2[idx - 1],
            )
            row2[idx] = min(
                nums[idx] * row1[idx - 1],
                nums[idx] * row2[idx - 1],
                key=abs,
            )
        return max(row1)


if __name__ == "__main__":
    assert 4 == Solution().maxProduct([3, -1, 4])
    assert 2 == Solution().maxProduct([0, 2])
    assert 108 == Solution().maxProduct([-1, -2, -9, -6])
    assert 24 == Solution().maxProduct([-2, 3, -4])
    assert 0 == Solution().maxProduct([-2, 0, -1])
    assert 24 == Solution().maxProduct([2, -5, -2, -4, 3])
