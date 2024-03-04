"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, ϕ(9)=6.

    n   Relatively Prime    φ(n)    n/φ(n)
    2   1                   1       2
    3   1,2                 2       1.5
    4   1,3                 2       2
    5   1,2,3,4             4       1.25
    6   1,5                 2       3
    7   1,2,3,4,5,6         6       1.1666...
    8   1,3,5,7             4       2
    9   1,2,4,5,7,8         6       1.5
    10  1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

link: https://projecteuler.net/problem=69

Solution:

The totient function can be found using the formula:

    φ(n) = n * ∏(p|n) (1 - 1/p)

    so the n/φ(n) ratio is:

    n/φ(n) = n / n * ∏(p|n) (1 - 1/p)
           = 1 / ∏(p|n) (1 - 1/p)
           = ∏(p|n) (1 / (1 - 1/p))
           = ∏(p|n) (p / (p - 1))

    where p is distinct prime factor of n.

You can see that the maximum value of n/φ(n) is achieved when the product
contains the largest number of distinct primes. So let's multiply primes
until the product exceeds the limit. This product will be the maximum value of
n/φ(n) for a given n. So the n with maximum n/φ(n) will be the product of
maximum distinct primes. We don't need too mach primes, because the product
will exceed the limit very fast. So we will use the first 20 primes.
"""

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71)


def solution(N: int) -> int:
    product = 1
    for p in PRIMES:
        if (next_product := product * p) > N:
            return product
        product = next_product
    return product


# test
if __name__ == '__main__':
    print(solution(10))         # 6
    print(solution(1_000_000))  # 510510
