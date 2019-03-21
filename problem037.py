"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from problem003 import prime_sieve, is_prime


def prime_generator(n):
    """Generates primes greater than n."""
    while True:
        if n%6 == 1:
            n += 4
        elif n%6 == 5:
            n += 2
        else:
            n += 1
        if is_prime(n):
            yield n


def truncatable_primes(limit=None):
    """Returns all truncatable primes up to limit, or optionally all 11."""
    # This is similar to the circular primes problem in that we can eliminate
    # a lot of primes that may have even numbers or 5s anywhere but the first
    # digit.
    primes = prime_sieve(limit) if limit else prime_sieve(1000000)
    digits = '024568'
    end_dg = '14689'
    primes = [x for x in primes if not any([d in str(x)[1:] for d in digits])]
    primes = [x for x in primes if not any([d in str(x)[0] for d in end_dg])]
    primes = [x for x in primes if not any([d in str(x)[-1] for d in end_dg])]
    primes = primes[4:]
    p_gen = prime_generator(1000000)
    trunc_primes = []

    i = 0
    while len(trunc_primes) < 11 and (i < len(primes) or not limit):
        try:
            p = str(primes[i])
        except IndexError:
            p = str(next(p_gen))
        for j in range(1, len(p)):
            if not is_prime(int(p[j:])) or not is_prime(int(p[:-j])):
                break
        else:
            trunc_primes.append(int(p))
        i += 1
    return trunc_primes


if __name__ == '__main__':
    print(sum(truncatable_primes()))
