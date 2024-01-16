"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000.

link: https://projecteuler.net/problem=1
"""


# O(n), runs too long for n like 1 000 000
def solution(n):
  return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


# O(1), sum formula
def solution_2(n):
  def get_sum_of_multiples_of_k(k, n):
    end = n - (n % k) if n % k != 0 else n - k
    n_terms = (end - k) // k + 1
    return (n_terms * (k + end)) // 2

  sum_of_multiples_of_3 = get_sum_of_multiples_of_k(3, n)
  sum_of_multiples_of_5 = get_sum_of_multiples_of_k(5, n)
  sum_of_multiples_of_15 = get_sum_of_multiples_of_k(15, n)
  return sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15


# test
if __name__ == '__main__':
  N = 1000
  print(solution(N), solution_2(N)) # 233168 233168

  N = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
  print(solution_2(N)) # 233333333333333333333333333333333333333333333333333333166666666666666666666666666666666666666666666666666668
