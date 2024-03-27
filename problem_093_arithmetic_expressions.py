"""
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, -, *, /) and parentheses, it
is possible to form different positive integer targets.

For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) - 1
    36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer
as a string: abcd.

Link: https://projecteuler.net/problem=93
"""
from operator import add, sub, mul, truediv
from itertools import permutations, combinations, product


def is_new_sequence_max(sequence: set[int], last_n: int) -> bool:
    return (last_n + 1) in sequence and set(range(1, last_n)) <= sequence


def get_last_n(sequence: set[int], last_n: int) -> int:
    while (last_n + 1) in sequence:
        last_n += 1
    return last_n


def solution():
    last_n = 1
    for comb in combinations(range(1, 10), r=4):
        seen = set()
        for a, b, c, d in permutations(comb):
            for op1, op2, op3 in product((add, sub, mul, truediv), repeat=3):
                result_number = op3(op2(op1(a, b), c), d)
                if result_number > 0 and result_number.is_integer():
                    seen.add(result_number)

                result_number = op3(op1(a, b), op2(c, d))
                if result_number > 0 and result_number.is_integer():
                    seen.add(result_number)

        if is_new_sequence_max(seen, last_n):
            max_a_b_c_d, last_n = comb, get_last_n(seen, last_n)

    return ''.join(map(str, max_a_b_c_d))


if __name__ == '__main__':
    print(solution())  # 1258
