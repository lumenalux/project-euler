"""
The Fibonacci sequence is defined by the recurrence relation:

  Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1

Hence the first 12 terms will be:

  F1 = 1
  F2 = 1
  F3 = 2
  F4 = 3
  F5 = 5
  F6 = 8
  F7 = 13
  F8 = 21
  F9 = 34
  F10 = 55
  F11 = 89
  F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?

link: https://projecteuler.net/problem=25

Solution:

We can use the Binet's formula to calculate the nth Fibonacci number,
it isn't accurate for large n because of floating point errors, but it's
good enough for this problem. So the Fn can be calculated as:

  Fn = (phi^n - (-phi)^(-n)) / √5

where phi = (1 + √5) / 2, also known as the golden ratio.
Then we can apply the logarithm to the formula to get the number of digits:

  Number of digits = floor(log10(Fn)) + 1
                    = floor(log10((phi^n - (-phi)^(-n)) / √5)) + 1
                    = floor(log10(phi^n - (-phi)^(-n)) - 1/2 * log10(5)) + 1

Since we only care about the number of digits, we can ignore the last term,
so we can simplify the formula to:

    Number of digits = floor(n*log10(phi) - 1/2 * log10(5)) + 1

Finally, we can apply the binary search to find the index n of the first term
in the Fibonacci sequence to contain 1000 digits
"""
import math

LOG10_SQRT_5 = 0.5 * math.log10(5)
LOG10_PHI = math.log10((1 + math.sqrt(5)) / 2)


def get_number_of_digits_of_nth_fibonacci(n):
    return math.floor(n * LOG10_PHI - LOG10_SQRT_5) + 1


# O(log(N)) time | O(1) space
def solution(N):
    low, high = 1, 2
    while get_number_of_digits_of_nth_fibonacci(high) < N:
        low, high = high, high * 2

    while low < high:
        mid = (low + high) // 2
        if get_number_of_digits_of_nth_fibonacci(mid) < N:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == "__main__":
    print(solution(3))              # 12
    print(solution(1000))           # 4782
    print(solution(1_000_000))      # 4784969
    print(solution(1_000_000_000))  # 4784971964
