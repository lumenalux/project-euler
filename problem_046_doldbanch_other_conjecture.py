"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

    9 = 7 + 2*1^2
    15 = 7 + 2*2^2
    21 = 3 + 2*3^2
    25 = 7 + 2*3^2
    27 = 19 + 2*2^2
    33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

link: https://projecteuler.net/problem=46

Solution:

If the composite number is c, then the prime number is p, and the square number
is s, then:

    c = p + 2s^2 => s^2 = (c - p) / 2

So if (c - p)/2 isn't a square number, then the conjecture is false. We need to
find the smallest c that satisfies this condition. For efficient finding of
primes and composites we will use the sieve of Eratosthenes. If we didn't find
the smallest c, we will increase the limit of the sieve and go from the last
composite number we iterated over.
"""
import math


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return sieve


def get_next_primes_composites(last_composite):
    sieve = sieve_of_eratosthenes(last_composite * 2)
    primes = [2, *(2*i + 1 for i in range(1, last_composite) if sieve[i])]
    composites = [2*i + 1
                  for i in range(1, last_composite)
                  if not sieve[i] and 2*i + 1 > last_composite]
    return primes, composites


def is_sqrt(n):
    return math.isqrt(n)**2 == n


def solution():
    composites = [9]
    while True:
      primes, composites = get_next_primes_composites(composites[-1])
      for composite in composites:
          for prime in primes:
              if composite <= prime - 2:
                  return composite
              if is_sqrt((composite - prime) // 2):
                  break


# test
if __name__ == '__main__':
    print(solution()) # 5777
