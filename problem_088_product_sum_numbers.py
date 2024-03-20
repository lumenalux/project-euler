"""
A natural number, N, that can be written as the sum and product of a given set
of at least two natural numbers, {a1, a2, ..., ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a
minimal product-sum number. The minimal product-sum numbers for sets of size,
k = 2, 3, 4, 5, and 6 are as follows.

    k=2: 4 = 2 × 2 = 2 + 2
    k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
    k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
    k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
    k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 ≤ k ≤ 6, the sum of all the minimal product-sum numbers is

  4 + 6 + 8 + 12 = 30;

note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2 ≤ k ≤ 12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2 ≤ k ≤ 12000?
"""


def solution(N: int) -> int:
    min_product_sum = [2 * N] * (N + 1)

    def product_sum(product: int, sum_: int, length: int, start: int) -> None:
        k = product - sum_ + length
        if N < k:
            return

        if product < min_product_sum[k]:
            min_product_sum[k] = product

        for i in range(start, N // product * 2 + 1):
            product_sum(product * i, sum_ + i, length + 1, i)

    product_sum(product=1, sum_=1, length=1, start=2)
    return sum(set(min_product_sum[2:]))


# Test
if __name__ == '__main__':
    print(solution(6))       # 30
    print(solution(12))      # 61
    print(solution(12_000))  # 7587457
