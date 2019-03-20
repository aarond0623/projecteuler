"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial


def factorial_digits():
    """Returns a list of all numbers that are equal to the factorial of their
    digits."""

    # Any such number must be less than 8 digits long, because 9! * 8 is only
    # 7 digits long. The upper limit specifically is 9! * 7.

    factorial_list = []
    for n in range(3, factorial(9) * 7):
        digit_sum = 0
        for digit in str(n):
            digit_sum += factorial(int(digit))
            # We can break as soon as we exceed the number.
            if digit_sum > n:
                break
        else:
            if n == digit_sum:
                factorial_list.append(n)
    return factorial_list


if __name__ == '__main__':
    print(sum(factorial_digits()))

