"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

link: https://projecteuler.net/problem=38

Solution:

The maximum number which we can take into account would not be greater than
9999, because 2*9999 = 19998, which is a 5-digit number. If we take a 5-digit
the next value would be also 5 digit, so the concatenated product would be a
10-digit number, but we need only 9 digits. Next, let's take a look for these
products:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

We can see that the number n should have the digits once, cause n * 1 should
give us also the digits once. Iterating over all permutations of the digits
with length from 1 to 4, we will find the solution.
"""
from itertools import permutations


DIGITS_SET = frozenset('123456789')


def get_pandigital_product_number(number: int) -> int:
    product_number = str(number)
    i = 1
    while i < 9 and len(product_number) < 9:
        i += 1
        product_number += str(number * i)

    if 9 < i or len(product_number) != 9 or set(product_number) != DIGITS_SET:
        return -1

    return int(product_number)


def solution():
    return max(get_pandigital_product_number(int(''.join(permutation)))
               for r in range(1, 5)
               for permutation in permutations('123456789', r))


# test
if __name__ == '__main__':
    print(solution())  # 932718654
