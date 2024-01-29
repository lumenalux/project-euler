"""
All square roots are periodic when written as continued fractions and can be
written in the form:

    √N = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ...)))

For example, let us consider √23:

    √23 = 4 + √23 - 4 = 4 + 1 / (1 / (√23 - 4)) = 4 + 1 / (1 + (√23 - 3) / 7)

If we continue we would get the following expansion:

    √23 = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

The process can be summarized as follows:

    a0 = 4, 1 / (√23 - 4) = (√23 + 4) / 7 = 1 + (√23 - 3) / 7
    a1 = 1, 7 / (√23 - 3) = 7 * (√23 + 3) / 14 = 3 + (√23 - 3) / 2
    a2 = 3, 2 / (√23 - 3) = 2 * (√23 + 3) / 14 = 1 + (√23 - 4) / 7
    a3 = 1, 7 / (√23 - 4) = 7 * (√23 + 4) / 7 = 8 + (√23 - 4)
    a4 = 8, 1 / (√23 - 4) = (√23 + 4) / 7 = 1 + (√23 - 3) / 7
    a5 = 1, 7 / (√23 - 3) = 7 * (√23 + 3) / 14 = 3 + (√23 - 3) / 2
    a6 = 3, 2 / (√23 - 3) = 2 * (√23 + 3) / 14 = 1 + (√23 - 4) / 7
    a7 = 1, 7 / (√23 - 4) = 7 * (√23 + 4) / 7 = 8 + (√23 - 4)

It can be seen that the sequence is repeating. For conciseness, we use the
notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

    √2  = [1;(2)],         period=1
    √3  = [1;(1,2)],       period=2
    √5  = [2;(4)],         period=1
    √6  = [2;(2,4)],       period=2
    √7  = [2;(1,1,1,4)],   period=4
    √8  = [2;(1,4)],       period=2
    √10 = [3;(6)],         period=1
    √11 = [3;(3,6)],       period=2
    √12 = [3;(2,6)],       period=2
    √13 = [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10,000 have an odd period?

link: https://projecteuler.net/problem=64

Solution:

The following algorithm is used to obtain the continued fraction expansion in
canonical form  (S is any natural number that is not a perfect square):

    m_0 = 0
    d_0 = 1
    a_0 = ⌊√S⌋

    m_n = d_n-1 * a_n-1 - m_n-1
    d_n = (S - m_n^2) / d_n-1
    a_n = ⌊(m_n-1 + √S) / d_n-1⌋

The algorithm terminates when this triplet is the same as one encountered
before.

link: https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend

Using it we will find all the periods of the square roots of the numbers and
count which ones are odd.
"""
import math

from itertools import count


def get_length_of_period(S):
    if math.isqrt(S) ** 2 == S:
        return 0

    a0 = a = math.isqrt(S)
    m, d = 0, 1

    seen = {(a0, m, d)}
    for i in count(1):
        m = d * a - m
        d = (S - m * m) // d
        a = math.floor((a0 + m) / d)
        if (a, m, d) in seen:
            return len(seen) - 1
        seen.add((a, m, d))


def solution(N):
    return sum(1 for n in range(2, N + 1) if get_length_of_period(n) % 2)


# test
if __name__ == '__main__':
    print(solution(25))     # 4
    print(solution(10_000)) # 1322
