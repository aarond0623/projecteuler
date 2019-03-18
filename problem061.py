import math
import itertools

def polygon(p, n):
    """Generates the nth polygonal number for polygon p."""
    return n * ((p - 2) * n + (4 - p)) // 2

def polygon_finder(p, x):
    """Finds the position of the smallest polygon p number greater than x."""
    n = ((p - 4) + ((4 - p) ** 2 - 4 * (p - 2) * -2 * x) ** 0.5) / (2 * p - 4)
    return math.ceil(n)

def check_cyclic(a, b, n):
    """Checks if b is cyclic with a to n digits."""
    a_cycle = a % 10 ** n
    b_cycle = b // 10 ** max((math.ceil(math.log10(b)) - n), 0)
    if a_cycle == b_cycle:
        return True
    else:
        return False

def find_index(n, l):
    """Finds the first index of a number in a sorted list that is greater than
    n."""
    return next(x[0] for x in enumerate(l) if x[1] >= n)

def poly_cyclic(x, p, n):
    """Returns True if there exists a polygon that is cyclic with n in list
    p to n digits."""
    d = x % 10 ** n
    i = find_index(d * 10 ** n, p)
    if p[i] >= (d + 1) * 10 ** n:
        return []
    return p[i:find_index((d + 1) * 10 ** n, p)]

def process_cyclicals(array, length):
    for item in array:
        for number in poly_cyclic(
          item[length-2], polygons[perm_list[length-1]], 2):
            item.append(number)
    array = [x for x in array if len(x) == length]
    if length == 6:
        for match in array:
            if len(match) == 6:
                matches.append(match)
    return array


polygons = []
for p in range(3, 9):
    polygons.append([polygon(p, x) for x in range(polygon_finder(p, 1000),
                                                  polygon_finder(p, 10000))])

permutations = list(itertools.permutations(range(0, 6)))

matches = []
for perm_list in permutations:
    cycles = []
    p = polygons[perm_list[0]]
    for item in p:
        for number in poly_cyclic(item, polygons[perm_list[1]], 2):
            cycles.append([item, number])
    for n in range(3, 7):
        cycles = process_cyclicals(cycles, n)

matches = [x for x in matches if check_cyclic(x[-1], x[0], 2)]

print(matches[0])
print(sum(matches[0]))
