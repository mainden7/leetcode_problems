# https://leetcode.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()

        def twoSum(arr, t):
            d = {}
            ax = set()
            for idx, ele in enumerate(arr):
                if (t - ele) in d:
                    ax.add(tuple(sorted([ele, t - ele])))
                else:
                    d[ele] = idx
            return ax

        for idxa in range(len(nums) - 3):
            for idxb in range(idxa + 1, len(nums) - 2):
                part = target - (nums[idxa] + nums[idxb])
                for subres in twoSum(nums[idxb + 1 :], part):
                    result.add((nums[idxa], nums[idxb], *subres))
        return result


if __name__ == "__main__":
    print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
