# https://leetcode.com/problems/minimum-path-sum/


def brute_force(arr):
    cols = len(arr)
    rows = len(arr[0])
    ans = []

    def go(cur, x=0, y=0):
        if x + 1 == cols and y + 1 == rows:
            ans.append(cur)
        if x + 1 < cols:
            x += 1
            go(cur + arr[x][y], x, y)
            x -= 1
        if y + 1 < rows:
            y += 1
            go(cur + arr[x][y], x, y)
            y -= 1

    go(arr[0][0])
    return min(ans)


def dp(arr):
    aa = [[float("inf") for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if x == 0 and y == 0:
                aa[0][0] = arr[0][0]
            else:
                aa[x][y] = min(
                    arr[x][y] + aa[x - 1][y], arr[x][y] + aa[x][y - 1]
                )
    return aa[-1][-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # grid = [[1, 2], [1, 1]]
    # grid = [[1, 2, 3], [4, 5, 6]]
    print(dp(grid))
