# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3974/
import re


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        nc = re.findall(r"[^a-zA-Z]", s)
        i = 0
        j = len(s) - 1
        list_ = list(s)
        while i <= j:
            if list_[i] not in nc and list_[j] not in nc:
                list_[i], list_[j] = list_[j], list_[i]
                i += 1
                j -= 1
            else:
                if list_[i] in nc:
                    i += 1
                if list_[j] in nc:
                    j -= 1
        return "".join(list_)


if __name__ == "__main__":
    print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
