# https://leetcode.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [
            [float("inf") for _ in range(len(triangle[-1]))]
            for _ in range(len(triangle))
        ]
        dp[0][0] = triangle[0][0]
        for row_idx in range(1, len(triangle)):
            for idx in range(len(triangle[row_idx])):
                dp[row_idx][idx] = min(
                    triangle[row_idx][idx] + dp[row_idx - 1][idx],
                    triangle[row_idx][idx] + dp[row_idx - 1][idx - 1],
                )

        return min(dp[-1])


if __name__ == "__main__":
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
