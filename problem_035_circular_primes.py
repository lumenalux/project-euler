"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 and 97

How many circular primes are there below one million?

link: https://projecteuler.net/problem=35
"""
from collections import deque


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


def is_circular_prime(number: int, primes: set[int]) -> bool:
    number = deque(str(number))
    for _ in range(len(number)):
        number.rotate()
        if int(''.join(number)) not in primes:
            return False
    return True


def solution(N: int) -> int:
    primes = set(sieve_of_eratosthenes(N))
    return len({prime for prime in primes if is_circular_prime(prime, primes)})


# test
if __name__ == '__main__':
    print(solution(100))  # 13
    print(solution(1_000_000))  # 55
