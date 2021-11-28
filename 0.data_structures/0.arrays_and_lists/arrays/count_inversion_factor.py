from typing import List


def count_inversion(nums: List[int]):
    if len(nums) == 0:
        return 0

    def merge_and_count(left, right, count=0):
        out = [min(left), min(right)]
        if min(left) < min(right):
            pass


    mid = len(nums) // 2
    A = nums[:mid]
    B = nums[mid:]
    rA, A = count_inversion(A)
    rB, B = count_inversion(B)
    r, L = merge_and_count(A, B)
    return rA + rB + r, L

if __name__ == '__main__':
    count_inversion([2, 4, 1, 3, 5])