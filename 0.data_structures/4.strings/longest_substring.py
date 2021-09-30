class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 1
        ln = 0
        while True:
            if end + 1 > len(s):
                break

            if s[end] in s[start : end]:
                start += 1
                continue
            ln = max(ln, end - start)
            end += 1
        return ln + 1


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("bbbbbbbb"))
