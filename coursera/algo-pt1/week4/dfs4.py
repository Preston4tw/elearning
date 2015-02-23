import pickle
import pdb
import sys
import itertools
import collections

sys.setrecursionlimit(10**7)

def dfs_loop(graph):
    # Number of nodes processed so far
    global t
    t = 0
    
    # Leaders?
    global s
    s = None

    global finishing_time
    finishing_time = {}

    global leaders
    leaders = {}

    global seen
    seen = {}

    for tail in sorted(graph.keys(), reverse=True):
        if tail not in seen:
            s = tail
            dfs(graph, tail)

def dfs(graph, vertex):
    global seen
    seen[vertex] = 1
    global leaders
    global s
    leaders[vertex] = s
    try:
        arc_heads = graph[vertex]
    except KeyError:
        arc_heads = []
    for head in arc_heads:
        if head not in seen:
            dfs(graph, head)
    global t
    t += 1
    global finishing_time
    finishing_time[t] = vertex

def get_sccs(graph_r, graph):
    # Compute finishing times
    dfs_loop(graph_r)
    print("first dfs loop done")

    # Reset seen
    global seen
    seen = {}

    global finishing_time

    for n in range(len(finishing_time), 0, -1):
        vertex = finishing_time[n]
        if vertex not in seen:
            global s
            s = vertex
            dfs(graph, vertex)

def main():
    graph = {}
    graph_r = {}
    f = open("tmp/SCC.txt")
    print("Reading in SCC.txt")
    text = f.readlines()
    print("Building graph")
    for line in text:
        tail, head = line.strip().split()
        tail, head = int(tail), int(head)
        if tail not in graph:
            graph[tail] = []
        graph[tail].append(head)
        if head not in graph_r:
            graph_r[head] = []
        graph_r[head].append(tail)
    sccs = get_sccs(graph_r, graph)
    global leaders
    print("scclengths")
    scc_lengths = collections.Counter(leaders.values()).most_common()[:6]
    print("done")
    print("scclengths: {}".format(scc_lengths))

if __name__ == '__main__':
    main()
