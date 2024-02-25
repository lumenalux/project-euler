"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less than
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

link: https://projecteuler.net/problem=23

Solution:

As seen on problem_021_amicable_numbers.py, we can use the same function to
calculate the sum of divisors of a number. So the task is to find all abundant
numbers and then sum all the numbers that can't be written as the sum of two
abundant numbers.
"""
import math

from itertools import islice
from collections import Counter


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n: int) -> list[int]:
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1
                                  for i in range(1, n // 2) if sieve[i])]


def factor_number(n: int, primes: list[int]) -> list[int]:
    factors = []
    for prime in islice(primes, 0, int(n**0.5) + 1):
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)

    return factors


def sum_of_divisors(n: int, primes: list[int]) -> int:
    return math.prod((p**(a + 1) - 1) // (p - 1)
                     for p, a in Counter(factor_number(n, primes)).items())


def solution(N: int) -> int:
    primes = sieve_of_eratosthenes(math.isqrt(N) + 1)
    abundant_numbers = [n for n in range(1, N + 1)
                        if sum_of_divisors(n, primes) - n > n]

    abundant_sums = set(n + k
                        for i, n in enumerate(abundant_numbers)
                        for k in abundant_numbers[i:] if k + n <= N)

    return N * (N + 1) // 2 - sum(abundant_sums)


# test
if __name__ == '__main__':
    print(solution(28123))  # 4179871
