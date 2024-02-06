"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximized?

link: https://projecteuler.net/problem=39

Solution:

We are dealing with Pythagorean triples, which are integer solutions to the
Pythagorean theorem. We can find every triple by using the following formulas:

    a = k*(m^2 - n^2)
    b = k*2mn
    c = k*(m^2 + n^2)

where m > n > 0, and m and n are coprime and not both odd, k is integer.
Summing the three equations, we get:

    p = a + b + c = k*(m^2 + 2mn + m^2 - n^2) = k*(2m^2 + 2mn) = 2km(m + n)

    if p_0 = 2m(n + m), then p = k*p_0, where k is an integer.

One more observation is that the maximum value of m and n is limited by the
perimeter p:

    2m(m + n) <= p_max = N
    m(m + n) <= N / 2

    substituting n = 1, we get:

    m(m + 1) <= N / 2
    m^2 + m - N / 2 <= 0
    m <= (√(2*N + 1) - 1) / 2

    for the N = 1000, m <= 21.86, but the m is integer, so m <= 21
"""
import math

from operator import itemgetter


def solution(N):
    perimeter_count = [0] * (N + 1)
    max_m = int((math.sqrt(2*N + 1) - 1) / 2)
    for m in range(2, max_m + 1):
        # add m%2 to 1 to iterate m and n, which are not both odd
        for n in range(1 + m % 2, m, 2):
            # ensure m and n are coprime
            if math.gcd(m, n) != 1:
                continue

            p_0 = 2 * m * (m + n)
            for kp_0 in range(p_0, N + 1, p_0):
                perimeter_count[kp_0] += 1

    return max(enumerate(perimeter_count), key=itemgetter(1))[0]


# test
if __name__ == '__main__':
    print(solution(200))      # 120
    print(solution(1000))     # 840 <--
    print(solution(10_000))   # 9240
    print(solution(100_000))  # 55440
