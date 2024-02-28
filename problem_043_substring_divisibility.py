"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

    d_2d_3d_4=406 is divisible by 2
    d_3d_4d_5=063 is divisible by 3
    d_4d_5d_6=635 is divisible by 5
    d_5d_6d_7=357 is divisible by 7
    d_6d_7d_8=572 is divisible by 11
    d_7d_8d_9=728 is divisible by 13
    d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

link: https://projecteuler.net/problem=43

Solution:

Let us first find all the 3 digit numbers that are divisible by 2, 3, 5, 7, 11,
13, 17. For this we can use permutations of the digits 0 to 9 with length 3.
When we have such triples, we can merge them. We will start from triples which
are divisible by 17, then we will merge them with triples divisible by 13. For
example, we have the triple 289 divisible by 17, and the triple 728 divisible
by 13. We can merge them to get 7289, which is divisible by 13 and 17. Than
we can merge the triple 572 divisible by 11 with 7289 to get 57289, which is
divisible by 11, 13 and 17. We can continue this process until we merge the
triples divisible by 2, 3, 5, 7, 11, 13, 17, which satisfies the problem. At
the end we will merge the triples divisible by 2 with the all the triples.
This will give us all the pandigital numbers with the property.
"""
from itertools import permutations, product


DIVISORS = (2, 3, 5, 7, 11, 13, 17)


def merge_triples(sequences: list[str], triples: list[str]) -> list[str]:
    new_sequences = []
    for sequence, triple in product(sequences, triples):
        if sequence[:2] != triple[-2:]:
            continue

        new_sequence = triple[:1] + sequence
        if len(new_sequence) == len(set(new_sequence)):
            new_sequences.append(new_sequence)

    return new_sequences


def solution():
    triples = list(permutations('0123456789', 3))
    valid_triples = [[t for t in triples if int(''.join(t)) % d == 0]
                     for d in DIVISORS[::-1]]
    valid_triples.append(triples)

    sequences = valid_triples[0]
    for triples in valid_triples[1:]:
        sequences = merge_triples(sequences, triples)

    return sum(int(''.join(seq)) for seq in sequences)


# test
if __name__ == '__main__':
    print(solution())  # 16695334890
