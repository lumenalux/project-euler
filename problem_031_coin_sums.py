"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?

link: https://projecteuler.net/problem=31

Solution:

Nothing special, just a classic dynamic programming problem.

If you are not familiar with dynamic programming, you can read about it in
chapter 9 of the book "Grokking Algorithms" by Aditya Bhargava.
link: https://livebook.manning.com/book/grokking-algorithms/chapter-9/1
"""
from functools import lru_cache


COINS = (1, 2, 5, 10, 20, 50, 100, 200)


@lru_cache(maxsize=max(COINS))
def recursive_solution(N: int, start: int = 0) -> int:
    return sum(recursive_solution(N - COINS[i], i)
               for i in range(start, len(COINS)) if COINS[i] <= N) if N else 1


def solution(N: int) -> int:
    dp = [0] * (N + 1)
    dp[0] = 1
    for coin in COINS:
        for i in range(coin, N + 1):
            dp[i] += dp[i - coin]
    return dp[N]


if __name__ == '__main__':
    print(solution(200))            # 73682
    print(recursive_solution(200))  # 73682
