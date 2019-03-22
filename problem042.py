"""
The nth term of the sequence of triangle numbers is given by,
t[n] = 1/2 n(n + 1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing two-thousand common English words,
how many are triangle words?
"""

from problem022 import score_name


def main(file):
    words = open(file).read().strip('"').split('","')
    word_scores = [score_name(x) for x in words]
    word_scores = [x for x in word_scores if ((8 * x + 1) ** 0.5) % 2 == 1]
    return word_scores


if __name__ == '__main__':
    print(len(main('problem042.txt')))