#!/usr/bin/env python3

"""
You are a given a unimodal array of n distinct elements, meaning that its
entries are in increasing order up until its maximum element, after which its
elements are in decreasing order. Give an algorithm to compute the maximum
element that runs in O(log n) time.
"""

import math
iterations = 0

def get_max_element(array):
    global iterations
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] < array[1]:
            return array[1]
        else:
            return array[0]
    # start at the middle of the array
    position = int(len(array)/2)
    # get the element at that position and the next element
    n1, n2 = array[position], array[position+1]
    # if the elements are increasing, the max is in the right segment
    if n1 < n2:
        iterations += 1
        # recursively search using the second half of the array
        return get_max_element(array[position:])
    else:
        iterations += 1
        # recursively search using the first half of the array
        return get_max_element(array[:position+1])

array = list(range(1,10**8,7))
array.extend(list(range(10**3,0,-4)))
n = len(array)
logn = math.log(n)
max_element = get_max_element(array)
print("Array size: {}. "
      "Max element in array: {} {}. "
      "Log of array size: {}. "
      "Iterations: {}.".format(
          n,
          max_element, max(array),
          logn,
          iterations)
      )
