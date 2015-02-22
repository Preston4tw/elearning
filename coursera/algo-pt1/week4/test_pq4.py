from graph_primitives import topological_order
from graph_primitives import dfs

def test_topological_order():
    """
    Given a directed graph represented as a dict of lists, where each key
    represents the tail of an arc and each list entry represents the head of an
    arc, return the topological ordering of the graph as a dict with the keys
    representing the graph verticies and the values representing the topological
    order.
    """
    graph = {
        's': ['v', 'w'],
        'v': ['t'],
        'w': ['t'],
        't': [],
    }
    """
    Graph visual representation
          v
          o
        s↗ ↘t
        o   o
         ↘ ↗
          o
          w
    """
    result = topological_order(graph)
    answers = [
        {
            's': 1,
            'w': 2,
            'v': 3,
            't': 4
        }, {
            's': 1,
            'v': 2,
            'w': 3,
            't': 4
        }
    ]
    assert result in answers

def test_dfs():
    """
    Given a directed graph represented as a dict of lists, where each key
    represents the tail of an arc and each list entry represents the head of an
    arc, return the traversed in-order path of each position in the graph
    """
    graph = {
        's': ['v', 'w'],
        'v': ['t'],
        'w': ['t'],
        't': [],
    }
    """
    Graph visual representation
          v
          o
        s↗ ↘t
        o   o
         ↘ ↗
          o
          w
    """
    assert dfs(graph, 't') == ['t']
    assert dfs(graph, 'v') == ['v', 't']
    assert dfs(graph, 'w') == ['w', 't']
    assert dfs(graph, 's') in [['s', 'v', 't', 'w'],
                               ['s', 'w', 't', 'v']]
