"""
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D = 13, the minimal solution in x is 649^2 - 13 * 180^2 = 1

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D = 5.

Find the value of D <= 1000 in minimal solutions of x for which the larget
value of x is obtained.
"""

from problem064 import cont_sqrt
from problem065 import cont_frac_convergent

def lagrange(n):
    """Uses Lagrange's method to find the minimal solution for Pell's equation.
    """
    if int(n ** 0.5) == n ** 0.5:
        return ()
    i = 0
    (x, y) = (0, 0)
    while x ** 2 - n * y ** 2 != 1:
        i += 1
        (x, y) = cont_frac_convergent(cont_sqrt(n), i)
    return (x, y)

if __name__ == '__main__':
    answer = 0
    largest = 0
    for ans in range(1001):
        try:
            x = lagrange(ans)[0]
            if x > largest:
                largest = x
                answer = ans
        except IndexError:
            pass

    print(answer)