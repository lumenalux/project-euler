"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?

link: https://projecteuler.net/problem=56
"""
from itertools import product


def solution():
    return max(sum(map(int, str(a ** b)))
               for a, b in product(range(100), repeat=2))


# test:
if __name__ == '__main__':
    print(solution())  # 972
