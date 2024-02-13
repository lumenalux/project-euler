"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

link: https://projecteuler.net/problem=36

Solution:

We can generate the binary palindromes using the following algorithm:

        1. Generate the binary representation of the number.
        2. Generate the binary representation of the number in reverse order.
        3. Concatenate the two binary representations.

So we only need to generate the binary palindromes and check if they are
palindromes in base 10. There are much less binary palindromes than the
actual numbers less than one million, so we significantly reduce the number
of iterations.
"""
from itertools import count


def generate_binary_palindromes():
    for i in count(1):
        binary = bin(i)[2:]
        yield int(binary + binary[-1::-1], 2)  # for even length
        yield int(binary + binary[-2::-1], 2)  # for odd length


def solution(N):
    result = 0
    binary_palindromes_generator = generate_binary_palindromes()
    while (palindrome := next(binary_palindromes_generator)) < N:
        result += palindrome if str(palindrome) == str(palindrome)[::-1] else 0
    return result


# test
if __name__ == '__main__':
    print(solution(1_000_000))  # 872187
