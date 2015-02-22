from graph_primitives import topological_order

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
