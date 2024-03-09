"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in bold red
and is equal to 2427.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in resources/0081_matrix.txt, a 31K text file
containing a 80 by 80 matrix, from the top left to the bottom right by moving
left, right, up, and down.

link: https://projecteuler.net/problem=81
"""
from itertools import accumulate


def solution(file_path: str) -> int:
    with open(file_path) as f:
        matrix = [list(map(int, line.split(','))) for line in f]

    dp = [list(accumulate(matrix[0])),
          *([0] * len(row) for row in matrix[1:])]

    for i in range(1, len(matrix)):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i, row in enumerate(matrix[1:], 1):
        for j, cell in enumerate(row[1:], 1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cell

    return dp[-1][-1]


# Test
if __name__ == '__main__':
    print(solution('resources/0081_matrix.txt'))  # 427337
