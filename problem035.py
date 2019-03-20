"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

from problem003 import prime_sieve


def circular_primes(limit):
    """Returns a list of circular primes up to limit."""
    

    # We can remove any prime that contains any even numbers and every prime
    # that contains a 5.

    if limit > 5:
        primes = prime_sieve(limit)[3:]
        digits = '024568'
        primes = [x for x in primes if not any([d in str(x) for d in digits])]
        primes = [2, 3, 5] + primes
    else:
        return [x for x in [2, 3, 5] if x <= limit]

    for i in range(len(primes)):
        p = str(primes[i])
        test = []
        for j in range(1, len(p)):
            if p == '0':
                break
            if int(p[j:] + p[:j]) not in primes:
                primes[i] = 0
                for fail in test:
                    primes[primes.index(fail)] = 0
                break
            else:
                test.append(int(p[j:] + p[:j]))
    return [x for x in primes if x != 0]


if __name__ == '__main__':
    print(len(circular_primes(1000000)))
