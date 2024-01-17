"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

link: https://projecteuler.net/problem=16
"""
import math

def cheating_solution(power, base=2):
    return sum(map(int, str(base**power)))


class LargeNumber:
    DIGITS_IN_BUCKET = 6

    def __init__(self, number, number_of_buckets=500):
        self.separator = 10 ** self.DIGITS_IN_BUCKET
        self.number = []
        for _ in range(number_of_buckets):
            self.number.append(float(number % self.separator))
            number //= self.separator

    def __add__(self, other):
        carry = 0.0
        result = LargeNumber(0, number_of_buckets=len(self.number))
        for i, bucket in enumerate(other.number):
            addition = self.number[i] + bucket + carry
            result.number[i] = float(addition % self.separator)
            carry = float(addition // self.separator)
        return result

    def __mul__(self, other):
        result = LargeNumber(0, number_of_buckets=len(self.number))
        for i, bucket in enumerate(self.number):
            carry = 0.0
            for j, other_bucket in enumerate(other.number):
                addition = bucket * other_bucket + carry
                index = min(i + j, len(self.number) - 1)
                result.number[index] += float(addition % self.separator)
                carry = float(addition // self.separator)
        return result

    def __pow__(self, number):
        result = LargeNumber(1, number_of_buckets=len(self.number))
        if number == 0:
            return result
        if number == 1:
            result.number = self.number.copy()
            return result

        squared = self * self
        if number % 2 == 0:
            return squared ** (number // 2)

        return self * (squared ** ((number - 1) // 2))

    def __str__(self):
        str_number = [str(int(bucket)).zfill(self.DIGITS_IN_BUCKET)
                      for bucket in self.number[::-1]]

        return ''.join(str_number).lstrip('0')


def solution(power, base=2):
    number_of_buckets = int(1 + power * math.log(10, base) // 6)
    return sum(map(int, str(LargeNumber(base, number_of_buckets) ** power)))


# test
if __name__ == '__main__':
    print(cheating_solution(15)) # 26
    print(cheating_solution(1000)) # 1366
    print(cheating_solution(5000)) # 6790

    print(solution(15)) # 26
    print(solution(1000)) # 1366
    print(solution(5000)) # 6790
