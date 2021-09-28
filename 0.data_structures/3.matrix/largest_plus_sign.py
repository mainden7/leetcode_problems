# https://leetcode.com/problems/largest-plus-sign/
from typing import List
from typing import Tuple
from itertools import product


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if n % 2 == 0:
            order = n // 2
        else:
            order = n // 2 + 1
        if order <= 0:
            return 0 if len(mines) == n ** 2 else 1
        while order > 0:
            coordinates = get_coordinates(order, n)
            for x, y in coordinates:
                rows = list(range(x - (order - 1), x + order))
                cols = list(range(y - (order - 1), y + order))
                mine = False
                for r in rows:
                    if [r, y] in mines:
                        mine = True
                        break
                if mine:
                    continue
                for c in cols:
                    if [x, c] in mines:
                        mine = True
                        break
                if mine:
                    continue
                return order
            order -= 1
        return order

    def orderOfLargestPlusSign2(self, n, mines):

        banned = {tuple(mine) for mine in mines}
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]

        return ans


def get_coordinates(order: int, size: int) -> List[Tuple[int, int]]:
    return list(
        product(
            range(order - 1, size - (order - 1)),
            range(order - 1, size - (order - 1)),
        )
    )


if __name__ == "__main__":
    print(Solution().orderOfLargestPlusSign(5, [[4, 2]]))
    # print(Solution().orderOfLargestPlusSign(2, [[0, 0], [0, 1], [1, 0]]))
    # print(
    #     Solution().orderOfLargestPlusSign(
    #         5,
    #         [
    #             [0, 0],
    #             [0, 1],
    #             [0, 2],
    #             [0, 3],
    #             [1, 0],
    #             [1, 1],
    #             [1, 2],
    #             [1, 3],
    #             [1, 4],
    #             [2, 2],
    #             [2, 4],
    #             [3, 0],
    #             [3, 2],
    #             [3, 3],
    #             [3, 4],
    #             [4, 0],
    #             [4, 1],
    #             [4, 2],
    #             [4, 3],
    #             [4, 4],
    #         ],
    #     )
    # )
