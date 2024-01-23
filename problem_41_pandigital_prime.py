"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

link: https://projecteuler.net/problem=41

Solution:

The 2, 3, 5, 6, 8, 9 digit pandigitals has the sum of digits divisible by 3,
so they are not prime.

The only 4 and 7 digits pandigitals left. If we generate all permutations of
the digits 1 to n and create the number from them, the number would be
pandigital. We can check all the the permutations of the digits 1 to 7 and
1 to 4, and check if the number is prime. The largest prime number will be
the answer.
"""
import math

from itertools import islice, permutations

# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1 for i in range(1, n // 2) if sieve[i])]


def is_prime(n, primes):
    return all(n % prime for prime in islice(primes, 0, math.isqrt(n) + 1))


def solution():
    primes = sieve_of_eratosthenes(math.isqrt(10_000_000) + 1)
    return max(int(''.join(p))
               for r in (4, 7)
               for p in permutations('1234567'[:r], r)
               if is_prime(int(''.join(p)), primes))


# test
if __name__ == "__main__":
    print(solution())  # 7652413
