"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of abc.
"""

def product(mult_list):
    product = 1
    for mult in mult_list:
        product *= mult
    return product


def find_pythag_triplet_sum(triplet_sum):
    """Finds a pythagorean triplet summing to a certain number."""
    for c in range(triplet_sum // 3, triplet_sum + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2 and a + b + c == triplet_sum:
                    return(a, b, c)
    return False


if __name__ == '__main__':
    print(product(find_pythag_triplet_sum(1000)))
