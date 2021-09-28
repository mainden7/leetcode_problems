https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                if val in rows[row]:
                    return False
                rows[row].add(val)
                
                if val in cols[col]:
                    return False
                cols[col].add(val)
                
                idx = (row // 3) * 3 + col // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True
