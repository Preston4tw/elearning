#!/usr/bin/env python3

"""
data: https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt

The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications). The file contains 1
million integers, both positive and negative (there might be some
repetitions!).This is your array of integers, with the ith row of the file
specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the input
file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line
addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space
provided.


OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your
own hash table for it. For example, you could compare performance under the
chaining and open addressing approaches to resolving collisions.
"""

def main():
    """
    This problem and its solution seems fairly straight forward.

    Create a hash. Take the input integer array and for each integer x present,
    set hash[x] = 1. Then, Iterate over every integer x in the hash. For each
    integer x there are 20000 possible numbers y that satisfy x+y=t, where t is
    the range -10000 to 10000.  Using a little algebra, subtract x from both
    sides and y=t-x. Let t be the bottom end of the range, -10000. We can then
    just do 20k lookups starting from the bottom end of the range all the way to
    the top.

    If any lookup is successful, verify x and y are distinct, and then set the
    value of the number t in an answer hash to 1.

    To get the answer to the problem, return the number of keys in the answer
    hash.
    """
    filename = '2sum.txt'
    with open(filename) as f:
        data = f.readlines()
    integer = {}
    for line in data:
        integer[int(line)] = 1

    answers = {}
    for x in integer:
        t = -10000
        for i in range(20000):
            y = t - x
            if y in integer:
                if x != y:
                    answers[t] = 1
                    print("x: {}, y: {}, t: {}, len(answers): {}".format(x, y,
                        t, len(answers)))
            t += 1
    print(len(answers)) # 427

if __name__ == '__main__':
    main()
