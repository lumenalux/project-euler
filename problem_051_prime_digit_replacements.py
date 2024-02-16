"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.

link: https://projecteuler.net/problem=51

Solution:

Let's generate all possible patterns for the prime numbers. For example:

    56003 -> *6003, 5*003, 560*3, 56*03, 56**3, 5600*,

Then we will count how many times each pattern appears. Then we will find the
first pattern that appears N times. Finally, we will replace the stars with
digits from 0 to 9 and first number which is prime will be the result.
"""
from itertools import product, islice

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


def generate_all_possible_patterns(number):
    number = list(str(number))
    indexes = {}
    for index, digit in enumerate(number):
        indexes.setdefault(digit, []).append(index)

    for digit, indexes in indexes.items():
        for comb in islice(product(range(2), repeat=len(indexes)), 1, None):
            pattern = number.copy()
            for i, index in enumerate(indexes):
                pattern[index] = '*' if comb[i] else digit
            yield ''.join(pattern)


def solution(N):
    primes = sieve_of_eratosthenes(1_000_000)
    count = {}
    suitable_pattern = None
    for prime in primes:
        for pattern in generate_all_possible_patterns(prime):
            count[pattern] = count.get(pattern, 0) + 1
            if count[pattern] >= N:
                suitable_pattern = pattern
                break
        if suitable_pattern:
            break

    if not suitable_pattern:
        return None

    primes_set = set(primes)
    for digit in range(0 if suitable_pattern[0] != '*' else 1, 10):
        prime = int(suitable_pattern.replace('*', str(digit)))
        if prime in primes_set:
            return prime


# test
if __name__ == '__main__':
    print(solution(6))  # 13
    print(solution(7))  # 56003
    print(solution(8))  # 121313
