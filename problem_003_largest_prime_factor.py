"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

link: https://projecteuler.net/problem=3
"""


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n: int) -> list[int]:
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            start, end, step = i*i // 2, n // 2, i
            sieve[start:end:step] = [False] * ((end - start - 1) // step + 1)

    return [] if n < 3 else [2, *(2*i + 1
                                  for i in range(1, n // 2) if sieve[i])]


def factor_number(n: int) -> list[int]:
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


def solution(n: int) -> int:
    factors = factor_number(n)
    return factors[-1] if factors else None


# test
if __name__ == '__main__':
    print(solution(600851475143))  # 6857
