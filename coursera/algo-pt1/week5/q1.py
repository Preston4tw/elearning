from collections import namedtuple
import pdb
import sys
import pprint

import dijkstra

"""
http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt

The file dijkstraData.txt contains an adjacency list representation of an
undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists
of the node tuples that are adjacent to that particular vertex along with the
length of that edge.  For example, the 6th row has 6 as the first entry
indicating that this row corresponds to the vertex labeled 6. The next entry of
this row "141,8200" indicates that there is an edge between vertex 6 and vertex
141 that has length 8200. The rest of the pairs of this row indicate the other
vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
(the first vertex) as the source vertex, and to compute the shortest-path
distances between 1 and every other vertex of the graph. If there is no path
between a vertex v and vertex 1, we'll define the shortest-path distance between
1 and v to be 1000000. 

You should report the shortest-path distances to the following ten vertices, in
order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a
comma-separated string of integers. So if you find that all ten of these
vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000
distance away, then your answer should be
1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of
reporting DOES MATTER, and the string should be in the same order in which the
above ten vertices are given. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For
those of you seeking an additional challenge, try implementing the heap-based
version. Note this requires a heap that supports deletions, and you'll probably
need to maintain some kind of mapping between vertices and their positions in
the heap.
"""

def get_adjacency_list(text):
    graph = []
    Edge = namedtuple('Edge', ['vertex_source', 'vertex_dest', 'distance'])
    for line in text:
        line = line.strip()
        vertex_source, *edges = line.split()
        vertex_source = int(vertex_source)
        for edge in edges:
            vertex_dest, distance = edge.split(',')
            vertex_dest = int(vertex_dest)
            distance = int(distance)
            e = Edge(vertex_source, vertex_dest, distance)
            graph.append(e)
    return graph

def get_hash(text):
    graph = {}
    Edge = namedtuple('Edge', ['vertex_dest', 'distance'])
    for line in text:
        line = line.strip()
        vertex_source, *edges = line.split()
        vertex_source = int(vertex_source)
        graph[vertex_source] = []
        for edge in edges:
            vertex_dest, distance = edge.split(',')
            vertex_dest = int(vertex_dest)
            distance = int(distance)
            e = Edge(vertex_dest, distance)
            graph[vertex_source].append(e)
    return graph

def main():
    f = open("dijkstraData.txt")
    text = f.readlines()
    graph = get_adjacency_list(text)
    #graph = get_hash(text)
    shortest_paths = dijkstra.compute_shortest_paths(graph, 1)
    result = ",".join(
        shortest_paths[7],
        shortest_paths[37],
        shortest_paths[59],
        shortest_paths[82],
        shortest_paths[99],
        shortest_paths[115],
        shortest_paths[133],
        shortest_paths[165],
        shortest_paths[188],
        shortest_paths[197],
    )
    print(result)

if __name__ == '__main__':
    main()
