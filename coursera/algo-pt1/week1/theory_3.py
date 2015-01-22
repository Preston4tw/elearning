#!/usr/bin/env python3

"""
You are given a sorted (from smallest to largest) array A of n distinct integers
which can be positive, negative, or zero. You want to decide whether or not
there is an index i such that A[i] = i. Design the fastest algorithm that you
can for solving this problem.
"""

"""
Since we're dealing with distinct integers, IF there is a point in the array
where indexes and values match, it is contiguous, meaning we only have to look
for the start of the section and follow it until it ends.

To search for this area we'll want to bisect the array.

If value > index, check left
If value < index, check right
"""

def index_equals_value(array):
    array_length = len(array)
    position = array_length
    if array[position] == position:
        # Position is within the A[i] = i section
    elif array[position] > index:
        subarray = array[:position]

    for index, value in enumerate(array):
        if index == value:
            print("Index {}: {}".format(index, value))


array = [-10,0,2,3,5,10]
index   value   check
0     > -10     right
1     > 0       right
2     = 2       !
3     = 3       !
4     < 5       left

index_equals_value(array)
