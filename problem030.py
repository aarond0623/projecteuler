"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
8204 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of the fifth
powers of their digits.
"""


def sum_fifth_powers(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 5
    return total


if __name__ == '__main__':
    total = 0
    for n in range(2, 999999):
        if n == sum_fifth_powers(n):
            total += n
    print(total)
