"""
It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

link: https://projecteuler.net/problem=76

Solution:

Nothing special, just a classic dynamic programming problem. But do not forget
that we need to find the number of ways to write the number as a sum of at
least two positive integers. So we need to subtract 1 from the result.
"""

def solution(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            dp[j] += dp[j - i]
    return dp[N] - 1


if __name__ == '__main__':
    print(solution(100))  # 190569291
    print(solution(1000)) # 24061467864032622473692149727990
