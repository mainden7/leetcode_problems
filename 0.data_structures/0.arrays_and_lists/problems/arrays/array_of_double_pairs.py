# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3877/
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dict_ = dict()
        for ele in arr:
            dict_[ele] = dict_.get(ele, 0) + 1
        dict_ = {k: dict_[k] for k in sorted(dict_)}
        for k, v in dict_.items():
            if v == 0:
                continue
            if k == 0 and dict_[k] % 2 == 0:
                dict_[k] -= v
            elif k < 0:
                if k % 2 == 0 and k // 2 in dict_:
                    val = min(v, dict_[k // 2])
                    dict_[k // 2] -= val
                    dict_[k] -= val
            else:
                if k * 2 in dict_:
                    val = min(v, dict_[k * 2])
                    dict_[k * 2] -= val
                    dict_[k] -= val
        return all([v == 0 for v in dict_.values()])
