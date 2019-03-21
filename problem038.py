"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""

from problem032 import is_pandigital, repeated_digits


def main():
    # Given we know that 918273645 is one known concatenated product and we
    # have to find the largest, any such largest must start with 9 as its first
    # digit, else it would not be bigger than the concatenated product of 9.
    # That means it must also start with 9, as the first product is interger*1.
    # We also know the max is 10000, otherwise we run out of digits.
    lst = list(range(1, 10000))
    lst = [x for x in lst if str(x)[0] == '9']
    # The number also cannot end in either a 5 or a 0, and cannot contain 0.
    # If it does it will die by either step 1 or 2.
    lst = [x for x in lst if '0' not in str(x)]
    lst = [x for x in lst if str(x)[-1] != '5']
    # We also can't have repeated digits.
    lst = [x for x in lst if not repeated_digits(x)]

    concat_products = []
    for n in lst:
        candidate = str(n)
        i = 2
        while not is_pandigital(candidate, 9):
            if repeated_digits(candidate):
                break
            candidate += str(i * n)
            i += 1
        else:
            concat_products.append(int(candidate))
    return max(concat_products)


if __name__ == '__main__':
    print(main())
