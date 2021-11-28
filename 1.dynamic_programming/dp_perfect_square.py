# https://leetcode.com/problems/perfect-squares/


class Solution:
    # def numSquares(self, n: int) -> int:
    #     row = [float('inf') for _ in range(n + 1)]
    #     ps = [i ** 2 for i in range(1, int(n ** (1 / 2)) + 1)]
    #     print(ps)
    #     row[0] = 0
    #     row[1] = 1
    #     for i in range(2, n + 1):
    #         # import pdb;pdb.set_trace()
    #         for p in ps[::-1]:
    #             if p > i:
    #                 continue
    #             row[i] = min(row[i], row[i - p] + 1)
    #     print(row)
    #     return row[-1]

    def numSquares(self, n: int) -> int:
        x = n ** 0.5
        if x == int(x):
            return 1
        x = n
        while x % 4 == 0:
            x //= 4
        if x % 8 == 7:
            return 4
        i = 1
        while i * i < n:
            x = n - i * i
            y = x ** 0.5
            if y == int(y):
                return 2
            i += 1
        return 3


if __name__ == "__main__":
    print(Solution().numSquares())
