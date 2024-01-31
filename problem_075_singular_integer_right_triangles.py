"""
It turns out that 12 cm is the smallest length of wire that can be bent to
form an integer sided right angle triangle in exactly one way, but there are
many more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form
exactly three different integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000
can exactly one integer sided right angle triangle be formed?

link: https://projecteuler.net/problem=75

Solution:

This problem extends Problem 39 by seeking perimeters up to 1,500,000 that
can form exactly one integer-sided right-angle triangle. The approach
involves generating Pythagorean triples using Euclid's formula:

    a = k*(m^2 - n^2)
    b = k*2mn
    c = k*(m^2 + n^2)

    where m > n > 0, m and n are coprime, and not both odd

The perimeter p is given by:

    p = a + b + c = 2km(m + n)

To ensure a unique triangle for a given perimeter, we need to find all k, m,
and n combinations such that each perimeter is achieved exactly once.

 * Limits on m and n: Given the maximum perimeter L, the limits on m and n
   are derived from the inequality m(m + n) <= L/2, leading to an upper
   bound for m.

 * Iterating through m and n: We iterate over m and n within their limits,
   ensuring m and n are coprime and not both odd, to generate primitive
   Pythagorean triples and their multiples.

 * Counting Unique Perimeters: For each generated perimeter, we increment
   a count in an array indexed by perimeter values. After generating all
   triples, we count how many entries in this array are equal to 1,
   indicating exactly one right-angle triangle for that perimeter.

"""
import math


def solution(N):
    perimeter_count = [0] * (N + 1)
    max_m = int((math.sqrt(2*N + 1) - 1) / 2)
    for m in range(2, max_m + 1):
        # add m%2 to 1 to iterate m and n, which are not both odd
        for n in range(1 + m%2, m, 2):
            # ensure m and n are coprime
            if math.gcd(m, n) != 1:
                continue

            p_0 = 2 * m * (m + n)
            for kp_0 in range(p_0, N + 1, p_0):
                perimeter_count[kp_0] += 1

    return sum(count == 1 for count in perimeter_count)


# test
if __name__ == '__main__':
    print(solution(1_500_000)) # 161667
