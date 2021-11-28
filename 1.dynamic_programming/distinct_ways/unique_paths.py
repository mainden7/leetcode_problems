# https://leetcode.com/problems/unique-paths
# https://leetcode.com/problems/unique-paths-ii
import math
from functools import lru_cache
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        table = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 and j > 0) or (j == 0 and i > 0):
                    table[i][j] = 1
                else:
                    table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[-1][-1]

    def uniquePathTopDown(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        @lru_cache
        def topdown(x: int, y: int) -> int:
            if x == 0 and y == 0:
                return 0
            if x == 0 or y == 0:
                return 1
            return topdown(x - 1, y) + topdown(x, y - 1)

        return topdown(m - 1, n - 1)

    def uniquePathMath(self, m: int, n: int) -> int:
        return (
            math.factorial(m + n - 2)
            // math.factorial(m - 1)
            // math.factorial(n - 1)
        )

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0 and j > 0:
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0 and i > 0:
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = (
                        0
                        if obstacleGrid[i][j] == 1
                        else obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    )
        return obstacleGrid[-1][-1]


if __name__ == "__main__":
    # print(Solution().uniquePaths(3, 7))
    # print(
    #     Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    # )
    print(Solution().uniquePathTopDown(3, 7))
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePathMath(3, 7))
