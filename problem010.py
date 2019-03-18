"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all primes below two million.
"""

from problem003 import prime_sieve

if __name__ == '__main__':
    print(sum(prime_sieve(2000000)))
