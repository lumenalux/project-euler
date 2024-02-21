"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order
of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, *2/5*, 3/7, 1/2, 4/7, 3/5, 5/8,
    2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d <= 1,000,000?

link: https://projecteuler.net/problem=72

Solution:

The length of Farey sequence of order n is equal to the sum of totient:

    1 + ϕ(1) + ϕ(2) + ϕ(3) + ⋯ + ϕ(n-1) + ϕ(n)

It would take too long to calculate totient for each number. The main idea of
this solution is to adapt the Sieve of Eratosthenes algorithm to find all
totients up to n.

What we need to change is the initialization of sieve instead of boolean
would be just a number 1. The totient can be calculated by the formula:

    phi(n) = p1^(k1-1)*(p1-1) * p2^(k2-1)*(p2-1) * ... * pn^(kn-1)*(pn-1)

    where p1, p2, ..., pn are prime factors of n.

Instead of marking the number as not prime we will multiply it by the
prime - 1 and the powers of primes. If the totient is 1, then the number
is prime and we need to proceed with it, otherwise the number is not
prime and we will skip it.

Adding 1 and sum of totients up to n will give us the length of Farey
sequence of order n. But since the Farey sequence includes 0/1 nad 1/1 we
need to subtract 2 to get the result. So the final formula will be:

    1 + ϕ(1) + ϕ(2) + ϕ(3) + ⋯ + ϕ(n-1) + ϕ(n) - 2

    or

    ϕ(1) + ϕ(2) + ϕ(3) + ⋯ + ϕ(n-1) + ϕ(n) - 1

"""
import math


def get_totient_up_to_n(n):
    totient = [1] * (n + 1)

    for i in range(2, n):
        if totient[i] != 1:
            continue

        for j in range(i, n + 1, i):
            totient[j] *= i - 1

        for k in range(2, math.floor(math.log(n, i)) + 1):
            for j in range(i**k, n + 1, i**k):
                totient[j] *= i

    # remove totient for 0
    return totient[1:]


def solution(N):
    return sum(get_totient_up_to_n(N)) - 1


# test
if __name__ == '__main__':
    print(solution(8))          # 21
    print(solution(1_000_000))  # 303963552391
