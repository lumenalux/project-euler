"""
Consider quadratic Diophantine equations of the form:

    x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

    3^2 - 2*2^2 = 1
    2^2 - 3*1^2 = 1
    9^2 - 5*4^2 = 1
    5^2 - 6*2^2 = 1
    8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.

link: https://projecteuler.net/problem=66

Solution:

The solution is based on the Chakravala method.
link: https://en.wikipedia.org/wiki/Chakravala_method

After that, we just need to find the maximum value of x for each D.
"""
import math

from itertools import count
from operator import itemgetter


def chakravala_method(D):
    a, k, x, y = 1, 1, 1, 0
    m = math.isqrt(D)
    D_sqrt = math.sqrt(D)

    while k != 1 or y == 0:
        # Adjust m to the nearest value to minimize |m^2 - d|
        m = k * ((m // k) + 1) - m
        m -= int((m - D_sqrt) / k) * k

        next_x = (m * x + D * y) // abs(k)
        next_y = (m * y + x) // abs(k)
        next_k = (m * m - D) // k

        x, y, k = next_x, next_y, next_k

    return x


def solution(N):
    D = [d for d in range(2, N+1) if math.isqrt(d) ** 2 != d]
    return max(zip(map(chakravala_method, D), D), key=itemgetter(0))[1]


# test
if __name__ == '__main__':
    print(solution(7))    # 5
    print(solution(1000)) # 661
