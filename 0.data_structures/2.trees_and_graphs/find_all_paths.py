# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        paths = []

        def traverse(idx, path=None):
            if path is None:
                path = [idx]

            if n in path:
                paths.append(path.copy())
                return

            for node in graph[idx]:

                traverse(node, path + [node])

        traverse(0)
        return paths


if __name__ == "__main__":
    print(
        Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []])
    )
