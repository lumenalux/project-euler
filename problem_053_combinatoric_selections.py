"""
There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5, 3) = 10.

In general, C(n, r) = n! / (r! * (n-r)!)
            where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23, 10) = 1144066.

How many, not necessarily distinct, values of C(n, r) for 1 <= n <= 100, are
greater than one-million?

link: https://projecteuler.net/problem=53

Solution:

The first observation is that C(n, r) = C(n, n-r). So we only need to check
r <= n/2 and multiply by 2 the result. The second observation is that C(n, r)
is increasing for r <= n/2 and decreasing for r > n/2. This means we can use
binary search to find the first r which C(n, r) > 1_000_000. The amount of
r's for which C(n, r) > 1_000_000 is n - 2*r_min + 1.
"""
import math

def find_r(n):
    low, high = 0, n // 2 + 1
    while low < high:
        mid = (low + high) // 2
        if math.comb(n, mid) > 1_000_000:
            high = mid
        else:
            low = mid + 1
    return low


def solution():
    return sum(max(0, n - 2*find_r(n) + 1) for n in range(1, 101))


# test
if __name__ == '__main__':
    print(solution()) # 4075
