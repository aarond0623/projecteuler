"""Project Euler, Problem 64"""

from math import floor

def cont_sqrt(x):
    """Returns the continued fraction of the square root of a number."""
    m = 0
    d = 1
    a0 = floor(x ** 0.5)
    a = a0
    triplet_list = []
    frac_list = []
    if x ** 0.5 - a0 == 0:
        return (a0, frac_list)
    while True:
        triplet_list.append((m, d, a))
        m = d * a - m
        d = (x - m ** 2) / d
        a = floor((a0 + m) / d)
        if (m, d, a) in triplet_list:
            return (a0, frac_list)
        else:
            frac_list.append(a)

if __name__ == '__main__':
    answer = 0
    for i in range(2, 10001):
        if len(cont_sqrt(i)[1]) % 2 == 1:
            answer += 1
    print(answer)
