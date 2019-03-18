"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from random import randrange


def is_prime(number):
    """Determines if a number is prime or not."""
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if number < 2:
        return False
    for prime in small_primes:
        if number < prime * prime:
            return True
        if number % prime == 0:
            return False
    r, s = 0, number - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(5):
        a = randrange(2, number - 1)
        x = pow(a, s, number)
        if x == 1 or x == number - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True


def prime_sieve(max_p):
    """Generates a list of primes less than or equal to some max_p."""
    try:
        max_p = int(max_p)
    except (TypeError, ValueError) as err:
        print("ERROR: argument must be a positive real number.")
        print("%s: %s" % (type(err).__name__, err))
        return
    if max_p < 2:
        return []
    primes = dict()
    for i in range(2, max_p + 1):
        primes[i] = True

    for p in primes:
        factors = range(p, max_p + 1, p)
        for f in factors[1:]:
            primes[f] = False
    return [p for p in primes if primes[p] == True]


def prime_factors(number):
    """Returns the prime factors of a number."""
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
    if number == 1:
        return []
    primes = prime_sieve(int(number ** 0.5) + 1)
    factors = []
    while number > 1:
        for p in primes:
            if is_prime(number):
                factors.append(number)
                number = 1
                break
            while number % p == 0:
                factors.append(p)
                number //= p
    return sorted(factors)


def largest_prime_factor(number):
    """
    Finds the largest prime factor of a number.
    """
    factors = prime_factors(number)
    return factors[len(factors) - 1]


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
