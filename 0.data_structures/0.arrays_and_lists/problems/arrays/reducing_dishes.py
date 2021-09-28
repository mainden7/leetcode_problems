# https://leetcode.com/problems/reducing-dishes/
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        while sum(satisfaction) < 0:
            satisfaction.pop()
        total = 0
        ll = len(satisfaction)
        for i in range(ll):
            total += satisfaction[i] * (ll - i)
        return total


if __name__ == "__main__":
    print(Solution().maxSatisfaction([-1, -8, 0, 5, -9]))
