"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from problem003 import is_prime


def pandigital_generator(start=1, backwards=False):
    """Generates pandigital numbers, optionally starting with a certain number
    of digits and optionally going backwards."""
    skip = -1 if backwards else 1
    while 0 < start < 10:
        perms = list(permutations(range(1, start+1)))
        pandigitals = [int(''.join(str(d) for d in x)) for x in perms]
        for n in pandigitals[::skip]:
            yield n
        start += skip


def largest_pandigital_prime():
    # The prime cannot have 9 digits, because the sum of the numbers 1 through
    # 9 is divisible by 9, and hence will never be prime. The same logic holds
    # for 8, as eliminating 9 from a number divisible by 9 is still divisible.
    pandigitals = pandigital_generator(7, True)
    while True:
        p = next(pandigitals)
        if str(p)[-1] in '024568':
            continue
        if is_prime(p):
            break
    return p


if __name__ == '__main__':
    print(largest_pandigital_prime())