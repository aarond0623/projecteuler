"""
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagons is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

# Expanding the spiral a bit, a pattern emerges:
#
# 73 74 75 76 77 78 79 80 81
# 72 43 44 45 46 47 48 49 50
# 71 42 21 22 23 24 25 26 51
# 70 41 20  7  8  9 10 27 52
# 69 40 19  6  1  2 11 28 53
# 68 39 18  5  4  3 12 29 54
# 67 38 17 16 15 14 13 30 55
# 66 37 36 35 34 33 32 31 56
# 65 64 63 62 61 60 59 58 57
#
# SE = 2, 10, 18, 26
# SW = 4, 12, 20, 28
# NW = 6, 14, 22, 30
# NE = 8, 16, 24, 32
# That is, the NE spiral counts up by 8s + 1, with the other spirals decreasing
# their count by 2, 4, and 6. The reason for this can be seen. For the first
# spiral, we must form a 3x3 grid to suround the 1x1 grid, thus the number of
# spaces used is 3² - 1² = 8. The same for the next level which is 5² - 3² = 16.
# Generalized the equation for number of positions for a n x n grid is
# n² - (n - 2)² which can be simplified to 4n - 4, and using only odd numbers,
# this becomes multiples of 8.


def diagonal_generator(offset, max):
    lst = [1]
    while lst[-1] < max ** 2:
        lst.append(lst[-1] + len(lst) * 8 - offset)
    if lst[-1] > max ** 2:
        del lst[-1]
    return lst


def sum_diagonals(size):
    SE = diagonal_generator(6, size)[1::] # Otherwise 1 will be counted 4x.
    SW = diagonal_generator(4, size)[1::]
    NW = diagonal_generator(2, size)[1::]
    NE = diagonal_generator(0, size)
    return sum(SE) + sum(SW) + sum(NW) + sum(NE)


if __name__ == '__main__':
    print(sum_diagonals(1001))
