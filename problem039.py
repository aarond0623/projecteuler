"""
If p is the perimeter of a right angle triangle with integral length sides,
{a, b, c}, there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p ≤ 1000 is the number of solutions maximized?
"""

def pythag_list(limit):
    """Generates all pythagorean triplets with c <= limit using Euclid's
    formula."""
    a, b, c = 0, 0, 0
    m = 2
    pythags = set()
    while c <= limit:
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            # Euclid's formula only catches all primitive pythagorean triples.
            # Any triple can be formed into a new one by scaling up the right
            # triangle they formed by k, where k is an integer.
            k = 1
            while k * c <= limit:
                triplet = tuple(sorted((k * a, k * b, k * c)))
                pythags.add(triplet)
                k += 1
        m += 1
    return list(pythags)


def right_triangle_list(perimeter):
    """Returns all right triangles less than or equal to a given perimeter."""
    return [x for x in pythag_list(perimeter) if sum(x) <= perimeter]


if __name__ == '__main__':
    triangles = [sum(x) for x in right_triangle_list(1000)]
    # Print the perimeter that occurs most often.
    print(max(set(triangles), key=triangles.count))
