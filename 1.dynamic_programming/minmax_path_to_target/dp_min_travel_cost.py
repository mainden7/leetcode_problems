# https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days) == 1:
            return min(costs)

        row = [0 for _ in range(max(days) + 1)]
        row[0] = 0
        for i in range(1, len(row)):
            if i not in days:
                row[i] = row[i - 1]
                continue
            row[i] = min(
                costs[0] + row[i - 1],
                costs[1] + (row[i - 7] if i - 7 >= 0 else 0),
                costs[2] + (row[i - 30] if i - 30 >= 0 else 0),
            )
        return row[-1]


if __name__ == "__main__":
    print(
        Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[7, 2, 15])
    )
    print(
        Solution().mincostTickets(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]
        )
    )
    print(
        Solution().mincostTickets(
            [
                1,  # 3   13
                4,  # 6   13
                6,  # 9   13
                9,  # 12  26
                10,  # 15
                11,  # 18
                12,  # 21
                13,  # 24
                14,  # 27
                15,  # 30  39
                16,  # 33
                17,  # 36
                18,  # 39
                20,  # 42
                21,  # 45
                22,  # 48  52
                23,  # 51  52
                27,  # 54  52
                28,  # 57  52
            ],
            [3, 13, 45],
        )
    )
