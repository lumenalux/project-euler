"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

link: https://projecteuler.net/problem=33

Solution:

The non-trivial fraction which could be simplified by cancelling the digits
can be written as:

    10a + b / 10b + c = a / c, where a, b, c are digits from 1 to 9.

Since there are 3 digits, there are only 9^3 = 729 possible fractions. We can
just iterate through all of them and check if the fraction is equal to a / c.
To find the value of denominator in its lowest common terms, we can use the
gcd function or just fractions module from Python.
"""
from fractions import Fraction
from itertools import product


def solution():
    product_fraction = Fraction(1, 1)
    for a, b, c in product(range(1, 10), repeat=3):
        fraction = Fraction(10 * a + b, 10 * b + c)
        if fraction < 1 and Fraction(a, c) == fraction:
            product_fraction *= fraction
    return product_fraction.denominator


# test
if __name__ == '__main__':
    print(solution())  # 100
