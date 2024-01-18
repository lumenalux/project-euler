"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?

link: https://projecteuler.net/problem=24

Solution:

Let's determine each element of the permutation one at a time, based on the
desired permutation index.

Example for [A B C D]:
- Total permutations = 4! (24).
- To find the 10th permutation (index 9), we arrange permutations in a 6x4 grid
  (3! rows, 4 columns).
- First element: Divide the permutation index (9) by 3! (6). Result is 1 with a
  remainder of 3, indicating 'B' is the first element (column 1).
- Remove 'B' and repeat with the remainder (3) for the next set [A C D].
- Continue this process, reducing the set size and recalculating the index, to
  determine each subsequent element.

For our task (millionth permutation of '0123456789'):
- Follow the same steps, recalculating the index at each stage by dividing by
  the factorial of the remaining set size.
- The first digit is found by dividing 999999 by 9!, then 274239 by 8!, and so
  on, each time reducing the set by the digit determined.

We directly compute the desired lexicographic permutation by progressively
narrowing down the possibilities and eliminating already-placed elements.
"""
import math


def permutation_of_n(n, sequence):
  if len(sequence)==1:
    return sequence

  d, m = divmod(n, math.factorial(len(sequence)-1))
  return sequence[d] + permutation_of_n(m, sequence[:d] + sequence[d + 1 :])


def simple_solution(N, k=10):
  sequence = ''.join(map(str, range(k)))
  return permutation_of_n(N - 1, sequence)


# test
if __name__ == '__main__':
  print(simple_solution(1_000_000))