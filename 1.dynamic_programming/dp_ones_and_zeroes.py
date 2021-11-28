# https://leetcode.com/submissions/detail/532650143/
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    table[i][j] = max(
                        1 + table[i - zeros][j - ones], table[i][j]
                    )
        return table[-1][-1]


if __name__ == "__main__":
    print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 3, 4))
    # print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    # print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
    # print(Solution().findMaxForm(["00", "000"], 1, 10))
