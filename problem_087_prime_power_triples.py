"""
The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

    28 = 2^2 + 2^3 + 2^4
    33 = 3^2 + 2^3 + 2^4
    49 = 5^2 + 2^3 + 2^4
    47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?

Link: https://projecteuler.net/problem=87
"""
import math

from itertools import takewhile, product


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n: int) -> list[int]:
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, math.isqrt(n) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1
                                  for i in range(1, n // 2) if sieve[i])]


def solution(N: int) -> int:
    primes = sieve_of_eratosthenes(math.isqrt(N) + 1)

    squares, cubes, fourths = ([*takewhile(N.__gt__, (i**n for i in primes))]
                               for n in (2, 3, 4))

    sums = (s + c + f for s, c, f in product(squares, cubes, fourths))
    return len(set(sum_ for sum_ in sums if sum_ < N))


# Test
if __name__ == '__main__':
    print(solution(50))          # 4
    print(solution(50_000_000))  # 1097343
