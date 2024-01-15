"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

link: https://projecteuler.net/problem=3
"""


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    if n <= 2:
        return []

    sieve = [True] * n
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = [False] * len(sieve[i*i:n:i])  # Set multiples of i to False

    return [i for i, prime in enumerate(sieve) if prime]


def factor_number(n):
    factors = []
    prime_candidates = sieve_of_eratosthenes(int(n**0.5) + 1)
    for prime in prime_candidates:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)

    return factors

# time:  O(√n(log(log(√n))))
# space: O(√n)
def solution(n):
    factors = factor_number(n)
    return factors[-1] if factors else None


# test
if __name__ == '__main__':
    N = 600851475143
    print(solution(N))

    print(factor_number(104))
    print(factor_number(13195))
    print(factor_number(600851475143))
    # print(sieve_of_eratosthenes(202))