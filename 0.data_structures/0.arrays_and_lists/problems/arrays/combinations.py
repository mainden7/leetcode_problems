# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = list(range(1, n + 1))

        def make(list_, com=None, res=None):
            if com is None:
                com = []
            if res is None:
                res = []
            if len(com) == k:
                res.append(com.copy())
                return

            for idx, ele in enumerate(list_):
                com.append(ele)
                make(list_[idx + 1 :], com.copy(), res)
                com = com[:-1]
            return res

        return make(ls)

    def combine_iterative(self, n: int, k: int) -> List[List[int]]:
        ls = tuple(range(1, n + 1))
        n = len(ls)
        if k > n:
            return []
        indices = list(range(k))
        yield tuple(ls[i] for i in indices)
        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1
            yield tuple(ls[i] for i in indices)


if __name__ == "__main__":
    print(list(Solution().combine_iterative(4, 2)))
