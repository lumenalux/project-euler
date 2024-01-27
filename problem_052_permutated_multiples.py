"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

link: https://projecteuler.net/problem=52

Solution:

The first observation is that the number of digits of x and 6x must be the
same. So 6x must have the same number of digits as x. this means that
number of digits of x = number of digits of 6x:

  n = ⌊log10(6x)⌋ + 1 = ⌊log10(x)⌋ + 1

  10^n < 6x < 10^(n+1) which means x < 10^(n+1) / 6

This already reduces the search space roughly by 13.5 times.

The next observation is the difference of numbers with permuted digits is
always divisible by 9. If d one of the digits of permutation of numbers,
then with the difference we have:

  10^p * d - 10^q * d = 10^q * (10^(p-q) - 1) * d, if p > q and
  10^p * d - 10^q * d = 10^p * (10^(q-p) - 1) * d, if p < q and
  10^p * d - 10^q * d = 0,                         if p = q

Since 10^(p-q) - 1, 10^(q-p) - 1 and 0 are divisible by 9, the difference is
also divisible by 9. Now let's look at the numbers 2x, 3x, 4x, 5x, and 6x.

Since they are all permutations of x, their difference must be divisible by 9.
So we have:

  2x - x = x

So the x is divisible by 9. This means we could only iterate over multiples
of 9.
"""
from itertools import count


def solution():
    for n in count(1):
        for x in range(10**(n-1) + 8, 10**n // 6 + 1, 9):
            digits = sorted(str(x))
            if all(sorted(str(i * x)) == digits for i in range(2, 7)):
                return x


# test
if __name__ == '__main__':
    print(solution()) # 142857
