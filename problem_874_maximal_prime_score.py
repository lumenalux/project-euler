"""
Let p(t) denote the (t + 1)-th prime number. For example:

    p(0) = 2, p(1) = 3, etc.

We defined the prime score of a list of nonnegative integers
[a_1, ..., a_n] as the sum Σp(a_i).

Let M(k, n) be the maximal prime score among all lists [a_1, ..., a_n]
such that:

    *  0 <= a_i < k for each i
    *  the sum Σp(a_i) is a multiple of k

For example, M(2, 5) = 14 as [0, 1, 1, 1, 1] attains a maximal prime score
of 14.

Find M(7000, p(7000)).

link: https://projecteuler.net/problem=874

Solution:

Let's see what the maximal prime score for M(n, p(n)) looks like for small
values of n:

    M(2, p(2))   = M( 2,  5) -> [2, 3, 3, 3, 3]                     -> 14
    M(3, p(3))   = M( 3,  7) -> [3, 5, 5, 5, 5, 5, 5]               -> 33
    M(4, p(4))   = M( 4, 11) -> [2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]   -> 72
    M(5, p(5))   = M( 5, 13) -> [3,  11, 11, 11, ... , 11, 11, 11]  -> 135
    M(6, p(6))   = M( 6, 17) -> [2,  13, 13, 13, ... , 13, 13, 13]  -> 210
    M(7, p(7))   = M( 7, 19) -> [13, 13, 17, 17, ... , 17, 17, 17]  -> 315
    M(8, p(8))   = M( 8, 23) -> [2,  17, 17, 19, ... , 19, 19, 19]  -> 416
    M(9, p(9))   = M( 9, 29) -> [13, 13, 23, 23, ... , 23, 23, 23]  -> 657
    M(10, p(10)) = M(10, 31) -> [2,  17, 29, 29, ... , 29, 29, 29]  -> 860

We can see the clear pattern in the maximal prime score for M(n, p(n)) that
the most of the numbers are the prime numbers p(n - 1). The distinct numbers
of primes would be at most 2 if n is odd and at most 3 if n is even.

If n is even, the maximal prime score should contain the 2 because the p(n) is
odd, and if we add odd number of odd numbers we would get an odd number, so we
need to add even number to sum of even number of odd number to get even number,
that is multiple of even number. The only one even prime number is 2. So the
maximal prime score if n is even should always contain the 2.

There are two cases to consider what maximal prime score should be:

    For n is odd:
        M(n, p(n)) = p(n - 1) * i + p(m) * (p(n) - i)
        where 0 < m <= n - 1 and 0 < i < p(n)

    For n i even:
        M(n, p(n)) = p(n - 1) * i + p(m) * (p(n) - i - 1) + 2
        where 0 < m <= n - 1 and 0 < i < p(n) - 1

To reduce the number of iterations, let's consider the limit of the maximal
prime score. The maximal prime score should be less than or equal:

    For n is odd:
        p(n) * p(n - 1).

    For n is even:
        (p(n) - 1) * p(n - 1) + 2.

The limit - score < n, there are no need to iterate further, as the minimal
distance between the next maximal prime score is n, but it will exceed the
limit. So we can stop the iteration and return the maximal prime score.

The last thing is the prime limit for the Sieve of Eratosthenes algorithm.
The Rosser's theorem states that:

    log(n) + log(log(n)) - 1 < Pn / n < log(n) + log(log(n)), for n >= 6

    => Pn < n(log(n) + log(log(n))), for n >= 6

So the we will get the prime limit

P.S.

Why is the 4992764000 the maximal prime score for M(7000, p(7000))?

The 7000 is even, so the maximal prime score should contain the 2. There are
p(7000) = 70663 numbers. This score can be achieve by:

    70657 * 70610 + 70639 * 52 + 2 = 4992764000

The limit is:

    (70663 - 1) * 70657 + 2 = 4992764936

The difference between the limit and the maximal prime score is 936, which
is less than 7000. If there was a maximal prime score greater than 4992764000,
it should be at least be 4992764000 + 7000 = 4992771000, but the maximal sum
we can achieve that is even would be the max prime times the max length - 1
plus 2 (because the sum should be even) which is 4992764936. But the greater
maximal prime score is 4992771000, which already exceeds the limit, so the
4992764000 is the maximal prime score for M(7000, p(7000)).
"""
from math import log, ceil

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


def solution(k):
    prime_limit = 14 if k < 6 else ceil(k * (log(k) + log(log(k))))
    primes = sieve_of_eratosthenes(prime_limit)

    n, c, m = primes[k], 0, 0
    if k % 2 == 0:
        n, c, m = n - 1, 2, k - 2

    b = primes[k-1]
    max_sum = 0
    limit = b * n + c
    for a in primes[k-1::-1]:
        for i in range(1, n + 1):
            new_sum = b * (n - i) + a * i
            if new_sum % k == m:
                max_sum = max(max_sum, new_sum + c)
                break
        if limit - max_sum < k:
            return max_sum
    return max_sum


# Test
if __name__ == '__main__':
    print(solution(2))    # 14
    print(solution(7000)) # 4992764000
