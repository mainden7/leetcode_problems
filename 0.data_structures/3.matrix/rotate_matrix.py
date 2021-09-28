import typing as ty


def rotate(matrix: ty.List[ty.List[int]]) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = (
                matrix[i][n - j - 1],
                matrix[i][j],
            )


if __name__ == '__main__':
    N = 4
    x = 0
    M = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            M[a][b] = x
            x += 1
    for r in M:
        print(r)
    print("*" * 80)
    rotate(M)
