import itertools

def topological_order(graph):
    global current_label
    current_label = len(graph)
    global label_offset
    label_offset = -1
    global ordered_graph
    ordered_graph = {}
    explored_nodes = []
    for node in graph:
        if node not in explored_nodes:
            explored_nodes.extend(dfs(graph, node, explored_nodes=explored_nodes))
    return ordered_graph

def dfs(graph, start_node, explored_nodes=None, stack=None):
    """
    Given a graph as a dict of lists and a start node (a key in the graph dict)
    perform a depth first search
    """
    #print("dfs(g, start_node: {}, explored_nodes: {}, stack: {})".format(start_node, explored_nodes, stack))
    if not explored_nodes:
        explored_nodes = []
    if not stack:
        stack = []
    stack.append(start_node)
    tail = start_node
    explored_nodes.append(tail)
    #print("added start node {} to stack and explored nodes".format(start_node))
    #print("stack: {}, en: {}".format(stack, explored_nodes))
    try:
        for head in graph[tail]:
            #print("head: {}, en: {}".format(head, explored_nodes))
            if head not in explored_nodes:
                dfs(graph, head, explored_nodes, stack)
    except KeyError:
        # tail has no outgoing edges
        pass
    #print("stack pre-pop: {}".format(stack))
    stack.pop()
    #print("stack post-pop: {}".format(stack))
    #print("start_node: {}".format(start_node))
    # If current_label is set, we want to compute topological ordering
    global current_label
    global label_offset
    global ordered_graph
    if 'current_label' in globals():
        #print("setting {} to {}".format(start_node, current_label))
        ordered_graph[start_node] = current_label
        current_label += label_offset
    return explored_nodes

def reverse_graph(graph):
    reversed_graph = {}
    for vertex in graph:
        for head in graph[vertex]:
            if head not in reversed_graph:
                reversed_graph[head] = []
            reversed_graph[head].append(vertex)
    return reversed_graph

def get_graph_finishing_times(graph):
    reversed_graph = reverse_graph(graph)
    reversed_graph_explored_nodes = []
    global current_label
    current_label = 1
    global label_offset
    label_offset = 1
    global ordered_graph
    ordered_graph = {}
    for node in reversed(list(reversed_graph.keys())):
        if node not in reversed_graph_explored_nodes:
            reversed_graph_explored_nodes.extend(
                dfs(reversed_graph,
                    node,
                    explored_nodes=reversed_graph_explored_nodes
                )
            )
    return ordered_graph

def get_strongly_connected_components(graph):
    # Kosaraju two-pass
    graph_finishing_times = get_graph_finishing_times(graph)
    rgft = dict([(v,k) for k,v in graph_finishing_times.items()])
    explored_nodes = []
    leader_nodes = []
    for n in range(len(rgft), 0, -1):
        node = rgft[n]
        if node not in explored_nodes:
            leader_nodes.append(node)
            explored_nodes.extend(
                    dfs(graph,
                        node,
                        explored_nodes=explored_nodes
                    )
            )
    print(leader_nodes)
    sccs = []
    scc_explored_nodes = []
    last_dfsr = []
    for node in leader_nodes:
        print("N: {}".format(node))
        dfs_result = dfs(graph, node, explored_nodes=scc_explored_nodes)
        print(" dfsr: {}, last_dfsr: {}".format(dfs_result, last_dfsr))
        scc = list(set(dfs_result) - set(last_dfsr))
        scc_explored_nodes.extend(scc)
        scc_explored_nodes = list(set(scc_explored_nodes))
        print(" explored: {}".format(scc_explored_nodes))
        print(" scc: {}".format(scc))
        last_dfsr = dfs_result
        sccs.append(scc)
        print(" sccs: {}".format(sccs))
    return sccs
