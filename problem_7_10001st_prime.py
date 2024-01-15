"""
By listing the first six prime numbers: 2, 3, 5, 7,
11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

link: https://projecteuler.net/problem=7
"""

from itertools import compress, cycle, islice, count

def eratosthenes_sieve_gen():
    """
    An optimized implementation of the Sieve of
    Eratosthenes using wheel factorization.

    This function generates prime numbers by
    employing the following key concepts:

    - Basic Sieve Mechanism: Iteratively marks
      multiples of each prime number as non-prime.

    - Wheel Factorization: Utilizes a wheel
      (constructed from the first few primes: 2, 3, 5)
      to skip numbers that are not potential primes,
      significantly reducing the computational workload.

    - Modulo Set: Contains specific remainders (of division
      by 30) that potential primes greater than 5 can have.
      These are based on the wheel's spokes representing
      positions where primes are likely to be found.

    - Dynamic Composite Tracking: Maintains a dictionary to
      track the next composite number for each discovered
      prime, enabling efficient marking of composites.

    - Generator-Based Yielding: Efficiently yields primes one
      at a time, optimizing memory usage.
    """
    # Dictionary to store the next composite number and its prime factor
    next_composite = {9: 3, 25: 5}

    # Yielding the first few prime numbers
    yield from (2, 3, 5)

    # Mask for wheel factorization optimization
    mask = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    modulos = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    # Iterating over potential prime candidates
    for candidate in compress(islice(count(7), 0, None, 2), cycle(mask)):
        prime = next_composite.pop(candidate, None)
        if prime is None:
            # Candidate is a prime number
            next_composite[candidate * candidate] = candidate
            yield candidate
        else:
            # Update the dictionary with the next composite number for this prime
            next_multiple = candidate + 2 * prime
            while next_multiple in next_composite or (next_multiple % 30) not in modulos:
                next_multiple += 2 * prime
            next_composite[next_multiple] = prime


def solution(n):
    prime_sieve_generator = eratosthenes_sieve_gen()
    for _ in range(n - 1):
        next(prime_sieve_generator)
    return next(prime_sieve_generator)


# test
if __name__ == '__main__':
    print(solution(10001)) # 104743
