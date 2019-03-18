"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""

from problem003 import prime_factors


def lcm_up_to(number):
    """Returns the least common multiple of all numbers of a limit."""
    multiply = []
    for n in range(2, number):
        factors = prime_factors(n)
        for f in factors:
            while factors.count(f) > multiply.count(f):
                multiply.append(f)
    product = 1
    for m in multiply:
        product *= m
    return product


if __name__ == '__main__':
    print(lcm_up_to(20))
