class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        arr = []
        arr.append(0)
        arr.append(1)
        arr.append(1)
        i = 2
        while i < n:
            arr.append(
                arr[-1] + arr[-2] + arr[-3]
            )
            i += 1
            arr = arr[-3:]

        return arr[-1]


if __name__ == '__main__':
    print(Solution().tribonacci(4))
