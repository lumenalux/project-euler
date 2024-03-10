"""
NOTE: This problem is a significantly more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
the left column and finishing in any cell in the right column, and moving only
up, down, and right, is indicated in red and bold; the sum is equal to 994.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in resources/0082_matrix.txt, a 31K text file
containing a 80 by 80 matrix, from the left column to the right column.

link: https://projecteuler.net/problem=82
"""
import math


def solution(matrix: list[list[int]]) -> int:
    rows, columns = len(matrix), len(matrix[0])
    dp = [[math.inf] * columns for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = matrix[i][0]

    for j in range(1, columns):
        for i in range(rows):
            dp[i][j] = min(dp[i][j], dp[i][j-1] + matrix[i][j])

        for i in range(1, rows):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])

        for i in range(rows-2, -1, -1):
            dp[i][j] = min(dp[i][j], dp[i+1][j] + matrix[i][j])

    return min(dp[i][-1] for i in range(rows))


def load_matrix(file_path: str) -> list[list[int]]:
    with open(file_path) as f:
        return [list(map(int, line.split(','))) for line in f]


# Test
if __name__ == '__main__':
    print(solution([[131, 673, 234, 103,  18],
                    [201,  96, 342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524,  37, 331]]))  # 994

    print(solution(load_matrix('resources/0082_matrix.txt')))  # 260324
