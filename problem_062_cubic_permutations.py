"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.

link: https://projecteuler.net/problem=62
"""
from itertools import count


def has_exactly_n_permutations(n: int, cube: int) -> bool:
    digits = sorted(str(cube))

    k_min = round(int(int(''.join(digits))) ** (1/3)) - 1
    k_max = round(int(''.join(digits[::-1])) ** (1/3)) + 1

    return sum(1 for k in range(k_min, k_max)
               if sorted(str(k ** 3)) == digits) == n


def solution(N: int) -> int:
    cube_with_digits = {}
    for n in count(1):
        cube = n ** 3
        digits = ''.join(sorted(str(cube)))
        cube_with_digits.setdefault(digits, []).append(cube)

        if len(cube_with_digits[digits]) != N:
            continue
        if has_exactly_n_permutations(N, cube):
            return cube_with_digits[digits][0]


# test
if __name__ == '__main__':
    print(solution(3))  # 41063625
    print(solution(4))  # 1006012008
    print(solution(5))  # 127035954683
