"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

link: https://projecteuler.net/problem=4

Solution:
These are palindrome numbers: 123321, 545545, 101101...
We can write the numbers as: abccba where a, b, c are digits.
The palindrome abccba = 100001a + 10010b + 1100c
                      = 11(9091a + 910b + 100c)
So the palindrome numbers must be divisible by 11.
We can reduce the search space by a factor of 11.
"""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def solution():
    return max(i * j
               # iterate over all 3-digit numbers
               for i in range(100, 1000)
               # iterate over all 3-digit numbers divisible by 11
               for j in range(110, 1000, 11)
               if is_palindrome(i * j))


# test
if __name__ == '__main__':
    print(solution())  # 906609
