#!/usr/bin/env python3

"""
The file QuickSort.txt contains all of the integers between 1 and 10,000
(inclusive, with no repeats) in unsorted order. The integer in the ith row of
the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given
input file by QuickSort. As you know, the number of comparisons depends on which
elements are chosen as pivots, so we'll ask you to explore three different
pivoting rules.  You should not count comparisons one-by-one. Rather, when there
is a recursive call on a subarray of length m, you should simply add m - 1
to your running total of comparisons. (This is because the pivot element is
compared to each of the other m - 1 elements in the subarray in this
recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways,
and different implementations can give you differing numbers of comparisons.
For this problem, you should implement the Partition subroutine exactly as it is
described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always use the
first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:

Type the numeric answer in the space provided.  So if your answer is
1198233847, then just type 1198233847 in the space provided without any space /
commas / other punctuation marks. You have 5 attempts to get the correct
answer.  (We do not require you to submit your code, so feel free to use the
programming language of your choice, just type the numeric answer in the
following space.)
"""

import itertools

"""
Choose pivot functions should return indexes because to get the correct answers
for the programming exercise, as a pre-processing step we will swap the first
element of the array with the pivot
"""

def choose_pivot(array):
    # Return the first element of the array
    return 0

def quicksort(array):
    global comparisons
    comparisons += len(array) - 1
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        else:
            return [array[1],array[0]]
    # Partition index starts between array[0] and array[1]
    # The subarray syntax for arrays in python can be thought of as 'up to but
    # not including' when used as [:n], ex.
    # a = [1,2,3,4,5]; a[:2] == [1,2]
    # When picking elements to the left and right of the partition index:
    #   left  = partition_index - 1
    #   right = partition_index
    partition_index = 1

    # Move the pivot to the first element
    pivot_index = choose_pivot(array)
    array[0], array[pivot_index] = array[pivot_index], array[0]
    # pivot = choose_pivot(array)
    # assume pivot is the first element of the array
    pivot = array[0]
    for index,value in list(enumerate(array))[1:]:
        if pivot < value:
            continue
        if pivot > value:
            # In the case that array[1] hits this condition, it 'swaps' with
            # itself
            array[index], array[partition_index] = array[partition_index], array[index]
            partition_index += 1
    # Move the pivot into place
    array[0], array[partition_index-1] = array[partition_index-1], array[0]
    first_half = quicksort(array[:partition_index])
    second_half = quicksort(array[partition_index:])
    return list(itertools.chain(first_half, second_half))

def main():
    global comparisons
    comparisons = 0
    f = open("QuickSort.txt")
    array = f.readlines()
    array = [int(i) for i in array]
    sorted_array = quicksort(array)
    print(comparisons)

if __name__ == "__main__":
    main()
