# https://leetcode.com/problems/number-of-enclaves/
from typing import List


def explore(grid, x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        if min(x, y) < 0 or x > len(grid[0]) - 1 or y > len(grid) - 1:
            continue

        if grid[y][x] == 1:
            grid[y][x] = -1

            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m <= 2 or n <= 2:
            return 0
        x, y, dx, dy = 0, 0, 1, 0
        while True:
            if x + dx == n or y + dy == m or x + dx < 0:
                dx, dy = -dy, dx
            print(x, y)
            if (x, y) == (9, 5):
                print("AAAAAAAAA")
            if grid[y][x] == 1:
                explore(grid, x, y)
            if x + dx == 0 and y + dy == 0:
                break
            x += dx
            y += dy

        counter = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    counter += 1
        return counter


if __name__ == "__main__":

    # print(
    #     Solution().numEnclaves(
    #         grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    #     )
    # )
    print(
        Solution().numEnclaves(
            grid=[
                [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            ]
        )
    )
