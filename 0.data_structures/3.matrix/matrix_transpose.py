from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = matrix[j][i]
    
    return res


if __name__ == "__main__":
    print(transpose_matrix(
        [[1, 2, 3], [4, 5, 6]]
    ))
        

