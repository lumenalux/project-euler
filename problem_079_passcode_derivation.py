"""
A common security method used for online banking is to ask the use for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, resources/0079_keylog.txt, contains fifty successful login
attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.

link: https://projecteuler.net/problem=79

Solution:

We assume that the shortest possible secret passcode is the one that has the
each digit only once. If that so, each digit can be smaller only than the
digits that come after it.

If we count how many times each digit is smaller than the distinct digits
that come after it, we can sort the digits by that count and get the shortest
possible secret passcode.
"""


def solution(file_path):
    with open(file_path) as f:
        data = f.read().splitlines()

    numbers = set(''.join(data))
    smaller = {number: set() for number in numbers}
    for subset in set(data):
        for number in numbers:
            if number in subset:
                smaller[number].update(subset[:subset.index(number)])

    return ''.join(sorted(smaller, key=lambda x: len(smaller[x])))


# test
if __name__ == '__main__':
    print(solution('resources/0079_keylog.txt'))  # 73162890
