"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

link: https://projecteuler.net/problem=10
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


# O(n*log(log(n))) - Sieve of Eratosthenes
def solution(n):
    return sum(sieve_of_eratosthenes(n))


# test
if __name__ == '__main__':
    print(solution(10)) # 17
    print(solution(2_000_000)) # 142913828922
