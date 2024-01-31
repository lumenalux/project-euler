"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order
of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, *3/8*, *2/5*, *3/7*, 1/2, 4/7, 3/5,
    5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8


How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d <= 12,000?

link: https://projecteuler.net/problem=73

Solution:

This problem requires counting the number of reduced proper fractions that lie
strictly between 1/3 and 1/2 for denominators up to 12,000. A brute-force
approach checking each fraction's reduced form and comparing it against the
bounds would be impractical due to the computational complexity.

Instead, we leverage a more nuanced understanding of fractions and their
distribution. For a given denominator d, the fractions between 1/3 and 1/2 are
those where the numerator n satisfies 1/3 < n/d < 1/2. This can be translated
to d/3 < n < d/2.

The key insight is that not all values of n need to be checked individually.
Since we are interested in reduced fractions, we can count the eligible
numerators for each denominator d directly using floor division: d//2 - d//3
gives the count of numerators between d/3 and d/2. However, this includes the
upper bound, so we subtract 1 to exclude fractions equal to 1/2.

However, this count includes fractions that are not in reduced form. To
address this, we iterate over each denominator d and adjust the counts for its
multiples to ensure that only reduced fractions are counted. This is done by
subtracting the count for d from its multiples, effectively removing
non-reduced fractions from the total count.

Finally, summing these counts across all denominators up to 12,000 gives the
desired number of reduced proper fractions within the specified range.
"""

def solution(N):
    number_of_new_fractions = [0] * (N + 1)
    for d in range(1, N + 1):
        # Count fractions between 1/3 and 1/2 for the denominator d
        number_of_new_fractions[d] += d // 2 - d // 3 - 1
        # Adjust counts for multiples of d to ensure reduced proper fractions are counted
        for k in range(2 * d, N + 1, d):
            number_of_new_fractions[k] -= number_of_new_fractions[d]

    # Sum the counts to get the total number of fractions
    return sum(number_of_new_fractions)

import math

from itertools import pairwise, chain


def solution(N):
    number_of_new_fractions = [0] * (N + 1)
    for d in range(1, N + 1):
        number_of_new_fractions[d] += d // 2 - d // 3 - 1
        for k in range(2 * d, N + 1, d):
            number_of_new_fractions[k] -= number_of_new_fractions[d]

    return sum(number_of_new_fractions)


# test
if __name__ == '__main__':
    print(solution(8)) # 7295372
    print(solution(12_000)) # 7295372
