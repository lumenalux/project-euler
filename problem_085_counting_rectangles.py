"""
By counting carefully it can be see that a rectangular board measuring 3 by 2
contains eighteen rectangles.

Although there exists no rectangular board that contains exactly two million
rectangles, find the area of the grid with the nearest solution.

link: https://projecteuler.net/problem=85
"""


def count_rectangles(n, k):
    return (n*k * (n+1) * (k+1)) // 4


def solution(N):
    min_n, max_n = 1, 2
    while count_rectangles(max_n, max_n) < N:
        min_n, max_n = max_n, max_n * 4

    return min(
        ((n*k, count_rectangles(n, k))
         for n in range(min_n, max_n + 1)
         for k in range(1, n + 1)),
        key=lambda x: abs(x[1] - N)
    )[0]


# Test
if __name__ == '__main__':
    print(solution(18))         # 6
    print(solution(2_000_000))  # 2772
