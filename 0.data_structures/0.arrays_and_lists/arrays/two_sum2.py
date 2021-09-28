# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(numbers):
            t = target - num
            if t in d:
                return [d[t], i + 1]
            else:
                d[num] = i + 1
