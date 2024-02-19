"""
Euler's totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.

link: https://projecteuler.net/problem=70

Solution:

For this function n/φ(n) we can see that the minimum value is achieved when
φ(n) is maximum. The maximum value of φ(n) is achieved when n is a prime
number.

But in our case if n is the prime than φ(n) is n - 1, and it is not
a permutation of n. So let's find the product of two primes, that satisfies
the conditions.

If we check all the pairs of primes, from 1 to 10^7, it will take too much
time. To reduce the search space we would iterate the primes that in product
are close to 10^7. Two primes would be close to √(N) ≈ 3162 for 10^7. To make
sure we will found the minimum of n/φ(n) we will include the primes which are
slightly bigger than N. In our case 50% more than √(N), and which are less
than our limit N in product.
"""
import math

from itertools import combinations


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(lower_limit, upper_limit):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((upper_limit + 1) // 2)
    for i in range(3, int(upper_limit**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, upper_limit // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    if upper_limit < 3:
        return []

    return [2, *(2*i + 1
                 for i in range(1, upper_limit // 2)
                 if sieve[i] and 2*i + 1 > lower_limit)]


def solution(N):
    ratio = 0.5

    upper_limit = int((1 + ratio) * math.sqrt(N))
    lower_limit = int((1 - ratio) * math.sqrt(N))
    primes = sieve_of_eratosthenes(lower_limit, upper_limit)

    n_phi_pairs = ((p * q, (p - 1) * (q - 1))
                   for p, q in combinations(primes, 2) if p * q < N)

    return min((n/phi, n) for n, phi in n_phi_pairs
               if sorted(str(n)) == sorted(str(phi)))[1]


# test
if __name__ == '__main__':
    print(solution(10_000_000))  # 8319823
