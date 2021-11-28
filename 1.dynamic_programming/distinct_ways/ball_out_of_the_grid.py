# https://leetcode.com/problems/out-of-boundary-paths/
from functools import lru_cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10 ** 9 + 7
        if maxMove == 0:
            return 0
        grid = [[0] * n for _ in range(m)]
        grid[startRow][startColumn] = 1
        count = 0
        for move in range(1, maxMove + 1):
            for i in range(m):
                tmp = [[0] * n for _ in range(m)]
                for j in range(n):
                    if i == m - 1:
                        count = (count + grid[i][j]) % mod
                    if j == n - 1:
                        count = (count + grid[i][j]) % mod
                    if i == 0:
                        count = (count + grid[i][j]) % mod
                    if j == 0:
                        count = (count + grid[i][j]) % mod

                    tmp[i][j] = (
                        (
                            (grid[i - 1][j] if i > 0 else 0)
                            + (grid[i + 1][j] if i < (m - 1) else 0)
                        )
                        % mod
                        + (
                            (grid[i][j - 1] if j > 0 else 0)
                            + (grid[i][j + 1] if j < (n - 1) else 0)
                        )
                        % mod
                    ) % mod
                    print(tmp)
                grid = tmp
        return count

    def findPathsRecursive(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10 ** 9 + 7

        @lru_cache
        def go(move, i, j):
            if move < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            return (
                go(move - 1, i - 1, j)
                + go(move - 1, i + 1, j)
                + go(move - 1, i, j - 1)
                + go(move - 1, i, j + 1)
            )

        return go(maxMove, startRow, startColumn) % mod


if __name__ == "__main__":
    print(Solution().findPathsRecursive(2, 2, 2, 0, 0))
