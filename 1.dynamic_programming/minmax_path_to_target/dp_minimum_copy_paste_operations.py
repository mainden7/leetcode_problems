# https://leetcode.com/problems/2-keys-keyboard/
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        row = [i for i in range(n + 1)]
        row[1] = 0
        for i in range(4, n + 1):
            half = i // 2
            for j in range(half, 1, -1):
                if i % j == 0:
                    row[i] = min(row[i], row[j] + i // j)

        print(row)
        return row[n]

    def minStepsRec(self, n):
        if n == 1:
            return 0

        def calc(y):
            i = 2
            while i <= y ** (1 / 2):
                if n % i == 0:
                    return i
                i += 1
            else:
                return 1

        mf = calc(n)
        if mf == 1:
            return n
        return mf + self.minSteps(n // mf)


if __name__ == "__main__":
    print(Solution().minSteps(21))
