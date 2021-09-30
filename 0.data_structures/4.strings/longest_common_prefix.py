import typing as ty


class Solution:
    def longest_common_prefix(self, strs: ty.List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        for z in zip(*strs):
            if len(set(z)) == 1:
                prefix += z[0]
            else:
                break

        return prefix
