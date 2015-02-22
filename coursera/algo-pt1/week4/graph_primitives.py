def topological_order(graph):
    pass

def dfs(graph, start_node, seen_nodes=[]):
    """
    Given a graph as a dict of lists and a start node (a key in the graph dict)
    perform a depth first search
    """
    tail = start_node
    seen_nodes.append(tail)
    for head in graph[tail]:
        if head not in seen_nodes:
            dfs(graph, head, seen_nodes)
