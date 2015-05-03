#!/usr/bin/env python3

"""
http://www.smashcompany.com/technology/embarrassing-code-i-wrote-under-stress-at-a-job-interview

Happy number sequence

Take each digit in a number and square it. Then add the sums together. Keep
doing this recursively. The sequence will either go to one or infinitely

If the sequence goes infinitely it loops over a finite set of numbers. If the
same number is ever seen twice the recursion can end.
"""

import sys # argv

def happy(number, seen_numbers=None):
    if not seen_numbers:
        seen_numbers = {}
    if number in seen_numbers:
        return "recurses infinitely"
    seen_numbers[number] = 1
    numbers = str(number)
    total = 0
    for n in numbers:
        n = int(n)
        n_square = n**2
        total += n_square
    if total == 1:
        return "to 1"
    return happy(total, seen_numbers)

def main():
    input_number = sys.argv[1]
    try:
        output = happy(input_number)
    except RuntimeError as e:
        output = "{}".format(e)
    print("{}: {}".format(input_number, output))

if __name__ == '__main__':
    main()
