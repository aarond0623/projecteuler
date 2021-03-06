"""
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over 500 divisors?
"""

def factors(number):
    """Returns the factors of a number."""
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
        return
    factors = [1]
    if number != 1:
        factors.append(number)
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            factors.append(d)
            if number // d != d:
                factors.append(number // d)
    return sorted(factors)


def triangle_generator():
    """Generates triangle numbers."""
    triangle = 1
    number = 1
    while True:
        yield triangle
        number += 1
        triangle += number


def triangle_divisors(n):
    """Finds the first triangle number with n divisors."""
    triangle = triangle_generator()
    t = next(triangle)
    while len(factors(t)) < n:
        t = next(triangle)
    return t


if __name__ == '__main__':
    print(triangle_divisors(500))