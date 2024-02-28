"""
The n_th term of the sequence of triangle numbers is given by,
t_n = 1/2 * n * (n + 1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
value is a triangle number then we shall call the word a triangle word.

Using resources/0042_words.txt, a 16K text file containing nearly
two-thousand common English words, how many are triangle words?

link: https://projecteuler.net/problem=42

Solution:

The triangle number t_n = 1/2 * n * (n + 1) is a quadratic equation, so we
can find the n from the equation:

    n = (√(8*t_n + 1) - 1) / 2

If the 2*t_n = round(n) * (round(n) + 1), then the t_n is triangle number.
The only thing left is to check if the word value is triangle number for all
the words and count the number of triangle words.
"""
import math


def is_triangle(number: int) -> bool:
    n = round((math.sqrt(8 * number + 1) - 1) / 2)
    return 2 * number == round(n) * (round(n) + 1)


def solution(file_name: str) -> int:
    with open(file_name) as f:
        return sum(is_triangle(sum(ord(c) - 64 for c in word.strip('"')))
                   for word in f.read().split(','))


# test
if __name__ == '__main__':
    print(solution('resources/0042_words.txt'))  # 162
