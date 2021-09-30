import re
from typing import List


class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str],
    ) -> str:
        ss = list(s)
        aa = list(zip(indices, sources, targets))
        aa.sort(key=lambda x: x[0], reverse=True)
        for idx, source, target in (
            aa
        ):
            import pdb;pdb.set_trace()
            n = len(source)
            if source == "".join(ss[idx:(idx + n)]):
                del ss[idx:(idx + n)]
                ss.insert(idx, target)

        return "".join(ss)


if __name__ == "__main__":
    print(
        Solution().findReplaceString(
            "vmokgggqzp",
            [3, 5, 1],
            ["kg", "ggq", "mo"],
            ["s", "so", "bfr"],
        )
    )
