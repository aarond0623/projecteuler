"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of abc.
"""

if __name__ == '__main__':
    for c in range(334, 1001): 
    # I have picked 334 as a start point because if a + b + c = 1000, then the
    # lowest the biggest number can be is 334.
        for b in range(2, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    print(a * b * c)
                    quit()
