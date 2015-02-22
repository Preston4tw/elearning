import pytest

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
        1: [2],
        2: [3, 4],
        3: [1, 8, 11],
        4: [5, 7],
        5: [6],
        6: [7],
        7: [5],
        8: [7, 9, 10],
        9: [6, 10],
        10: [11],
        11: [8],
    }

    """
    Graph visual representation:
        2       4           5
        o------→o----------→o
       ↗|        \      7  ↗ \
     1/ |         \----→o-/  |
     o  |         _____↗ ↖6 ↙
      ↖ |       8/        o
       \↓/-----→o--      ↗
        o   11 ↗|  ↘9   /
        3\-→o-/ |   o---
             ↖  ↓  /
              --o←-
                10
    """
    sccs = get_strongly_connected_components(graph)
    assert [1, 2, 3] in sccs
    assert [4] in sccs
    assert [5, 6, 7] in sccs
    assert [8, 9, 10, 11] in sccs

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
    """
    TODO: accept arbitrary node identifiers
    graph = {
        'a': ['d'],
        'b': ['h'],
        'c': ['f'],
        'd': ['g'],
        'e': ['b'],
        'f': ['i'],
        'g': ['a'],
        'h': ['e', 'f'],
        'i': ['c', 'g']
    }
    results = get_graph_finishing_times(graph)
    assert results == {
        'a': 7,
        'b': 3,
        'c': 1,
        'd': 8,
        'e': 2,
        'f': 5,
        'g': 9,
        'h': 4,
        'i': 6,
    }
    """
