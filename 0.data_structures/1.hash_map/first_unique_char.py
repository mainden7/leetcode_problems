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

    def first_unique_char(self, s: str) -> int:
        arr = [0] * 26
        for ch in s:
            idx = ord(ch) - ord("a")
            arr[idx] += 1
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if arr[idx] == 1:
                return i

        return -1



if __name__ == "__main__":
    print(Solution().first_unique_char("aaaaaaaaaaabaaaaaaaabc"))
    print(Solution().firstUniqChar("aaaaaaaaaaabaaaaaaaabc"))
