"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all amicable numbers under 10000.
"""

from problem012 import factors

def sum_amicable_numbers(n):
    amicable = []
    numbers = list(range(6,n))
    for number in numbers:
        pair = sum(factors(number)) - number
        if number != pair and sum(factors(pair)) - pair == number and pair < n:
            amicable.append(number)
            amicable.append(pair)
            numbers.remove(pair)
    return sum(amicable)


if __name__ == '__main__':
    print(sum_amicable_numbers(10000))
    