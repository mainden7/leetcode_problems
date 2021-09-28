# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(arr, v, x=0):
            if v < arr[0] or v > arr[-1]:
                return -1
            if len(arr) == 1:
                return -1 if arr[0] != v else x
            mid = len(arr) // 2
            if v == arr[mid]:
                return mid + x
            elif v < arr[mid]:
                return search(arr[:mid], v, x)
            else:
                return search(arr[mid:], v, x + mid)

        idx = search(nums, target)
        if idx == -1:
            return [-1, -1]
        i = j = idx
        while True:
            if (
                i == 0
                and j + 1 == len(nums)
                or (nums[i] != target and nums[j] != target)
                or (nums[i] != target and j + 1 == len(nums))
                or (nums[j] != target and i == 0)
            ):
                if nums[i] != target:
                    i += 1
                if nums[j] != target:
                    j -= 1
                break
            if nums[i] == target and i > 0:
                i -= 1
            if nums[j] == target and j + 1 < len(nums):
                j += 1

        return [i, j]


if __name__ == "__main__":
    print(Solution().searchRange([1, 2, 3, 4, 10, 11, 12], 10))
