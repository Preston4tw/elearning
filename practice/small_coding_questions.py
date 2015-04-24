#!/usr/bin/python3

# Write a function to reverse a string
def reverse_string(string):
    new_string = ""
    # Damn off-by-one errors
    for i in range(len(string)):
        new_string += string[-i-1]
    return new_string

# Write a function to compute fibonacci numbers
def fib():
    pass

# Print out the grade school multiplication tables
def multiplication_tables(low=1, high=12):
    for i in range(low,high+1):
        for j in range(low,high+1):
            print(i*j, end="\t")
        print()

# Sum integers from a text file, one per line
def sum_integers(file_handle):
    pass

# Print odd numbers from 1 to 99
def print_odds():
    pass

# Find the largest int value in an array
def find_max(int_array):
    pass

# Convert a three integer RGB value to hex
# ex. (255,0,17) to 0xff0011
def rgb_int_to_hex(rgb):
    pass

# Find the most frequently occurring number in a list (the mode)
def find_mode(int_list):
    pass
