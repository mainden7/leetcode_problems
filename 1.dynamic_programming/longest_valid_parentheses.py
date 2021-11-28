# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        max_length = 0
        for b in s:
            if b == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left * 2)
            if right > left:
                left = right = 0

        left = right = 0
        for b in s[::-1]:
            if b == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left * 2)
            if left > right:
                left = right = 0

        return max_length

    def longestValidParenthesesDP(self, s: str) -> int:
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)


if __name__ == "__main__":
    print(Solution().longestValidParentheses(s="())"))
