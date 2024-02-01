"""
Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

link: https://projecteuler.net/problem=78

Solution:

It turns out that the number of partitions can be calculated using the
pentagonal number theorem:

    p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + p(n - 12) + ...

where the signs alternate between positive and negative, and the numbers
used are the generalized pentagonal numbers:

    gk = k(3k - 1) / 2, for n = 2k - 1
    gk = k(3k + 1) / 2, for n = 2k

We will use a dynamic programming approach to calculate the number of
partitions for each number, starting from 1. Once we find a number that is
divisible by one million, we return that number as the solution.
"""
from itertools import count, chain


def solution(mod=1_000_000):
    dp, sign = [1], (1, 1, -1, -1)
    gk = tuple(chain.from_iterable((k*(3*k - 1) // 2, k*(3*k + 1) // 2)
                                   for k in range(1, 200)))

    for n in count(1):
        pn, k = 0, 0
        while gk[k] <= n:
            pn += dp[n - gk[k]] * sign[k % 4]
            k += 1

        dp.append(pn % mod)
        if dp[n] == 0:
            return n


if __name__ == '__main__':
    print(solution()) # 55374
