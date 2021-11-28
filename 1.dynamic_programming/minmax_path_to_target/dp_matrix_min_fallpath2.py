# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr) == 1:
            return min(arr[0])

        # take two lowest values from first row
        row_min = sorted(enumerate(arr[0]), key=lambda x: x[1])[:2]
        for row in range(1, len(arr)):
            result_row = []
            # take two lowest values from current row
            cur_ror_min = sorted(enumerate(arr[row]), key=lambda x: x[1])[:2]

            # pair rows and calculate sum for those which indices are not equal
            # and save two lowest results with different indices
            for idx, val in cur_ror_min:
                tmp = []
                for prev_idx, prev_val in row_min:
                    if prev_idx == idx:
                        continue
                    tmp.append((idx, prev_val + val))
                result_row.append(min(tmp, key=lambda x: x[1]))
            # reinitialize previous row as current row
            row_min = result_row
        return min(row_min, key=lambda x: x[1])[1]


if __name__ == "__main__":
    print(
        Solution().minFallingPathSum(
            [
                [-37, 51, -36, 34, -22],
                [82, 4, 30, 14, 38],
                [-68, -52, -92, 65, -85],
                [-49, -3, -77, 8, -19],
                [-60, -71, -21, -62, -73],
            ]
        )
    )
    # print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
