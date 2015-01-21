#!/usr/bin/env python3

"""
Gain a better understanding of growth rates of various functions
Used for week 1 problem set questions
"""

import math

a = lambda n: n**2*math.log(n)
b = lambda n: 2**n
c = lambda n: 2**2**n
d = lambda n: n**math.log(n)
e = lambda n: n**2

for f in e, a, d, b, c:
    print("f: ", end="")
    for e in 1,5,10,100:
        try:
            print("{:2e}".format(f(e)), end=" ")
        except OverflowError:
            break
    print()
