#!/usr/bin/env python3

"""
You are given as input an unsorted array of n distinct numbers, where n is a
power of 2. Give an algorithm that identifies the second-largest number in the
array, and that uses at most n+log₂n-2 comparisons.
"""

"""
for input size n make a binary tree of level log₂n deep
n/2**level comparisons and results
"""

import math
import pdb
from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.value)

    def __lt__(self, x):
        if self.value < x:
            return True
        return False

    def __gt__(self, x):
        if self.value > x:
            return True
        return False

def get_second_largest(array):
    # Max comparisons: n+log₂n-2 
    # The smallest array we operate on is an array of len 2 and is a special
    # case since we're trying to limit our operations there's no need to do
    # anything but compare the two elements and return
    num_comparisons = 0
    if len(array) == 2:
        if array[0] < array[1]:
            num_comparisons += 1
            return num_comparisons, array[0]
        else:
            num_comparisons += 1
            return num_comparisons, array[1]
    global tree
    tree = {}
    tree_depth = int(math.log(len(array),2))

    # Init our tree
    for level in range(tree_depth+1):
        tree[level] = []

    # Build the tree, always putting the larger node on the right
    for level in range(tree_depth):
        if level == 0:
            for left, right in chunk(array, 2):
                left = Node(left)
                right = Node(right)
                tree[level].append(left)
                tree[level].append(right)
                if left < right:
                    num_comparisons += 1
                    tree[level+1].append(Node(right, left, right))
                else:
                    num_comparisons += 1
                    tree[level+1].append(Node(left, right, left))
        else:
            for left, right in chunk(tree[level], 2):
                if left < right:
                    num_comparisons += 1
                    tree[level+1].append(Node(right, left, right))
                else:
                    num_comparisons += 1
                    tree[level+1].append(Node(left, right, left))
    """
    Max will be at the top. The second largest will either be second from the
    top OR will have been selected against the largest. To find the second
    largest need to compare tree level second from the top vs all numbers that
    were selected against from the largest

    2nd largest will           8
    be in the path of      8       7      <--- Largest will either be at this
    the largest number   8   3   5   7         level or
                        8 1 2 3 4 5 6 7
    """
    # The first candidate will be the left node of the top of the tree
    first_candidate = tree[level+1][0].left
    # The rest of the candidates will be nodes selected against by the largest
    # number in the array. Traverse to the bottom of the tree recording all
    # nodes to the left as we walk down the right
    second_candidates = []
    top_node = tree[level+1][0]
    node = top_node.right
    for level in range(level):
        second_candidates.append(node.left)
        node = node.right
            
    print("sc: {}".format(second_candidates))
    second_candidate = second_candidates[0]

    for candidate in second_candidates[1:]:
        if candidate > second_candidate:
            num_comparisons += 1
            second_candidate = candidate

    if first_candidate > second_candidate:
        num_comparisons += 1
        second_largest_number = first_candidate
    else:
        num_comparisons += 1
        second_largest_number = second_candidate
    print(tree)

    return num_comparisons, second_largest_number

array = [1,2]
array = range(1,5)
#array = range(1,9)
#array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#array = [8,1,2,3,4,5,6,7]
#array = [8,7,1,2,3,4,5,6]

array_length = len(array)
max_comparisons = int(array_length + math.log(array_length,2) - 2)

print("Array size: {}, Max allowed comparisons: {}".format(array_length,
    max_comparisons))
num_comparisons, second_largest = get_second_largest(array)
print("Comparisons: {}, Second Largest Number: {}".format(num_comparisons,
    second_largest))
