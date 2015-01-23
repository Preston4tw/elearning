#!/usr/bin/env python3

"""
You are given a sorted (from smallest to largest) array A of n distinct integers
which can be positive, negative, or zero. You want to decide whether or not
there is an index i such that A[i] = i. Design the fastest algorithm that you
can for solving this problem.
"""

"""
I see two possible interpretations of this problem:
    1. boolean index_equals_value: does the array contain *any* value at an
       index where the index equals the value. Return true/false.

    2. index_start, index_end index_equals_Value: if the array contains 1 or
       more values at indexes where the value and index is equivalent, return
       the index where that range begins and ends*. Return array indicies for
       the beginning and end of the range*.

    *  Since we're dealing with distinct integers, there can be a section of an
       array where A[i] = i, ex:
           A = [-10, -5, -2, 3, 4, 5, 7, 9, 11]

           A[3] = 3, A[4] = 4 , A[5] = 5

       As soon as there is a break in the section, because the integers are
       distinct, there can't be a point later in the array for which A[i] = i is
       true: the smallest possible incremental value is 1, which is the
       same value by which the index increases.
                                      V
                  0   1   2  3  4  5  6  7  8
           A = [-10, -5, -2, 3, 4, 5, 7, 8, 9]

    index   value   check
    0     > -10     right
    1     > -5      right
    2     > -2      right
    3     = 3       !
    4     = 4       !
    5     = 5       !
    6     < 7       left
    7     < 8       left
    8     < 9       left
"""

def index_equals_value(array):
    array_length = len(array)
    # Quickly check for the edge case that the entire array is A[i] = i
    # Array is zero indexed so use length - 1
    if array[0] == 0 and array[array_length-1] == array_length - 1:
        return True
    position = array_length
    if array[position] == position:
        # Position is within the A[i] = i section
    elif array[position] > index:
        subarray = array[:position]

    for index, value in enumerate(array):
        if index == value:
            print("Index {}: {}".format(index, value))

array = [-10, -5, -2, 3, 4, 5, 7, 9, 11]
print(index_equals_value(array))
