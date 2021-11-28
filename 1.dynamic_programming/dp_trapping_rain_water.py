# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        lm = rm = res = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] >= lm:
                    lm = height[i]
                else:
                    res += (lm - height[i])

                i += 1
            else:
                if height[j] >= rm:
                    rm = height[j]
                else:
                    res += (rm - height[j])

                j -= 1
        return res


if __name__ == "__main__":
    result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)
