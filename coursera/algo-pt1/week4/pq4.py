#!/usr/bin/env python3

"""
The file SCC.txt contains the edges of a directed graph. Vertices are labeled as
positive integers from 1 to 875714. Every row indicates an edge, the vertex
label in first column is the tail and the vertex label in second column is the
head (recall the graph is directed, and the edges are directed from the first
column vertex to the second column vertex). So for example, the 11th row looks
liks : "2 47646". This just means that the vertex with label 2 has an outgoing
edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on the given
graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given
graph, in decreasing order of sizes, separated by commas (avoid any spaces). So
if your algorithm computes the sizes of the five largest SCCs to be 500, 400,
300, 200 and 100, then your answer should be "500,400,300,200,100". If your
algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if
your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your
answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course.
Because of the size of the graph you may have to manage memory carefully. The
best way to do this depends on your programming language and environment, and we
strongly suggest that you exchange tips for doing this on the discussion forums.

SCC.txt is available at
http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.zip
"""

import graph_primitives

def main():
    f = open('SCC.txt')
    data = f.readlines()
    graph = {}
    # Build forward and reversed graphs as hash of lists from input data
    for line in data:
        line = line.strip()
        arc_source, arc_dest = line.split()
        arc_source = int(arc_source)
        arc_dest = int(arc_dest)
        if not arc_source in graph:
            graph[arc_source] = []
        graph[arc_source].append(arc_dest)
        graph[arc_source].sort()
    sccs = graph_primitives.get_strongly_connected_components(graph)
    print(len(sccs))

if __name__ == '__main__':
    main()
