# https://leetcode.com/problems/best-sightseeing-pair/
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0
        for v in values:
            res = max(res, cur + v)
            cur = max(cur, v) - 1
        return res


if __name__ == "__main__":
    print(Solution().maxScoreSightseeingPair([1, 3, 5]))
    print(Solution().maxScoreSightseeingPair([1, 2]))
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
