"""
The square root of 2 can be written as an infinite continued fraction.

    √2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for √2.

    1 + 1 / 2 = 3 / 2
    1 + 1 / (2 + 1 / 2) = 7 / 5
    1 + 1 / (2 + 1 / (2 + 1 / 2)) = 17 / 12
    1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / 2))) = 41 / 29

Hence the sequence of the first ten convergents for √2 are:

  1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,

    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

  2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.

link: https://projecteuler.net/problem=65

Solution:

If the nth convergent is written as n / d, then the next convergent is
a + 1 / (n / d) = (a * n + d) / n, so:

    n_k = a_k * n_k-1 + d_k-1
    d_k = n_k-1

So we can find the nth convergent using this recurrence relation. The last
thing is to find the sum of digits in the numerator of the 100th convergent.
"""
def get_a(n):
  if n == 0:
    return 2

  return 2 * (n + 1) // 3 if n % 3 == 2 else 1


def solution(N):
    n, d = 1, get_a(N - 1)
    for k in range(N - 2, -1, -1):
        n, d = d, get_a(k)*d + n
    return sum(map(int, str(d)))


# test
if __name__ == '__main__':
    print(solution(10)) # 17
    print(solution(100)) # 272
