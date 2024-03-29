"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000.

link: https://projecteuler.net/problem=1
"""


# O(n), runs too long for n like 1 000 000
def solution(n: int) -> int:
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


# O(1), sum formula
def solution_2(n: int) -> int:
    def get_sum_of_multiples_of_k(k: int, n: int) -> int:
        end = n - (n % k) if n % k != 0 else n - k
        n_terms = (end - k) // k + 1
        return (n_terms * (k + end)) // 2

    result = get_sum_of_multiples_of_k(3, n)
    result += get_sum_of_multiples_of_k(5, n)
    return result - get_sum_of_multiples_of_k(15, n)


# test
if __name__ == '__main__':
    N = 1000
    print(solution(N), solution_2(N))  # 233168 233168

    N = 10 ** 60
    print(solution_2(N))  # ≈ 23.3 * 10^118
