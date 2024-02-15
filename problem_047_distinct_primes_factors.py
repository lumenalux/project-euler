"""
The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2^2 x  7 x 23
    645 = 3   x  5 x 43
    646 = 2   x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?

link: https://projecteuler.net/problem=47

Solution:

If the sequence of numbers is the length of N, then if we iterate with the step
of N - 1, then we will hit one of the numbers from the finding sequence. So if
the number has N distinct prime factors, then we need to additionally check
the 2*N - 1 number. With that knowledge let us start from the number N and
iterate until we find the sequence of numbers with N distinct prime factors.
"""
import math

from itertools import count
from collections import deque

# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1
                                  for i in range(1, n // 2) if sieve[i])]


def count_distinct_primes_divisors(n, primes):
    count = 0
    upper_limit = math.isqrt(n) + 1
    for prime in primes:
        if prime > upper_limit:
            break
        if n % prime == 0:
            count += 1
        while n % prime == 0:
            n //= prime
    if n > 1:
        count += 1

    return count


def get_valid_sequence(number, N, primes):
    first_sequence = ((i, count_distinct_primes_divisors(i, primes))
                      for i in range(number - N + 1, number))
    sequence = deque(first_sequence, maxlen=N)
    for i in range(number, number + N):
        sequence.append((i, count_distinct_primes_divisors(i, primes)))
        if all(count == N for _, count in sequence):
            return tuple(n for n, _ in sequence)
    return None


def solution(N):
    primes_limit_squared = 1000
    primes = sieve_of_eratosthenes(math.isqrt(primes_limit_squared) + 1)
    for number in count(N, step=N - 1):
        if number >= primes_limit_squared:
            primes_limit_squared *= 2
            primes = sieve_of_eratosthenes(
                math.isqrt(primes_limit_squared) + 1)

        if count_distinct_primes_divisors(number, primes) != N:
            continue

        sequence = get_valid_sequence(number, N, primes)
        if sequence is not None:
            return sequence[0]


# test
if __name__ == '__main__':
    print(solution(2))  # 14
    print(solution(3))  # 644
    print(solution(4))  # 134043
