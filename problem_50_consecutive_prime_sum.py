"""
The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

link: https://projecteuler.net/problem=50

Solution:

Let's sum up all the primes within the range. Then we will use the sliding
window technique. We will start with the largest window and check if the sum
is prime. If it is, we will stop the algorithm and return the result. If not,
we will reduce the window by one and check again. To reduce the window, we
can subtract the first element and add the next one.
"""
from statistics import mean

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


def solution(N):
    primes = sieve_of_eratosthenes(N)
    primes_sum = sum(primes)
    for window in range(len(primes), 1, -1):
        sequence_sum = primes_sum
        for i in range(len(primes) - window):
            if sequence_sum >= N:
                break
            if sequence_sum in primes:
                return sequence_sum
            sequence_sum += primes[i + window] - primes[i]
        primes_sum -= primes[window - 1]


# test
if __name__ == '__main__':
    print(solution(100))       # 41
    print(solution(1000))      # 953
    print(solution(1_000_000)) # 997651
