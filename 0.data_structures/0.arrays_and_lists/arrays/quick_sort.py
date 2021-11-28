import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # can also be a first element or a random
    pivot = arr[len(arr) // 2]
    eq = [ele for ele in arr if ele == pivot]
    less = [ele for ele in arr if ele < pivot]
    more = [ele for ele in arr if ele > pivot]
    return quick_sort(less) + eq + quick_sort(more)


def quick_sort_iterative(arr):
    if len(arr) < 2:
        return arr

    stack = list()
    stack.append(len(arr) - 1)
    stack.append(0)
    while stack:
        left = stack.pop()
        right = stack.pop()
        index = partition(arr, left, right)
        if left < index - 1:
            stack.append(index - 1)
            stack.append(left)
        if right > index + 1:
            stack.append(right)
            stack.append(index + 1)


def partition(arr, start, end):
    # Partition operation, return to baseline subscript
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # Now start = end
    arr[start] = pivot
    return start

