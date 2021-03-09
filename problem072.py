"""
Consider the fraction n/d where n and d are positive integers. If n < d and
HCF(n, d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements could be contained in the set of reduced proper fractions for
d <= 1,000,000?
"""

# Sequences of reduced fractions with denominator d <= n are called Farey
# sequences. The length of a Farey sequence for n is related ot Euler's Totient
# function φ(n):
#
# len(F(n)) = len(F(n - 1)) + φ(n)
#
# See problem 69 for more about Euler's Totient.

from problem003 import prime_factors, prime_sieve
from math import prod


def euler_totient_list(limit):
    """Generates a list of Euler's totient solutions for numbers up to n."""
    # Generating Euler's Totient's from 1 to 1,000,000 is a very hard problem
    # unless we are clever about how we're doing it. At one point, this program
    # was finding distinct prime factors and then raising the factors to powers
    # in an attempt to reduce the workload. However, even that was too slow.
    # Fortunately, there is a more clever and better way of doing this through
    # a sieve-like function.
    #
    # Consider the list of numbers from 0 to n, so that the index matches n:
    #
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
    #
    # The distinct prime factors are thus:
    #
    # [(0), (1), (2), (3), (2), (5), (2, 3), (7), (2), (3), (2, 5), ...]
    #
    # For each number, we must 
    totients = [0, 1] + [None] * (limit - 1)
    # The totient of a prime is always p - 1.
    primes = prime_sieve(limit)
    for p in primes:
        totients[p] = p - 1
    n = 2
    # Not using a for loop so that instead of checking it an item is in the
    # list every time, we can skip to the next None item.
    while True:
        print(n)
        # Don't calculate the totient if it has already been found.
        factors = list(set(prime_factors(n)))
        # Partial totient, since the totient depends on the value of n.
        p_totient = prod([1 - 1/x for x in factors])
        totients[n] = int(n * p_totient)
        powers = len(factors) * [1]
        i = len(factors) - 1
        # Iterate through powers by increasing until we go over the limit, then
        # changing place values. If we run out of place values, we end the
        # loop.
        while (i >= 0):
            powers[i] += 1
            new_n = prod([pow(*x) for x in zip(factors, powers)])
            if new_n > limit:
                powers[i] = 1
                i -= 1
            else:
                totients[new_n] = int(new_n * p_totient)
                i = len(factors) - 1
        try:
            # Go to next None item.
            n = totients[n:].index(None) + n
        except ValueError:
            # If there isn't one...
            break
    # Don't include 0 on return.
    return totients[1:]


def farey(n)
    # Usually, F(1) is defined as 2, with 0/1 and 1/1. However, this problem
    # does not include 0/1 or 1/1, so instead we will defined F(1) = 0.
    total = 0
    for i in range(2, n + 1):
        total += euler_totient(i)
    return total
    # The recursive function goes way too deep.
    # if n == 1:
    #     return 0
    # else:
    #     return farey(n - 1) + euler_totient(n)
