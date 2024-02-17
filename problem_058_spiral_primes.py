"""
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

link: https://projecteuler.net/problem=58

Solution:

We can use the same formula from problem_028_number_spiral_diagonals.py to
calculate the sum of numbers on diagonals in an N by N spiral formed in the
same way. We will check if the number is prime or not and get our
statistic for the ratio of primes along both diagonals.
"""
import math

PRIMES_LIMIT = 30_000


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


def is_prime(n, primes):
    if n < PRIMES_LIMIT:
        return n in primes
    limit = math.isqrt(n) + 1
    for p in primes:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True


def solution(ratio):
    primes = dict.fromkeys(sieve_of_eratosthenes(PRIMES_LIMIT), None)
    primes_count = 3
    n = 5
    while primes_count / (2*n - 1) >= ratio:
        primes_count += sum(is_prime(n*(n - i) + i, primes) for i in range(4))
        n += 2
    return n


# test
if __name__ == '__main__':
    print(solution(0.1))  # 26241
