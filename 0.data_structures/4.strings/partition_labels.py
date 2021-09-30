# https://leetcode.com/problems/partition-labels/
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = defaultdict(lambda: (float("inf"), float("-inf")))
        for idx, letter in enumerate(s):
            index[letter] = (
                min(idx, index[letter][0]),
                max(idx, index[letter][1]),
            )
        partitions = []
        start, end = float("inf"), float("-inf")
        for idx, letter in enumerate(s):
            start, end = min(start, index[letter][0]), max(
                end, index[letter][1]
            )
            if idx == end:
                partitions.append(end - start + 1)
                start, end = float("inf"), float("-inf")
        return partitions


if __name__ == "__main__":
    print(Solution().partitionLabels(""))
