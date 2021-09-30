# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        i = 0
        j = len(s) - 1
        ls = list(s)
        while i < j:
            v1 = ls[i]
            v2 = ls[j]
            if v1 in vowels and v2 in vowels:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            else:
                if v1 not in vowels:
                    i += 1
                if v2 not in vowels:
                    j -= 1
        return "".join(ls)


if __name__ == "__main__":
    print(Solution().reverseVowels("hellou"))
