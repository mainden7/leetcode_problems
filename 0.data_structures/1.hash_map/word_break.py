# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    def word_break(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if dp[i - len(w)] and s[i - len(w) : i] == w:
                    dp[i] = True
        return dp[-1]



if __name__ == "__main__":
    Solution().word_break("aaaaaaa", ["aaaa", "aaa"])
