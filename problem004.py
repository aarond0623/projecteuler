"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome_product(min_product, max_product):
    """
    Finds the largest product of two numbers between min_product and max_product
    that is also a palindrome.
    """
    largest = 0
    for product1 in range(min_product, max_product + 1):
        for product2 in range(min_product, max_product + 1):
            if (str(product1 * product2) == str(product1 * product2)[::-1] and
                    product1 * product2 > largest):
                largest = product1 * product2
    return largest

if __name__ == '__main__':
    print(largest_palindrome_product(100, 999))
