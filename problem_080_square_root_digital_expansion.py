"""
It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots is
infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of
the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.

link: https://projecteuler.net/problem=80


"""
import math

from decimal import Decimal, getcontext


def decimal_module_solution(N: int, K: int) -> int:
    getcontext().prec = K + 10
    return sum(sum(map(int, str(Decimal(n).sqrt()).replace('.', '')[:K]))
               for n in range(1, N + 1)
               if math.isqrt(n) ** 2 != n)


def get_sum_of_nth_digits_of_square_root(number: int, k: int) -> int:
    high, low, limit = 5*number, 5, 10**(k + 10)

    while low < limit:
        if high >= low:
            high -= low
            low += 10
        else:
            high *= 100
            low = 10 * (low - low % 10) + low % 10

    return sum(map(int, str(low)[:k]))


def solution(N: int, K: int) -> int:
    return sum(get_sum_of_nth_digits_of_square_root(n, K)
               for n in range(1, N + 1)
               if math.isqrt(n) ** 2 != n)


# Test
if __name__ == '__main__':
    print(solution(2, 100))   # 475
    print(solution(100, 100))  # 40886

    # Using decimal module
    print(decimal_module_solution(2, 100))   # 475
    print(decimal_module_solution(100, 100))  # 40886
