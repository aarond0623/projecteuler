"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
"""

from problem003 import prime_sieve


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


if __name__ == '__main__':
    print(nth_prime(10001))
