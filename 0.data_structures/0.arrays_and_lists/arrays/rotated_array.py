# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/617/week-5-august-29th-august-31st/3958/
# Find Minimum in Rotated Sorted Array
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def div(arr):
            if len(arr) == 1:
                return arr[0]

            if arr[-1] > arr[0]:
                return arr[0]
            n = len(arr) // 2
            left = arr[:n]
            right = arr[n:]
            arr = left
            if right[0] < left[-1] or right[0] > right[-1]:
                arr = right

            return div(arr)

        return div(nums)
