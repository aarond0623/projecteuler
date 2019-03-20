"""
The cube, 41063625 (345^3), can be permuted to provide two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""


def largest_perm(number):
    """Returns the largest permutation of a given number."""
    return int(''.join(sorted(str(number))[::-1]))


def permutation_cube(perms):
    """Returns the smallest cube that can be represented as cubes in exactly
    perms permutations."""
    n = 1
    cubes = {}
    while True:
        try:
            cubes[largest_perm(n ** 3)].append(n ** 3)
        except KeyError:
            cubes[largest_perm(n ** 3)] = [n ** 3]
        if len(cubes[largest_perm(n ** 3)]) >= perms:
            break
        n += 1
    return cubes[largest_perm(n ** 3)][0]


if __name__ == '__main__':
    print(permutation_cube(5))
