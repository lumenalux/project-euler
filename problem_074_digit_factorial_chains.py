"""
The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

    169 -> 363601 -> 1454 -> 169
    871 -> 45361 -> 871
    872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

    69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
    78 -> 45360 -> 871 -> 45361 (-> 871)
    540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?

link: https://projecteuler.net/problem=74

Solution:

There are much less distinct factorials than numbers. The maximum chain of
factorials would be 1 length less than the maximum chain of numbers. This is
because the chain itself consists of one number and the rest are factorials.

If we find the maximum chain of factorials, then we can find the first number
by comparing the number factorial sum of digit with the first factorial in the
chain. If they are equal, then we found the first number.

It is easier to find the digit combination that produces the factorial sum than
to find all the suitable numbers. Then we can just count the number of distinct
numbers that can be produced from the digit combination. Also, we can find the
digits combination in the stage of finding the distinct factorials. So we can
store both distinct factorials and the digits combination that produces them
in a hash map.

To count distinct numbers from the digits combination we can use the formula:

    n! / (k1! * k2! * ... * kn!), where n = k1 + k2 + ... + kn

The only problem is that we need to subtract the number of distinct numbers
that start with 0, because they will not product the same factorial sum as
the distinct numbers without leading 0.
"""
import math

from itertools import combinations_with_replacement
from collections import Counter

FACTORIALS = list(map(math.factorial, range(10)))


def factorial_sum(digits):
    return sum(FACTORIALS[int(digit)] for digit in digits)


def distinct_permutations(K):
    return math.factorial(sum(K)) // math.prod(map(math.factorial, K))


def count_distinct_numbers(digits):
    count = Counter(digits)
    t_length = distinct_permutations(count.values())
    if 0 in count:
        t_length -= distinct_permutations((count - Counter([0])).values())
    return t_length


def generate_chains(factorials):
    seen = set()
    for number in factorials:
        if number in seen:
            continue

        chain = []
        while number not in chain:
            chain.append(number)
            number = factorial_sum(map(int, str(number)))

        yield chain
        seen.update(chain)


def solution(N):
    factorials = dict()
    for r in range(1, len(str(N))):
        for comb in combinations_with_replacement(range(10), r):
            factorials.setdefault(factorial_sum(comb), []).append(comb)

    return sum(count_distinct_numbers(digits)
               for chain in generate_chains(factorials)
               for digits in factorials[chain[0]]
               if len(chain) == 59)


if __name__ == '__main__':
    print(solution(  1_000_000)) # 402
    print(solution(100_000_000)) # 62058
