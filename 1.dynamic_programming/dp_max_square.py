# https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        table = [
            [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]
        matrix = list(map(lambda j: list(map(int, j)), matrix))
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0:
                    table[x][y] = int(matrix[x][y])
                else:
                    if matrix[x][y] != 0:
                        table[x][y] = (
                            min(
                                table[x - 1][y],
                                table[x - 1][y - 1],
                                table[x][y - 1],
                            )
                            + 1
                        )
        return max([max(t) for t in table]) ** 2


if __name__ == "__main__":
    # mx = [
    #     ["1", "0", "1", "0", "0"],
    #     ["1", "0", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "0", "0", "1", "1"],
    # ]

    mx = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().maximalSquare(mx))
