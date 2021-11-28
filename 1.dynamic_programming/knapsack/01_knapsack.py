from typing import List


def solution(values: List[int], weights: List[int], weight: int) -> int:
    # get the item with min weight
    items = sorted(zip(values, weights), key=lambda x: x[1])
    table = [[float("-inf")] * (weight + 1) for _ in range(len(values))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            item = items[i]
            v, w = item
            if j < w:
                table[i][j] = table[i - 1][j]
                continue
            table[i][j] = max(
                table[i][j - 1], table[i - 1][j], v, v + table[i - 1][j - w]
            )
    return int(table[-1][-1])


if __name__ == "__main__":
    solution([60, 100, 120], [10, 20, 30], 50)
