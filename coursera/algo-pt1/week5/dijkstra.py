from collections import namedtuple
import itertools
import sys

def compute_shortest_paths(graph, starting_vertex):
    """
    Given a graph (adj list) and starting vertex, compute path lengths to all
    other verticies and return a hash where each hash key is the ending node and
    the hash value is the distance of the shortest path
    """
    distance = {}
    path = {}
    all_verticies = set(list(itertools.chain.from_iterable(
            [(edge.vertex_1, edge.vertex_2)
                for edge in graph])))

    distance[starting_vertex] = 0
    path[starting_vertex] = "{}".format(starting_vertex)

    while set(distance.keys()) != all_verticies:
        a_side_verticies = set(distance.keys())
        b_side_verticies = all_verticies - a_side_verticies
        print("a: {}, b:{}".format(a_side_verticies, b_side_verticies))
        edge_filter = (
            lambda edge:
                True
                        if   edge.vertex_1 in a_side_verticies
                         and edge.vertex_2 in b_side_verticies
                    or
                             edge.vertex_2 in a_side_verticies
                        and  edge.vertex_1 in b_side_verticies
                else False )
        candidate_edges = filter(edge_filter, graph)
        best_score = None
        for edge_c in candidate_edges:
            if edge_c.vertex_1 in a_side_verticies:
                a_side_vertex = edge_c.vertex_1
                b_side_vertex = edge_c.vertex_2
            else:
                a_side_vertex = edge_c.vertex_2
                b_side_vertex = edge_c.vertex_1
            print(" edge candidate: {}, a: {}, b: {}".format(
                edge_c,
                a_side_vertex,
                b_side_vertex)
            )
            score = distance[a_side_vertex] + edge_c.distance
            if not best_score or score < best_score:
                best_score = score
                best_edge = edge_c
        if best_edge.vertex_1 in a_side_verticies:
            a_side_vertex = best_edge.vertex_1
            b_side_vertex = best_edge.vertex_2
        else:
            a_side_vertex = best_edge.vertex_2
            b_side_vertex = best_edge.vertex_1
        distance[b_side_vertex] = best_score
        path[b_side_vertex] = "{},{}".format(path[a_side_vertex], b_side_vertex)
        print("best edge: {}, edge_dist: {}, tot_dist: {}".format(best_edge,
            best_edge.distance, best_score))
    return distance
