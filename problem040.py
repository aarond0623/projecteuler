"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the nth digit of the fractional part, find the value of the
following expression.

d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

from math import log10


def champernowne_spigot(pos):
    """Returns the digit of a certain position in the fractional part of 
    Champernowne's constant."""
    # The length of the 1-digit section is 9, then the 2-digit section is
    # 2 * 90, the 3-digit 3 * 900 and so on. We can isolate just our section by
    # subtracting off the length of all previous sections using log10.
    section = 0
    max_n = 0
    while max_n < pos:
        new_pos = pos - max_n
        max_n += (section + 1) * 9 * 10 ** section
        section += 1
    pos = new_pos - 1
    section = section - 1
    number = int(pos / (section + 1)) + 10 ** section
    return int(str(number)[pos % (section + 1)])


if __name__ == '__main__':
    result = 1
    for i in range(0, 7):
        result *= champernowne_spigot(10 ** i)
    print(result)