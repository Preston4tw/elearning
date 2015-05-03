#!/usr/bin/env python3

"""
http://www.smashcompany.com/technology/embarrassing-code-i-wrote-under-stress-at-a-job-interview

Happy number sequence

Take each digit in a number and square it. Then add the sums together. Keep
doing this recursively. The sequence will either go to one or infinitely
"""

import sys # argv

def happy(number):
    numbers = str(number)
    total = 0
    for n in numbers:
        n = int(n)
        n_square = n**2
        total += n_square
    if total == 1:
        return 1
    return happy(total)

def main():
    input_number = sys.argv[1]
    try:
        output = happy(input_number)
    except RuntimeError as e:
        output = "infinity?: {}".format(e)
    print(output)

if __name__ == '__main__':
    main()
