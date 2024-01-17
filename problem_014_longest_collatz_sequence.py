"""
The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 13 and
finishing at 1) contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from functools import lru_cache

def solution(N):
  sequence_length = [0] * (N + 1)
  sequence_length[1] = 1
  for i in range(2, N):
    n = i
    while n > N or sequence_length[n] == 0:
      n = (3 * n + 1) // 2 if n % 2 else n // 2
      sequence_length[i] += n % 2 or 2
    sequence_length[i] += sequence_length[n]

  return max(enumerate(sequence_length), key=lambda x: x[1])[0]


def recursive_solution(N):
  sequence_length = {1: 1}

  # lru_cache(maxsize=None)
  def find_sequence_length(n):
    if n in sequence_length:
      return sequence_length[n]

    if n % 2 == 0:
      sequence_length[n] = 1 + find_sequence_length(n // 2)
    else:
      sequence_length[n] = 2 + find_sequence_length((3*n + 1) // 2)

    return sequence_length[n]

  for i in range(2, N):
    find_sequence_length(i)

  return max(sequence_length.items(), key=lambda x: x[1])[0]


# test
if __name__ == '__main__':
  print(solution(1_000_000)) # 837799
  print(recursive_solution(1_000_000)) # 837799
