"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from problem012 import factors


def is_pandigital(number, n):
    """Returns true if a number is pandigital from 1 to n and false otherwise.
    """

    if len(str(number)) != n:
        return False
    else:
        number = list(str(number))
        for digit in range(1, n+1):
            try:
                number.remove(str(digit))
            except ValueError:
                return False
        if len(number) > 0:
            return False
        return True


def repeated_digits(number):
    """Returns true if a number has digits that are repeated."""
    number = list(str(number))
    for digit in range(1, 10):
        try:
            number.remove(str(digit))
        except ValueError:
            pass
    if len(number) > 0:
        return True
    return False


def pandigital_products(digits):
    """Finds all numbers that can be represented as a pandigital multiplcation
    problem with n digits."""
    pandigital_list = []
    # The max number can only have digits//2 digits, or else you run out of
    # digits for the equation itself.
    for n in range(1, 10**(digits//2 + 1)):
        # Zero can't be in the pandigital number, and it can't have repeated
        # digits.
        if '0' in str(n) or repeated_digits(n):
            continue
        factor_list = factors(n)
        # Remove any factors that have the same digits.
        for i in range(len(factor_list)):
            for digit in str(factor_list[i]):
                if digit in str(n):
                    factor_list[i] = 0
                    factor_list[len(factor_list) - 1 - i] = 0
        factor_list = [x for x in factor_list if x != 0]
        # Test if the equation is pandigital
        for i in range(len(factor_list)//2):
            a = str(factor_list[i])
            b = str(factor_list[len(factor_list) - 1 - i])
            c = str(n)
            if is_pandigital(a + b + c, digits):
                pandigital_list.append(int(c))
                break
    return pandigital_list


if __name__ == '__main__':
    print(sum(pandigital_products(9)))

