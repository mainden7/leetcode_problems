# https://leetcode.com/problems/dungeon-game/
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                elif i == m - 1:
                    dungeon[i][j] = max(dungeon[i][j + 1] - dungeon[i][j], 1)
                elif j == n - 1:
                    dungeon[i][j] = max(dungeon[i + 1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(
                        min(dungeon[i][j + 1], dungeon[i + 1][j])
                        - dungeon[i][j],
                        1,
                    )
        return dungeon[0][0]


if __name__ == "__main__":
    # dd = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    # dd = [[-3, 5]]
    # dd = [[2, 1], [1, -1]]
    dd = [[0, 0, 0], [1, 1, -1]]
    # dd = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    print(Solution().calculateMinimumHP(dd))
