# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3825/
import typing as ty
from utils import diff


def scan(d, fl):
    for ele in d:
        if ele.isdir():
            fl.extend(scan(ele, fl))
        fl.append(ele)
    return fl


def ds(g, node, visited, gc=None):
    if gc is None:
        gc = []

    visited.append(node)

    for w in g[node]:
        if w not in visited:
            ds(g, w, visited.copy(), gc)
    gc.append(visited)
    return gc


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: ty.List[str]
    ) -> ty.List[ty.List[str]]:

        if endWord not in wordList:
            return []
        ll = wordList
        ll.insert(0, beginWord)

        _G = {}
        for w in ll:
            _G[w] = []
            for j in ll:
                if j == w:
                    continue
                if len(diff(w, j)) == 1:
                    _G[w].append(j)

        aaa = ds(_G, beginWord, [])
        aaa = [i for i in aaa if i[0] == beginWord and i[-1] == endWord]
        ans = [i for i in aaa if len(i) == min(map(len, aaa))]
        print(ans)


if __name__ == "__main__":
    print(
        Solution().findLadders(
            "qa",
            "sq",
            [
                "si",
                "go",
                "se",
                "cm",
                "so",
                "ph",
                "mt",
                "db",
                "mb",
                "sb",
                "kr",
                "ln",
                "tm",
                "le",
                "av",
                "sm",
                "ar",
                "ci",
                "ca",
                "br",
                "ti",
                "ba",
                "to",
                "ra",
                "fa",
                "yo",
                "ow",
                "sn",
                "ya",
                "cr",
                "po",
                "fe",
                "ho",
                "ma",
                "re",
                "or",
                "rn",
                "au",
                "ur",
                "rh",
                "sr",
                "tc",
                "lt",
                "lo",
                "as",
                "fr",
                "nb",
                "yb",
                "if",
                "pb",
                "ge",
                "th",
                "pm",
                "rb",
                "sh",
                "co",
                "ga",
                "li",
                "ha",
                "hz",
                "no",
                "bi",
                "di",
                "hi",
                "qa",
                "pi",
                "os",
                "uh",
                "wm",
                "an",
                "me",
                "mo",
                "na",
                "la",
                "st",
                "er",
                "sc",
                "ne",
                "mn",
                "mi",
                "am",
                "ex",
                "pt",
                "io",
                "be",
                "fm",
                "ta",
                "tb",
                "ni",
                "mr",
                "pa",
                "he",
                "lr",
                "sq",
                "ye",
            ],
        )
    )
