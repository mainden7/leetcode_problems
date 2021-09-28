# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n^2) O(1)
        n = len(height)
        max_area = 0
        for idx in range(n):
            for next_ in range(idx, n):
                area = min(height[idx], height[next_]) * (next_ - idx)
                max_area = max(max_area, area)
        return max_area

    def maxArea2(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        while True:
            if i == j:
                break
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area




if __name__ == "__main__":
    Solution().maxArea2(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
    Solution().maxArea2(height=[0, 1, 0, 1])
