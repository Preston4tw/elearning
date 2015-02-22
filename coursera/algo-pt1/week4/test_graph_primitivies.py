from graph_primitives import topological_order
from graph_primitives import dfs
from graph_primitives import get_strongly_connected_components
from graph_primitives import get_graph_finishing_times

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

def test_get_strongly_connected_components():
    """
    Given a directed graph represented as a dict of lists, where each key
    represents the tail of an arc and each list entry represents the head of an
    arc, return lists of vertexes that are strongly connected
    """
    graph = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': ['a', 'h', 'k'],
        'd': ['e', 'g'],
        'e': ['f'],
        'f': ['g'],
        'g': ['e'],
        'h': ['g', 'i', 'j'],
        'i': ['f', 'j'],
        'j': ['k'],
        'k': ['h'],
    }

    """
    Graph visual representation:
        b       d           e
        o------→o----------→o
       ↗|        \      g  ↗ \
     a/ |         \----→o-/  |
     o  |         _____↗ ↖f ↙
      ↖ |       h/        o
       \↓/-----→o--      ↗
        o   k  ↗|  ↘i   /
        c\-→o-/ |   o---
             ↖  ↓  /
              --o←-
                j
    """
    sccs = get_strongly_connected_components(graph)
    assert ['a', 'b', 'c'] in sccs
    assert ['d'] in sccs
    assert ['e', 'f', 'g'] in sccs
    assert ['h', 'i', 'j', 'k'] in sccs

def test_get_graph_finishing_times():
    graph = {
        1: [4],
        2: [8],
        3: [6],
        4: [7],
        5: [2],
        6: [9],
        7: [1],
        8: [5, 6],
        9: [3, 7]
    }
    results = get_graph_finishing_times(graph)
    assert results == {
        1: 7,
        2: 3,
        3: 1,
        4: 8,
        5: 2,
        6: 5,
        7: 9,
        8: 4,
        9: 6,
    }
