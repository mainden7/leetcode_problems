# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if nums[0] != 0:
            counter = {-nums[0]: 1, nums[0]: 1}
        else:
            counter = {0: 2}
        for i in range(1, len(nums)):
            temp = {}
            for key in counter:
                temp[key + nums[i]] = temp.get(key + nums[i], 0) + counter.get(
                    key, 0
                )
                temp[key - nums[i]] = temp.get(key - nums[i], 0) + counter.get(
                    key, 0
                )
            counter = temp
        return counter.get(target, 0)


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
