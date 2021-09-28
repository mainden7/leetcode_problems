# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == len(nums):
                result.append(nums[:])

            for current in range(first, len(nums)):
                nums[first], nums[current] = nums[current], nums[first]
                backtrack(first + 1)
                nums[first], nums[current] = nums[current], nums[first]

        result = []
        backtrack(0)
        return result


if __name__ == "__main__":
    print(list(Solution().permute([1, 2, 3])))
