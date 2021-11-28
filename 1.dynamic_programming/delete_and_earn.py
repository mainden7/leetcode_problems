# https://leetcode.com/problems/delete-and-earn/
import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = collections.Counter(nums)
        keys = sorted(list(counter.keys()))
        n = len(keys)
        row = [0, counter[keys[0]] * keys[0]]
        for i in range(1, n):
            if keys[i] > keys[i - 1] + 1:
                row = [row[1], row[1] + counter[keys[i]] * keys[i]]

            else:
                row = [row[1], max(row[1], row[0] + counter[keys[i]] * keys[i])]
        return row[1]

if __name__ == "__main__":
    print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
