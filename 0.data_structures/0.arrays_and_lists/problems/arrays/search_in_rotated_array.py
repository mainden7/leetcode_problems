# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(list_, t):
            left = 0
            right = len(list_) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if t == list_[mid]:
                    return mid
                elif t < list_[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        pivot = adj = 0
        search_in = nums
        while pivot < len(nums) - 1:
            if nums[pivot] < nums[pivot + 1]:
                pivot += 1
                continue
            else:
                bigger = nums[: pivot + 1]
                smaller = nums[pivot + 1 :]
                if target > smaller[-1] and target < bigger[0]:
                    return -1
                if target < smaller[0] or target > bigger[-1]:
                    return -1
                if target > smaller[-1]:

                    search_in = bigger
                else:
                    adj = pivot + 1
                    search_in = smaller
                break
        idx = search(search_in, target)
        if idx != -1:
            return adj + idx
        else:
            return idx


if __name__ == "__main__":
    print(Solution().search(nums=[1], target=1))
    print(Solution().search(nums=[5, 1, 3], target=2))
