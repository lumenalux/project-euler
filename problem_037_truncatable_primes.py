"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

link: https://projecteuler.net/problem=37
"""
from itertools import compress, cycle, islice, count


def eratosthenes_sieve_gen():
    next_composite = {9: 3, 25: 5}

    yield from (2, 3, 5)

    mask = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    modulos = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for candidate in compress(islice(count(7), 0, None, 2), cycle(mask)):
        prime = next_composite.pop(candidate, None)
        if prime is None:
            next_composite[candidate * candidate] = candidate
            yield candidate
            continue

        next_multiple = candidate + 2 * prime
        while next_multiple in next_composite \
              or (next_multiple % 30) not in modulos:
            next_multiple += 2 * prime
        next_composite[next_multiple] = prime


def is_truncatable_prime(prime, primes_set):
    prime_str = str(prime)
    for i in range(len(prime_str) - 1, 0, -1):
        if int(prime_str[i:]) not in primes_set:
           return False
        if int(prime_str[:-i]) not in primes_set:
            return False
    return True


def solution():
    primes_generator = eratosthenes_sieve_gen()
    primes_set = set(islice(primes_generator, 4))

    truncatable_primes = []
    while len(truncatable_primes) < 11:
        prime = next(primes_generator)
        primes_set.add(prime)
        if is_truncatable_prime(prime, primes_set):
            truncatable_primes.append(prime)

    return sum(truncatable_primes)


# test
if __name__ == '__main__':
    print(solution()) # 748317
