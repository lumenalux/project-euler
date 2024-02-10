"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are:

    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110

Therefore d(220) = 284. The proper divisors of 284 are:

    1, 2, 4, 71 and 142

So d(284) = 220.

Evaluate the sum of all the amicable numbers under n.

link: https://projecteuler.net/problem=21

Solution:

If the N is positive integer, then the N can be represented as a product of
prime numbers:

  n = p_1^a_1 * p_2^a_2 * ... * p_k^a_k,

where p_i are prime numbers and a_i are positive integers. The sum of
divisors of σ(n) can be calculated as:

  σ(n) = σ(p_1^a_1) * σ(p_2^a_2) * ... * σ(p_k^a_k),

The σ(p_i^a_i) can be calculated as the sum of geometric progression:

  σ(p_i^a_i) = 1 + p_i + p_i^2 + ... + p_i^a_i
  σ(p_i^a_i) = (p_i^(a_i + 1) - 1) / (p_i - 1)

Now since σ(n) is multiplicative, we have:

  σ(n) = σ(p_1^a_1) * σ(p_2^a_2) * ... * σ(p_k^a_k)
       = ∏((p_i^(a_i + 1) - 1) / (p_i - 1))

link: https://en.wikipedia.org/wiki/Divisor_function

We can use this formula to calculate the sum of divisors of any integer.
So we will calculate the sum of divisors of all numbers under N, then we
will find out all the amicable numbers.
"""
import math

from itertools import islice
from collections import Counter


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


def factor_number(n, primes):
    factors = []
    for prime in islice(primes, 0, int(n**0.5) + 1):
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)

    return factors


def sum_of_divisors(n, primes):
    return math.prod((p**(a + 1) - 1) // (p - 1)
                     for p, a in Counter(factor_number(n, primes)).items())


def solution(N):
    primes = sieve_of_eratosthenes(int(N**0.5) + 1)
    divisors_sums = {n: sum_of_divisors(n, primes) - n for n in range(2, N)}
    amicable_numbers = [n for n, d_sum in divisors_sums.items()
                        if n != d_sum
                        and d_sum in divisors_sums
                        and n == divisors_sums[divisors_sums[n]]]

    return sum(amicable_numbers)


# test
if __name__ == '__main__':
    print(solution(1000))  # 504
    print(solution(10_000))  # 31626
    print(solution(100_000))  # 852810
    print(solution(1_000_000))  # 25275024
