"""
An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...
                 ^

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

    d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

Solution:

The length of nth digit fractional part can be represented as:

    n = 9 + 9 * 10 * 2 + 9 * 10^2 * 3 + ... + 9 * 10^(k - 1) * k + m

Where the m is the length of the remaining sequence after the last kth digit
number. The length of the remaining sequence is:

    m = n - 9 - 9 * 10 * 2 - 9 * 10^2 * 3 - ... - 9 * 10^(k - 1) * k

The number of the remaining sequence is:

    number = 10^k + (m - 1) / (k + 1)

and the nth digit is the (m - 1) % (k + 1)th digit of the number

With all of this information we can find the nth digit of the fractional part
of the concatenation of positive integers, then get product of the digits of
the following expression:

    d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""
import math


def get_nth_digit(n: int) -> int:
    m = n
    k = 1
    while (length_of_all_k_digit_numbers := 9 * 10 ** (k - 1) * k) < m:
        m -= length_of_all_k_digit_numbers
        k += 1
    # The formulas differ, because the k here is k + 1 in the formula
    return int(str(10**(k-1) + (m-1) // k)[(m-1) % k])


def solution(nth_digits: list[int]) -> int:
    return math.prod(map(get_nth_digit, nth_digits))


# test
if __name__ == '__main__':
    print(solution([1, 10, 100, 1000, 10000, 100000, 1000000]))  # 210
