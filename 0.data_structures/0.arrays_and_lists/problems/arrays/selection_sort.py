import random
import typing as ty


def selection_sort(list_: ty.List[int]) -> ty.List[int]:
    # O(n^2)
    nl = []

    while True:
        if not list_:
            break
        max_, idx = 0, 0
        for i in range(len(list_)):
            if list_[i] > max_:
                max_ = list_[i]
                idx = i
        nl.append(max_)
        del list_[idx]
    return nl


if __name__ == "__main__":
    print(selection_sort([random.randint(0, 100) for _ in range(100)]))
