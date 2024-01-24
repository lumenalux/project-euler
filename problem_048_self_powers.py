"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

link: https://projecteuler.net/problem=48

Solution:

The modulo of the sum of numbers is equal to the sum of the modulo of numbers
with the same modulo. So we can calculate the modulo of each power and then
sum them up:

    (1**1 + 2**2 + 3**3 + ... + N**N) % 10**k =
    = (1**1 % 10**k + 2**2 % 10**k + ... + N**N % 10**k) % 10**k

We will use the pow function with the third argument to calculate
the modulo of the power, which is more efficient than calculating the power
and then calculating the modulo.
"""

def solution(N, k=10):
    modulos = 10**k
    number = sum(pow(i, i, modulos) for i in range(1, N + 1)) % modulos
    return str(number).zfill(10)


# test
if __name__ == '__main__':
    print(solution(10))   # 0405071317
    print(solution(1000)) # 9110846700
