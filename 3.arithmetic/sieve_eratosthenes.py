import math
from typing import List


def sieve(max_val: int) -> List[bool]:
    flags = [1] * (max_val + 1)
    flags = list(map(bool, flags))
    prime = 2

    while prime <= math.sqrt(max_val):
        flags = cross_of(flags, prime)
        prime = get_next_prime(flags, prime)

    return flags


def cross_of(flags, prime) -> List[bool]:
    i = prime * prime
    while True:
        if i >= len(flags):
            break
        flags[i] = False
        i += prime

    return flags


def get_next_prime(flags, prime) -> int:
    next_ = prime + 1
    while next_ < len(flags) and not flags[next_]:
        next_ += 1

    return next_


if __name__ == '__main__':
    fl = sieve(131)
    print(fl[131])



