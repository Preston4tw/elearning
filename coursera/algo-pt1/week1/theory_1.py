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

array = [8,1,2,3,4,5,6,7]
array = [8,7,1,2,3,4,5,6]

nodes = {}

node_levels = int(math.log(len(array),2))

for level in range(node_levels):
    nodes[level] = []
    nodes[level+1] = []

# Build the tree
for level in range(node_levels):
    if level == 0:
        for left, right in chunk(array, 2):
            left = Node(left)
            right = Node(right)
            nodes[level].append(left)
            nodes[level].append(right)
            if left < right:
                nodes[level+1].append(Node(right, left, right))
            else:
                nodes[level+1].append(Node(left, left, right))
    else:
        for left, right in chunk(nodes[level], 2):
            if left < right:
                nodes[level+1].append(Node(right, left, right))
            else:
                nodes[level+1].append(Node(left, left, right))

print(nodes)

"""
Max will be at the top. The second largest will either be second from the top OR
will have been selected against the largest. To find the second largest need to
compare tree level second from the top vs all numbers that were selected against
from the largest
"""
"""
2nd largest will           8
be in the path of      8       7      <--- Largest will either be at this level or
the largest number   8   3   5   7
                    8 1 2 3 4 5 6 7
"""

candidate_1 = nodes[level+1][0].right
candidate_2 = []
node = nodes[level+1][0].left
for level in range(level):
    candidate_2.append(node.right)
    node = node.left
        
max_c2 = 0
for n in candidate_2:
    if n > max_c2:
        max_c2 = n

if candidate_1 > max_c2:
    second_largest_number = candidate_1
else:
    second_largest_number = max_c2

print("c1: {}, c2: {}. sln: {}".format(candidate_1, candidate_2,
    second_largest_number))

