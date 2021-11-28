# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        row = [0 for _ in range(n + 1)]
        row[0] = 0
        row[1] = 1
        row[2] = 2
        for i in range(3, n + 1):
            row[i] = row[i - 1] + row[i - 2]
        return row[-1]

if __name__ == "__main__":
    # 1 1 2 3 5
    print(Solution().climbStairs(4))
