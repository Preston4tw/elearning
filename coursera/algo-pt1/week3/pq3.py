#!/usr/bin/env python3

"""
The file kargerMinCut.txt contains the adjacency list representation of a simple
undirected graph. There are 200 vertices labeled 1 to 200. The first column in
the file represents the vertex label, and the particular row (other entries
except the first column) tells all the vertices that the vertex is adjacent to.
So for example, the 6th row looks like:
"6  155     56      52      120 ......".
This just means that the vertex with label 6 is adjacent to (i.e., shares an
edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min
cut problem and use it on the above graph to compute the min cut (i.e., the
minimum-possible number of crossing edges). (HINT: Note that you'll have to
figure out an implementation of edge contractions. Initially, you might want to
do this naively, creating a new graph from the old every time there's an edge
contraction. But you should also think about more efficient implementations.)
(WARNING: As per the video lectures, please make sure to run the algorithm many
times with different random seeds, and remember the smallest cut that you ever
find.) Write your numeric answer in the space provided. So e.g., if your answer
is 5, just type 5 in the space provided.
"""

import itertools
import random

def find_min_cut(verticies, edges):
    """Given a graph represented by a list of verticies and an adjacency list
    (list of tuples) for edges, return the split as represented by each side of
    the split of verticies and the edges through which the cut passes"""
    return [None, None, None]

def find_min_cut_count(verticies, edges):
    """
    Given a graph represented as a list of verticies and an adjacency list of
    tuples edges, return the number of edges crossing the minimum cut of a graph
    """
    while len(verticies) > 1:
        # Choose at random an edge to contract
        contract_edge = random.choice(edges)
        # Contract: delete and fuse the verticies at each end of the edge
        del edges[edges.index(contract_edge)]
        ce_vertex1, ce_vertex2 = contract_edge
        # Fuse: (delete) the second vertex into the first
        del verticies[verticies.index(ce_vertex2)]
        # All edges pointing to ce_vertex2 need to be updated to reflect the
        # fusing. Find all references to ce_vertex2 and replace them with
        # references to ce_vertex1
        #
        # The way we're going to update the edges list requires use of enumerate
        # to have an index to overwrite the tuple at each index (though could
        # use lookup via .index for every iteration, but that would be
        # inefficient
        for index, edge in enumerate(edges):
            edge_vertex1, edge_vertex2 = edge
            if edge_vertex1 == ce_vertex2:
                edges[index] = (ce_vertex1, edge_vertex2)
            if edge_vertex2 == ce_vertex2:
                edges[index] = (edge_vertex1, ce_vertex1)
        # Remove self loops
        edges = [edge for edge in edges if edge[0] != edge[1]]
    return len(edges)

def randomized_contract(verticies, edges):
    """At random, choose an edge to contract. Contract by fusing the two
    verticies and their edges together"""
    contract_edge = random.choice(edges)
    pass

def main():
    # Parse our input file into an array of verticies and edges
    f = open("kargerMinCut.txt")
    text = f.readlines()
    verticies = []
    edges = []
    for line in text:
        # Remove the trailing newline character
        line = line.strip()
        vertex, *vertex_edges = line.split("\t")
        vertex = int(vertex)
        vertex_edges = [int(i) for i in vertex_edges]
        vertex_edge_list = list(itertools.product([vertex,], vertex_edges))
        verticies.append(vertex)
        edges.extend([Edge(v1, v2) for v1, v2 in vertex_edge_list])

if __name__ == "__main__":
    main()
