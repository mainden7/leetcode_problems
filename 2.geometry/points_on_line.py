import typing as ty


class Solution:
    def max_points(self, points: ty.List[ty.List[int]]) -> int:
        if len(points) == 1:
            return 1
        if all([abs(p[0] - p[1]) == 0 for p in points]):
            return len(points)

        formulas = {}
        max_ = 0
        for idx, pair in enumerate(points):
            for pair2 in points[idx + 1 :]:
                try:
                    a = (pair2[1] - pair[1]) / (pair2[0] - pair[0])
                    b = pair[1] - a * pair[0]
                    f = f"y={a}x + {b}"
                except ZeroDivisionError:
                    f = f"x={pair[0]}"

                if f not in formulas.keys():
                    formulas[f] = [pair, pair2]
                    max_ = max(max_, 2)
                else:
                    if pair not in formulas[f]:
                        formulas[f].append(pair)
                    if pair2 not in formulas[f]:
                        formulas[f].append(pair2)
                    max_ = max(max_, len(formulas[f]))

        return max_


if __name__ == "__main__":
    ans = Solution().max_points([[0, 1], [0, 0]])
    assert ans == 2
