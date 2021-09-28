# https://leetcode.com/problems/3sum/
from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3 or (len(nums) == 3 and sum(nums) != 0):
            return []

        counter = Counter(nums)
        nums = list(counter.keys())

        ans = set()

        if counter[0] >= 3:
            ans.add((0, 0, 0))
        pos, neg = [x for x in nums if x > 0], [x for x in nums if x < 0]

        for a in neg:
            for b in pos:
                c = -(a + b)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    ans.add((sorted([a, b, c])))
        return list(ans)
