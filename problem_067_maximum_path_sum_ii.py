"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in resources/0067_triangle.txt, a
15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2^99 altogether! If you
could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;O)

link: https://projecteuler.net/problem=67
"""


def solution(file_path: str) -> int:
    with open(file_path) as file:
        triangle = [[int(number) for number in line.split(' ')]
                    for line in file]

    total = [0] * (len(triangle[-1]) + 1)
    for row in triangle[::-1]:
        total = [value + max(total[j], total[j + 1])
                 for j, value in enumerate(row)]
    return total[0]


# test
if __name__ == '__main__':
    print(solution('resources/0067_triangle.txt'))  # 7273
