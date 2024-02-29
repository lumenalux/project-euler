"""
Triangle, pentagonal, and hexagonal numbers are generated by the following
formula:

    Triangle:   Tn=n(n+1)/2   1, 3, 6, 10, 15, ...
    Pentagonal: Pn=n(3n-1)/2  1, 5, 12, 22, 35, ...
    Hexagonal:  Hn=n(2n-1)    1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

link: https://projecteuler.net/problem=45

Solution:

The hexagonal numbers are a subset of the triangular numbers:

    Hn = Tk
    n(2n-1) = k(k+1)/2
    2n(2n-1) = k(k+1)
    k = 2n - 1

So if we have the nth hexagonal number, this number would be the kth
triangular number, where k = 2n - 1

In previous problem problem_044_pentagon_numbers.py we found that the number is
pentagonal if and only if:

    sqrt(24n + 1) % 6 == 5

Combining all of that we will get the solution.
"""
import math

from itertools import count


def is_pentagonal(n: int) -> int:
    return math.sqrt(24 * n + 1) % 6 == 5


def solution():
    for n in count(144):
        hexagonal = n * (2 * n - 1)
        if is_pentagonal(hexagonal):
            return hexagonal


# test
if __name__ == '__main__':
    print(solution())  # 1533776805
