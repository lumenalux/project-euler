"""
The sum of the squares of the first ten natural numbers is,

  1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

  (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is

  2025 - 385 = 2640

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.

link: https://projecteuler.net/problem=6

Solution:

    Sum of squares = 1^2 + 2^2 + ... + n^2
                   = n(n+1)(2n+1)/6
    link: https://proofwiki.org/wiki/Sum_of_Sequence_of_Squares

    Square of sum = (1 + 2 + ... + n)^2
                  = (n(n+1)/2)^2

    Difference = Sum of squares - Square of sum
               = n*(n+1)*(3*n*(n+1) - 4*n - 2)/12
"""


# O(1)
def solution(n):
    return n * (n+1) * (3*n*(n+1) - 4*n - 2) // 12


# O(n)
def brute_force_solution(n):
    return sum(range(1, n+1))**2 - sum(i**2 for i in range(1, n+1))

# test
if __name__ == '__main__':
    print(brute_force_solution(10)) # 2640
    print(solution(10)) # 2640
    print(brute_force_solution(100)) # 25164150
    print(solution(100)) # 25164150
