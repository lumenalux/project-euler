"""
For a positive integer n define T(n) to be the number of strictly larger
integers which can be formed by permuting the digits of n.

Leading zeros are not allowed and so for $n = 2302$ the total list of
permutations would be:

  2023,2032,2203,2230,_2302_,2320,3022, 3202,3220

giving T(2302) = 4.

Further define S(k) to be the sum of T(n) for all k-digit numbers n.
You are given S(3) = 1701.

Find S(12).

link: https://projecteuler.net/problem=862

Solution:

The sum of T of all distinct digit numbers is just a arithmetic progression
that relates only to the length of sequence. So we can find the sum of T
using only the information about the length of the T sequence. If n = length
of T sequence, then the sum of T is:

    n * (n - 1) / 2

We can find the length of T sequence as distinct permutations of digits of a
multiset, using the formula:

    (k1 + k2 + ... + kn)! / (k1! * k2! * ... * kn!)

where k1, k2, ..., kn are the number of each digit in the multiset.

The only problem with zeros is that they can't be the first digit of a number,
so we need to subtract the number of sequences with zeros as the first digit
from the total number of sequences. Summing up all the sum of T for all
possible digit sequences we get the answer.
"""
import math

from itertools import combinations_with_replacement, islice
from collections import Counter


def distinct_permutations(K):
    return math.factorial(sum(K)) // math.prod(map(math.factorial, K))


def get_t_sequence_length(digits):
    count = Counter(digits)
    t_length = distinct_permutations(count.values())
    if 0 in count:
        t_length -= distinct_permutations((count - Counter([0])).values())
    return t_length


def sum_of_t(digits):
    n = get_t_sequence_length(digits)
    return n * (n - 1) // 2


def S(N):
    return sum(sum_of_t(digits)
               for digits in combinations_with_replacement(range(10), r=N))


def solution(N):
    return S(N)


if __name__ == '__main__':
    print(solution(3)) # 1701
    print(solution(12)) # 6111397420935766740
