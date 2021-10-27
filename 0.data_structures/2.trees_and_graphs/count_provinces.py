# https://leetcode.com/problems/number-of-provinces/submissions/
from typing import List


def out_of_bounds(x, grid):
    return x < 0 or x > len(grid) - 1


def explore_province(x, grid):
    if out_of_bounds(x, grid):
        return
    for y in range(len(grid)):
        if grid[x][y] == 1:
            grid[x][y] = "*"
            grid[y][x] = "*"
            explore_province(y, grid)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    provinces += 1
                    explore_province(i, isConnected)
        return provinces


if __name__ == "__main__":
    print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
