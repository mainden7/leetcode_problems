# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3888/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zeroes = set()
        col_zeroes = set()
        for row_idx in range(m):
            for col_idx in range(n):
                if matrix[row_idx][col_idx] == 0:
                    row_zeroes.add(row_idx)
                    col_zeroes.add(col_idx)
        for row_idx in range(m):
            if row_idx in row_zeroes:
                matrix[row_idx] = [0] * n
                continue
            for col_idx in col_zeroes:
                matrix[row_idx][col_idx] = 0
