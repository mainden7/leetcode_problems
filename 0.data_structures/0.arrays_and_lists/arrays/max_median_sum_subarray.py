from typing import List
from statistics import median

# divide given array on k parts such that sum of median of these partitions
# will be maximum and return that sum


def max_median_sum_array(arr: List[int], k: int, max_sum=float("-inf")) -> int:
    if not arr:
        return 0
    if k == 1:
        return median(arr)
    if k == len(arr):
        return sum(arr)
    print(arr[: len(arr) - k + 1], arr[len(arr) - k + 1 :])
    return median(arr[: len(arr) - k + 1]) + sum(arr[len(arr) - k + 1 :])


if __name__ == "__main__":
    print(max_median_sum_array([1, 2, 3, 4, 5], 3))
