"""
The square root of 2 can be written as an infinite continued fraction.

√2 = 1 + 1
        /2 + 1
            /2 + 1
                /2 + 1
                    /2...

The infinite fraction can be written √2 = [1; (2)], (2) indicates that 2
repeats ad infinitum. In a similar way, √23 = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents of √2.

1 + 1/2 = 3/2
1 + 1/(2 + 1/2) = 7/5
1 + 1/(2 + 1/(2 + 1/2)) = 17/12
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

Hence the sequence of the first ten convergents of √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that teh important mathematical constant,
e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms of the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/17, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

from itertools import cycle, islice

def e_cont_frac(n):
    """Returns the continued fraction of e to the nth term."""
    root = 2
    frac_list = []
    for i in range(0, n-1):
        if i % 3 == 1:
            frac_list.append(2 * (i // 3 + 1))
        else:
            frac_list.append(1)
    return (2, frac_list)

def cont_frac_convergent(cont_frac, l=0):
    """Returns the convergent of a given continued fraction in form (a, b)
    where the convergent is equal to a/b."""
    l -= 1
    if l > len(cont_frac[-1]):
        frac_list = list(islice(cycle(cont_frac[-1]), l))
    elif l == -1:
        frac_list = cont_frac[-1] 
    else:
        frac_list = cont_frac[-1][0:l]
    try:
        convergent = [1, frac_list[-1]]
    except IndexError:
        return (cont_frac[0], 1)
    for term in frac_list[-2::-1]:
        (convergent[0], convergent[1]) = (term * convergent[1] + convergent[0],
                                          convergent[1])
        convergent = convergent[::-1]
    return (cont_frac[0] * convergent[1] + convergent[0], convergent[1])

if __name__ == '__main__':
    numerator = cont_frac_convergent(e_cont_frac(100), 100)[0]
    total = 0
    for digit in str(numerator):
        total += int(digit)
    print(total)