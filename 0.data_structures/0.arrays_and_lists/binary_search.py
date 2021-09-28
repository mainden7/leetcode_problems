import random
import timeit
import typing as ty


def binary_search_recursive(
    list_: ty.List[int], element: int, m=0
) -> ty.Union[None, int]:
    if element > list_[-1] or element < list_[0]:
        return
    if len(list_) == 1:
        if list_[0] == element:
            return m
        else:
            return
    mid = len(list_) // 2
    if element == list_[mid]:
        return mid + m
    elif element < list_[mid]:
        return binary_search_recursive(list_[:mid], element, m)
    elif element > list_[mid]:
        m += mid
        return binary_search_recursive(list_[mid:], element, m)


def binary_search_iterative(
    list_: ty.List[int], element: int
) -> ty.Union[None, int]:
    if element > list_[-1] or element < list_[0]:
        return
    left = 0
    right = len(list_)
    while True:
        if left + 1 >= right:
            return
        mid = left + (right - left) // 2
        if element == list_[mid]:
            return mid
        elif element < list_[mid]:
            right = mid
        elif element > list_[mid]:
            left = mid

