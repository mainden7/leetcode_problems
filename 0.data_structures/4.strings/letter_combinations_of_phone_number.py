# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

characters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def backtrack(s, sub=""):
            if not s:
                if sub:
                    res.append(sub)
                return
            for char in list(characters[s[0]]):
                sub += char
                backtrack(s[1:], sub)
                sub = sub[:-1]

        backtrack(digits)
        return res


if __name__ == "__main__":
    print(Solution().letterCombinations("234"))
