"""
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

link: https://projecteuler.net/problem=5

Solution:

The number should include all the prime factors of the
numbers from 1 to 20. So we can just factor them out,
then find minimum number of each factor. And then get
our answer by multiplying them all together.
"""

from collections import Counter

# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    if n <= 2:
        return []

    sieve = [True] * n
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = [False] * len(sieve[i*i:n:i])  # Set multiples of i to False

    return [i for i, prime in enumerate(sieve) if prime]


def factorize(n):
    factors = []
    prime_candidates = sieve_of_eratosthenes(int(n**0.5) + 1)
    for prime in prime_candidates:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)

    return factors


def solution(n):
  min_factors = {}
  for factors in [Counter(factorize(i)) for i in range(1, n + 1)]:
      for factor, count in factors.items():
          min_factors[factor] = max(min_factors.get(factor, 0), count)

  result = 1
  for factor, count in min_factors.items():
      result *= factor ** count
  return result


# test
if __name__ == '__main__':
    print(solution(10)) # 2520
    print(solution(20)) # 232792560
