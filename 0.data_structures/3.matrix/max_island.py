# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def calc_square(x: int, y: int) -> int:
            queue = list()
            searched = set()
            queue.append((x, y))
            square = 0
            while queue:
                x, y = queue.pop(0)
                if (
                    (x, y) in searched
                    or x < 0
                    or x >= len(grid)
                    or y < 0
                    or y >= len(grid[0])
                ):
                    continue
                searched.add((x, y))
                visited.add((x, y))
                if grid[x][y] == 1:
                    square += 1
                else:
                    continue
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))

            return square

        max_square = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_square = max(max_square, calc_square(i, j))
        return max_square


if __name__ == "__main__":
    print(
        Solution().maxAreaOfIsland(
            grid=[
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
    )
