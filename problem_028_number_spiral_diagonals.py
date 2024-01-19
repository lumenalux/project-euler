"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a N by N spiral formed in
the same way?

link: https://projecteuler.net/problem=28

Solution:

Let's take a look at the 5 by 5 spiral:

      21 22 23 24 25
      20  7  8  9 10
      19  6  1  2 11
      18  5  4  3 12
      17 16 15 14 13

We can see that the top right corner is 25, which is 5**2. The top left corner
is 21, which is 5**2 - 5 + 1. The bottom left corner is 17, which is 5**2 - 2*5
+ 2. The bottom right corner is 13, which is 5**2 - 3*5 + 3. The same apply to
the right corner with 9. The top left corner is 7, which is 3**2 - 3 + 1. The
bottom left corner is 5, which is 3**2 - 2*3 + 2. The bottom right corner is 3,
which is 3**2 - 3*3 + 3. With it we can see the pattern:

    top right corner = n**2           = n**2 - 0*n + 0
    top left corner  = n**2 - n + 1   = n**2 - 1*n + 1
    bottom left      = n**2 - 2*n + 2 = n**2 - 2*n + 2
    bottom right     = n**2 - 3*n + 3 = n**2 - 3*n + 3

The sum of the corners is 4*n**2 - 6*n + 6. Apply this formula to every layer
of the spiral and we get the sum of the numbers on the diagonals in a N by N.
There are formulas for sum of squares and arithmetic series:


    sum of squares of odds   = k*(2k + 1)*(2k - 1)/3
    sum of arithmetic series = k*(n + 1)/2

    where k = (N - 1) / 2 is the number of layers of the spiral

    ∑(4*n**2 - 6*n + 6) = 4*∑(n**2) - 6*∑(n) + 6*∑(6)
                        = (4N**3 + 3N**2 + 8N - 9) / 6
                        = (N * (N * (4N + 3) + 8) - 9) / 6

Applying all this, we get a formula for calculating the sum of numbers on
diagonals in an N by N spiral formed in the same way.
"""

def solution(N):
    return  (N * (N * (4*N + 3) + 8) - 9) // 6


if __name__ == '__main__':
  print(solution(1)) # 1
  print(solution(3)) # 25
  print(solution(5)) # 101
  print(solution(1001)) # 669171001
