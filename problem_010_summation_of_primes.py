"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

link: https://projecteuler.net/problem=10
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


# O(n*log(log(n))) - Sieve of Eratosthenes
def solution(n):
    return sum(sieve_of_eratosthenes(n))


# test
if __name__ == '__main__':
    print(solution(10)) # 17
    print(solution(2_000_000)) # 142913828922
