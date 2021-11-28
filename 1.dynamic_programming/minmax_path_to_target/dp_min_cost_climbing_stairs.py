# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        row = [float("inf") for _ in range(len(cost))]
        row.append(0)
        cost.append(0)
        row[0] = cost[0]
        row[1] = cost[1]
        for i in range(2, len(row)):
            row[i] = min(cost[i] + row[i - 1], cost[i] + row[i - 2])
        return row[-1]



if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(
        Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    )
