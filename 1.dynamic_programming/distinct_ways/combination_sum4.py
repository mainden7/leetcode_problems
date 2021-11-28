# https://leetcode.com/problems/combination-sum-iv/
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if min(nums) > target:
            return 0
        nums = [n for n in nums if n <= target]
        row = [0] * (target + 1)
        for idx in range(1, target + 1):
            for numb in nums:
                if numb > idx:
                    continue
                elif numb == idx:
                    row[idx] += 1
                    continue
                else:
                    row[idx] = row[idx] + row[idx - numb]
        return row[-1]


if __name__ == "__main__":
    print(Solution().combinationSum4([1, 2, 3], 4))
    # print(
    #     Solution().combinationSum4(
    #         [
    #             3,
    #             4,
    #             5,
    #             6,
    #             7,
    #             8,
    #             9,
    #             10,
    #             11,
    #             12,
    #             13,
    #             14,
    #             15,
    #             16,
    #             17,
    #             18,
    #             19,
    #             20,
    #             21,
    #             22,
    #             23,
    #             24,
    #             25,
    #         ],
    #         10,
    #     )
    # )
