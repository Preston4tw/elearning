#!/usr/bin/python3

# Write a function to reverse a string
def reverse_string(string):
    new_string = ""
    # Damn off-by-one errors
    for i in range(len(string)):
        new_string += string[-i-1]
    return new_string

# Write a function to compute fibonacci numbers
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Print out the grade school multiplication tables
def multiplication_tables(low=1, high=12):
    for i in range(low,high+1):
        for j in range(low,high+1):
            print(i*j, end="\t")
        print()

# Sum integers from a text file, one per line
def sum_integers(filename):
    fh = open(filename)
    data = fh.readlines()
    i = 0
    for line in data:
        i = int(line)
        total += i
    return total

# Print odd numbers from 1 to 99
def print_odds():
    for i in range(1,100,2):
        print(i)

# Find the largest int value in an array
def find_max(int_array):
    largest_int = int_array[0]
    for i in int_array[1:]:
        if i > largest_int:
            largest_int = i
    return largest_int

# Convert a three integer RGB value to hex
# ex. (255,0,17) to 0xff0011
def rgb_int_to_hex(rgb):
    # Lets assume we're given a three digit tuple
    pass

# Find the most frequently occurring number in a list (the mode)
def find_mode(int_list):
    h = {}
    for n in int_list:
        if not h[n]:
            h[n] = 1
        else:
            h[n] += 1
    max_occur = -1
    max_occur_int = None
    for k,v in h.items()
        if v > max_occur:
            max_occur_int = k
            max_occur = v
    return max_occur_int
