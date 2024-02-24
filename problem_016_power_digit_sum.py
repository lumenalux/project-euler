"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

link: https://projecteuler.net/problem=16
"""


def cheating_solution(power: int, base: int = 2) -> int:
    return sum(map(int, str(base**power)))


class LargeNumber:
    DIGITS_IN_BUCKET: int = 6

    def __init__(self, number: int):
        self.separator: int = 10 ** self.DIGITS_IN_BUCKET
        self.number: list[float] = []
        while number > 0:
            self.number.append(float(number % self.separator))
            number //= self.separator

    def __add__(self, other: 'LargeNumber') -> 'LargeNumber':
        carry = 0.0
        result = LargeNumber(0)
        result.number = [0.0] * max(len(self.number), len(other.number))

        bucket_pairs = zip(self.number, other.number)
        for i, (bucket, other_bucket) in enumerate(bucket_pairs):
            addition = other_bucket + bucket + carry
            result.number[i] = float(addition % self.separator)
            carry = float(addition // self.separator)
        if carry:
            result.number.append(carry)

        return result

    def __mul__(self, other: 'LargeNumber') -> 'LargeNumber':
        result: 'LargeNumber' = LargeNumber(0)
        for i, bucket in enumerate(self.number):
            carry = 0.0
            for j, other_bucket in enumerate(other.number):
                addition = bucket * other_bucket + carry
                while i + j >= len(result.number):
                    result.number.append(0.0)

                result.number[i + j] += float(addition % self.separator)
                carry = float(addition // self.separator)

            while carry:
                result.number.append(float(carry % self.separator))
                carry = float(carry // self.separator)

        return result

    def __pow__(self, number: int) -> 'LargeNumber':
        result = LargeNumber(1)
        if number == 0:
            return result
        if number == 1:
            result.number = self.number.copy()
            return result

        squared = self * self
        if number % 2 == 0:
            return squared ** (number // 2)

        return self * (squared ** ((number - 1) // 2))

    def __str__(self) -> str:
        str_number = [str(int(bucket)).zfill(self.DIGITS_IN_BUCKET)
                      for bucket in self.number[::-1]]

        return ''.join(str_number).lstrip('0')


def solution(power: int, base: int = 2) -> int:
    return sum(map(int, str(LargeNumber(base) ** power)))


# test
if __name__ == '__main__':
    print(cheating_solution(15))  # 26
    print(cheating_solution(1000))  # 1366
    print(cheating_solution(5000))  # 6790
    # print(cheating_solution(100_000)) # Exceeds the limit

    print(solution(15))  # 26
    print(solution(1000))  # 1366
    print(solution(5000))  # 6790
    print(solution(100_000))  # 136357
