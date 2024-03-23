"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; 
the same is done to a second cube. By placing the two cubes side-by-side in
different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
     ____ ___
    /___/___/|
    | 6 | 4 ||
    |___|___|/

In fact, by carefully choosing the digits on both cubes it is possible to
display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down
so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
for all nine square numbers to be displayed; otherwise it would be impossible
to obtain 09.

In determining a distinct arrangement we are interested in the digits on each
cube, not the order.

{1, 2, 3, 4, 5, 6} is not considered to be a distinct arrangement for this
problem.

Given that two cubes can display all of the square numbers below one-hundred,
determine all the distinct arrangements of the two cubes.

Link: https://projecteuler.net/problem=90
"""
from itertools import combinations


def solution():
    return sum(all(dr in cr and dl in cl or dr in cl and dl in cr
                   for dr, dl in zip('00012348', '14665661'))
               for cr, cl in combinations(combinations('0123456678', r=6), r=2))


# Test
if __name__ == "__main__":
    print(solution())  # 1217

