# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from typing import List


class Master:
    def guess(self, word: str) -> bool:
        return len([(i, j) for (i, j) in zip("acckzz", word) if i == j])


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        print(master.guess(wordlist[1]))


if __name__ == "__main__":
    print(
        Solution().findSecretWord(
            wordlist=["acckzz", "ccbazz", "eiowzz", "abcczz"], master=Master()
        )
    )
