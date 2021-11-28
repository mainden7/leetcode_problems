# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])

        table = [
            [float("inf") for _ in range(len(matrix[0]))]
            for _ in range(len(matrix))
        ]
        table[0] = matrix[0]
        for row in range(1, len(table)):
            for col in range(len(table[0])):
                table[row][col] = min(
                    matrix[row][col] + table[row - 1][col - 1]
                    if col - 1 >= 0
                    else float("inf"),
                    matrix[row][col] + table[row - 1][col],
                    matrix[row][col] + table[row - 1][col + 1]
                    if col + 1 < len(table[0])
                    else float("inf"),
                )
        return min(table[-1])


if __name__ == "__main__":
    # print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
