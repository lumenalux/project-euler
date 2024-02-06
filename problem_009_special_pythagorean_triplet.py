"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

  a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which $a + b + c = 1000.
Find the product abc.

link: https://projecteuler.net/problem=9

Solution:

The Pythagorean triples can be defined by the following formulas:

  a = n^2 - m^2
  b = 2mn
  c = n^2 + m^2

where m > n > 0 are integers of opposite parity.
link: https://en.wikipedia.org/wiki/Pythagorean_triple

a + b + c = 1000
          = n^2 - m^2 + 2mn + n^2 + m^2
          = 2n^2 + 2mn
          = 2n(n + m)

2n(n + m) = 1000
n(n + m) = 500
m = 500/n - n

We know that n > m and they are both positive integers.
Also, since n*(n+m) = 500, n cannot be greater than sqrt(500)
"""

# O(√n)


def solution():
    for n in range(1, int(500**0.5) + 1):
        m = 500/n - n
        if m.is_integer() and m > 0 and n > m:
            return int(n**2 - m**2), int(2*m*n), int(n**2 + m**2)

    return None, None, None


# test
if __name__ == '__main__':
    print(solution())  # (375, 200, 425)
