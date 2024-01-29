"""
The 5 digit number, 16807=7^5, is also a fifth power. Similarly, the 9 digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

link: https://projecteuler.net/problem=63

Solution:

The first observation is that we could get a number with n digits with the
power power of 10^(n-1), so that's mean that the base number is less then 10.

Let's find out what is the maximum power that we need to check for each base
number. We can use this inequality:

    10^(n-1) < 9^n
        n-1  < n*log10(9)
        n    < 1/(1-log10(9))
        n    < 21.85

So we need to check the first 21 power of each base number between 1 and 9.
There are only 9 * 21 = 189 numbers to check.

The number of digits n of a number is given by the formula:

    n = ⌊log10(m^n)⌋ + 1
    n = ⌊n*log10(m)⌋ + 1

We don't need to evaluate the actual value of m^n, we can just check the number
of digits of m^n. If the number of digits is equal to n, then we found a number.
"""
import math


def solution():
    return sum(1 for m in range(1, 10)
                 for n in range(1, 22)
                 if math.floor(n * math.log10(m)) + 1 == n)


# test
if __name__ == '__main__':
    print(solution()) # 49
