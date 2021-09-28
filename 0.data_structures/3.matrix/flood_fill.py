# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        queue = list()
        searched = set()
        queue.append((sr, sc))
        original_color = image[sr][sc]
        while queue:
            x, y = queue.pop(0)
            if (x, y) in searched:
                continue
            if (
                x < 0
                or x >= len(image)
                or y < 0
                or y >= len(image[0])
                or image[x][y] != original_color
            ):
                continue
            image[x][y] = newColor
            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))
            searched.add((x, y))
        return image


if __name__ == "__main__":
    print(
        Solution().floodFill(
            image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2
        )
    )
    print(Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
