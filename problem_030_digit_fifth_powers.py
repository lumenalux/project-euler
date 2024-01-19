"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of Nth powers of
their digits.

link: https://projecteuler.net/problem=30

Solution:

Let's find the upper bound for the number. The max digit is 9, so the max sum of
the fifth powers of digits is 9**5, and if we add n such numbers we would get
9**5*n. The min n is 0, the max is 9. If we get the 5-digit number, the max sum
would be 9**5*5 = 295245. If we get the 7-digit number, the max sum would be
9**5*7 = 413343, but it is less than 7-digit number, so we can't get the 7-digit.
The upper bound is 9**5*6 = 354294.

If we get the sum of fifth powers of digits of numbers 1234 and 4321, the sums
would be the same. So we can use the combinations of digits to get the sums,
reducing the search space.
"""
from itertools import combinations_with_replacement


def solution():
    digits = range(10)
    powers = [i**5 for i in digits]

    r = 6
    sum_of_numbers = 0
    for comb in combinations_with_replacement(map(str, digits), r):
        number = sum(powers[int(i)] for i in comb)
        if tuple(sorted(str(number).zfill(r))) == comb:
            sum_of_numbers += number

    # exclude 1, since 1**5 = 1
    return sum_of_numbers - 1


# test
if __name__ == '__main__':
    print(solution()) # 443839
