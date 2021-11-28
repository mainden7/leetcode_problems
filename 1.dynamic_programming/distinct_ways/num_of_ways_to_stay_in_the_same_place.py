# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
from functools import lru_cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        if arrLen == 1:
            return 1

        len_ = min(arrLen, steps + 1)
        row = [1] + [0] * (arrLen - 1)

        for step in range(1, steps + 1):
            old = 0
            for j in range(len_):
                old_left = old
                old = row[j]
                if j > 0:
                    row[j] += old_left
                if j < len_ - 1:
                    row[j] += row[j + 1]

        return row[0] % mod

    def numWaysRecursive(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        if arrLen == 1:
            return 1

        @lru_cache
        def go(move, idx):
            if move < 0 or idx < 0 or idx >= arrLen:
                return 0
            if idx == 0 and move == 0:
                return 1
            res = go(move - 1, idx - 1)
            if idx <= move:
                res += go(move - 1, idx + 1)
                res += go(move - 1, idx)
            return res

        return go(steps, 0) % mod


if __name__ == "__main__":
    print(Solution().numWays(3, 2))
