# https://leetcode.com/problems/subarray-product-less-than-k/submissions/
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        if len(nums) == 1:
            return 1
        prod = 1
        counter = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k and left < len(nums):
                prod /= nums[left]
                left += 1
            counter += right - left + 1
        return counter
