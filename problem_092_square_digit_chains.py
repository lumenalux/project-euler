"""
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Link: https://projecteuler.net/problem=92
"""
import math

from functools import lru_cache
from itertools import combinations_with_replacement as cwr
from collections import Counter


def distinct_permutations(multiset: list[str]) -> int:
    K = Counter(multiset).values()
    return math.factorial(sum(K)) // math.prod(map(math.factorial, K))


@lru_cache(maxsize=None)
def chain(n: int) -> int:
    return chain(sum(int(d)**2 for d in str(n))) if n not in (0, 1, 89) else n


def solution(N: int) -> int:
    return sum(distinct_permutations(comb)
               for comb in cwr('1234567890', r=(len(str(N)) - 1))
               if chain(int(''.join(comb))) == 89)


if __name__ == '__main__':
    print(solution(10_000_000))  # 8581146
