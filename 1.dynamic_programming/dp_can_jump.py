# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        row = [0] * len(nums)
        row[0] = nums[0]
        for i in range(1, len(nums)):
            if row[i - 1] == 0:
                return False
            row[i] = max(row[i - 1] - 1, nums[i])

        return True

    def canJump2(self, nums) -> bool:
        moves = 0
        for idx, j in enumerate(nums):
            if idx > moves:
                return False
            moves = max(moves, idx + j)
        return True


if __name__ == "__main__":

    assert Solution().canJump([2, 3, 1, 1, 4])
    assert not Solution().canJump([3, 2, 1, 0, 4])
    assert not Solution().canJump([0, 1])
