# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(list_, k, idx=0):
            if k > list_[-1]:
                return idx + len(list_)
            elif k < list_[0]:
                return idx
            else:
                mid = len(list_) // 2
                if k < list_[mid]:
                    list_ = list_[:mid]
                elif k > list_[mid]:
                    list_ = list_[mid:]
                    idx += mid
                else:
                    return idx + mid
            return search(list_, k, idx)

        return search(nums, target)


if __name__ == "__main__":
    print(Solution().searchInsert([1, 2, 4, 6, 8, 9, 10], 10))
