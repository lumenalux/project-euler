""""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2  =   0.5
    1/3  =   0.(3)
    1/4  =   0.25
    1/5  =   0.2
    1/6  =   0.1(6)
    1/7  =   0.(142857)
    1/8  =   0.125
    1/9  =   0.(1)
    1/10 =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.

link: https://projecteuler.net/problem=26

Solution:

We can just find all the length of the recurring cycle of the unit fraction
1/d and return the d of the maximum one. But we can go further and reduce
the search space by observing that the length of the recurring cycle of 1/md
can not be larger than length of 1/d, where m is an integer. So we need to
proceed only the prime numbers.
"""


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


def get_length_of_recurring_cycle(d):
    remainder_index = {}
    remainder, index = 1, 0
    while remainder and remainder not in remainder_index:
        remainder_index[remainder] = index
        remainder = (remainder * 10) % d
        index += 1
    return index - remainder_index.get(remainder, 0)


def solution(N):
    primes = sieve_of_eratosthenes(N)
    return max(primes, key=get_length_of_recurring_cycle)


if __name__ == "__main__":
    print(solution(10))  # 7
    print(solution(1000))  # 983
    print(solution(10_000))  # 9967
