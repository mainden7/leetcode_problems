class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()
        indexes = dict()
        for idx, l in enumerate(s):
            counter[l] = counter.get(l, 0) + 1
            indexes.setdefault(l, idx)
        for k, v in counter.items():
            if v == 1:
                return indexes[k]
        return -1
