from typing import List
from typing import Tuple


def is_possible_to_place(
    board: List[List[str]], coors: Tuple[int, int], target: str
) -> bool:
    """Checks if it is possible to place given number at goven place in the board"""
    # check row
    row, col = coors
    if target in board[row]:
        return False
    # check column
    if target in [board[r][col] for r in range(len(board))]:
        return False

    # and finally check square
    row_sq = row // 3 * 3
    col_sq = col // 3 * 3
    for i in range(row_sq, row_sq + 3):
        for j in range(col_sq, col_sq + 3):
            if board[i][j] == target:
                return False
    return True


def solve_sudoku(board: List[List[str]]) -> None:
    """"""
    # queue = set([(i, j) for i in range(9) for j in range(9) if board[i][j] == "."])
    queue = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                queue.append((i, j))

    def solve():
        if not queue:
            return True

        i, j = queue.pop()
        if board[i][j] == ".":
            for number in range(1, 10):
                if is_possible_to_place(board, (i, j), str(number)):
                    board[i][j] = str(number)
                    if solve():
                        return True
                    board[i][j] = "."
        queue.append((i, j))
        return False

    solve()
    return board


if __name__ == "__main__":
    ans = solve_sudoku(
        board=[
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
    )

    assert ans == [
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
    for a in ans:
        print(a)
