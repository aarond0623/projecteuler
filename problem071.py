"""
Consider the fraction n/d, where n and d are positive integers. If n < d and
HCF(n, d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.
"""

# We will generalize the problem as this: for any number n, find the closest
# fraction with denominator = d that is less than n.
# 
# This problem is the same as solving for floor(x) in:
# x / d = n     x = floor(n * d)

from math import floor


def closest_fraction(n, d):
    return floor(n * d)

# We can't just end here, though. My immediate thought was that since 3/7 =
# 428571/999999 (because it is a repeating decimal), that because 428571/10^6
# was both smaller and part of a fraction with the smallest increments, that
# must be the answer. But it isn't. Making the numerator smaller decreases the
# fraction, but making the denominator smaller increases the fraction, so it is
# possible to combine those effects and create a fraction closer to 3/7. It
# does, however, make sense to start with larger denominators.

def left_fraction(n, limit):
    closest_delta = float('inf')
    for d in range(limit, 0, -1):
        x = floor(n * d)
        delta = abs(n - x/d)
        # We have to check if the delta is zero, since we want the fraction to
        # the left, and the delta of 428571/999999 will be 0.
        if delta < closest_delta and delta != 0:
            closest_delta = delta
            closest = (x, d)
    return closest

if __name__ == '__main__':
    print(left_fraction(3/7, 10**6))
