"""
Common functions for use in Project Euler problems.
"""


def factors(number):
    """Returns the factors of a number."""
    try:
        if int(number) != float(number):
            raise ValueError("number was not an integer.")
        elif int(number) < 1:
            raise ValueError("number was not positive.")
        else:
            number = int(number)
    except (TypeError, ValueError) as err:
        print("ERROR: argument must be a positive integer.")
        print("%s: %s" % (type(err).__name__, err))
        return
    factors = [1]
    if number != 1:
        factors.append(number)
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            factors.append(d)
            if number // d != d:
                factors.append(number // d)
    return sorted(factors)


def nth_prime(position):
    """Returns the nth prime number."""
    from math import log
    try:
        if int(position) != float(position):
            raise ValueError("number was not an integer.")
        elif int(position) < 1:
            raise ValueError("number was not positive.")
        else:
            position = int(position)
    except (TypeError, ValueError) as err:
        print("ERROR: argument must be a positive integer.")
        print("%s: %s" % (type(err).__name__, err))
        return
    small_primes = [2, 3, 5, 7, 11, 13, 17]
    if position < 8:
        return small_primes[position - 1]
    max_p = position * log(position)
    max_p += position * log(log(position))
    primes = prime_sieve(max_p)
    return primes[position - 1]
