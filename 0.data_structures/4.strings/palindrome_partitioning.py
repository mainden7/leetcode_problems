# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3872/
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        cut = list(range(-1, size))
        for idx in range(1, size):
            for low, high in (idx, idx), (idx - 1, idx):
                while low >= 0 and high < size and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1
                    high += 1
        return cut[-1]


if __name__ == "__main__":
    print(Solution().minCut("ddccddbb"))
