"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sum_of_squares(min_n, max_n):
    """Finds the sum of the squares of a range of numbers."""
    total = 0
    for i in range(min_n, max_n + 1):
        total += i**2
    return total


if __name__ == '__main__':
    print(sum(range(1, 101)) ** 2 - sum_of_squares(1, 100))
