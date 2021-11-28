# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(list_):
            row = [0] * len(list_)
            row[0] = list_[0]
            row[1] = max(list_[0], list_[1])
            for i in range(2, len(list_)):
                row[i] = max(row[i - 1], list_[i] + row[i - 2])

            return row[-1]

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))


if __name__ == "__main__":
    print(Solution().rob([2, 3, 4, 5]))
    print(Solution().rob([2, 3, 2]))
    print(Solution().rob([1, 2, 3, 10]))
    print(Solution().rob([200, 3, 140, 20, 10]))
