class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for letter in s:
            if letter == "1":
                ones += 1
            else:
                flips += 1

            flips = min(flips, ones)
        return flips


if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr("00011000"))
