#!/usr/bin/python3

"""
http://www.careercup.com/question?id=5127611667709952

Given a set top box:

a,b,c,d,e
f,g,h,i,j
k,l,m,n,o
p,q,r,s,t
u,v,w,x,y
z

Write code to give the character sequence given a word. For example, if the word
is "CON", the function should print:

    right, now we're at b
    right, now we're at c
    select, c
    down, now we're at h
    down, now we're at m
    right, now we're at n
    right, now we're at o
    select, o
    left, now we're at n
    select, n

Assume no wrapping. There is no left of a to e, no up of a to z, etc
"""

"""
This problem seems like graph search. BFS would probably work well here. We can
create a cursor class to keep track of where we are in between BFS searches for
each character. I think a NamedTuple can be used to represent outgoing arcs for
each node of the graph. The arc namedtuple can be (direction, node). So 'a' will
have the arcs [(right, b), (down, f)]. 

Some kind of list of lists may work for initializing the graph but I may just
brute force it for the first iteration.

Worst case performance of a single BFS is O(m+n) where m and n are the number of
nodes / edges, giving overall worst case lookups polynomial time.

Another possible approach would be to simply generate up front all possible
paths from one node to any other given node and throw it in a nested hash table.
This is computationally expensive up front but afterwards lookups are constant,
eg. O(1).
"""

from collections import namedtuple

class Cursor(object):
    def __init__(self, starting_position):
        self.position = starting_position

    def move(self, direction, graph):
        node = [n for d,n in graph[self.position] if d == direction][0]
        self.position = node
        print("{}, now we're at {}".format(direction, self.position))

    def select(self):
        print("select, {}".format(self.position))

def dfs(graph, start, destination, seen_nodes=None, path=None):
    #print("dfs(g, s:{}, d:{}, seen:{}, path:{})".format(start, destination, seen_nodes, path))
    if not path:
        path = []
    if not seen_nodes:
        seen_nodes = []
    path.append(start)
    seen_nodes.append(start)
    outgoing_arcs = graph[start]
    neighbors = [node for direction,node in outgoing_arcs]
    if destination in neighbors:
        path.append(destination)
        return path
    else:
        for neighbor in neighbors:
            if neighbor not in seen_nodes:
                #print(" neighbors: {}".format(neighbors))
                #print(" seen: {}".format(seen_nodes))
                dfs(graph, neighbor, destination, seen_nodes, path)
                if destination in path:
                    return path

def main():
    layout = [
        "a,b,c,d,e",
        "f,g,h,i,j",
        "k,l,m,n,o",
        "p,q,r,s,t",
        "u,v,w,x,y",
        "z",
    ]

    # Construct a navigatable representation of our graph
    graph = {}
    arc = namedtuple("arc", ["direction", "node"])

    row_count = len(layout)

    for y in range(row_count):
        compute = []
        row = layout[y].split(",")
        if y > 0:
            # Not the top row
            row_above = layout[y-1].split(",")
            compute.append("up")
        if y < row_count - 1:
            # Not the bottom row
            row_below = layout[y+1].split(",")
            compute.append("down")
        previous_letter = None
        for x,letter in enumerate(row):
            if letter not in graph:
                graph[letter] = []
            if x > 0:
                left_arc = arc("left", row[x-1])
                graph[letter].append(left_arc)
            if x != len(row) - 1:
                right_arc = arc("right", row[x+1])
                graph[letter].append(right_arc)
            if "up" in compute:
                up_arc = arc("up", row_above[x])
                graph[letter].append(up_arc)
            if "down" in compute:
                try:
                    down_arc = arc("down", row_below[x])
                    graph[letter].append(down_arc)
                except IndexError:
                    # The last row having only a Z will trigger this code block
                    # for the above row
                    pass

    #import pprint
    #pprint.pprint(graph)

    cursor = Cursor('a')
    word = "con"
    for letter in word:
        path = dfs(graph, cursor.position, letter)
        # get the directions
        for letter in path[1:]:
            direction = [d for d,n in graph[cursor.position] if n == letter][0]
            cursor.move(direction, graph)
        cursor.select()

if __name__ == '__main__':
    main()
