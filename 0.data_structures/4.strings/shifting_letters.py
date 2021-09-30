# https://leetcode.com/problems/shifting-letters/
from typing import List
from string import ascii_lowercase


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sums_ = [sum(shifts[i:]) for i in range(len(shifts))]
        res = ""
        for idx, letter in enumerate(s):
            cur_index = ascii_lowercase.index(letter)
            shift = sums_[idx]
            new_index = shift + cur_index
            if new_index >= len(ascii_lowercase):
                new_index %= len(ascii_lowercase)
            res += ascii_lowercase[new_index]
        return res

    def shiftingLetters2(self, s: str, shifts: List[int]) -> str:
        res = ""
        sum_ = 0
        for idx, letter in enumerate(s[::-1]):
            shift = shifts[len(shifts) - 1 - idx]
            cur_index = ascii_lowercase.index(letter)
            shift += sum_
            sum_ = shift
            new_index = shift + cur_index
            if new_index >= len(ascii_lowercase):
                new_index %= len(ascii_lowercase)
            res += ascii_lowercase[new_index]
        return res[::-1]


if __name__ == "__main__":
    print(Solution().shiftingLetters("zzz", shifts=[1, 2, 3]))
