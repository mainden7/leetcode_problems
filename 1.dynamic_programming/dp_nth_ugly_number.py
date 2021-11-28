# https://leetcode.com/problems/ugly-number-ii/submissions/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # TLE
        if n == 1:
            return n
        # row = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        row = [1, 2, 3]
        if n <= len(row):
            return row[n - 1]

        def is_ugly(number: int) -> bool:
            if number in row:
                return True
            return (
                (number % 2 == 0 and number // 2 in row)
                or (number % 3 == 0 and number // 3 in row)
                or (number % 5 == 0 and number // 5 in row)
            )

        for idx in range(len(row), n):
            i = 1
            while True:
                next_ = row[-1] + i
                if is_ugly(next_):
                    row += [next_]
                    break
                i += 1
        return row[-1]

    def nthUglyNumber2(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

    def nthUglyNumber3(self, n):
        ugly = sorted(
            2 ** a * 3 ** b * 5 ** c
            for a in range(32)
            for b in range(20)
            for c in range(14)
        )
        return ugly[n - 1]


if __name__ == "__main__":

    print(Solution().nthUglyNumber2(1690))
