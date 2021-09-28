# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/
from typing import List


def combs(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(3))

    ans = {}
    x = [pool[i] for i in indices]
    if sum(x) == r:
        return r
    else:
        ans[sum(x)] = x

    while True:
        for i in reversed(range(3)):
            if indices[i] != i + n - 3:
                break
        else:
            break
        indices[i] += 1
        for j in range(i + 1, 3):
            indices[j] = indices[j - 1] + 1
        x = [pool[i] for i in indices]
        if sum(x) == r:
            return r
        else:
            ans[sum(x)] = x

    less = [k for k in ans.keys() if k < r]
    more = [k for k in ans.keys() if k > r]

    if not less:
        return min(more)
    if not more:
        return max(less)
    if r - max(less) < min(more) - r:
        return max(less)
    else:
        return min(more)


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        return combs(nums, target)
