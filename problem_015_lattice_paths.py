"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

link: https://projecteuler.net/problem=15
"""

import math


# O(n^2) time | O(n^2) space
def dp_solution(N):
  grid = [[1] * (N + 1)] + [[1] + [0] * N for _ in range(N)]
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
  return grid[-1][-1]


# O(n) time | O(1) space
def solution(N):
  return math.comb(2 * N, N)


# test
if __name__ == '__main__':
  print(solution(20)) # 137846528820
  print(dp_solution(20)) # 137846528820
