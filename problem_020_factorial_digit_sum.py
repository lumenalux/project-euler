"""
n! means n x (n - 1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum
of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

link: https://projecteuler.net/problem=20

Solution:

It isn't hard to iterate and multiply using large numbers, but we
choose the hard way. We will use the fact that

  (2n)! = 1 * 2 * ... * n * (n + 1) * ... * (2n - 1) * (2n)
  (2n)! = n! * 2^n * 1 * 3 * 5 * ... * (2n - 1)

With this fact, we can calculate (2n)! using previously calculated
n!. We can also can use previously calculated 2^n and odd product
which is 1 * 3 * 5 * ... by multiplying it with the odd numbers
that we skipped in the previous step. There would be log(n) such
iterations, but the time complexity is still O(n), because we
calculate the odd product in O(n) time.
"""
import math


def generate_factorial_steps(n):
    if n > 1:
        yield from generate_factorial_steps(n - 1 if n % 2 else n // 2)
        yield n


def fast_factorial(n):
    result = 1
    last_odd = 1
    odd_product = 1
    power_of_2 = 2

    for num in generate_factorial_steps(n):
        if num % 2 == 0:
            odd_product *= math.prod(range(last_odd + 2, num, 2))
            last_odd = num - 1
            result *= power_of_2 * odd_product
            power_of_2 *= power_of_2
        else:
            result *= num
            power_of_2 *= 2

    return result


def solution(n):
    return sum(map(int, str(fast_factorial(n))))


if __name__ == '__main__':
    print(solution(100))  # 648
