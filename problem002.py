"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibonacci(position):
    """
    Returns the Fibonacci number in a certain position.
    """
    fib1, fib2 = 1, 1
    for _ in range(position - 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1

def sum_of_fibs(max_n):
    """Returns the sum of all Fibonacci numbers less than max_n."""
    i = 3
    total = 0
    while True:
        fib = fibonacci(i)
        if fib > max_n:
            break
        else:
            total += fib
            i += 3
    return total

if __name__ == '__main__':
    print(sum_of_fibs(4000000))
