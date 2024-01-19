"""
Using resources/0022_names.txt, a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical value
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

link: https://projecteuler.net/problem=22
"""
from itertools import chain


def solution(file_name):
    with open(file_name) as f:
        return sum((i + 1) * sum(ord(c) - 64 for c in name.strip('"'))
                   for i, name in enumerate(sorted(f.read().split(','))))


# test
if __name__ == '__main__':
    print(solution('resources/0022_names.txt')) # 871198282
