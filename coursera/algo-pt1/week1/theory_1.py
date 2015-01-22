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
        return str(self.value)

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

array = [8,1,2,3,4,5,6,7]

nodes = {}

node_levels = int(math.log(len(array),2))

for level in range(node_levels):
    nodes[level] = []
    nodes[level+1] = []

# Build the tree
for level in range(node_levels):
    if level == 0:
        for left, right in chunk(array, 2):
            nodes[level].append(left)
            nodes[level].append(right)
            if left < right:
                nodes[level+1].append(right)
            else:
                nodes[level+1].append(left)
    else:
        for left, right in chunk(nodes[level], 2):
            if left < right:
                nodes[level+1].append(right)
            else:
                nodes[level+1].append(left)

print(nodes)
