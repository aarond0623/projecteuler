"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hunred and forty-
two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def number_to_words(n):
  """Returns a number in words for any number up to 1000."""
    words = {
                1 : "one",
                2 : "two",
                3 : "three",
                4 : "four",
                5 : "five",
                6 : "six",
                7 : "seven",
                8 : "eight",
                9 : "nine",
               10 : "ten",
               11 : "eleven",
               12 : "twelve",
               13 : "thirteen",
               14 : "fourteen",
               15 : "fifteen",
               16 : "sixteen",
               17 : "seventeen",
               18 : "eighteen",
               19 : "nineteen",
               20 : "twenty",
               30 : "thirty",
               40 : "forty",
               50 : "fifty",
               60 : "sixty",
               70 : "seventy",
               80 : "eighty",
               90 : "ninety",
              100 : "hundred",
             1000 : "thousand"
            }
    if n <= 20:
        return words[n]
    elif n < 100:
        word = words[n // 10 * 10]
        if n % 10 != 0:
            word = word + "-" + words[n % 10]
        return word
    elif n < 1000:
        word = words[n // 100] + " " + words[100]
        if n % 100 != 0:
            word += " and "
            n %= 100
            if n <= 20:
                word += words[n]
            else:
                word += words[n // 10 * 10]
                if n % 10 != 0:
                    word = word + "-" + words[n % 10]
        return word
    else:
        return "one thousand"

if __name__ == '__main__':
    total = 0
    for n in range(1, 1001):
        total += len(number_to_words(n).replace(" ","").replace("-",""))
    print(total)