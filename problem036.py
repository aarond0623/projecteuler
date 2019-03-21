"""The decimal number, 585 = 1001001001₂ (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeroes.)
"""

def main(max_n):
    palindromes = list(range(1, max_n))
    palindromes = [x for x in palindromes if str(x) == str(x)[::-1]]
    palindromes = [bin(x)[2:] for x in palindromes]
    palindromes = [x for x in palindromes if x == x[::-1]]
    palindromes = [int(x, 2) for x in palindromes]
    return sum(palindromes)


if __name__ == '__main__':
    print(main(1000000))