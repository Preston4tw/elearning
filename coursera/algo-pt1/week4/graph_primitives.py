def topological_order(graph):
    global current_label
    current_label = len(graph)
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
    for head in graph[tail]:
        #print("head: {}, en: {}".format(head, explored_nodes))
        if head not in explored_nodes:
            dfs(graph, head, explored_nodes, stack)
    #print("stack pre-pop: {}".format(stack))
    stack.pop()
    #print("stack post-pop: {}".format(stack))
    #print("start_node: {}".format(start_node))
    # If current_label is set, we want to compute topological ordering
    global current_label
    global ordered_graph
    if 'current_label' in globals():
        #print("setting {} to {}".format(start_node, current_label))
        ordered_graph[start_node] = current_label
        current_label -= 1
    return explored_nodes

def get_strongly_connected_components(graph):
    pass
