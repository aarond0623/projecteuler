"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from problem003 import prime_factors


def product(mult_list):
    product = 1
    for mult in mult_list:
        product *= mult
    return product


def simplify_fraction(numerator, denominator):
    """Simplifies a fraction given in (numerator, denominator) to simplest
    terms."""
    num_factors = prime_factors(numerator)
    den_factors = prime_factors(denominator)

    for n in range(len(num_factors)):
        if num_factors[n] in den_factors:
            den_factors.remove(num_factors[n])
            num_factors[n] = 1

    return (product(num_factors), product(den_factors))


def naive_simplify(numerator, denominator):
    """Simplifies a fraction in the naive way described above."""
    num_digits = [int(x) for x in list(str(numerator))]
    den_digits = [int(x) for x in list(str(denominator))]

    for digit in range(len(num_digits)):
        if num_digits[digit] in den_digits:
            den_digits.remove(num_digits[digit])
            num_digits[digit] = None

    num_digits = [x for x in num_digits if x is not None]

    try:
        numerator = int("".join([str(x) for x in num_digits]))
        denominator = int("".join([str(x) for x in den_digits]))
    except ValueError:
        return (0, 0)

    return (numerator, denominator)




if __name__ == '__main__':
    numerators = []
    denominators = []
    for d in range(1, 99):
        for n in range(1, d):
            if n % 10 == 0 and d % 10 == 0:
                continue
            simp_frac = simplify_fraction(n, d)
            naive_frac = naive_simplify(n, d)
            if naive_frac == (n, d):
                continue
            try:
                if 0 in naive_frac:
                    raise ValueError
                if simp_frac == simplify_fraction(*naive_frac):
                    numerators.append(n)
                    denominators.append(d)
            except ValueError:
                continue
    print(simplify_fraction(product(numerators), product(denominators))[1])