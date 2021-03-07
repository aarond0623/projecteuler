"""
Euler's Totient Function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8 are all less than nine and relatively
prime to nine, φ(9) = 6.

     n  Rel. Primes  φ(n)  n/φ(n)
     2            1   1      2
     3          1,2   2     1.5
     4          1,3   2      2
     5      1,2,3,4   4     1.25
     6          1,5   2      3
     7  1,2,3,4,5,6   6    1.166
     8      1,3,5,7   4      2
     9  1,2,4,5,7,8   6     1.5
    10      1,3,7,9   4     2.5

It can be seen that n = 6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from problem003 import prime_sieve


if __name__ == '__main__':
    # Euler's Totient Function is defined as n * ∏(1 - 1/p) where p are the
    # distinct primes of n.
    # The ratio n / φ(n) can thus be simplified to 1 / ∏(1 - 1/p), and
    # maximizes when the number of distinct primes is maximized.
    result = 1
    limit = 1000000
    primes = prime_sieve(200)
    for p in primes:
        result *= p
        if result > limit:
            print(result // p)
            break
