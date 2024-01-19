"""
Euler discovered the remarkable quadratic formula:

  n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39. However, when

  n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41

is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| <= 1000
    where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

link: https://projecteuler.net/problem=27

Solution:

Let's take a look at the formula the sequence with n = 0:

  n^2 + an + b = 0^2 + a*0 + b = b = prime number

So b must be a prime number. Now let's take a look at the formula with n = 1:

  n^2 + an + b = 1^2 + a*1 + b = 1 + a + b = prime number

  a = prime number - b - 1

We can evaluate the a and b by iterating through all the prime numbers less
than 1000 and check if the formula produces the maximum number of primes for
consecutive values of n. Lastly, when we find the maximum sequence length,
we can skip the sequence if max_n**2 + a*max_n + b is not a prime number.
Such sequence definitely not the maximum sequence, so we can skip it.
"""

# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1 for i in range(1, n // 2) if sieve[i])]

def solution_(N):
    primes_set = set(sieve_of_eratosthenes(N**2))
    primes = sieve_of_eratosthenes(N)
    max_n, max_a, max_b = 0, 0, 0
    for b in primes:
        for p in primes:
            a = p-b-1
            if max_n**2 + a*max_n + b not in primes_set:
                continue

            n = 0
            while n**2 + a*n + b in primes_set:
                n += 1

            if n > max_n:
                max_n, max_a, max_b = n, a, b

    return max_a*max_b


if __name__ == "__main__":
    print(solution_(1000)) # -59231
