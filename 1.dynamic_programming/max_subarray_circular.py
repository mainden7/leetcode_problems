# https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def row_max(row):
            if len(row) == 1:
                return row[0]
            subrow = [float("-inf") for _ in range(len(row))]
            subrow[0] = row[0]
            for idx in range(1, len(row)):
                subrow[idx] = max(row[idx], row[idx] + subrow[idx - 1])
            return max(subrow)

        mm = float("-inf")
        for idx in range(len(nums)):
            mm = max(mm, row_max(nums[idx:] + nums[:idx]))
        return mm


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]))
