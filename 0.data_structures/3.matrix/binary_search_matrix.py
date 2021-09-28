# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(list_, t):
            left = 0
            right = len(list_) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if t == list_[mid]:
                    return True
                elif t < list_[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                return search(row, target)
        return False


if __name__ == "__main__":
    print(
        Solution().searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=1
        )
    )
