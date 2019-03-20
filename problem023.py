"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is caled abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smalest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all positive integers which cannot be written as the sum of two
abundant numbers.
"""

from problem012 import factors


def is_abundant(number):
    """Returns True if a number is abundant."""
    return sum(factors(number)) - number > number


def all_nonabundant_sums():
    """Returns a list of all the numbers that cannot be expressed as the sum of
    two abundant numbers."""
    # All numbers greater than 28123 can be expressed as the sum of two
    # abundant numbers.
    max_n = 28123
    abundants = [x for x in range(1, max_n+1) if is_abundant(x)]
    sums = set()
    for i in range(len(abundants)):
        a = abundants[i]
        for j in range(i, len(abundants)):
            b = abundants[j]
            if a + b <= max_n:
                sums.add(a + b)
    return set(range(1, max_n+1)) - sums

if __name__ == '__main__':
    print(sum(all_nonabundant_sums()))
