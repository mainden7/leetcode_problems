# https://leetcode.com/problems/longest-palindromic-substring/
import re


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        longest_l, length = 1, 1
        for i in range(1, len(s)):
            odd_l, even_l, r = i - length - 1, i - length, i + 1
            odd, even = s[odd_l: r], s[even_l: r]
            print(f"{s=} {odd_l} {odd=}, {even_l=} {even=}, {i=}, {r=}")
            if odd_l >= 0 and odd == odd[::-1]:
                longest_l = odd_l
                length += 2
            elif even_l >= 0 and even == even[::-1]:
                longest_l = even_l
                length += 1

        return s[longest_l: longest_l + length]


if __name__ == "__main__":
    print(Solution().longestPalindrome("aacabdkacaa"))
