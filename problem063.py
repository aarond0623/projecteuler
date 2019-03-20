"""
The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def n_digit_nth_power(n):
    """Returns a list of numbers n digits long that are also represented as
    numbers raised to the nth power."""
    power_numbers = []

    # Any n-digit number that can be expressed as a number to the nth power
    # must have a number less than 10 as its base. This is because 10 to the
    # power of n always has n + 1 digits, and any number greater than 10 will
    # have that many digits or more.

    for base in range(1, 10):
        if len(str(base ** n)) == n:
            power_numbers.append(base ** n)
        elif len(str(base ** n)) > n:
            # As soon as the digits are longer than n, we can break.
            break
    return power_numbers


def main():
    power_numbers = []

    # Further, this means that whenever the lowest n-digit number, 10^(n - 1),
    # when raised to the power of 1/n, is greater than 9, that number cannot be
    # expressed simultaneously with a number less than 9 as the base and with
    # n as an exponent. This limits our search.

    n = 1
    while (10 ** (n - 1)) ** (1 / n) <= 9:
        power_numbers += n_digit_nth_power(n)
        n += 1
    return power_numbers


if __name__ == '__main__':
    print(len(main()))
