"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8 are all less than
nine and relatively prime to nine, φ(9) = 6.

The number 1 is considered to be relatively prime to every positive number, so
φ(1) = 1.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
""" 

# From Problem 69, we know that n / φ(n) = 1 / ∏(1 - 1/p). Since we are instead
# trying to minimize this value, we need a number with the fewest prime
# factors, and preferably should be large since larger values of p make our
# denominator larger.
#
# We cannot use a prime itself since φ(p) = p - 1, and thus it cannot be a
# permutation of p. Instead, we should search for numbers with two large prime
# factors, p1 * p2, where p1 and p2 are close to √(10^7) ≈ 3162

from problem003 import prime_sieve
from itertools import combinations

def is_perm(n1, n2):
    return sorted(list(str(n1))) == sorted(list(str(n2)))

if __name__ == '__main__':
    primes = [p for p in prime_sieve(5000) if p > 2000]
    numbers = list(combinations(primes, 2))

    # Because φ(n) = n * (1 - 1/p1) * (1 - 1/p2), and n = p1 * p2, we can
    # simplify the Totient function to
    # φ(n) = p1 * p2 * (1 - 1/p1) * (1 - 1/p2) = (1 - p1) * (1 - p2)

    minimum = float('inf')
    for p in numbers:
        n = p[0] * p[1]
        if n > 10 ** 7: continue
        T = (1 - p[0]) * (1 - p[1])
        if is_perm(n, T) and (n / T) < minimum:
            minimum = n / T
            answer = n
    print(answer)
