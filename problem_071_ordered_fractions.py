"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order
of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, *2/5*, 3/7, 1/2, 4/7, 3/5, 5/8,
    2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.

link: https://projecteuler.net/problem=71

Solution:

Let's add numerator and denominator this way:

    (2 + 3) / (5 + 7) = 5 / 12

5/12 is already closer to 3/7 than 2/5. If we continue this addition up to
infinity, the result will never be more than 3/7. This is because:

    2 + 3(n - 1) < 3n
    5 + 7(n - 1) < 7n

    (2 + 3(n - 1)) / (5 + 7(n - 1)) < 3n / 7n
    (2 + 3(n - 1)) / (5 + 7(n - 1)) <  3 / 7

Also the 2 + 3n and 5 + 7n are coprime, because 2 and 5 are coprime and 3 and 7
are coprime. The fraction is reduced. Let's find the limit of denominator
and find the numerator. Combining this we will get the inverse formula for the
numerator and get the answer.
"""
def solution(N):
    return 2 + 3*((N - 5) // 7)


# test
if __name__ == '__main__':
    print(solution(8))         # 2
    print(solution(1_000_000)) # 428570
