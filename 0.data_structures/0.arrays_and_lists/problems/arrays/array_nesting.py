from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = set()
        max_counter = 0
        for i in range(len(nums)):
            counter = 0
            while i < len(nums):
                num = nums[i]
                if num in s:
                    break
                i = num
                s.add(num)
                counter += 1
            max_counter = max(counter, max_counter)
        return max_counter
