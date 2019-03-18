"""
Starting at the top left corner of a 2x2 grid, and only be able to move to the
right and down, there are exactly 6 routes to the bottom right corner.

┍━┯━┓ ┍━┱─┐ ┍━┱─┐
├─┼─┨ ├─╄━┪ ├─╂─┤
└─┴─┚ └─┴─┚ └─┺━┙
┎─┬─┐ ┎─┬─┐ ┎─┬─┐
┡━┿━┪ ┡━╅─┤ ┠─┼─┤
└─┴─┚ └─┺━┙ ┗━┷━┙

How many such routes are there through a 20x20 grid?
"""

# Consider a square 5x5 grid. The number of paths along the edges is only 1.
#
# 1  1  1  1  1
# 1
# 1
# 1 
# 1
#
# The number of paths to the next diagonal is 2--through either of the ones.
#
# 1  1  1  1  1
# 1  2 
# 1
# 1
# 1
#
# This is true for the rest of the grid as well; The number of paths to a node
# is the sum of the previous two nodes connecting backwards:
#
# 1  1  1  1  1
# 1  2  3  4  5
# 1  3  6 10 15
# 1  4 10 20 35
# 1  5 15 35 70
#

def grid_paths(n):
    # Initialize the grid.

    # An n x n grid contains n + 1 columns and rows of paths.
    n += 1
    array = []
    list = []
    for column in range(0,n):
        list.append(1)
    array.append(list)
    list = [1]
    for column in range(0, n-1):
        list.append(0)
    for row in range(0, n-1):
        array.append(list)
    # Begin arithmetic
    for y in range(1,n):
        for x in range(1,n):
            array[y][x] = array[y][x-1] + array[y-1][x]
    return array[n-1][n-1]

if __name__ == '__main__':
    print(grid_paths(20))
    
            