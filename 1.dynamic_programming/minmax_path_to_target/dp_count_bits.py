from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        bits = [0, 1]

        for i in range(2, n + 1):
            bits.append(bits[i // 2] + bits[i % 2])

        return bits


if __name__ == "__main__":
    print(Solution().countBits(3))
