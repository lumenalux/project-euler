"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the letters
used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty
two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

NUMBERS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def number_to_words(number: int) -> str:
    if number == 1000:
        return NUMBERS[1] + NUMBERS[number]

    if number < 20:
        return NUMBERS[number]

    if number < 100:
        return NUMBERS[number // 10 * 10] + NUMBERS[number % 10]

    if number % 100 == 0:
        return NUMBERS[number // 100] + NUMBERS[100]

    decades = number_to_words(number % 100)
    return f"{NUMBERS[number // 100]}{NUMBERS[100]}and{decades}"


def solution():
    return sum(len(number_to_words(number)) for number in range(1, 1001))


# test
if __name__ == '__main__':
    print(solution())  # 21124
