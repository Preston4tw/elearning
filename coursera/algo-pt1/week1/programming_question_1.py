#!/usr/bin/env python3

"""
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures. The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
"""

"""
whenever you pick a number from the right array, the number of inversions
increases by the number of remaining elements in the left array
"""

def merge_sort(array):
    global inversions
    length = len(array)
    half_length = int(length/2)
    if length == 1:
        return array
    elif length == 2:
        if array[0] < array[1] or array[0] == array[1]:
            return array
        elif array[0] > array[1]:
            inversions += 1
            return [array[1], array[0]]
    else:
        return merge(merge_sort(array[:half_length]),
                merge_sort(array[half_length:]))

def merge(array_one, array_two):
    global inversions
    merged_array = []
    while len(array_one) > 0 and len(array_two) > 0:
        if array_one[0] < array_two[0]:
            merged_array.append(array_one.pop(0))
        else:
            inversions += len(array_one)
            merged_array.append(array_two.pop(0))
    if len(array_one) > 0:
        merged_array.extend(array_one)
    elif len(array_two) > 0:
        merged_array.extend(array_two)
    return merged_array

inversions = 0

f = open("IntegerArray.txt").readlines()
array = [int(n) for n in f]
sorted_array = merge_sort(array)
print("inversions: {}".format(inversions))
