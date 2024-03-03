r"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.

                    (4)
                     \
                    (3)
                   /  \
                (1)---(2)--(6)
                /
              (5)

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set:

    4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals:

    9, 10, 11, and 12.

There are eight solutions in total.

    Total       Solution Set
    9           4,2,3; 5,3,1; 6,1,2
    9           4,3,2; 6,2,1; 5,1,3
    10          2,3,5; 4,5,1; 6,1,3
    10          2,5,3; 6,3,1; 4,1,5
    11          1,4,6; 3,6,2; 5,2,4
    11          1,6,4; 5,4,2; 3,2,6
    12          1,5,6; 2,6,4; 3,4,5
    12          1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16- and 17-digit strings. What is the maximum 16-digit string for a
"magic" 5-gon ring?

                    ( )
                      \
                      ( )     ( )
                     /   \    /
                   /      \ /
                ( )      ( )
               /  \      /
              /  ( )---( )---( )
            ( )   \
                  ( )

link: https://projecteuler.net/problem=68

Solution:

We can't use the 10 in the inner ring, cause it will be used twice and the
length of the string will be 17.

Let's assume that the maximum 16-digit string for a "magic" 5-gon ring is
starting with the number 6, cause it's the highest digit which can be used as
the starting point of the outer ring. Then, the sum of the outer ring is:

    6 + 7 + 8 + 9 + 10 = 40

The numbers of inner ring are 1 to 5, and they are used twice. So, the sum of
the inner ring is:

    2 * (1 + 2 + 3 + 4 + 5) = 30

The full sum of the 5-gon ring is:

    40 + 30 = 70

The average of the 5-gon ring is:

    70 / 5 = 14

The sum of the 3 numbers in the outer ring is 14. So the possible sets are:

    { 6, 3, 5},
    { 7, 2, 5},
    { 7, 3, 4},
    { 8, 1, 5},
    { 8, 2, 4},
    { 9, 1, 4},
    { 9, 2, 3},
    {10, 1, 3}

With the replacement of the two numbers there are 8 * 2 = 16 possible sets.

Also, the last number of each set is the second number of the next set and
there are unique first number in each set. With that knowledge, we can chain
the sets which suits the conditions and find the maximum 16-digit string.
"""
from itertools import chain
from collections import Counter


def generate_partial_sets():
    sets = []
    for x in range(6, 11):
        for y in range(1, 6):
            if 13 < x + y:
                continue
            for z in range(1, 6):
                if x + y + z == 14 and y != z:
                    sets.append((x, y, z))
    return sets


def get_next_sets(solution_set: list[int],
                  partial_sets: list[tuple[int, ...]]):
    outer = set(solution_set[::3])
    inner = Counter(solution_set[1::3]) + Counter(solution_set[2::3])

    x0, y0, z0 = solution_set[-3:]
    for partial_set in partial_sets:
        x, y, z = partial_set
        max_count = max((Counter((y, z)) + inner).values())
        if x not in outer and z0 == y and max_count < 3:
            yield solution_set + partial_set


def solution():
    partial_sets = generate_partial_sets()
    solutions = partial_sets[:2]
    for _ in range(4):
        solutions = chain.from_iterable(
            get_next_sets(s, partial_sets[2:]) for s in solutions
        )

    solutions = (s for s in solutions
                 if s[1] == s[-1])

    return int(''.join(map(str, max(solutions))))


if __name__ == '__main__':
    print(solution())  # 6531031914842725
