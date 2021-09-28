# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3887/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [[strs[0]]]
        dict_ = {}
        for word in strs:
            transformed_word = "".join(sorted(word))
            if transformed_word in dict_:
                dict_[transformed_word].append(word)
            else:
                dict_[transformed_word] = [word]
        return list(dict_.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(Solution().groupAnagrams(["asda"]))
