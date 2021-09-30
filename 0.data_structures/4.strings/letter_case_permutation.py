# https://leetcode.com/problems/letter-case-permutation/
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = list()

        def make(string, i=0, sub=None):
            if sub is None:
                sub = string
            res.append(sub)
            if i == len(string):
                return res
            for i in range(i, len(string)):
                if not sub[i].isdigit():
                    ls = list(sub)
                    ls[i] = ls[i].upper() if ls[i].islower() else ls[i].lower()
                    make(string, i + 1, "".join(ls))
            return res

        return make(s)


if __name__ == "__main__":
    # print(Solution().letterCasePermutation("a1b2"))
    # print(Solution().letterCasePermutation("12345"))
    print(Solution().letterCasePermutation("0"))
    # print(Solution().letterCasePermutation("3z4"))
