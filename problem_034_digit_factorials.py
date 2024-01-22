"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

link: https://projecteuler.net/problem=34

Solution:

The upper bound of the number is 9! * 7 = 2540160, since 9! * 8 = 2903040, which
has 7 digits, so the sum of the factorial of the digits can't be equal to the
number. We can find all the curious numbers by iterating through the combinations
of the digits and check if the sum of the factorial of the digits fits to the
definition of the curious number. To make sure we will not add the same number
twice, we will use the set to store the curious numbers.
"""
import math

from itertools import combinations_with_replacement
from collections import Counter


def solution():
    factorials = list(map(math.factorial, range(10)))
    curious_numbers = set()
    for r in range(2, 8):
      for digits in combinations_with_replacement(range(10), r):
          number = sum(factorials[digit] for digit in digits)
          if Counter(str(number)) == Counter(map(str, digits)):
              curious_numbers.add(number)
    return sum(curious_numbers)


# test
if __name__ == '__main__':
    print(solution()) # 40730
