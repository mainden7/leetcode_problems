# https://leetcode.com/problems/last-stone-weight-ii/
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for a in stones:
            dp = {a + x for x in dp} | {abs(a - x) for x in dp}
        return min(dp)


if __name__ == "__main__":
    # print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
    print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
