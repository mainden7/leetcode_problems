from typing import List


def solution(nums: List[int]) -> bool:
    sum_ = sum(nums)
    if sum_ % 2 != 0:
        return False
    target = sum_ // 2
    table = [False] * (target + 1)
    table[0] = True
    import pdb;pdb.set_trace()
    for num in nums:
        for i in range(target, num - 1, -1):
            if table[target]:
                return True
            table[i] = table[i] or table[i - num]
    return table[target]


if __name__ == '__main__':
    print(solution([1, 2, 3, 6]))