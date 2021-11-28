# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        row = [float("inf")] * len(nums)
        row[0] = 0
        for idx in range(len(nums)):
            for step in range(1, nums[idx] + 1):
                if idx + step < len(row):
                    row[idx + step] = min(
                        row[idx] + 1, row[idx + step - 1] + 1, row[idx + step]
                    )
        return row[-1]

    def jump2(self, nums):

        size = len(nums)

        # destination is last index
        destination = size - 1

        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0

        # counter for jump
        times_of_jump = 0

        # Quick response if start index == destination index == 0
        if size == 1:
            return 0

        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range(0, size):

            # extend current coverage as further as possible
            cur_coverage = max(cur_coverage, i + nums[i])

            # forced to jump (by lazy jump) to extend coverage
            if i == last_jump_index:

                # update last jump index
                last_jump_index = cur_coverage

                # update counter of jump by +1
                times_of_jump += 1

                # check if reached destination already
                if cur_coverage >= destination:
                    return times_of_jump

        return times_of_jump


if __name__ == "__main__":
    print(Solution().jump([2, 3, 0, 1, 4]))
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([1, 1, 1, 1, 4]))
