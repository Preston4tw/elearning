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

nodes = {}
nodes[0] = []

for n in a:
    nodes[0].append(Node(n))

nodes[1] = []
for left, right in chunk(nodes[0], 2):
    if left > right:
        node = Node(left, left, right)
    else:
        node = Node(right, left, right)
    nodes[1].append(node)

nodes[2] = []
for left, right in chunk(nodes[1], 2):
    if left > right:
        node = Node(left, left, right)
    else:
        node = Node(right, left, right)
    nodes[2].append(node)

nodes[3] = []
for left, right in chunk(nodes[2], 2):
    if left > right:
        node = Node(left, left, right)
    else:
        node = Node(right, left, right)
    nodes[3].append(node)

nodes[4] = []
for left, right in chunk(nodes[3], 2):
    if left > right:
        node = Node(left, left, right)
    else:
        node = Node(right, left, right)
    nodes[4].append(node)

print(nodes)
"""
4 3
\ /
 4
t2 = []
print(a)
for pos in range(1, len(a)):
    if a[pos] > a[pos-1]:
        t2.append(a[pos])
    else:
        t2.append(a[pos-1])
print(t2)
"""
