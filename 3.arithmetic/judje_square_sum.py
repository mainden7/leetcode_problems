import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(2, int(math.sqrt(c)) + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3



if __name__ == "__main__":
    print(Solution().judgeSquareSum(12132321))
