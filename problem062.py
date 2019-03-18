"""Project Euler, Problem 62"""

import itertools

def largest_perm(number):
    """Returns the largest permutation of a given number."""
    return int(''.join(sorted(str(number))[::-1]))

n = 345
cubes = {}
while True:
    try:
        cubes[largest_perm(n ** 3)].append(n ** 3)
    except KeyError:
        cubes[largest_perm(n ** 3)] = [n ** 3]
    if len(cubes[largest_perm(n ** 3)]) >= 5:
        break
    n += 1

print(cubes[largest_perm(n ** 3)][0])
