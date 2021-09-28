import random
import typing as ty


def bubble_sort(arr: ty.List[int]) -> ty.List[int]:
    count = 0
    for i in range(len(arr)):
        swaps = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
                count += 1
        if not swaps:
            break
    return arr

