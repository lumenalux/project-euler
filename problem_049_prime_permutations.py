"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

link: https://projecteuler.net/problem=49

Solution:

For the sequence p1, p2, p3 we have:

    p2 - p1 = d, p3 - p2 = d => p3 - p2 = p2 - p1 => p3 = 2*p2 - p1

Firstly we will find all 4-digit primes that are permutations of one another
and store them in a set. Then we will generate all possible combinations of
these primes and for each set and generate all possible sequences if they
meet the 2*p2 - p1 in the same set as these two. This way we will find the
sequence we are looking for. The last optimization, we will use the generators.
This way we will get the result without unnecessary calculations.
"""
from itertools import permutations, combinations_with_replacement, product


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


def solution():
    _4_digit_primes = {p for p in sieve_of_eratosthenes(10_000) if p > 1000}

    candidates = (set(int(''.join(perm)) for perm in permutations(comb))
                  for comb in combinations_with_replacement('0123456789', 4))
    candidates = (s & _4_digit_primes for s in candidates if len(s) > 2)

    sequences = (tuple(sorted((p1, p2, 2*p2 - p1)))
                 for candidates_set in candidates
                 for p1, p2 in product(candidates_set, repeat=2)
                 if p1 != p2 and 2*p2 - p1 in candidates_set)

    return ''.join(map(str, next(seq for seq in sequences if 1487 != seq[0])))


# test
if __name__ == '__main__':
    print(solution())  # 296962999629
