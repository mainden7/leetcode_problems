# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
from typing import List


class Solution:
    def minOperations2(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == "1":
                    count += abs(j - i)
            arr.append(count)
        return arr

    def minOperations3(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            sub = []
            if i > 0:
                sub2 = list(map(lambda x: x - 1, arr[i - 1].copy()))
                arr.append(sub2)
            else:
                for j in range(len(boxes)):
                    if boxes[j] == "1":
                        sub.append(abs(j - i))
                arr.append(sub)
        return list(map(sum, [list(map(abs, ele)) for ele in arr]))

    def minOperations(self, boxes: str) -> List[int]:
        sum_ = sum(i for i, v in enumerate(boxes) if v == '1')
        res = []
        count = boxes.count('1')
        for b in boxes:
            res.append(sum_)
            if b == '1':
                count -= 2
            sum_ -= count
        return res


if __name__ == "__main__":
    print(Solution().minOperations("001011"))
