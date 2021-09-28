from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[True] * 9 for _ in range(9)]
        col = [[True] * 9 for _ in range(9)]
        sub = [[True] * 9 for _ in range(9)]
        to_add = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = int(board[i][j]) - 1
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = False
                else:
                    to_add.append((i, j))

        def backtrack():
            if not to_add:
                return True
            i, j = to_add.pop()
            for d in range(9):
                if row[i][d] and col[j][d] and sub[i // 3 * 3 + j // 3][d]:
                    board[i][j] = str(d + 1)
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = False
                    if backtrack():
                        return True
                    board[i][j] = "."
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = True
            to_add.append((i, j))
            return False

        backtrack()


if __name__ == "__main__":
    grid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    output = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    Solution().solveSudoku(grid)
