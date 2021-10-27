# https://leetcode.com/problems/word-break-ii/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def split(str_, start=0, end=1, path=None):
            if path is None:
                path = list()

            if end > len(str_):
                res.append(" ".join(path))
                return

            while end <= len(str_):
                substr = s[start:end]
                if substr in wordDict:
                    path.append(substr)
                    split(str_, end, end + 1, path)
                    path.pop()
                end += 1

        split(s)
        return res


if __name__ == "__main__":
    # a = Solution().wordBreak(
    #     s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]
    # )
    a = Solution().wordBreak(s="abab", wordDict=["a", "b", "ab"])
    print(a)
