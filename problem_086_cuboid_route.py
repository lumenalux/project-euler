"""
A spider, S sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
fly, F sits in the opposite corner. By traveling on the surfaces of the room
the shortest "straight line" distance from S to F is 10 and the path is shown
on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring
rotations, with integer dimensions, up to a maximum size of M by M by M, for
which the shortest route has integer length when M = 100. This is the least
value of M for which the number of solutions first exceeds two thousand; the
number of solutions is 1975 when M = 99.

Find the least value of M such that the number of solutions first exceeds one
million.

link: https://projecteuler.net/problem=86
"""
import math

from itertools import count


def solution(N):
    total_sum = 0
    for a in count(2):  # S = √(a^2 + (b + c)^2)
        total_sum += sum(min(sum_bc, a + 1) - (sum_bc + 1) // 2
                         for sum_bc in range(3, 2 * a)
                         if math.sqrt(sum_bc**2 + a**2).is_integer())
        if total_sum >= N:
            return a


# Test
if __name__ == '__main__':
    print(solution(1975))       # 99
    print(solution(2000))       # 100
    print(solution(1_000_000))  # 1818
