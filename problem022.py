"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

from string import ascii_uppercase


def score_name(name):
    letters = {}
    position = 0
    for letter in ascii_uppercase:
        position += 1
        letters[letter] = position
    score = 0
    for letter in name:
        score += letters[letter]
    return score


if __name__ == '__main__':
    file = 'problem022.txt'
    total = 0
    names = sorted(open(file).read().strip('"').split('","'))
    for i in range(len(names)):
        total += score_name(names[i]) * (i + 1)
    print(total)