"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this way, we
note the following:

d[2]d[3]d[4] = 406 is divisible by 2
d[3]d[4]d[5] = 063 is divisible by 3
d[4]d[5]d[6] = 635 is divisible by 5
d[5]d[6]d[7] = 357 is divisible by 7
d[6]d[7]d[8] = 572 is divisible by 11
d[7]d[8]d[9] = 728 is divisible by 13
d[8]d[9]d[10] = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations
from problem003 import prime_sieve


def pandigital_list(max_digit, include_0 = False):
    """Returns a list of all pandigital numbers with digits less than or equal
    to max_digit, with the option of including zeroes."""
    first_digit = 0 if include_0 else 1
    digits = list(range(first_digit, max_digit + 1))
    digits = [str(x) for x in digits]
    pandigitals = list(permutations(digits))
    if include_0:
        pandigitals = [x for x in pandigitals if x[0] != '0']
    pandigitals = [int(''.join(x)) for x in pandigitals]
    return pandigitals


def main():
    # We're not going to worry about 2, 3, or 5--we can do that ourselves.
    primes = prime_sieve(17)[3:]
    pandigitals = pandigital_list(9, True)
    pandigitals = [x for x in pandigitals if str(x)[3] in '02468'] # 2
    pandigitals = [x for x in pandigitals if int(str(x)[2:5]) % 3 == 0] # 3
    pandigitals = [x for x in pandigitals if str(x)[5] in '05'] # 5
    for i in range(len(primes)):
        p = primes[i]
        pandigitals = [x for x in pandigitals if int(str(x)[i+4:i+7]) % p == 0]
    return sum(pandigitals)


if __name__ == '__main__':
    print(main())
