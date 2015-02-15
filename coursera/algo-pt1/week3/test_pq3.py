import pytest

from pq3 import find_min_cut, find_min_cut_count

"""
    1  2   5  6
    o--o---o--o
    |\/|   |\/|
    |/\|   |/\|
    o--o---o--o
    3  4   7  8

(1,2),(1,3),(1,4),
(2,1),(2,3),(2,4),(2,5),
(3,1),(3,2),(3,4),
(4,1),(4,2),(4,3),(4,7),
(5,2),(5,6),(5,7),(5,8),
(6,5),(6,7),(6,8),
(7,4),(7,5),(7,6),(7,8),
(8,5),(8,6),(8,7),


    1  2   5  6
    o--o---o--o
    |\/|   |\/|
    |/\|   |/\|
    o--o---o--o
    3  4   7  8

How do we represent that we combined the verticies 1 and 3

"""
@pytest.mark.xfail
def test_find_min_cut():
    """
    Given a graph, find_min_cut should return two lists of verticies and one
    list of edges representing verticies on either side of a cut which passes
    through the list of edges. For example:

    Given the following graph:
    1  2   5  6
    o--o---o--o
    |\/|   |\/|
    |/\|   |/\|
    o--o---o--o
    3  4   7  8

    Represented by the following adjacency list:
    (1,2),(1,3),(1,4),
    (2,1),(2,3),(2,4),(2,5)
    (3,1),(3,2),(3,4),
    (4,1),(4,2),(4,3),(4,7)
    (5,6),(5,7),(5,8),(5,2)
    (6,5),(6,7),(6,8),
    (7,5),(7,6),(7,8),(7,4)
    (8,5),(8,6),(8,7),

    find_min_cut should return verticies in two lists representing each side of
    the cut:
    a_side = [1,2,3,4]
    b_side = [5,6,7,8]

    and the following edges should be returned:
    (2,5),(4,7)
    """

    verticies = [1, 2, 3, 4, 5, 6, 7, 8]

    edges = [
        (1,2),(1,3),(1,4),
        (2,1),(2,3),(2,4),(2,5),
        (3,1),(3,2),(3,4),
        (4,1),(4,2),(4,3),(4,7),
        (5,6),(5,7),(5,8),(5,2),
        (6,5),(6,7),(6,8),
        (7,5),(7,6),(7,8),(7,4),
        (8,5),(8,6),(8,7),
    ]

    a_side, b_side, edges = find_min_cut(verticies, edges)
    assert a_side == [1,2,3,4]
    assert b_side == [5,6,7,8]
    assert (2,5) in edges or (5,2) in edges
    assert (4,7) in edges or (7,4) in edges

def test_find_min_cut_count():
    """As above, but only interested in the count of edges"""
    verticies = [1, 2, 3, 4, 5, 6, 7, 8]

    edges = [
        (1,2),(1,3),(1,4),
        (2,1),(2,3),(2,4),(2,5),
        (3,1),(3,2),(3,4),
        (4,1),(4,2),(4,3),(4,7),
        (5,6),(5,7),(5,8),(5,2),
        (6,5),(6,7),(6,8),
        (7,5),(7,6),(7,8),(7,4),
        (8,5),(8,6),(8,7),
    ]

    # The min cut has two edges crossing the left and right side of the split
    # graph, (2,5) and (4,7)

    assert find_min_cut_count(verticies, edges) == 2
