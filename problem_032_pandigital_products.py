"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

link: https://projecteuler.net/problem=32

Solution:

We can use the permutations of the numbers to solve this problem. Iterating
like this:

    1x2345
    12x345

If we find all the permutations, we don't need to check the product for all
of the sequences like 123x45, 1234x5, cause the permutation of the numbers
45x123, 5x1234 will cover all of them. So we can just check the half of the
permutation.

The two numbers can't have the 4 digits together, since 99x99 = 9801, so there
wouldn't be enough digits for the product to be pandigital. If the two numbers
together have 6 digits, then the product will have at least 5 digits, and there
are 11 digits in total, so there are more than 9 digits, so the product can't
be pandigital. So the two numbers together have 5 digits. So we need to check
the permutations of the numbers 1-9 with 5 digits.

Lastly, to ensure that we summing the products only once, we will use the
sieve bool array to mark the products that we already get to avoid summing
them again.
"""
from itertools import permutations, chain

DIGITS = '123456789'
DIGITS_SET = frozenset(DIGITS)
R = 5


def is_product_pandigital(a, b):
    product_set = set(chain.from_iterable(map(str, (a, b, a * b))))
    return len(str(a * b)) == 4 and product_set == DIGITS_SET


def solution():
    sieve = [False] * 10000
    for permutation in permutations(DIGITS, R):
        for i in (1, 2):
            a = int(''.join(permutation[:i]))
            b = int(''.join(permutation[i:]))
            if is_product_pandigital(a, b):
                sieve[a * b] = True

    return sum(i for i, is_pandigital in enumerate(sieve) if is_pandigital)


if __name__ == '__main__':
    print(solution())  # 45228
