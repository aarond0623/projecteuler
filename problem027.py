"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, -79 and
1601, is -126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""

from problem003 import prime_sieve, is_prime


if __name__ == '__main__':
    b_list = prime_sieve(1000) # Because f(0) = b, so b must be prime.
    # Further, when n = 1, p + 1 + even number will produce a non-prime. So a
    # must be odd. The only exception would be if b = 2, in which case if n = 2,
    # n² = 4 and a must again be odd to produce any more primes.
    a_list = [x for x in list(range(-999,1000)) if x % 2 == 1]
    max_length, max_a, max_b = 0, 0, 0
    for a in a_list:
        for b in b_list:
            n = 0
            while is_prime(n ** 2 + a * n + b):
                n += 1
            if n > max_length:
                max_length = n
                max_a = a
                max_b = b
    print(max_a * max_b)
