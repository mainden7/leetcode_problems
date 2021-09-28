import typing as ty


class Solution:
    def partition_disjoint(self, nums: ty.List[int]) -> int:
        if len(nums) == 2:
            return 1

        max_left = None
        min_right = None
        for i in range(1, len(nums)):

            if max_left is None:
                max_left = nums[i - 1]
            else:
                max_left = max(max_left, nums[i - 1])
            if min_right is None or min_right == nums[i - 1]:
                min_right = min(nums[i:])

            if max_left > min_right:
                continue
            return i
