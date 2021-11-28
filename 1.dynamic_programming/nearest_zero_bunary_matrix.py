# https://leetcode.com/problems/01-matrix/submissions/
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[float("inf")] * len(mat[0]) for _ in range(len(mat))]

        for i in range(len(res)):
            for j in range(len(res[0])):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i - 1][j] + 1, res[i][j])
                    if j > 0:
                        res[i][j] = min(res[i][j - 1] + 1, res[i][j])

        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res[0]) - 1, -1, -1):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i < len(res) - 1:
                        res[i][j] = min(res[i + 1][j] + 1, res[i][j])
                    if j < len(res[0]) - 1:
                        res[i][j] = min(res[i][j + 1] + 1, res[i][j])

        return res


if __name__ == "__main__":
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
