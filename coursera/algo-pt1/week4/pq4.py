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

"""
kosaraju

High level
reverse all the directed arcs
run DFS loop on the reversed graph
    because graph is directed have to DFS a double loop
    keep track of finishing times for each node
change the id of each node to its finishing time in the first dfs run
restore the original arc directions
run DFS loop on the updated orig graph with finishing time identifiers
magically watch as SCCs appear


# keeps track of nodes processed
global t = 0
# Most recent vertex from which DFS was initiated
global s = None

# Assume nodes are labeled 1 to n

for i=n, i>i, i--
    if i not yet explored
    Si = i
    DFS(G,i)

DFS(graph G, node i):
    mark i explored
    set leader(i) = node s
    for each arc (i,j) E G
        if j not yet explored
"""

def dfs(graph, start_node):
    pass

def main():
    f = open('SCC.txt')
    data = f.readlines()
    global graph
    global graph_reversed
    graph = {}
    graph_reversed = {}
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
        if not arc_dest in graph_reversed:
            graph_reversed[arc_dest] = []
        graph_reversed[arc_dest].append(arc_source)
        graph_reversed[arc_dest].sort()

if __name__ == '__main__':
    main()
