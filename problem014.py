"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(number, steps=1):
    """Finds the number of steps required to reach 1 using the Collatz
    sequence."""
    if number < 1:
        raise ValueError("Number must be a positive integer.")
    if number == 1:
        return steps
    elif number % 2 == 0:
        return collatz(number / 2, steps+1)
    else:
        return collatz(3 * number + 1, steps+1)

def max_collatz(limit):
    """Finds the number with the largest Collatz chain under a certain limit.
    """
    collatz_dict = {}
    max_steps = 0
    for number in range(1, limit):
        steps = 0
        n = number
        while n != 1:
            if n in collatz_dict:
                steps += collatz_dict[n]
                break
            elif n % 2 == 0:
                n //= 2
                steps += 1
            else:
                n = n * 3 + 1
                steps += 1
        collatz_dict[number] = steps
        if steps > max_steps:
            max_steps = steps
            max_number = number
    return max_number

if __name__ == '__main__':
    print(max_collatz(1000000))
