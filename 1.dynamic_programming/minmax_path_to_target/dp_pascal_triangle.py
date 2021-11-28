from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        tri = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            row = tri[-1]
            _row = [1]
            for place in range(1, i - 1):
                number = row[place - 1] + row[place]
                _row.insert(place, number)
            _row.append(1)
            tri.append(_row)

        return tri

    def generate2(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]

        row = [1]
        for i in range(0, rowIndex):
            row.append(
                int(row[i] * (rowIndex - i) / (i + 1))
            )
        return row


if __name__ == "__main__":
    print(Solution().generate2(10))
