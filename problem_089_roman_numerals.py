"""
For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number of
numerals.

The 11K text file, resources/0089_roman.txt, contains one thousand numbers
written in valid, but not necessarily minimal, Roman numerals; that is, they
are arranged in descending units and obey the subtractive pair rule.

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.

Link: https://projecteuler.net/problem=89
"""


def solution(file_path: str) -> int:
    with open(file_path, 'r') as file:
        roman_numerals = file.read()

    numerals = roman_numerals
    numerals = numerals.replace('DCCCC', 'CM')
    numerals = numerals.replace('CCCC', 'CD')
    numerals = numerals.replace('LXXXX', 'XC')
    numerals = numerals.replace('XXXX', 'XL')
    numerals = numerals.replace('VIIII', 'IX')
    numerals = numerals.replace('IIII', 'IV')

    return len(roman_numerals) - len(numerals)


# Test
if __name__ == "__main__":
    print(solution("resources/0089_roman.txt"))