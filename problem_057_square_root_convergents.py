"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

    sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2                         =  3/2  = 1.5
    1 + 1/(2 + 1/2)                 =  7/5  = 1.4
    1 + 1/(2 + 1/(2 + 1/2))         = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?

link: https://projecteuler.net/problem=57

Solution:

We can use recurrence relation to solve this problem. Let's define a function
f(n) which returns the nth expansion of the continued fraction. We can see that

    f(n) = 1 + 1 / (1 + f(n - 1))

We can use built-in fractions module to solve this problem. But we will go
further and solve this problem without using any built-in modules.
If f(n) = numerator / denominator, then:

    f(n + 1) = 1 + 1 / (1 + f(n))
             = 1 + 1 / (1 + numerator / denominator)
             = 1 + 1 / ((denominator + numerator) / denominator)
             = 1 + denominator / (denominator + numerator)
             = (2 * denominator + numerator) / (denominator + numerator)

We can use string to find the length of the number, but also we can use the
math formula:

    floor(log10(n)) + 1, where n is the number we want to find the length of.

And use this comparison:

    floor(log10(denominator)) < floor(log10(numerator))

With all of this, we can solve this problem.
"""
import math

from fractions import Fraction


def fractions_module_solution():
    fraction = Fraction(1, 1)
    count = 0
    for _ in range(1000):
        fraction = 1 + Fraction(1, 1 + fraction)
        if len(str(fraction.numerator)) > len(str(fraction.denominator)):
            count += 1
    return count


def solution():
    n, d = 1, 1
    count = 0
    for _ in range(1000):
        n, d = 2*d + n, d + n
        if math.floor(math.log10(n)) > math.floor(math.log10(d)):
            count += 1
    return count


# test
if __name__ == '__main__':
    print(fractions_module_solution())  # 153
    print(solution())  # 153
