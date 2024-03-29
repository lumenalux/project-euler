"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

link: https://projecteuler.net/problem=60

Solution:

For this problem we can use the graph theory to find the solution. First, we
will create the graph where each prime is a vertex and there is an edge between
two vertices if the concatenation of the two primes is also a prime. There are
too many values to check, so we will use parallelization for this process. We
will use the Sieve of Eratosthenes algorithm to find the primes. Then we will
use the multiprocessing module to speed-up the process of checking all the
pairs of primes.

Then we want to use the Bron-Kerbosch algorithm to find all maximal cliques in
the graph. The maximal cliques are the sets of vertices that are all connected
to each other and there are no other vertices that can be added to the set
without breaking the rule. The maximal cliques are the sets of primes that can
be concatenated to produce other primes. In the end we need just find the sum
of clique of 5. But the Bron-Kerbosch algorithm is working with undirected
graphs, so we need to create an undirected graph from our directed graph.
"""
import math

from multiprocessing import Pool
from itertools import combinations, repeat


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


# For more details about the algorithm:
# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def bron_kerbosch(R: set[int],
                  P: set[int],
                  X: set[int],
                  graph: dict[int, set[int]],
                  cliques: list[set[int]]) -> None:
    """
    Perform the Bron-Kerbosch recursive algorithm to find maximal cliques.

    Parameters:
    - R: The current set of vertices included in the clique.
    - P: Potential vertices that can be added to the clique.
    - X: Vertices already considered that should not be added
         to the current clique.
    - graph: The input graph as an adjacency list.
    - cliques: A list to collect the maximal cliques found.
    """
    if not P and not X:
        # Found a maximal clique
        cliques.append(R)
        return

    for vertex in P.copy():
        bron_kerbosch(R.union({vertex}),
                      P.intersection(graph[vertex]),
                      X.intersection(graph[vertex]),
                      graph, cliques)
        P.remove(vertex)
        X.add(vertex)


def is_prime(n: int, primes: dict[int, int], prime_limit: int) -> bool:
    if n < prime_limit:
        return n in primes

    limit = math.isqrt(n)
    for p in primes:
        if p > limit:
            return True
        if n % p == 0:
            return False
    return True


def check_match(pair: tuple[int, int],
                primes: dict[int, int],
                prime_limit: int) -> tuple[int, int] | None:
    a, b = pair
    if not is_prime(int(str(a) + str(b)), primes, prime_limit):
        return None

    if not is_prime(int(str(b) + str(a)), primes, prime_limit):
        return None

    return pair


def generate_matches(primes: dict[int, int],
                     prime_limit: int) -> dict[int, set[int]]:
    pool = Pool()
    results = pool.starmap(
        check_match,
        zip(combinations(primes, 2), repeat(primes), repeat(prime_limit))
    )

    matches = {}
    for a, b in filter(None, results):
        matches.setdefault(b, set()).add(a)
        matches.setdefault(a, set()).add(b)

    pool.close()
    pool.join()

    return matches


def solution(N: int) -> int:
    prime_limit = 10 ** max(3, N - 1)
    primes = sieve_of_eratosthenes(prime_limit)

    matches = generate_matches(primes, prime_limit)

    graph = {}
    for a, a_set in matches.items():
        edges = {b for b in a_set if a in matches.get(b, set())}
        if len(edges) > N - 2:
            graph[a] = edges

    cliques = []
    bron_kerbosch(set(), set(graph), set(), graph, cliques)

    return min(map(sum, (c for c in cliques if len(c) == N)))


# test
if __name__ == '__main__':
    print(solution(4))  # 792
    print(solution(5))  # 26033
